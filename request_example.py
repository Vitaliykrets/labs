from requests import get as pages

url = "https://www.example.com"  

response = pages(url)

print(response.text)
