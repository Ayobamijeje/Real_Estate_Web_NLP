import requests
from bs4 import BeautifulSoup
from embedchain import App
from urllib.parse import urljoin, urlparse
import time
from Base import Hugging_key
from Base import Hugging_config




Hugging_key = Hugging_key()
config = Hugging_config()




def crawl_website(base_url, max_pages=2):
    visited = set()
    to_visit = [base_url]
    app = App.from_config(config=config)

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException:
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        visited.add(url)

        page_text = soup.get_text(separator=' ', strip=True)
        if page_text:
            app.add(page_text, data_type='text')
            print(f"Added content from: {url}")

        for link in soup.find_all('a', href=True):
            full_url = urljoin(base_url, link['href'])
            if base_url in full_url and full_url not in visited:
                to_visit.append(full_url)

        time.sleep(1)

    print("Crawling complete!")
    return app


