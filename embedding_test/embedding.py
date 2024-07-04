import os
from typing import Dict, List
from dotenv import load_dotenv
import openai
import json
import numpy as np
import pandas as pd
from test_strings import class_definitions

# Setzen Sie Ihren API-Schlüssel hier ein
# Lade Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Zugriff auf die Umgebungsvariablen
api_key = os.getenv('OPENAI-API_KEY')
client = openai.OpenAI(api_key=api_key)

def embed_text(text):
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    embedding = response.data[0].embedding
    return embedding

def cosine_similarity(vec1, vec2):
    """Berechnet die Kosinusähnlichkeit zwischen zwei Vektoren."""
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    similarity = dot_product / (norm_vec1 * norm_vec2)
    return similarity

# Run embedding and store in dict:
# class_embeddings : Dict[str, List[float] ] = dict()
# for class_definition in class_definitions:
#     embedding = embed_text(class_definitions.get(class_definition))
#     class_embeddings[class_definition] = embedding

# # Schreiben des Dictionaries in eine JSON-Datei
# with open('data.json', 'w') as f:
#     json.dump(class_embeddings, f)

with open('data.json', 'r') as file:
    class_embeddings = json.load(file)

# Beispieltexte
n = len(class_definitions)
similarity_matrix = pd.DataFrame(index=range(n), columns=range(n))
embedding_values = list(class_embeddings.values())
# Berechnung der Kosinusähnlichkeit für jedes Paar
for i in range(n):
    for j in range(n):
        if i <= j:  # Kosinusähnlichkeit ist symmetrisch
            similarity = cosine_similarity(embedding_values[i], embedding_values[j])
            similarity_matrix.loc[i, j] = similarity
            similarity_matrix.loc[j, i] = similarity

# Setzen der Spalten- und Zeilenbeschriftungen
similarity_matrix.columns = pd.Index([f"{list(class_embeddings.keys())[i]}" for i in range(n)])
similarity_matrix.index = pd.Index([f"{list(class_embeddings.keys())[i]}" for i in range(n)])

print(similarity_matrix)

# Schreiben des DataFrames in eine Excel-Datei
similarity_matrix.to_excel('Beispiel_ada-2.xlsx', index=False, engine='openpyxl')