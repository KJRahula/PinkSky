#Kokkupakitud failide lahtipakkimiseks
import gzip
#Andmetetöötluseks
from io import BytesIO
#XML failisturktuuri parsimiseks
import xml.etree.ElementTree as ET
#Veebist andmete allalaadimiseks
#pip install requests
import requests
#Tegeleb puukujutamisega
from bs4 import BeautifulSoup

#Veebipäring
url = "https://cms.arvutitark.ee/sitemap/EST/product-catalog1.xml.gz"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

#Pakib mälus lahti
with gzip.GzipFile(fileobj=BytesIO(response.content)) as gz:
    xml_content = gz.read()

#XML parsemine
root = ET.fromstring(xml_content)

#Shortcut, millel on võti ja väärtus
ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

#Kirjutab listi kõik leitud lingid mis ta sai kätta xml failist.
product_urls = [loc.text for loc in root.findall(".//sm:loc", ns)]

#Proovime esimeselt lehelt infot saada
sample_url = product_urls[0]
print(f"Testime toodet: {sample_url}")

#Puukujuline kujutamine
page_res = requests.get(sample_url, headers=headers)
soup = BeautifulSoup(page_res.text, "html.parser")

#Üritame leida kindlaid detaile. 
hind = soup.find("span", class_="_main-price")
print(f"Hind : {hind}")