def single_root_words(root_word: str, *other_words) -> list:
    same_words: list = []
    root_word = root_word.lower()
    for word in other_words:
        if root_word.lower() in word.lower() or root_word.count(word.lower()):
            same_words.append(word)

    return same_words
        
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)