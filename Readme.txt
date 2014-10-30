TwittMap

Author: Songqiao Su (ss4555), Jiachen Li (jl4122)
Email: ss4555@columbia.edu	jl4122@columbia.edu
URL:http://mysite-env-ruefpzaeki.elasticbeanstalk.com/mapping/

Back End: Write in django. The TwittMap application is designed for tweets reading, recording, plotting, and filtering. We implemented all requirements and color gradient plot. We used Twitter Live API reads a bunch of tweets from twitter, and used SQL to store timestamp, geolocation, and key words into a database. The tweets are filtered based on city name showed in them. Behind the scene, an EC2 server is constantly collecting and parsing by using crontab. Elastic Beanstalk API was implemented to deploy the application programmatically. 

Front End: We created both scatter plot and heat plot with color gradient of the tweets based on Google Map API. Users can choose "Marked Map" for scatter plot and "Color Gradient Map" for heatmap. The "Key Word" represent a filter in backend - users can select a city and the Google Map will only show tweets with that city name.


