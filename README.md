# PrognoZ
Disaster prediction for Microsoft Code Fun do ++

We are making a web application to predict the severity of storms over a span of few weeks in advance. Our prediction will take place for regions where storms have occured very frequently creating devastation, like the Eastern coastal region of US.

There are different kinds of storms which we will be focusing on because of the major threat they possess: - Hurricane, Cyclone, Typhoon and Tornado.

First, we will take previous few years of data on pressure, temperature, humidity, wind speed and other such variables, which we call as weather variables. Then using ML we will predict the weather variables for the next few weeks.

We will fetch data for all storms in the past few years - weather variables of one month (prior to the storm) Now we will try and find similarities between the previous occurrences of storms using ML algorithms. By similarities we mean some peculiar patterns or odd extremes, in the month before the storm, which give rise to the storm.

Now we will try and find the patterns (which we got from the previous storms) in the predicted data over the next few weeks. According to the matches found we will give a probabilistic prediction on the storm status for the next few weeks.

We will alert the respective disaster management authority if the probability of the storm is high. We will also be predicting the trajectory of the storm, its lasting period and its velocity so that preventive measures can be taken in advance accordingly and many lives can be saved.
