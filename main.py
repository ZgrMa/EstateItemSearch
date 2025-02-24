import requests
import os
from bs4 import BeautifulSoup
#from PIL import Image -- see about using memory instead of disk to use images in the future

#Fetch user-given URL
print('Please input a URL.')
url = str(input())
response = requests.get(url)

#Fetch images
soup = BeautifulSoup(response.text, 'html.parser')
images = soup.find_all('a', href =True)

#Save and check images
os.makedirs('SaleImages', exist_ok=True)
for image in images:
    path = image['href']
    if path.endswith(('.png', '.jpg', '.jpeg')):
        if not path.startswith('http'):
            path = url.split('.com/')[0] + path

        imageName = path.split('/')[-1]
        imageData = requests.get(path).content
        with open(os.path.join('SaleImages', imageName), 'wb') as handler:
            handler.write(imageData)
            print(f'{imageName} has been saved.')