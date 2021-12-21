def create_phone_number(n):
    nText = ''.join(map(str, n))
    print(nText)
    section1 = nText[0:3]
    section2 = nText[3:6]
    section3 = nText[6:10]

    return f"({section1}) {section2}-{section3}"

def create_phone_number(n):
    m = ''.join(map(str, n))
    return f"({m[:3]}) {m[3:6]}-{m[6:]}"


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"


