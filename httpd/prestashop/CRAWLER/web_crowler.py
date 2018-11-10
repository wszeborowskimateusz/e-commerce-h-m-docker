import requests
import json
import re
from bs4 import BeautifulSoup

'''
Categories
10 - Ona
    15 - Koszulki - shortsleeve
    16 - Basics - basics
    17 - Koszule i bluzki - longsleeve/shirtsblouses/shirts/blouses
    18 - kardigany i swetry - cardigansjumpers/jumpers/cardigans
    19 - bluzy - hoodiesswetshirts/sweatshirts
    20 - dzianiny - turtlenecks/knitwear
    21 - marynarki i kamizelki - vests/blazerswaistcoats/blazers/jacketscoats
    22 - kurtki i płaszcze - jacketscoats/coats/jackets
    23 - spodnie - trousers/leggings/jeans/skinny
    24 - dźinsy - jeans
    25 - szorty - shorts
    26 - spódnice - skirts/midiskirts/shortskirts
    27 - sukienki - dresses/shortdresses
    28 - kombinezony - jumpsuits
    29 - buty - shoes/boots
    30 - dodatki - bags/shouldercross/accessories/hatscarvesgloves
    31 - stroje kąpielowe - swimwear/swimsuits
    32 - bielizna - lingerie/bras/balconette/pushup
    33 - piżamy - nightwear/pyjamas
    34 - skarpetki i rajstopy - sockstights/socks/
    35 - odzież sportowa -sport
    36 - mama - maternity
    37 - H&M+ - plus
    38 - rozszerzona rozmiarówka - trousers
    39 - uroda - beauty
11 - On
    40 - kurtki i płaszcze - jacketscoats/coats/jackets
    41 - bluzy - hoodiesswetshirts/sweatshirts
    42 - kardigany i swetry - cardigansjumpers/jumpers/cardigans
    43 - t-shirty i podkoszulki - tshirtstanks/shortsleeve/tshirts
    44 - buty - shoes/boots
    45 - koszule - shirts
    46 - basics - basics
    47 - marynarki i garnitury - blazerssuits/blazers/suits
    48 - shorty - shorts
    49 - spodnie - trousers/leggings/jeans/skinny
    50 - dżinsy - jeans
    51 - stroje kąpielowe - swimweear
    52 - bielizna - underwearloungewear/underwear
    53 - skarpetki - socks
    54 - dodatki - bags/shouldercross/accessories/hatscarvesgloves
    55 - odzież sportowa - sport
    56 - większe rozmiary - jacketscoats
12 - Divided
    57 - topy - tops
    58 - sukienki i kombinezony - dresses/shortdresses/jumpsuits
    59 - kolekcja podstawowa - już dodane
    60 - kurtki i marynarki - blazers/jacketscoats
    61 - buty - shoes/boots
    62 - dodatki - bags/shouldercross/accessories/hatscarvesgloves
    63 - bluzy i koszule - longsleeve/shirtsblouses/shirts/blouses/hoodiesswetshirts/sweatshirts
    64 - spódnice - skirts/midiskirts/shortskirts
    65 - spodnie - trousers/leggings/jeans/skinny
13 - Dziecko
    66 - niemowlęta do 9 mc - newborn
    67 - dziewczynki 4m-4y - babygirl
    68 - chłopcy 4m-4y - babyboy
    69 - baby exclusive 4-24mc - bottoms
    70 - dziewczynki 1,5-10 lat - girl8y
    71 - chłopcy 1,5-10 lat - boy8y
    72 - dziewczynki 8-14+ lat - girl14y
    73 - chłopcy 8-14+ lat - boy14y
14 - Home
    74 - poduszki - cushions/cushioncover
    75 - pościel - bedlinen/sheets
    76 - ręczniki - towels
    77 - dywaniki łazienkowe - bathmats
    78 - zasłony prysznicowe - showercurtains
    79 - koce - blankets
    80 - zasłony - curtains
    81 - dywany - carpets
    82 - przechowywanie - storage/bagsstorage


id - start 20
'''


URLS = ["https://www2.hm.com/pl_pl/ona/produkty/view-all.html?sort=stock&image-size=small&image=model&offset=0&page-size=216",
        "https://www2.hm.com/pl_pl/on/produkty/view-all.html?sort=stock&image-size=small&image=model&offset=0&page-size=216",
        "https://www2.hm.com/pl_pl/divided/shop-by-product/view-all.html?sort=stock&image-size=small&image=model&offset=0&page-size=216",
        "https://www2.hm.com/pl_pl/dziecko/produkty/view-all.html?sort=stock&image-size=small&image=model&offset=0&page-size=216",
        "https://www2.hm.com/pl_pl/dom/produkty/view-all.html?sort=stock&image-size=small&image=model&offset=0&page-size=216"]


