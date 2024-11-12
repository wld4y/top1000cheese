import requests
from bs4 import BeautifulSoup

def get_images(item, quantity):
    n = 1
    images = []
    
    while n < quantity:
        try:
            response = requests.get(f'https://www.bing.com/images/search?q={item} {n}')
        except:
            print('rate limit :(')
            images.append('placeholder.webp')
            continue
            
        if response.status_code != 200:
            print('error code :(')
            exit()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        img_divs = soup.find_all('div', class_='img_cont hoff')
        
        for div in img_divs:
            if n > quantity + 1: break # quick fix but ehhhhhh   
            img_tags = div.find_all('img')

            for img in img_tags:        
                img_src = img.get('src')
                
                if img_src:
                    
                    if not img_src.startswith(('http://', 'https://')):
                        img_src = response.url + img_src
                    
                    try:
                        img_r = requests.get(img_src)
                    except:
                        images.append('placeholder.webp')
                        continue
                    
                    if img_r.status_code != 200: continue
                    with open(f"images/{n}.jpg", 'wb') as file:
                        if img_r.content == '': continue
                        file.write(img_r.content)
                        
                    images.append(f"images/{n}.jpg")
                    print(f'downloaded image {n}: {img_src}')
                    n += 1
        
        print('going to next page...')

    return images