import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
def is_valid(url):
    """
    Проверяем, является ли url действительным URL
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
def get_all_images(url):
    """
    Возвращает все URL‑адреса изображений по одному `url`
    """
    soup = bs(requests.get(url).content, "html.parser")
    urls = []
    for img in soup.find_all("img"):
        img_url = img.attrs.get("src")
        if not img_url:
            continue

        img_url = urljoin(url, img_url)

        if is_valid(img_url):
            urls.append(img_url)
    return urls
url_adres= input('Введите адрес...\n')
get_all_images(url_adres)
x = get_all_images(url_adres)
print(x)