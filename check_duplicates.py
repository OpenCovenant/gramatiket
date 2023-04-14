import json

map_of_source_sentences = {}

with open('gramatiket.json', 'rb') as gec_file:
    gec_json = json.load(gec_file)

for element in gec_json:
    if element['source sentence'] in map_of_source_sentences:
        print(f'Duplicate found: {element}')
        raise ValueError(f'A duplicate has been found!')
    else:
        map_of_source_sentences[element['source sentence']] = element
