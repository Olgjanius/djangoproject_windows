"""
Hier kann pip nicht tabolism installieren!
# Laden des vortrainierten Bert-Modells
model = BertModel.from_pretrained("bert-base-uncased")

# Erfragen der Gewichte des Modells
weights = model.state_dict()
print(weights)

# Laden des BertTokenizers
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Tokenisieren des Textes
tokens = tokenizer.tokenize("Mein Text zum Tokenisieren")
print(tokens)

# Encodieren des Tokenized-Textes
encoded_tokens = tokenizer.encode(tokens)
print(encoded_tokens)

# Verwenden des vortrainierten Bert-Modells zur Vorhersage
output = model(torch.tensor([encoded_tokens]))
print(output)

# Öffnen der Datei zum Schreiben
with open("text4.txt", "w") as f:
    # Schreiben der Metriken in die Datei
    f.write(str(output))

import matplotlib.pyplot as plt
import seaborn as sns

# Laden der TABOLISTM-Bibliothek
!pip install tabolistm
from tabolistm import TaboListM

# Tokenisieren und Encodieren der Wortsequenzen
seq1_tokens = tokenizer.tokenize("resistant to immunosuppressive drugs")
seq1_encoded = tokenizer.encode(seq1_tokens)

seq2_tokens = tokenizer.tokenize("tumour as an infiltrating")
seq2_encoded = tokenizer.encode(seq2_tokens)

# Erstellen der TaboListM-Instanz und  Parametrisieren der encodierten Wortsequenzen
tabolistm = TaboListM(model)
tabolistm.add_sequence(seq1_encoded)
tabolistm.add_sequence(seq2_encoded)

# Visualisierung der Analyse
sns.heatmap(tabolistm.attention_matrix, annot=True, xticklabels=seq1_tokens, yticklabels=seq2_tokens)
plt.show()
"""