def get_sub_categorie(categories, general_cat):
    cat = []
    for category in categories.split('_'):
        if general_cat == "10":
            if category == "shortsleeve":
                cat.append("15")
            if category == "basics":
                cat.append("16")
            if category == "longsleeve" or category == "shirtsblouses" or category == "shirts" or category == "blouses":
                cat.append("17")
            if category == "cardigansjumpers" or category == "jumpers" or category == "cardigans":
                cat.append("18")
            if category == "hoodiesswetshirts" or category == "sweatshirts":
                cat.append("19")
            if category == "turtlenecks" or category == "knitwear":
                cat.append("20")
            if category == "vests" or category == "blazerswaistcoats" or category == "blazers" or category == "jacketscoats":
                cat.append("21")
            if category == "jacketscoats" or category == "coats" or category == "jackets":
                cat.append("22")
            if category == "trousers" or category == "leggings" or category == "jeans" or category == "skinny":
                cat.append("23")
            if category == "jeans":
                cat.append("24")
            if category == "shorts":
                cat.append("25")
            if category == "skirts" or category == "midiskirts" or category == "shortskirts":
                cat.append("26")
            if category == "dresses" or category == "shortdresses":
                cat.append("27")
            if category == "jumpsuits":
                cat.append("28")
            if category == "shoes" or category == "boots":
                cat.append("29")
            if category == "bags" or category == "shouldercross" or category == "accessories" or category == "hatscarvesgloves":
                cat.append("30")
            if category == "swimwear" or category == "swimsuits":
                cat.append("31")
            if category == "lingerie" or category == "bras" or category == "balconette" or category == "pushup":
                cat.append("32")
            if category == "nightwear" or category == "pyjamas":
                cat.append("33")
            if category == "sockstights" or category == "socks":
                cat.append("34")
            if category == "sport":
                cat.append("35")
            if category == "maternity":
                cat.append("36")
            if category == "plus":
                cat.append("37")
            if category == "trousers":
                cat.append("38")
            if category == "beauty":
                cat.append("39")
        elif general_cat == "11":
            if category == "jackets" or category == "coats" or category == "jackets" :
                cat.append("40")
            if category == "hoodiesswetshirts" or category == "sweatshirts":
                cat.append("41")
            if category == "cardigansjumpers" or category == "jumpers" or category == "cardigans":
                cat.append("42")
            if category == "tshirtstanks" or category == "shortsleeve" or category == "tshirts":
                cat.append("43")
            if category == "shoes" or category == "boots":
                cat.append("44")
            if category == "shirts":
                cat.append("45")
            if category == "basics":
                cat.append("46")
            if category == "blazerssuits" or category == "blazers" or category == "suits":
                cat.append("47")
            if category == "shorts":
                cat.append("48")
            if category == "trousers" or category == "leggings" or category == "jeans" or category == "skinny":
                cat.append("49")
            if category == "jeans":
                cat.append("50")
            if category == "swimweear":
                cat.append("51")
            if category == "underwearloungewear" or category == "underwear":
                cat.append("52")
            if category == "socks":
                cat.append("53")
            if category == "bags" or category == "shouldercross" or category == "accessories" or category == "hatscarvesgloves":
                cat.append("54")
            if category == "sport":
                cat.append("55")
            if category == "jacketscoats":
                cat.append("56")
        elif general_cat == "12":
            if category == "tops":
                cat.append("57")
            if category == "dresses" or category == "shortdresses" or category == "jumpsuits":
                cat.append("58")
            if category == "blazers" or category == "jacketscoats":
                cat.append("60")
            if category == "shoes" or category == "boots":
                cat.append("61")
            if category == "bags" or category == "shouldercross" or category == "accessories" or category == "hatscarvesgloves":
                cat.append("62")
            if category == "longsleeve" or category == "shirtsblouses" or category == "shirts" or category == "blouses" or category == "hoodiesswetshirts" or category == "sweatshirts":
                cat.append("63")
            if category == "skirts" or category == "midiskirts" or category == "shortskirts":
                cat.append("64")
            if category == "trousers" or category == "leggings" or category == "jeans" or category == "skinny":
                cat.append("65")
        elif general_cat == "13":
            if category == "newborn":
                cat.append("66")
            if category == "babygirl":
                cat.append("67")
            if category == "babyboy":
                cat.append("68")
            if category == "bottoms":
                cat.append("69")
            if category == "girl8y":
                cat.append("70")
            if category == "boy8y":
                cat.append("71")
            if category == "girl14y":
                cat.append("72")
            if category == "boy14y":
                cat.append("73")
        else:
            if category == "cushions" or category == "cushioncover":
                cat.append("74")
            if category == "bedlinen" or category == "sheets":
                cat.append("75")
            if category == "towels":
                cat.append("76")
            if category == "bathmats":
                cat.append("77")
            if category == "showercurtains":
                cat.append("78")
            if category == "blankets":
                cat.append("79")
            if category == "curtains":
                cat.append("80")
            if category == "carpets":
                cat.append("81")
            if category == "storage" or category == "bagsstorage":
                cat.append("82")
    return list(set(cat))


