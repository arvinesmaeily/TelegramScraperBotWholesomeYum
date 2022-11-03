
from bs4 import BeautifulSoup, NavigableString, Tag
import requests as r
import asyncio

def scrape_recipe(recipe):
    
    recipe = str(recipe)
    recipe = recipe.lower().replace(" ", "-")
    
    base_url = "https://www.wholesomeyum.com/"
    url = base_url + recipe +"/"

    res = r.request('GET', url).content

    soup = BeautifulSoup(res, 'html.parser')

    #extract title
    title = soup.title.contents[0]
    title = str(title).split("|")[0]

    #extract image
    img = soup.find("img", class_="exclude-lazyload featured-img wp-post-image")
    img = img['src']
    
    #extract headers
    items = []
    counter = 0
    for item in soup.findAll("span",class_="lwptoc_item_label", recursive=True):
        counter += 1

        items.append(str(counter) + ". " + item.contents[0])

    # extract context
    cont = soup.find('div', class_="entry-content",recursive=True)

    list_string = []
    for i in cont:
        msg = ""
        for j in i.stripped_strings:
            if str(j).strip('\n') != None or str(j).strip() != "\n":

                msg += str(j) + " "
        if len(msg) != 0:
            list_string.append(msg)

    list_string.pop(0)
    list_string.pop(0)
    list_string.pop(0)
    
    list_string.pop()
    list_string.pop() 

    return { "title" : title, "image" : img, "context" : list_string }