import re

def removeWordFromSentence(sentence, word):
    # stop if value is null
    if word is None:
        return sentence
        
    return re.sub(r'\s*' + word + '\S*', '', sentence) if len(word) > 0 else sentence