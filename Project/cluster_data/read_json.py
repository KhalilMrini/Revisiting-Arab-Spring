EN = 'english'
FR = 'french'
AR = 'arabic'
LANGS = [EN, FR, AR]

CODE_TO_LANG = dict((language[:2], language) for language in LANGS)

EG = 'Egypt'
TN = 'Tunisia'
COUNTRIES = [EG, TN]

KEYPHRASE_PATH = './Keyphrases/'

keyphrase_dict = dict((country, 
                       dict((language, open('{}{}_{}.txt'.format(
                           KEYPHRASE_PATH, country, language)).read().strip().split('\n')) 
                            for language in LANGS)) 
                      for country in COUNTRIES)

def keyphrase_score(country, language, text):
    """
    Computes how many keyphrases for the country and language are in the text.
    :param country: string
    :param language: string
    :param text: string
    :return: int
    """
    score = 0
    for keyphrase in keyphrase_dict[country][language]:
        if keyphrase in text:
            score += 1
    return score

def compute_keyphrase_scores(text, language):
    """
    Computes keyphrase scores for all countries given text and language.
    Returns False if all scores are inferior to 4.
    :param text: string
    :param language: string
    :return: dict or boolean
    """
    new_text = text.lower()
    data = {}
    score_sum = 0
    for country in keyphrase_dict:
        score = keyphrase_score(country, language, new_text)
        data[country] = score
        score_sum += score
    if score_sum <= 4:
        return False
    else:
        return data

import json

def try_to_get_content(entry_dict):
    """
    Attempts to get content from an entry.
    :param entry_dict: dict
    :return: string
    """
    try:
        return BeautifulSoup(zlib.decompress(entry_dict['feedEntry']['content']), "html.parser").text
    except:
        return ""
    
def check_datetime(datetime):
    """
    Checks if date given is within range of days studied: Jan 13, 2011 to Feb 14, 2011, included.
    :param datetime: string
    :return: boolean
    """
    try:
        year = int(datetime[:4])
        month = int(datetime[5:7])
        day = int(datetime[8:10])
        return year == 2011 and ((month == 1 and day in range(13,32)) 
                                 or (month == 2 and day in range(1,15)))
    except:
        return False

def sequential_operation(data_rows, entry):
    """
    Appends entry to data_rows if valid.
    :param data_rows: list of dict
    :param entry: string
    :return: list of dictionaries
    """
    try:
        # Loading the entry string as a dict
        entry_dict = json.loads(entry)
        
        lang_code = entry_dict['feedEntry']['language']
            
        # Proceeding if the language is English, French or Arabic
        if lang_code in CODE_TO_LANG:
            post_title = entry_dict['feedEntry']['title']
            
            # Post Content
            try:
                post_content = BeautifulSoup(zlib.decompress(
                    entry_dict['feedEntry']['content']), "html.parser").text
            except:
                post_content = ""
            
            data = compute_keyphrase_scores(post_title + ' ' + post_content, 
                                                CODE_TO_LANG[lang_code])
            
            if data:
                datetime = entry_dict['feedEntry']['lastPublished']
                if not datetime:
                    datetime = entry_dict['feed']['lastPublished']
                    
                if check_datetime(datetime):
                    # Language Code
                    data['Lang_Code'] = lang_code

                    # Post Title
                    data['Post_Title'] = post_title
                    
                    # Date & Time
                    data['Datetime'] = datetime
                
                    # Post Content
                    if post_content:
                        data['Post_Content'] = post_content

                    # Link
                    try:
                        data['Post_Link'] = entry_dict['feedEntry']['url']
                    except:
                        pass
                
                    # Author Name
                    try:
                        data['Author_Name'] = entry_dict['feedEntry']['authorName']
                    except:
                        pass

                    # Identifier
                    try:
                        data['Identifier'] = entry_dict['feedEntry']['identifier']
                    except:
                        pass

                    # Publisher Type
                    try:
                        data['Type'] = entry_dict['source']['publisherType']
                    except:
                        pass

                    data_rows.append(data)
    except:
        pass
    return data_rows

from pyspark import SparkContext, SQLContext 

SPINNER_JSON_PATH =  'hdfs:////datasets/Spinn3r/spinn3r.json'

sc = SparkContext()
sqlContext = SQLContext(sc)

rdd = sc.textFile(SPINNER_JSON_PATH)

comb_op = (lambda x, y: x + y)
data_rows = rdd.aggregate([], sequential_operation, comb_op)

import pickle

file = open('data.pkl', 'w')
pickle.dump(data_rows, file)
file.close()