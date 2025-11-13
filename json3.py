import json
data='{"title":"The old man and the sea","ISBN":"12345","Author":"Earnest Hemingway"}'
json_data=json.loads(data)
with open("book.json","w") as f:
    json.dump(json_data,f,indent="\t")
