from bs4 import BeautifulSoup
import requests

# response = requests.get("https://news.ycombinator.com/news")
with open('xyz.html', "r") as file:
    content = file.read()

yc_webpage = content
soup = BeautifulSoup(yc_webpage, 'html.parser')

# title
# article_text = soup.select_one(selector='td .title span a')
# print(article_text.string)

# another method
x = soup.findAll(name='span', class_='titleline')

article_texts = [article_text.a.string for article_text in x]
article_links = [article_link.a.get('href') for article_link in x]
article_upvotes = [int(scores.getText().split()[0]) for scores in soup.findAll(name='span', class_='score')]

print(article_links)
print(article_texts)
print(article_upvotes)

max_position = article_upvotes.index(max(article_upvotes))
print('#####################')

print(article_texts[max_position])
print(article_links[max_position])
print(article_upvotes[max_position])