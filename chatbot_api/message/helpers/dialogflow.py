import requests

def query_dialogflow(message):
    client_key = "<CLIENT_KEY>"
    headers = {"Authorization": "Bearer " + client_key}
    payload = {"lang": "fr", "query": message, "v":20150910, "sessionId":1}
    r = requests.get('https://api.dialogflow.com/v1/query', params=payload, headers=headers)
    return r
