import json
data='{"title":"The old man and the sea","ISBN":"12345","Author":"Earnest Hemingway"}'
json_data=json.loads(data)
print(type(json_data))
print(json_data['title'])
print(json_data['ISBN'])
print(json_data['Author'])