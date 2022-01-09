import http.client
import json

conn = http.client.HTTPSConnection("mysterious-everglades-08626.herokuapp.com")
payload = ''
headers = {
  'Authorization': 'Token 4e74f46a5d7ba3059ec6f1517dbb7540dc68e0e0'
}
conn.request("GET", "/esp/sentence_get", payload, headers)
res = conn.getresponse()
data = json.loads(res.read())

exp = data['expression']

# make every first letter in word is capital and others are lower case
words = exp.split(' ')
exp = ' '.join([words[i][0].upper() + words[i][1:].lower() for i in range(len(words))])

print(exp)


conn = http.client.HTTPSConnection("mysterious-everglades-08626.herokuapp.com")
payload = json.dumps({
  "expression": exp
})
headers = {
  'Authorization': 'Token 4e74f46a5d7ba3059ec6f1517dbb7540dc68e0e0',
  'Content-Type': 'application/json'
}
conn.request("POST", "/esp/sentence_submit", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))