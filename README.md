# 7 Years On, Revisiting The Demands of The Tunisian and Egyptian Springs

**Authors:** [Simão Moraes Sarmento](https://github.com/simaomsarmento), [Khalil Mrini](khalilmrini.github.io), [Khalid Omari](https://github.com/khalidomari)

[**Click here for our Project Website!**](https://khalilmrini.github.io/Revisiting-Arab-Spring/Website/)

For details on our Data Analysis, check our [**Jupyter Notebook**](https://github.com/KhalilMrini/Revisiting-Arab-Spring/blob/master/Revisiting_The_Arab_Spring.ipynb)!

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
