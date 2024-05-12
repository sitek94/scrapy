from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langsmith.wrappers import wrap_openai
from markdownify import markdownify as md
from openai import OpenAI
import argparse
import os
import re
import requests

load_dotenv()
# Wrap OpenAI API with Langsmith to trace usage
openai = wrap_openai(OpenAI(api_key=os.getenv("OPENAI_API_KEY")))


def url_to_markdown(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # Find article title and content
    article_title = soup.find("h1")
    article_content = soup.find("div", {"class": "devsite-article-body"})

    if article_content is not None and article_title is not None:
        markdown_content = (
            md(str(article_title), heading_style="ATX")
            + "\n"
            + md(str(article_content), heading_style="ATX")
        )
        return markdown_content, article_title.text
    else:
        return "No content found within div class='devsite-article-body' or h1"


def valid_filename(s):
    s = str(s).strip().replace(" ", "_").lower()
    return re.sub(r"(?u)[^-\w.]", "", s)


def cleanup_markdown(markdown_content):
    prompt = f"""
document:```{markdown_content}```

instructions:
- Clean up the document above by removing any extra spacing or characters
- Use `-` for all unordered lists
- Replace all `**` with `*`
- Return ONLY result without any comments
"""

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Follow user instructions as closely as possible",
            },
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert HTML from a URL to Markdown.")
    parser.add_argument("urls", nargs="+", help="The URLs to convert to Markdown")
    args = parser.parse_args()

    for url in args.urls:
        markdown_content, title = url_to_markdown(url)
        cleaned_content = cleanup_markdown(markdown_content)

        filename = valid_filename(title) + ".md"
        with open(filename, "w") as f:
            f.write(cleaned_content)

        print(f"Markdown content written to {filename}")
