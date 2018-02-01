import requests
import json

#My Unique App ID & Key
app_id = <app_id>
app_key = <api_key>

language = 'en'
word_id = raw_input("Please enter a word: ")

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

#Makes the data easier to read
r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})


result =  r.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
result = result[0].upper() + result[1:]
print word_id + "\n" + result