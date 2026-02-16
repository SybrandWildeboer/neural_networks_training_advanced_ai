ANSWER_KEY = {
    1: {
        'correct': 'A',
        'explanation': "Voor spam detectie heb je supervised learning nodig omdat je wilt classificeren (spam/geen spam). Supervised learning vereist gelabelde data, dus je moet eerst de e-mails handmatig labelen. Unsupervised learning (zoals K-means) kan wel patronen vinden maar weet niet welke patronen 'spam' zijn zonder labels.",
        'question_text': "Je wilt een model trainen om te voorspellen of een e-mail spam is. Je hebt 10.000 e-mails maar geen labels. Wat moet je eerst doen?"
    },
    2: {
        'correct': 'D',
        'explanation': "Dit is een klassiek geval van overfitting. Het model heeft de trainingsdata te goed geleerd (98%), inclusief ruis en details die niet belangrijk zijn. Hierdoor presteert het slecht op nieuwe data (65%). Bij underfitting zou zowel train als test score laag zijn. Het grote verschil tussen train en test performance is het kenmerk van overfitting.",
        'question_text': "Je model heeft 98% accuracy op trainingsdata en 65% op testdata. Wat is hier aan de hand?"
    },
    3: {
        'correct': 'C',
        'explanation': "Bij kNN met k=5 kijk je naar de 5 dichtstbijzijnde buren en classificeer je het nieuwe punt als de meest voorkomende klasse onder die 5. Bijvoorbeeld: als 3 buren klasse 'A' hebben en 2 klasse 'B', wordt het nieuwe punt klasse 'A'. Het gemiddelde berekenen (B) is voor regressie, niet classificatie.",
        'question_text': "Bij K-Nearest Neighbors (kNN) met k=5, hoe bepaal je de klasse van een nieuw datapunt?"
    },
    4: {
        'correct': 'D',
        'explanation': "Activation functions voegen non-lineariteit toe aan het netwerk. Zonder non-lineariteit zou het netwerk alleen rechte lijnen kunnen leren, hoe diep het ook is. Door non-lineariteit kunnen neural networks complexe patronen herkennen zoals krommen, cirkels, en andere niet-lineaire vormen in data.",
        'question_text': "Wat is de belangrijkste reden waarom we activation functions gebruiken in neural networks?"
    },
    5: {
        'correct': 'C',
        'explanation': "Als de loss wild schommelt, is de learning rate waarschijnlijk te hoog. De optimizer neemt dan te grote stappen en springt steeds over het minimum heen. Een te lage learning rate (A) zou juist resulteren in hele langzame maar stabiele vooruitgang. Te veel data (B) zou juist helpen, niet schaden.",
        'question_text': "Je training loss schommelt wild heen en weer en convergeert niet. Wat is de meest waarschijnlijke oorzaak?"
    },
    6: {
        'correct': 'B',
        'explanation': "Forward propagation gaat van input naar output en berekent de voorspelling van het netwerk. Backward propagation (backpropagation) gaat van output terug naar input en berekent de gradiënten om de gewichten te updaten. Beide zijn nodig tijdens training: forward voor voorspelling, backward voor leren.",
        'question_text': "Wat is het verschil tussen forward en backward propagation?"
    },
    7: {
        'correct': 'A',
        'explanation': "Mean Squared Error (MSE) wordt gebruikt voor regressieproblemen, waarbij je een continu getal voorspelt. Voorbeelden: huizenprijzen, temperatuur, omzet, leeftijd. Voor classificatie (kiezen uit categorieën) gebruik je cross-entropy of andere classificatie loss functions.",
        'question_text': "Wanneer gebruik je Mean Squared Error (MSE) als loss function?"
    },
    8: {
        'correct': 'C',
        'explanation': "Convolutional Neural Networks (CNNs) zijn specifiek ontworpen voor beeldverwerking. Ze gebruiken convolutional layers die ruimtelijke patronen herkennen (zoals randen, vormen, texturen). RNNs en LSTMs zijn voor sequentiële data zoals tekst. Feedforward networks zijn algemeen maar niet gespecialiseerd in beelden.",
        'question_text': "Welk type neural network is specifiek ontworpen voor beeldverwerking en herkent ruimtelijke patronen?"
    },
    9: {
        'correct': 'B',
        'explanation': "Tokenization breekt woorden op in subword-eenheden (tokens). Als het model 'running' kent, heeft het waarschijnlijk tokens zoals 'run' en 'ning' geleerd. Wanneer het dan 'outrunning' ziet, kan het dit herkennen als 'out' + 'run' + 'ning' - alle bekende tokens. Zo kan het model omgaan met nieuwe samengestelde woorden.",
        'question_text': "Waarom kan een model met tokenization beter omgaan met het woord 'outrunning' als het 'running' wel maar 'outrunning' niet gezien heeft?"
    },
    10: {
        'correct': 'A',
        'explanation': "In een embedding ruimte liggen woorden dicht bij elkaar als ze vergelijkbare betekenissen hebben en in vergelijkbare contexten gebruikt worden. 'King' en 'queen' zijn beide monarchen, komen in vergelijkbare zinnen voor ('the king/queen ruled'), en hebben semantische overeenkomsten. De afstand weerspiegelt betekenisverwantschap, niet letterlijke spelling.",
        'question_text': "In een word embedding ruimte liggen 'king' en 'queen' dicht bij elkaar. Wat betekent dit?"
    },
    11: {
        'correct': 'D',
        'explanation': "Dit toont aan dat semantische relaties (zoals gender) gevangen worden als richtingen in de vector ruimte. Het verschil tussen 'King' en 'Man' representeert 'royalty', en als je die richting toepast op 'Woman' kom je bij 'Queen'. Dit is een krachtig bewijs dat embeddings betekenisvolle structuur bevatten.",
        'question_text': "De relatie 'King - Man + Woman ≈ Queen' in word embeddings toont:"
    },
    12: {
        'correct': 'B',
        'explanation': "Cosine similarity meet de hoek tussen twee vectors, niet hun absolute afstand of lengte. Twee vectors die in dezelfde richting wijzen (klein hoek) hebben hoge similarity, zelfs als ze verschillende lengtes hebben. Dit is handig voor word embeddings omdat de richting de betekenis representeert. Deze maat wordt ook gebruikt in RAG modellen.",
        'question_text': "Cosine similarity meet de afstand tussen word embeddings. Wat meet het precies?"
    },
    13: {
        'correct': 'C',
        'explanation': "Het belangrijkste voordeel van LSTM is dat het informatie over langere tijd kan onthouden. Een standaard RNN heeft moeite om relaties te leggen tussen woorden die ver uit elkaar staan. LSTM lost dit op met zijn Cell State en gates die bepalen wat onthouden en vergeten wordt.",
        'question_text': "Wat is het belangrijkste voordeel van een LSTM ten opzichte van een standaard RNN?"
    },
    14: {
        'correct': 'A',
        'explanation': "Bij 'Peter' wisselt het onderwerp. De Forget Gate moet Anna als hoofdpersoon vergeten (niet meer relevant), en de Input Gate moet Peter als nieuw onderwerp toevoegen. Dit is een klassiek voorbeeld van hoe LSTM selectief informatie update: oud weg, nieuw erbij. Beide gates werken samen om de transitie te maken.",
        'question_text': "Bij 'Anna liep door het park. Peter zat thuis.' - welke gates zijn actief bij 'Peter'?"
    },
    15: {
        'correct': 'D',
        'explanation': "Een LSTM heeft 3 gates: (1) Forget Gate die bepaalt wat vergeten wordt, (2) Input Gate die bepaalt wat nieuw wordt toegevoegd aan het geheugen, en (3) Output Gate die bepaalt wat gedeeld wordt met de volgende laag. Deze 3 gates werken samen met de Cell State om slim te onthouden en vergeten.",
        'question_text': "Hoeveel gates heeft een LSTM om te bepalen wat onthouden en vergeten wordt?"
    },
    16: {
        'correct': 'B',
        'explanation': "De Output Gate filtert wat van de Cell State relevant is voor het huidige moment. Vergelijk het met een sollicitatiegesprek: je weet veel over jezelf (Cell State), maar bij 'Waarom moeten we jou aannemen?' deel je alleen relevante werkervaring, niet je favoriete eten. De Output Gate bepaalt wat nuttig is om nu te delen.",
        'question_text': "Het LSTM 'weet' veel in de Cell State. Waarom is de Output Gate nodig?"
    },
    17: {
        'correct': 'B',
        'explanation': "RNNs hebben twee grote beperkingen voor lange teksten: (1) ze moeten sequentieel verwerken (woord voor woord) wat traag is, en (2) zelfs met LSTM is het moeilijk om relaties over duizenden woorden te onthouden. Transformers lossen beide op: ze verwerken alles parallel en kunnen via attention direct naar elk eerder woord kijken, ongeacht afstand.",
        'question_text': "Waarom is een standaard RNN minder geschikt voor het vertalen van hele boeken dan een Transformer?"
    },
    18: {
        'correct': 'B',
        'explanation': "Self-attention laat 'bank' naar 'rivier' en 'groen' kijken om context te krijgen. 'Rivier' suggereert een buitenomgeving (geen geldbank), en 'groen' beschrijft waarschijnlijk de kleur van een object. Zo leert het model dat dit over een zitbank/parkbank gaat, niet over een financiële instelling. Dit is de kracht van attention.",
        'question_text': "In 'De bank aan de rivier was groen', naar welke woorden moet 'bank' vooral kijken?"
    },
    19: {
        'correct': 'C',
        'explanation': "Encoder + Decoder wordt gebruikt voor sequence-to-sequence taken zoals vertalen. De Encoder leest en begrijpt de brontaal (Nederlands), de Decoder genereert de doeltaal (Engels). Voor begrijpen (BERT) is alleen Encoder nodig, voor genereren (GPT) alleen Decoder. Sentiment analyse en classificatie zijn begrijp-taken (alleen Encoder).",
        'question_text': "BERT gebruikt alleen Encoder, GPT alleen Decoder. Wanneer gebruik je beide?"
    },
    20: {
        'correct': 'B',
        'explanation': "Self-attention kijkt binnen één sequence (alle woorden kijken naar elkaar in dezelfde zin). Cross-attention kijkt van de ene sequence naar een andere - bij vertalen kijkt de Decoder (die Engels schrijft) terug naar de Encoder output (die Nederlands begrepen heeft). Zo blijft de vertaling verbonden met de originele betekenis.",
        'question_text': "Bij vertalen gebruikt de Decoder cross-attention. Wat is het verschil met self-attention?"
    },
    21: {
        'correct': 'B',
        'explanation': "Multi-head attention laat het model verschillende aspecten parallel leren. Bijvoorbeeld: Head 1 let op grammaticale relaties (onderwerp-werkwoord), Head 2 op semantische overeenkomsten (synoniemen), Head 3 op lange-afstand verwijzingen ('hij' → 'Peter'). Elk head specialiseert zich, wat rijkere representaties geeft dan één enkele attention.",
        'question_text': "Waarom hebben Transformers 'multi-head' attention in plaats van één enkele attention?"
    },
    22: {
        'correct': 'B',
        'explanation': "RNN/LSTM moeten sequentieel werken (woord 1, dan woord 2, dan woord 3...), wat langzaam is. Transformers kunnen alle woorden tegelijk verwerken, wat perfect is voor GPU's die parallel kunnen rekenen. Dit maakt training 10-100x sneller. Daarom domineren Transformers nu - niet per se betere architectuur, maar veel sneller te trainen op moderne hardware.",
        'question_text': "Transformers kunnen alle tokens parallel verwerken. Waarom is dit een groot voordeel?"
    },
    23: {
        'correct': 'C',
        'explanation': "Dit is het 'black box' probleem. Neural networks kunnen wel goede voorspellingen maken, maar het is vaak onduidelijk waarom ze een bepaalde beslissing nemen. Voor regulatie en wetgeving (zoals bij leningen) moet je kunnen uitleggen waarom iemand werd afgewezen. Simpelere modellen zoals logistische regressie zijn transparanter maar mogelijk minder accuraat.",
        'question_text': "Een bank wil neural networks gebruiken maar moet kunnen uitleggen waarom een lening wordt afgewezen. Wat is het probleem?"
    },
    24: {
        'correct': 'B',
        'explanation': "50 voorbeelden zijn veel te weinig voor een neural network, dat zou vrijwel zeker overfitten. Neural networks hebben meestal duizenden tot miljoenen voorbeelden nodig. Bij kleine datasets werken simpelere methoden (logistische regressie, decision trees, kNN) vaak beter omdat ze minder parameters hebben en dus minder data nodig hebben om goed te generaliseren.",
        'question_text': "Je hebt een dataset met 50 voorbeelden. Welke uitspraak is waar?"
    },
    25: {
        'correct': 'B',
        'explanation': "ChatGPT (GPT = Generative Pre-trained Transformer) is gebouwd op een Transformer neural network, specifiek een decoder-only architectuur. Generatieve AI is niet een vervanging van neural networks, maar juist een toepassing ervan. De hiërarchie: AI → Machine Learning → Neural Networks → Deep Learning → Generatieve modellen (zoals ChatGPT).",
        'question_text': "ChatGPT is Generatieve AI. Wat is de relatie met Neural Networks?"
    }
}
