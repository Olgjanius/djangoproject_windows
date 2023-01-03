import tensorflow as tf
import pandas as pd
from spacy.lang.ja.syntax_iterators import labels
from transformers import BertTokenizer, BertForSequenceClassification
# Load the corpus file
with open("corpus.txt", "r", encoding="utf-8") as f:
  corpus = f.read()

# Tokenize the input data
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
input_ids = tokenizer.encode(corpus, add_special_tokens=True, max_length=64, pad_to_max_length=True)
input_ids = tf.convert_to_tensor([input_ids])
attention_masks = tf.ones_like(input_ids)

# Schritt 1: Erfragen der Gewichte von dem vortrainiertem Bert-base-uncased
import transformers
import torch
model = transformers.BertModel.from_pretrained('bert-base-uncased')
model_weights = model.state_dict()
print(model_weights)

# Schritt 2: Analysieren von fertigem output nach BertTokenizer
from transformers import BertTokenizer

# Initialisieren des Tokenizers
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Tokenisieren des Texts
text = "resistant to immunosuppressive drugs"
tokens = tokenizer.tokenize(text)
print(tokens)

# Schritt 3: Vorhersage mit vortrainiertem Bert-base-uncased
input_ids = tokenizer.convert_tokens_to_ids(tokens)
input_ids = torch.tensor([input_ids]).cpu()

output = model(input_ids)
print(output)

# Schritt 4: Schreiben der Metriken in die Datei "text5.txt"
with open("../docsources/text5.txt", "w+") as f:
    f.write("Gewichte des vortrainierten Modells:")
    for key, value in model_weights.items():
        f.write(f"\n{key}: {value}")
    f.write("\n\nTokenisierter Text:")
    f.write("\n" + " ".join(tokens))
    f.write("\n\nVorhersage:")
    f.write(str(output))
