import json
import os
from typing import Dict

import requests
import re

from src.crawlers import Crawler


class ScratchCrawler(Crawler):
    def __init__(self):
        self._base_url = 'https://www.heilbronn.de/'
        regex = '<a href="[\/,\w,\.,\w]+'
        self._regex = re.compile(regex)
        self._visited_links = []
        self._pdfs = []

    def run(self, save_path='pdfs') -> Dict:
        self._visited_links = []
        self._crawl_all_websites([self._base_url])
        print('start download')
        self._pdfs = [self._download_pdf(pdf_data) for pdf_data in self._pdfs]
        json_doc = {"Result": self._pdfs}
        res = json.dumps(json_doc, indent=4, sort_keys=True)
        with open(os.path.join(save_path, "result.json"), 'w') as fd:
            fd.write(res)

        return json_doc

    def _download_pdf(self, pdf_data, chunk_size=2000, save_path='pdfs'):
        url = pdf_data['Pdflink']
        storage_path = url.split('/')[-1]
        storage_path = os.path.join(save_path, storage_path)
        r = requests.get(url, stream=True)

        with open(storage_path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size):
                fd.write(chunk)
        pdf_data['Metadata'] = {
            'Storagepath': os.path.abspath(storage_path)
        }
        return pdf_data

    def _crawl_all_websites(self, websites):
        new_websites = []
        for website in websites:
            new_websites = self._crawl_website(website)
            new_websites = list(new_websites)

        unvisited_websites = [x for x in new_websites if x not in self._visited_links]
        if len(unvisited_websites) > 0:
            self._crawl_all_websites(unvisited_websites)

    def _crawl_website(self, link):
        if link in self._visited_links:
            return
        print(f"{link} Visited: {len(self._visited_links)} Pdfs: {len(self._pdfs)}")
        self._visited_links.append(link)
        websites = ...
        try:
            r = requests.get(link, allow_redirects=True)
            html = r.content.decode()
            internal_links = re.findall(self._regex, html)
            internal_links = [x[9:] for x in internal_links]
            pdfs = [self._base_url + x for x in internal_links if x.endswith('.pdf')]
            websites = [self._base_url + x for x in internal_links if x not in pdfs]

            all_pdf_links = [y["Pdflink"] for y in self._pdfs]
            pdfs += [x for x in pdfs if x not in all_pdf_links]
            pdfs = set(pdfs)
            websites = set(websites)
            self._pdfs += [{"Websitelink": link, "Pdflink": pdf_link} for pdf_link in pdfs]
        except Exception as e:
            print(f"Error scraping website {link}\n{e}")
        return websites if websites else []
