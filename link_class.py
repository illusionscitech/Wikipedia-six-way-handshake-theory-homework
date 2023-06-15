# -*- coding: utf-8 -*-
# @Time ： 08.06.2023 20:02
# @Auth ： 张卓 zhang zhuo Чжан Чжо
# @File ：link_class.py
# @IDE ：PyCharm
# @Motto：To live is to change the world.
import requests
import urllib.request,urllib.error
from bs4 import BeautifulSoup
import time

class WikiLinkFinder:
    def __init__(self, start_url, target_url, rate_limit,root_url,start_time):
        self.start_url = start_url
        self.target_url = target_url
        self.root_url = root_url
        self.rate_limit = rate_limit
        self.st_time = start_time
        self.visited = set()
        self.queue = [[start_url]]


    def get_wiki_links(self, url):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = []

        # link_div = soup.find('div', {'class': 'mw-parser-output'})
        #vector-body ve-init-mw-desktopArticleTarget-targetContainer
        link_div = soup.find('div', {'class': 'vector-body'})
        if link_div:
            con_links = link_div.find_all('a', href=True)
            links += [link['href'] for link in con_links]

        return links

    def find_link_chain(self):
        while self.queue:
            path = self.queue.pop(0)
            cur_url = path[-1]
            if len(path) == 3:
                print("time:", round(time.time() - self.st_time, 2), " s ,up one level:", path[-2], "->current_url:",
                      cur_url)
            elif len(path) == 4:
                print("time:", round(time.time() - self.st_time, 2), " s ,up two level:", path[-3],"->up one level:", path[-2], "->current_url:",
                      cur_url)
            elif len(path) == 5:
                print("time:", round(time.time() - self.st_time, 2), " s ,up three level:", path[-4],"->up two level:", path[-3],"->up one level:", path[-2], "->current_url:",
                      cur_url)
            else:
                print("time:",round(time.time()-self.st_time,2)," s ,current_url:", cur_url)

            if cur_url == self.target_url:
                return path

            if cur_url in self.visited or len(path) > self.rate_limit:
                continue

            self.visited.add(cur_url)
            print("len(path):", len(path))

            links = self.get_wiki_links(cur_url)
            # print(links)
            for link in links:
                if link.startswith('/wiki/'):
                    next_url = self.root_url + link
                    new_path = list(path)
                    new_path.append(next_url)
                    self.queue.append(new_path)
        return None
