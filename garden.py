#] Importing relevant modules ##
import spacy
nlp = spacy.load("en_core_web_sm")

## Writing out sentences ##
g1 = 'Mary gave the child the dog bit a Band-Aid.'
g2 = 'The florist sent the flowers was pleased.'
g3 = 'I know the words to that song about the queen don\'t rhyme.'
g4 = 'The man who hunts ducks out on weekends.'
g5 = 'When Fred eats food gets thrown.'

gardenpathSentences = [g1, g2, g3, g4, g5]

token_dict = {}
entity_dict = {}
## Tokenising sentences, placing in dictionary ##
for count, sentence in enumerate(gardenpathSentences):
    token_dict[count] = [token.orth_ for token in nlp(sentence)]
    print([(i, i.label_, i.label) for i in nlp(sentence).ents])

'''Of note regarding the entities that were found, I was surprised that weekend shows as a date
type. This would be useful in instances where they are defining a specific weekend (labour day weekend 
has a set date for example). Of more interest to me however is the absence of any found entities in sentences
2 and 3 however. I would have expected nouns to be important enough to count as entities so I was surprised
by this.'''