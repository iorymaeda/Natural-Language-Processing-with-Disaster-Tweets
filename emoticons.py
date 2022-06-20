import re
import json
import pickle


import bs4
import requests
from bs4 import BeautifulSoup


def proces_text(text:str) -> str:
    text = text.lower()
    text = text.replace('\n', '')
    text = text.strip()
    return text


if __name__ == "__main__":
    vocab = {}

    resp = requests.get('https://en.wikipedia.org/wiki/List_of_emoticons')
    soup = BeautifulSoup(resp.text)
    tables = soup.find_all('table', attrs={'class': 'wikitable'})

    table_num = [0, 1, 2, 4, 5, 6]
    for idx, table in enumerate(tables):
        try:
            if table.attrs['class'] == ['wikitable'] and idx in table_num:
                trs = table.find('tbody').find_all('tr')
                for row in trs[1:]:
                    tds = row.find_all('td')
                    emoticons = []
                    meaning = proces_text(re.sub(r'\[\d+\]', '', tds[-1].text))
                    meaning = meaning.split(',')[0]
                    for td in tds[:-1]:
                        for child in td.children:
                            if child != bs4.element.Tag(name='br'):
                                child = proces_text(child.text)
                                if child:
                                    emoticons.append(child)



                    for emote in emoticons:
                        vocab[emote] = meaning
        except:
            pass

    for k, v in vocab.items():
        print(k, v, sep=' : ')

    with open('data/emoticons.pkl', 'wb') as f:
        pickle.dump(vocab, f)

    with open("data/emoticons.json", "w") as fp:
        json.dump(vocab , fp) 

        