class Product:
    def __init__(self, name, categories, price, description, imgs, sizes):
        self.active = "1"
        self.name = name
        self.categories = categories
        self.description = description
        self.imgs = imgs
        self.price = price
        self.amount = "100"
        self.sizes = sizes


def convert_to_csv(products):
    f = open('produkty.csv', 'w+', encoding='utf-8')
    f.write('"Aktywny (0 lub 1)";"Nazwa";"Kategorie (x,y,z...)";"Cena zawiera podatek. (brutto)";"Opis";"Adresy URL zdjęcia (x,y,z...)";"Ilosc"\n')
    print(products)
    for product in products:
        if product is not None:
            output = product.active + ";" + product.name + ";"
            for category in product.categories:
                output += category + "$"
            output = output[:-1]
            output += ";"
            output += product.price + ";" + product.description + ";"
            for img in product.imgs:
                output += img + "$"
            output = output[:-1]
            output = output + ";" + product.amount + "\n"
            f.write(output)
    f.close()


def generate_combination(products):
    f_combination = open('kombinacje.csv', 'w+', encoding='utf-8')
    f_combination.write("Identyfikator Produktu (ID);Atrybut (Nazwa:Typ:Pozycja);Wartość (Wartość:Pozycja);Ilość\n")
    i = 1
    for product in products:
        if product is not None:
            output = ""
            if len(product.sizes) == 0:
                continue
            for size in product.sizes:
                output += str(i) + ";Rozmiar:rozmiar:0;" + size.replace("\"", "") + ":0;100" + "\n"
            i += 1
            f_combination.write(output)
    f_combination.close()


def extract_info(url, name, categories, img_url):
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    for script in s.find_all('script'):
        if script.string is not None and 'var isDesktop' in script.string:
            data = script.string
            data = data[82:]
            data = data[:-3]
            m = re.search("'description': '(.*)',", data)
            description = m.group(0)
            description = description[16:]
            description = description[:-3]
            description = json.dumps(json.loads('"' + description + '"'), ensure_ascii=False)

            m = re.search("'whitePriceValue': '(.*)',", data)
            price = m.group(0)
            price = price[20:]
            price = price[:-2]
            price = json.dumps(json.loads('"' + price + '"'), ensure_ascii=False)

            imgs = []
            product_id = url.split(".")[-2]
            m = re.findall("'" + product_id + "': {[\s\S]*'sizes':\[", data)
            m = re.findall("'image': isDesktop \? '(.*)' :", m[0])

            for i in range(0, 3):
                if i <= len(m) - 1:
                    img = m[i]
                    img = img[2:]
                    img = img[:-1]
                    img = "http://" + img
                    img = json.dumps(json.loads('"' + img + '"'), ensure_ascii=False)
                    imgs.append(img)

            general_categorie = categories[0]
            if img_url is not None:
                m = re.search("category\[(.*)\],", img_url)
                if m is not None:
                    categories = categories + get_sub_categorie(m.group(0).split(',')[0].split('[')[1][:-1], general_categorie)

            sizes = ""
            m = re.findall("'" + product_id + "': {[\s\S]*'whitePrice':", data)
            m = re.findall('"name":(.*)\r', m[0])
            if len(m) > 0:
                m = list(filter(lambda x: 'P' not in x, sorted(list(set(m)))))
                sizes = m

            print(categories)
            return Product(name, categories, price, description, imgs, sizes)


def get_main_category(url):
    if url == "https://www2.hm.com/pl_pl/ona/produkty/view-all.html?sort=stock&image-size=small&image=model&offset=0&page-size=216":
        return "10"
    elif url ==  "https://www2.hm.com/pl_pl/on/produkty/view-all.html?sort=stock&image-size=small&image=model&offset=0&page-size=216":
        return "11"
    elif url == "https://www2.hm.com/pl_pl/divided/shop-by-product/view-all.html?sort=stock&image-size=small&image=model&offset=0&page-size=216":
        return "12"
    elif url == "https://www2.hm.com/pl_pl/dziecko/produkty/view-all.html?sort=stock&image-size=small&image=model&offset=0&page-size=216":
        return "13"
    else:
        return "14"


def web(url):
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    products = []
    categories = [get_main_category(url)]
    if url == "https://www2.hm.com/pl_pl/divided/shop-by-product/view-all.html?sort=stock&image-size=small&image=model&offset=0&page-size=216":
        categories.append("59")
    for link in s.findAll('li', {'class': 'product-item'}):
        img_url = link.findAll('img')
        if len(img_url) > 0:
            img_url = img_url[0]
        img_url = img_url.get('data-altimage')
        products.append(extract_info('https://www2.hm.com' + link.findAll('a')[0]['href'], link.findAll('a')[0]['title'], categories, img_url))
    return products


products = []
for url in URLS:
    products += web(url)


convert_to_csv(products)
generate_combination(products)
