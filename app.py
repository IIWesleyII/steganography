  
import cv2
from random import randint
import webbrowser

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~`:!@#$%^&*()_+-=.,'*/ "

def encrypt(url:str, img_path:str) -> list:
    img_data = cv2.imread(img_path, 1)
    num = []
    locs = []

    for i in url:
        num.append(alpha.index(i))
    for i in range(len(num)):
        locs.append((randint(0, len(img_data) - 1), randint(0, len(img_data[0]) - 1), randint(0, 2)))
    for i, j in zip(locs, num):
        img_data[i[0]][i[1]][i[2]] = j

    cv2.imwrite('encrypted-img.png', img_data)

    return locs

def decrypt(img_name:str, locs:list) -> str:
    img_data = cv2.imread(img_name, 1)
    url = ""
    for i in locs:
        url += alpha[img_data[i[0]][i[1]][i[2]]]
    
    return url

"""
User input's a URL from the console, the application embeds the URL in the image,
then it requests the resource from the url and displays it in a browser window.
"""
if __name__ == "__main__":
    # example url = "https://static01.nyt.com/images/2020/05/19/science/30TB-BORINGSUN1/merlin_172064805_d476abdd-f4da-4015-8ca3-8c45c92c61fa-superJumbo.jpg"
    url = input("Enter an image URL to embed in your local image.")
    locs = encrypt(url, 'steganography-pics\sunglasses-chicken.jpeg')
    webbrowser.open(decrypt('encrypted-img.png', locs))