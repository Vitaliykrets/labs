from  requests import get as getpages

url = "https://www.example.com"
response = getpages(url)
print(response.text)

