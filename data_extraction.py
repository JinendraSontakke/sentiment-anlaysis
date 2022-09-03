# extracting data from a google play store app
import pandas as pd
import numpy as np
import google_play_scraper as app, Sort, reviews_all

# Get the app details
app_details = reviews_all('com.hikingproject.android', lang='en',sort=Sort.NEWEST)

# normalize the data
df = pd.json_normalize(app_details)

# store the data in a csv file
df.to_csv('app_details.csv', index=False)
