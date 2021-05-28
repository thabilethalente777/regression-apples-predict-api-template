"""

    Simple Script to test the API once deployed

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Plase follow the instructions provided within the README.md file
    located at the root of this repo for guidance on how to use this
    script correctly.
    ----------------------------------------------------------------------

    Description: This file contains code used to formulate a POST request
    which can be used to develop/debug the Model API once it has been
    deployed.

"""

# Import dependencies
import requests
import pandas as pd
import numpy as np

# Load data from file to send as an API POST request.
# We prepare a DataFrame with the public test set 
# from the Kaggle challenge.
test = pd.read_csv('data/test_data.csv')
#test.drop('Index',axis=1,inplace=True)
#test['Date'] = pd.to_datetime(test['Date'])
#test['Month'] =  [row.month for row in test['Date']]
#test['Season'] = ['summer' if m in [1, 2, 12] else 'autumn' if m in [3, 4, 5] else 'winter' if m in [6,7,8] else 'spring' for m in test['Month']]
#test = pd.get_dummies(test,columns=['Province','Container','Size_Grade','Season'],drop_first=True)
#test.columns = [col.replace(" ","_") for col in test.columns]
#test.columns = [col.replace(".","_") for col in test.columns]
#test.columns = [col.replace("-","_") for col in test.columns]
#test = test.drop(['Date','Commodities'],axis=1)
# Convert our DataFrame to a JSON string.
# This step is necessary in order to transmit our data via HTTP/S
feature_vector_json = test.iloc[1].to_json()

# Specify the URL at which the API will be hosted.
# NOTE: When testing your instance of the API on a remote machine
# replace the URL below with its public IP:

# url = 'http://{public-ip-address-of-remote-machine}:5000/api_v0.1'
url = 'http://3.250.56.135:5000/api_v0.1'

# Perform the POST request.
print(f"Sending POST request to web server API at: {url}")
print("")
print(f"Querying API with the following data: \n {test.iloc[1].to_list()}")
print("")
# Here `api_response` represents the response we get from our API
api_response = requests.post(url, json=feature_vector_json)

# Display the prediction result
print("Received POST response:")
print("*"*50)
# print(f"API prediction result: {api_response.json()[0]}")
print(f"API prediction result: {api_response.json()}")
print(f"The response took: {api_response.elapsed.total_seconds()} seconds")
print("*"*50)
