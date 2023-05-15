import requests

#api.nasa.gov

url_nasa="https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=2&api_key=DEMO_KEY"

response_nasa = requests.request("GET", url=url_nasa)

photos = response_nasa.json()

img = photos["photos"][0]["img_src"]

print(img)