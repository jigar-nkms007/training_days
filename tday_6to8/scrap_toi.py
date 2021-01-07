from bs4 import BeautifulSoup as soup
import requests
import os

myurl = 'https://timesofindia.indiatimes.com'

page = requests.get(myurl)
page_html = page.content

page_soup = soup(page_html, 'html5lib')
html = page_soup.decode('utf-8')



directoty='newsheadlines'
parente_directory='/home/hiren/PycharmProjects/practice/tday_6to8'

path=os.path.join(parente_directory,directoty)
os.mkdir(path)



def pagedata(a,c):
    if a.find('//') == 6:
        b = a
    else:
        b = myurl + a

    d=c[0:6]
    filename=os.path.join(path,d+'.txt')
    f=open(filename,'w+')
    f.write(c)
    f.write('\n')

    page1 = requests.get(b)
    page_html1 = page1.content

    page_soup1 = soup(page_html1, 'html5lib')

    if page_soup1.find('div', {'class': 'ga-headlines'}):
        f.write(page_soup1.find('div', {'class': 'ga-headlines'}).text)
    elif page_soup1.find('div', {'class': 'Normal'}):
        f.write(page_soup1.find('div', {'class': 'Normal'}).text)
    elif page_soup1.find('div', {'class': 'photo_desc'}):
        f.write(page_soup1.find('div', {'class': 'photo_desc'}).text)
    f.close()


def loop(ultag):
    for litag in ultag.findAll('li'):
        for atag in litag.findAll('a'):
            if atag.get('title'):
                c=atag.attrs['title']
                if atag.get('rel'):
                    break
                else:
                    a = atag.attrs['href']
                    pagedata(a,c)


containers = page_soup.find('div', {'class': 'top-story'})
for ultag in containers.findAll('ul', {'class': 'list8'}):
    loop(ultag)

containers1 = page_soup.find('div', {'class': 'latestNewContainer'})
for ultag in containers1.findAll('ul', {'class': 'list9'}):
    loop(ultag)

containers2 = page_soup.find('div', {'class': 'toicity toi-widgets'})
for ultag in containers2.findAll('ul', {'class': 'list2'}):
    loop(ultag)

containers3 = page_soup.find('div', {'class': 'widget'})
for ultag in containers3.findAll('ul', attrs={'id': 'col1_latest'}):
    loop(ultag)