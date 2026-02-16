# Advanced AI: Neural Networks — Hands-on Notebooks

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SybrandWildeboer/neural_networks_training_advanced_ai/main)

Interactieve notebooks bij de training **Advanced AI: Neural Networks** van D-Data.

De repository is opgesplitst in:
- `demos/` → klassikale demo-notebooks
- `exercises/` → opdrachten voor deelnemers
- `answers/` → uitwerkingen voor trainer of zelfcontrole

## Leerroute (aanbevolen volgorde)

| # | Notebook | Onderwerp | Duur |
|---|----------|-----------|------|
| 0 | `demos/00_Basis_ML_Supervised_Unsupervised.ipynb` | Supervised vs unsupervised, K-Means, KNN, train/val/test split | ~30 min |
| 0B | `demos/00B_Logistische_Regressie.ipynb` | Logistische regressie als brug naar neural nets | ~25 min |
| 1 | `demos/01_Churn_Neural_Network.ipynb` | Neural Network trainen voor churn-voorspelling | ~30 min |
| 2 | `demos/02_MNIST_Getalherkenning.ipynb` | Getalherkenning met een Neural Network | ~20 min |
| 3 | `demos/03_BERT_Tokenizer.ipynb` | Hoe tokenization werkt in taalmodellen | ~15 min |
| 4 | `demos/04_Word_Embeddings.ipynb` | Word embeddings begrijpen en visualiseren | ~20 min |
| 5 | `demos/05_Topic_Classificatie_SKLearn.ipynb` | Simpele topic-classificatie met scikit-learn | ~20 min |
| 6 | `demos/06_Text_Generatie.ipynb` | Tekst genereren met een simpel model | ~15 min |

## Oefenen

| Type | Notebook | Doel |
|---|---|---|
| Oefening | `exercises/01_Iris_Classificatie_Opdracht.ipynb` | Deelnemers bouwen zelf een eenvoudige classifier |
| Antwoorden | `answers/01_Iris_Classificatie_Uitwerking.ipynb` | Volledige uitwerking met modelselectie en evaluatie |

## Starten

### Optie 1: Binder (geen account nodig)
Klik op de Binder-badge hierboven. Het kan 1-2 minuten duren om de omgeving op te starten.

### Optie 2: Lokaal
```bash
pip install -r requirements.txt
jupyter notebook
```

## Instructies voor deelnemers

1. Klik op de Binder-link die je van de trainer hebt gekregen
2. Wacht tot de omgeving is opgestart
3. Open het notebook dat de trainer aangeeft
4. Voer de cellen uit met **Shift+Enter** of via de ▶️ knop bovenaan
5. **Let op**: Binder-sessies verlopen na ~10 minuten inactiviteit

## Opmerkingen
- Alle notebooks draaien **zonder GPU** en zijn geoptimaliseerd voor Binder
- Alle notebooks gebruiken scikit-learn en/of gensim
- De dataset voor notebook 1 zit in de `data/` map
