
# What we talk about when we talk about Affordable Housing

## Context

According to the U.S. Department of Housing and Urban Development, Affordable Housing is generally defined as housing on which the occupant is paying no more than 30 percent of gross income for housing costs, including utilities.

Search on twitter the hashtag [#affordablehousing](https://twitter.com/search?q=%23affordablehousing&src=typed_query&f=live) and we will likely find the following: successful housing projects and campaigns, advertisement for houses for sale or for rent, complaints on expensive housing prices, and appeals for more affordable housing initiatives.

## Scrapping

## Visualization


## Spark NLP


### top 20 words

```
+-----------+-----+
|       word|count|
+-----------+-----+
|affordableh| 8435|
|       hous| 4021|
|     afford| 1975|
|        new| 1171|
|       home| 1133|
|     commun|  928|
|    develop|  851|
|      build|  833|
|         ne|  755|
|       help|  598|
|       citi|  565|
|       make|  550|
|       unit|  539|
|    project|  525|
|   homeless|  519|
|       work|  497|
|    support|  480|
|      learn|  456|
|        via|  455|
|       rent|  442|
+-----------+-----+
```

## Topics

```
|topic | topic_words  
|0     |[new, home, hous, on, afford, todai, support, team, celebr, thank]               |
|1     |[hous, rent, afford, ne, citi, build, increas, realest, market, big]             |
|2     |[hous, afford, home, help, homeless, commun, build, peopl, new, work]            |
|3     |[thank, help, commun, hous, righthous, park, grant, survei, coverag, particip]   |
|4     |[hous, afford, unit, multifamili, develop, haigroup, home, stori, construct, via]|
```

## Named Entity Recognition (NER) with Bert Embeddings

### Top names
```
+-------------------+-----+
|name               |count|
+-------------------+-----+
|Biden              |18   |
|Dave Chappelle     |13   |
|Doug Ford          |11   |
|Matt Kurzmann      |9    |
|Chappelle          |7    |
|Andrew Mikula      |7    |
|Eric Salongo Kalisa|7    |
|MacKenzie Scott    |5    |
|Jeremiah Jarmin    |5    |
|Anthony Buonicore  |5    |
|Seth Barnett       |5    |
|Alex Melikan       |4    |
|Chrystal Kornegay  |4    |
|Ford               |4    |
|Neil Rosenthal     |4    |
|Cruz III           |4    |
|Katie Goar         |4    |
|Emilio Dorcely     |4    |
|Marcia Fudge       |4    |
|John B             |4    |
+-------------------+-----+
```
### Top locations

```
+-------------+-----+
|location     |count|
+-------------+-----+
|America      |88   |
|U.S          |73   |
|California   |61   |
|Bamboo       |60   |
|Crypto       |60   |
|Ontario      |56   |
|US           |52   |
|Canada       |49   |
|Florida      |42   |
|Toronto      |29   |
|NYC          |29   |
|CA           |24   |
|Vancouver    |23   |
|LA           |22   |
|Colorado     |20   |
|NY           |20   |
|MA           |20   |
|BC           |18   |
|San Francisco|17   |
|Charlotte    |17   |
+-------------+-----+
```

## Applying pre-trained pipelines
### Emotion
```
+---------+-----+
|sentiment|count|
+---------+-----+
|      joy| 4429|
|     fear| 2876|
| surprise|  733|
|  sadness|  379|
+---------+-----+
```

Example of joy
```
Here to support passing the Hotel Conversion Bill that will create critically needed #affordablehousing. This is a successful program in Cali which converted 6,000 affordable units already!
```

Example of fear
```
A cautionary tale if there ever was one.

It’s bad when people choose death because they can’t AFFORD life.
```

Example of surprise
```
Look at all those signatures! Big thanks to everyone across our coalition and beyond who 
came through to sign our petition and help us gather signatures!
```

Example of sadness
```
I just have no words. HB1601/HB978 was returned to the house with  
#GovLee signature making #homelessness a felony by closing encampments. 
Not enough shelter beds & not enough #affordablehousing 
```

### Sarcasm

```
+---------+-----+
|sentiment|count|
+---------+-----+
|   normal| 8265|
|  sarcasm|  152|
+---------+-----+
```

Examples of sarcastic text:
```
"Housing is where jobs go to sleep at night."

"I think of that Parks & Rec Leslie Knope quote: ' when people are yelling, I just hear people caring very loudly' "

“An outcome in which nearly 1,000 households don’t get the assistance they are entitled to is unacceptable”

Today, I proudly introduced my bill: Affordable Housing And Area Median Income Fairness Act of 2022
```

## References
https://www.hud.gov/
https://github.com/shaikhsajid1111/twitter-scraper-selenium
https://spark.apache.org/docs/latest/sql-data-sources-csv.html
https://medium.com/trustyou-engineering/topic-modelling-with-pyspark-and-spark-nlp-a99d063f1a6e
https://medium.com/@lily_su/accessing-s3-bucket-from-google-colab-16f7ee6c5b51
https://nlp.johnsnowlabs.com/demo

