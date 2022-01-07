def generate_hashtag(s):
    if len(s) > 140:
        return False

    words = s.split()
    new_list = []
    for word in words:
        cap_word = word.capitalize()
        new_list.append(cap_word)

    new_string = "#"
    for item in new_list:
        new_string += item
    
    if new_string == "#":
        return False

    return new_string

generate_hashtag(" Hello there thanks for trying my Kata" )
generate_hashtag("")


#more succinct solution from codewars
def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output