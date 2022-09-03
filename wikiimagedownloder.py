import bs4
import requests
import os

def downloadimageof(search):
    path = "https://en.wikipedia.org/wiki/"
    path = path + search
    print(path)
    try:
        os.mkdir(os.path.join(os.getcwd(), search))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), search))

    raw = requests.get(path).text

    soup = bs4.BeautifulSoup(raw, "lxml")
    a = soup.find_all("img")
    number = 1
    for i in a:
        if ".jpg" in i["src"]:
            elink = "http:" + i["src"].replace("thumb/", "")
            j = elink.find(".jpg")
            ilink = elink[0:(j + 4)]

            name = ilink.replace("/", "").replace("commons","").replace("wikipedia","").replace(".", "").replace("http:", "").replace("jpg", "").replace("uploadwiki",
                                                                                                           "") + ".jpg"

            with open(name, "wb") as l:
                down = requests.get(ilink)
                l.write(down.content)
            print("writing  ", name, "  ", number, " of ", len(a))
            number += 1

search=input("search wiki page to scrap")
downloadimageof(search)



