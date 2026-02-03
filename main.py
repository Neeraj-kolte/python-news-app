import requests

query = input("What type of news you want to read ? ")
api = "pub_d0b7417e58ee4433ba064133d2b5c7ab"


url = f"https://newsdata.io/api/1/latest?apikey={api}&q={query}"


print(url)
response = requests.get(url)
data = response.json()

results = data["results"]

for index, result in enumerate(results):
    print(index + 1,":","Title: ",result["title"],"\n","   Link: ",result["link"])
    print("\n*********************************************\n")





