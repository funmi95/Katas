def order(sentence: str):
    words = sentence.split()
    ordered_words = [None] * len(words)
    
    for word in words:
        for char in word:
            if str.isdigit(char):
                ordered_words[int(char) - 1] = word
                break
            continue

    return ' '.join(ordered_words)

order("is2 Thi1s T4est 3a f5or findin6g o7t i8f th9s b10reaks")

order("is2 Thi1s T4est 3a")
order("")



def order(sentence):
    sorted_words = []
    words = sentence.split()
    possibleNumbersInWords = list(range(len(words)))
    print(possibleNumbersInWords)
    for number in possibleNumbersInWords:
        for index, word in enumerate(words):
            if str(number+1) in word: 
                sorted_words.append(word)
                break
    return ' '.join(sorted_words)
    print(sorted_words)



        #while str(index) + 1 not in word:
            #print('no match')
            #continue
            #print('no match')
        #if i == sentence[index]:
            #print()

order("b10reaks is2 Thi1s T4est 3a f5or findin6g o7t i8f th9s")
order("")
#"Thi1s is2 3a T4est"

sentence = "is2 Thi1s T4est 3a"
words = sentence.split()
list(range(len(words)))
len(words)
num_list = []
num_list[1:len(words)]
