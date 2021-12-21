def to_camel_case(text):
    new_text = ""
    make_upper = False
    for idx, character in enumerate(text):
        print (idx, character)
        if character == '_' :
            make_upper = True
        elif character == '-':
            make_upper = True
        else:
            if make_upper:
                new_text += character.upper()
            else:
                new_text += character
            make_upper = False

    return new_text


to_camel_case("mark_is_smart")