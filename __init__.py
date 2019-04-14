#import requests
import json
import requests
import time
from time import sleep

data = requests.get('http://positive-quotes.herokuapp.com/v1//quotes').json()

for quote in data:
    print (quote['content'])
    
    sleep(4000)

