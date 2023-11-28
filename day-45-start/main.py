from bs4 import BeautifulSoup
import requests



response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")


articles = soup.find_all(name="a", rel="noreferrer")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


print(max(article_upvotes))
largest_index = article_upvotes.index(max(article_upvotes))
print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])






















# import lxml
#
# with open("website.html") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
#
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
