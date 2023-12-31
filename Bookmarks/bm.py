from bs4 import BeautifulSoup

# Leer el archivo HTML
with open('bookmarks.html', 'r') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')

# Buscar todos los enlaces
links = soup.find_all('a')

markdown_links = []

for link in links:
    markdown_links.append(f'[{link.text}]({link.get("href")})')

# Guardar en un archivo Markdown
with open('bookmarks.md', 'w') as f:
    f.write('\n'.join(markdown_links))