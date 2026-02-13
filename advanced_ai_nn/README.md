# Advanced AI: Neural Networks — Hands-on Notebooks

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SybrandWildeboer/neural_networks_training_advanced_ai/main)

Interactieve notebooks bij de training **Advanced AI: Neural Networks** van D-Data.

## Notebooks

| # | Notebook | Onderwerp | Duur |
|---|----------|-----------|------|
| 1 | `01_Churn_Neural_Network.ipynb` | Neural Network trainen voor churn-voorspelling | ~30 min |
| 2 | `02_MNIST_Getalherkenning.ipynb` | Getalherkenning met een Neural Network | ~20 min |
| 3 | `03_BERT_Tokenizer.ipynb` | Hoe tokenization werkt in taalmodellen | ~15 min |
| 4 | `04_Word_Embeddings.ipynb` | Word embeddings begrijpen en visualiseren | ~20 min |
| 5 | `05_Text_Generatie.ipynb` | Tekst genereren met een simpel model | ~15 min |

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
- Geen PyTorch of TensorFlow nodig — we gebruiken scikit-learn en gensim
- De dataset voor notebook 1 zit in de `data/` map
