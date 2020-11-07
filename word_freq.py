"""
Программа считает Топ-100 слов для переданного ей текстового файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""
import re
import argparse
import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords
from collections import Counter


def parser_creation():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', default='hpmor.txt', type=argparse.FileType('r'),
                        help='Specify file name for which to count word frequency')
    parser.add_argument('-c', '--count', default=100, type=int,
                        help='Number of most common words to be printed')
    parser.add_argument('-l', '--language', default='english',
                        help='Language of the text in the given file')
    return parser


def text_cleaning(text):
    cleaned_file_content = re.sub(r'[^\w]', ' ', text)
    cleaned_file_content = re.sub(r'[^\D]', ' ', cleaned_file_content).lower()
    return cleaned_file_content


if __name__ == '__main__':
    parser = parser_creation()
    # args_values = parser.parse_args('EULA.txt -c 10 -l english'.split())
    args_values = parser.parse_args()

    stop_words = stopwords.words(args_values.language)
    text = args_values.file_name.read()
    text = text_cleaning(text)

    # TODO: consider moving this part to token_and_count()
    tokenized_words = nltk.word_tokenize(text)
    for sword in stop_words:
        while sword in tokenized_words:
            tokenized_words.remove(sword)
    word_freq = Counter(tokenized_words)
    print(word_freq.most_common(args_values.count))