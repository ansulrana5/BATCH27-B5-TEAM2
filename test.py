from englisttohindi.englisttohindi import EngtoHindi
from urllib.request import urlopen
import json

# message to be translated
a={'b':"Hello"}
message = a['b']

# creating a EngtoHindi() object
res = EngtoHindi(message)

# displaying the translation
print(res.convert)
url = "http://127.0.0.1:5080/apiV1"
response = urlopen(url)
data_json = json.loads(response.read())
for i in data_json['data']:
    e=EngtoHindi(i['state'])
    print(e.convert)
