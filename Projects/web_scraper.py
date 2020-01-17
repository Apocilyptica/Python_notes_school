import requests as req
from bs4 import BeautifulSoup as bs
from inflection import titleize

# My Solution
page = req.get("http://www.dailysmarty.com/topics/python")
soup = bs(page.text, "html.parser")

for a in soup.select(".post-link-title h2 a"):
    print((titleize((a["href"].replace("/posts/", '"')).replace("-", " ")) + '"'))


# JH Solution Don't work
"""
def title_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)


    for link in links:
        post_formatter(link["href"])


    return titles


r = req.get('http://www.dailysmarty.com/topics/python')
soup = bs(r.text, 'html.parser')
links = soup.find_all('a')
titles = title_generator(links)

for title in titles:
    print(title)
"""
