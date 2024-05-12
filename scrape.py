import requests
from markdownify import markdownify as md
import argparse
from bs4 import BeautifulSoup

def url_to_markdown(url):
  response = requests.get(url)
  response.raise_for_status()  # Ensure the request was successful
  soup = BeautifulSoup(response.text, 'html.parser')
  
  # Find the title of the article
  article_title = soup.find('h1')
  article_content = soup.find('div', {'class': 'devsite-article-body'})
  
  if article_content is not None and article_title is not None:
    markdown_content = md(str(article_title), heading_style="ATX") + "\n" + md(str(article_content), heading_style="ATX")
    return markdown_content
  else:
    return "No content found within div class='devsite-article-body' or h1"

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Convert HTML from a URL to Markdown.')
  parser.add_argument('url', help='The URL to convert to Markdown')
  args = parser.parse_args()

  # Example usage
  print(url_to_markdown(args.url))