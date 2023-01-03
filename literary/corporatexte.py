import nltk
import pandas as pd
import os

from nltk.corpus import stopwords
from nltk.corpus import gutenberg
from nltk.corpus import brown


import re
import string
import unidecode

# Examples
# 1. Text Preprozessing
class infocleanup:
    # 1a. Stopwords definieren und ausgeben
    stopwords_en = stopwords.words('english')
    print("Anzahl engliche Stopwörter:  ", len(stopwords_en))
    print("Engliche Stopwörter:  ", ','.join(stopwords_en))

    fileidsgut = " |  ".join(gutenberg.fileids())
    fileidsbrown = brown.categories()
    print('gutenberg: ', fileidsgut)
    print('brown:  ', ','.join(fileidsbrown))

# info: stopwords biomedicine https://figshare.com/articles/dataset/Stopwords_/21263389

class sortingwords:
    # Freq_Dist ermöglicht, eine Sammlung von Häufigkeitsverteilungen zu erstellen
    # (wie oft ein Wort in einem Text verwendet worden ist)
    learned_text = brown.words(categories='learned')
    freq_dist = nltk.FreqDist(w.lower() for w in learned_text)
    # Nach Worthäufigkiet sortieren
    stopwords_en = stopwords.words('english')
    # sorted_freq_dist = {k: v for k, v in sorted(freq_dist.items(), key=lambda item: item[1], reverse=True)}
    # for k,v in sorted_freq_dist.items():
    # if k not in stopwords_en:
    # print(f"{k}: {v}")

    # ConditionalFreqDist ermöglicht, eine Sammlung von Häufigkeitsverteilungen nach eine Bedingung (z.B. genre) zu erstellen


class conditional:
    stopwords_en = stopwords.words('english')
    brown_categories = brown.categories()
    conditionals = []
    for genre in brown.categories():
        for word in brown.words(categories=genre):
            conditionals.append((genre, word))
    conditionals[:10]
    cfd_genre = nltk.ConditionalFreqDist(conditionals)
    cfd_genre.tabulate(conditions=brown_categories, samples=stopwords_en[:10])  # nur die ersten 10 engl. Stopwörter
    # Stopworter in anderen Sprachen
    print("Russische Stopwörter:  ", ",".join(stopwords.words("russian")))
    print("Deutsche Stopwörter:  ", ",".join(stopwords.words("german")))


# print("/nSprachen:  ", os.listdir("file:///olgadakischew/nltk_data/corpora/stopwords")
# Texte bereinigen mit REGEXE
class cleanreg:
    text = "Ein Regular Expression, oder 'regex', ist ein Muster, nach dem in einer Textzeichenfolge\
         gesucht wird. In NLP werden regexes häufig zur Textbereinigung verwendet.\
         Ein Regular Expression, oder 'regex', ist ein Muster, nach dem in einer Textzeichenfolge\
         gesucht wird. In NLP werden regexes häufig zur Textbereinigung verwendet."

    # findet nur das Wort "regex"
    regex_pattern = re.compile('regex')
    print(re.findall(regex_pattern, text))

    # Findet alle Eventuelitäten
    regex_pattern_improved = re.compile('regular expression|regex[es]*', re.I)  # re.I ist re.IGNORECASE
    print(re.findall(regex_pattern_improved, text))
    # Mehr dazu: https://docs.python.org/3/library/re.html
with open('../docsources/text.txt', 'w+') as file:
    # dataframe wird nicht in file geschrieben:
    file.write("Stopwords english:" + stopwords.words("english"))
    file.write("regex" + re.findall(regex_pattern_improved, text))
    #file.write("Dataframe as string in lowercase cleaned:" + dataframe)