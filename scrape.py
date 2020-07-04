# https://news.ycombinator.com/robots.txt
# Crawl-delay: 30 seconds


import requests
from bs4 import BeautifulSoup
import pprint

# Get the website save the parsed html.
response = requests.get("https://news.ycombinator.com/news")
parsed_html = BeautifulSoup(response.text, 'html.parser')

# Use CSS selector to grab data.
article_links = parsed_html.select('.storylink')
art_subtext = parsed_html.select('.subtext')


def create_custom(links, subtext):
    """Creates a list of article names and their links."""
    news_list = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        subtext_votes = subtext[index].select('.score')
        # If article has votes, convert to int, drop "points" suffix.
        if len(subtext_votes):
            votes = int(subtext_votes[0].getText().replace(' points', ''))
            # If votes are > 99, append to list.
            if votes > 99:
                news_list.append({'title': title, 'link': href, 'votes': votes})
    return news_list


pprint.pprint(create_custom(article_links, art_subtext))



