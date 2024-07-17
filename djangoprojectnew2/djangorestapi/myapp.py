import requests, json

# URL = "http://127.0.0.1:8000//createclient"
# data = {
#     'client_name':'Aaaa',
#     'created_at':'7',
#     'created_by':'Rohit'
#
# }
# json_data = json.dumps(data)
# r = requests.post(url=URL, data=json_data)
# data = r.json()
# print(data)


URL = "http://127.0.0.1:8000//createproject"
data = {
      'project_name' :'Project C',
       'client':'2',
      ' users':'Rohit',
       'created_at':'',
       'created_by':'Rohit'


}
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)