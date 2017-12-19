# Title

## 7 years on, revisiting the demands of the Tunisian and Egyptian springs 
 
# Abstract
In the 2011 Arab Spring, the two most significant revolutions happened in Tunisia and Egypt. 7 years later, we aim to revisit the most recurrent demands expressed by the people on social media. Instead of fishing for pre-defined topics or keywords, we want to let the data directly reflect popular concerns. Here, we want to tell the story of the people behind the revolutions from their own perspective. The motivation behind this project is to bring you closer to the story to understand what drove Tunisians and Egyptians to the streets.
 
The dataset used extends from January 13th to February 14th 2011, roughly covering the time period in between the Tunisian presidential resignation and the Egyptian one. This provides an opportunity to look into how one uprising led to the second. The types of textual data include news articles, online blogs and social media posts. We want also to know whether news articles followed the social media trends.
 
# Research questions
- What were the main demands and concerns expressed by Tunisians and Egyptians? How do they relate to each other?
- How did the Tunisian revolution bring about the Egyptian one?
- How accurately did the news represent popular demands and concerns?
 
# Dataset
The dataset we want to use is the ICWSM 2011 spinn3r dataset. The documentation shows that there are large amounts of social media posts and online blogs, as well as news articles. The data size is gigantic (3TB) and we expect to use it from the cluster. The dataset was the subject of a Data Challenge and we read the only paper that participated in that challenge [1]. We found that there is more room to improve on their analysis, as they did not tackle the popular demands, the non-English-language data, and sentiment analysis did not bring useful insights. To process the textual data, we use NLP and Information Retrieval methods to filter words and get highly frequent topics.
 
[1] Park, Jaehyuk, et al. "Revolution 2.0 in Tunisia and Egypt: Reactions and sentiments in the online world." Proceedings of the fifth international AAAI conference on weblogs and social media. Vol. 1. 2011.
 
# Milestone Tasks

## Milestone 2
- As we saw that in the dataset that posts about Tunisia and Egypt are not separated, we want to split the data by country
- Get counts of the size of the data per day
- Pre-process the data
- Start experiments to extract frequent topics
 
## Milestone 3
- Verify the validity of the keywords approach with ground truth data;
- A data sample was successsfuly analysed. Time to extract and filter the entire data from Spark;
- Create a 3-D model representation for our data: `Country`,  `Post Type`, `Language`
- Apply topic extraction algorithms and infer meaningfull information from data
- Produce a Time Series Analysis
- For every possible combination of parameters (`Country`,  `Post Type`, `Language`), answer the research questions.
- Create Web Site for visualization
 
# Contributions

## Task Distribution
 
Khalil: Responsible for extracting and filtering the Spinn3r data from the cluster, organization of the notebook, and non-English-Language analysis.
 
Khalid: Responsible for the visualization, concerning plots and website.
 
Simão: Responsible for topic modelling methodology and English-Language analysis.
 
## For the final presentation

Khalid and Simão will work on the poster. Khalil will be responsible for the presentation.
 
