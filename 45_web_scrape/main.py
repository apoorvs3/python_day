from bs4 import BeautifulSoup
# imp ort lxml

with open('website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.a)
# print(soup.li.string)
#
anchor_tags = soup.findAll(name='a')
# para_tags = soup.findAll(name='p')
# print(anchor_tags)
# print(para_tags)

for anchors in anchor_tags:
    # print(anchors.getText())
    # print(anchors.get("href"))
    pass

headings = soup.find(name='h1', id='name')
# print(headings)
# section_heading = soup.find(name='h3', class_="heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))
company_url = soup.select_one(selector="p a")
print(company_url)
print(soup.select_one(selector="#name"))

print(soup.select(selector=".heading"))
