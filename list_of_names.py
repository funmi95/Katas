def namelist(names):
    namesText = list(map(lambda n: n['name'], names))
    
    if len(namesText) == 0:
        return ''
    elif len(namesText) == 1:
        return namesText[0]
    
    name = ', '.join(namesText[:-1])

    return f"{name} & {namesText[-1]}"

namelist([])

def namelist(names):
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    all_names = []
    for dict in names[:-1]:
        name = dict['name']
        all_names.append(name)
    answer = ', '.join(all_names)
    last_name = names[-1]['name']
    return f"{answer} & {last_name}"

namelist([ {'name': 'Bart'}])





