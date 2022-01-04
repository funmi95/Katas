def duplicate_count(text):
    text = text.lower()
    repeated_characters = []
    for character in text:
        if text.count(character) > 1:
            repeated_characters.append(character)
    
    return len(set(repeated_characters))

duplicate_count("Indivisibilities")

#A solution similiar to mine but uses and i not in duplicates rather than set
def duplicate_count(text):
    text = text.lower()
    duplicates = []
    for i in text:
        if text.count(i) > 1 and i not in duplicates:
            duplicates.append(i)    
    return len(duplicates)

a="Hello"
a.lower()
a.count('l')