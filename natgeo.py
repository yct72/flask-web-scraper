import requests
from bs4 import BeautifulSoup

titles = []; links = []; dates = []

def get_soup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'lxml')
    soup.encoding = 'utf-8'
    return soup

def get_topic(soup, class_name):
    articles = soup.find_all('div', class_name)
    for a in articles:
        node = a.find('h4')
        if node:
            node = node.find('a')
        else:
            continue
        title = node.text.strip()
        if title not in titles:
            titles.append(title)
            links.append(node['href'])
            dates.append(node.find_parent('h4').find_previous_sibling('h6').text)

def get_natgeo():
    # root 
    root = 'https://www.natgeomedia.com/'
    soup = get_soup(root)
    categories = soup.find(attrs={'class': 'menu-content menu-left'}).find_all('a')
    category_links = []
    for category in categories:
        category_links.append(root + category['href'])

    # go to topic - science
    soup = get_soup(category_links[0])
    

    # large
    classes = ['art-btn-la-content', 'art-btn-s-content', 'artcle-btn-mv', 'art-btn-mh-content']
    for c in classes:
        get_topic(soup, c)

    data = [{'title': t, 'link': l, 'date': d} for t, l, d in zip(titles, links, dates)]
    return data

if __name__ == '__main__':
    data = get_natgeo()
    print(data)
