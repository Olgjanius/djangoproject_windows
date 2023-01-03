
# Coding
#!pip install tensorflow
#!pip install biobert_bern
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from spacy.lang.ja.syntax_iterators import labels
# for tokenizer
from transformers import AutoTokenizer
# for model
from transformers import AutoModel, AutoTokenizer
from wasabi.util import input_
# import of model (default Wert emilyalsentzer/BioBert-Base)
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
# convert the text in token (input_ids is a vector, contains the token-id for each word in the inputtext)
with open('../corporasource/corpus.txt', 'w+') as file:
    input_text = file.read()
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    # load the Biobert_model and the tokenizer
    model = AutoModel.from_pretrained("bert-base-uncased")
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    # implement the Tokenizer for Text
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    # prognose
    output = model(input_ids)
    print(output)
# write
with open('../docsources/text3.txt', 'w+') as file:
    # text write in the file
    file.write(str(output))
import matplotlib.pyplot as plt
from PIL import Image
# Extract the values from the last_hidden_state tensor
values = output.last_hidden_state.detach().numpy()[0]
# Plot the values
plt.plot(values)
# Save the plot to a file
plt.savefig('plot.png')

"""Interpretation des Graphen aus dem Ausgabefile "plot.png":
Die Linien mit negativer Steigung, die nach unten verlaufen, deuten darauf hin, dass die Werte des letzten versteckten Zustandes
 für einige wenige Tokens in der Eingabesequenz niedriger sind als für die anderen Tokens. Dies könnte bedeuten, 
dass diese Tokens im Vergleich zu den anderen Tokens weniger wichtig oder relevant für die Ausgabe des BertModels sind."""