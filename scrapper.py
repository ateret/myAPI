import requests
import json
from bs4 import BeautifulSoup as soup
from collections import Counter


def letter_count(text):
    return Counter(c for c in text.lower() if c.isalpha())


def count_vovels(data: str) -> int:
    vovel_number = 0
    for letter in data:
        if letter in ('a', 'e', 'o', 'u', 'i', 'y'):
            vovel_number += 1
    return (vovel_number)


def get_statistics(url: str) -> dict:
    response = requests.get(url)
    print(response)

    if response.status_code != 200:
        print('Nie można otworzyć stony')
        return

    html_data = soup(response.text, 'html.parser')
    znaczniki_a = html_data.find_all('a')
    znaczniki_p = html_data.find_all('p')

    vovel_counter = 0
    word_counter = 0
    letter_counter = dict()


    for a in znaczniki_a:
        text = a.text
        number_of_words = a.text.split(' ')
        word_counter += len(number_of_words)
        dict_of_letters = letter_count(text)
        vovel_counter += count_vovels(a.text)
        for letter,value in dict_of_letters.items():
            if letter_counter.get(letter,None):
                letter_counter[letter] += value
            else:
                letter_counter[letter] = value

    most_frequent_letter = (max(letter_counter,key=letter_counter.get))
    return {
        'Number of words': word_counter,
        'Number of Vovels': vovel_counter,
        'Most frequent letter': most_frequent_letter
    }


print(get_statistics('https://pl.wikipedia.org/wiki/Iga_%C5%9Awi%C4%85tek'))
