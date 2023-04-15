import requests
from bs4 import BeautifulSoup
import json
import textwrap

# 1 - recuperer la page principale
# 2 - récupérer les deux liens
# 3 - récuperer les donées du lien un
# 4 - récuperer les donées du lien deux

# 1
url = "http://fastandfurious.chall.malicecyber.com"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# 2

content = soup.find("div", {"class", "content"})
a = content.find_all('a')
link_list = []
for l in a:
	link = url + l['href']
	link_list.append(link)

# 3

data1 = requests.get(link_list[0])
json_data = json.loads(data1.text)
print(json_data)
step = json_data['step']
matrix = json_data['matrix']

# 4

data2 = requests.get(link_list[1])
flag_encoded = data2.text
flag = ''

print("matrice = ", matrix)

print()
print()

print("step : ", step)
print("flag_encoded : ", flag_encoded)
feeder = textwrap.wrap(flag_encoded, step)
print("feeder : ", feeder)

for i in range(len(feeder)):
	flag = flag + str(matrix[feeder[i]])

print(flag)