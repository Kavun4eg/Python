import requests
import os

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)
data = response.json()

os.makedirs('mars_photos', exist_ok=True)

photos = data['photos']
for idx, photo in enumerate(photos[:2]):
    img_url = photo['img_src']
    img_response = requests.get(img_url)
    if img_response.status_code == 200:
        file_name = f'mars_photos/mars_photo{idx+1}.jpg'
        with open(file_name, 'wb') as file:
            file.write(img_response.content)
        print(f'Saved {file_name}')
    else:
        print(f'Failed to download {img_url}')

print('Finished downloading photos')