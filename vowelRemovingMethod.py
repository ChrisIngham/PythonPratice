def disemvowel(word):
    final = []
    for words in word:
        if not words.lower() in  ["a","e","i","o","u"] :
            final += words
    
    final = "".join(final) 
    return (final)


disemvowel("hello")