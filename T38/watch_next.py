## Importing modules, changing directory ##
import os
import sys
import spacy

os.chdir(sys.path[0])
nlp = spacy.load("en_core_web_md")

## Pasting string to compare against other descriptions ##
test = "Will he save their world or destroy it? When the Hulk becomes too \
dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch\
him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk\
land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

def movie_rec(desc):
    '''Takes in a string (most likely movie description) and outputs a movie recommendation
    based on semantic similarities between given string and descriptions in file movies.txt'''

    ## Tokenising given string, initialising var to compare similarities in films to ## 
    test = nlp(desc)
    max_sim = -100
    ## Reading in text file ##
    with open("movies.txt", "r") as f:
        
        for line in f:
            ## Tokenising line to compare ##
            token = nlp(line)
            sim = test.similarity(token)
            if sim > max_sim:
                max_sim = sim
                movie_rec = line.split(":")[0]
    return movie_rec

## Testing function ##
print(f"The movie with the strongest recommendation is {movie_rec(test)}")
            



