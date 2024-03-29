## Importing Spacy ##
import spacy
nlp = spacy.load('en_core_web_md')

## Creating list to investigate semantic similarities between ## 
tokens = nlp("cat monkey banana apple sauce monday split")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

'''Interesting to note although sauce is not a fruit, it recognises it as similar to the fruits
and not to the animals. Monday has virtually no similarity with any of the words given which was
to be expected. Split held the most similarities with banana, as was expected'''

## Speaking on differences between language models when applied to example file ##
'''Most strikingly clear when using the simpler language model is that the similarities scores are generally
much lower. This may be as a result of the more complex model being trained to notice less clear relationships
between words. There appeared to also be a slight increase in run-time when using the more complicated model'''