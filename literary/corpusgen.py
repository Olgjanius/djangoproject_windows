"""
with open('../docsources/MACCROBAT2020onlytxt/15939911.txt', 'r') as file:
    # Leeren der Liste, die die Texte im Corpus enthalten wird
    corpus = []
    # Iterieren über jede Zeile in der .txt-Datei
    for line in file:
        # Hinzufügen der Zeile zur Liste
        corpus.append(line)"""
# Coding
import os
# generate and open the new text file for write
with open('corpus.txt', 'w') as corpus_file:
    startfile = "../docsources/MACCROBAT2020onlytxt/15939911.txt"
    # iterate in the directory for read from text
    for file in os.listdir('../corporasource/MACCROBAT2020onlytxt'):
        # control for existence of the text file
        if file.endswith('.txt'):
            # open the text file for read
            with open(startfile, 'r') as file:
                # iterated through the lines for write
                for line in file:
                    # write in the corpus file
                    corpus_file.write(line)
