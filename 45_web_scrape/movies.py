from bs4 import BeautifulSoup

# response = requests.get(url='https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')

with open("xyz.txt", mode='r') as file:
    content = file.read()
soup = BeautifulSoup(content, 'html.parser')

headings = soup.findAll(name='h3')

# update movies in a text file
fi = open("movies_100.txt", mode='w')
num = 1
for heading in headings:
    movie = ''
    title_list = heading.text.split(' ')[1:]
    for title in title_list:
        movie += title + ' '
    fi.write(f"{num}) {movie.strip()}\n")
    num += 1

fi.close()
