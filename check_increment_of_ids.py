import json

with open('gramatiket.json', 'r') as gec_file:
    gec_json = json.load(gec_file)

sentence_id = 1
for element in gec_json:
    curr_sent_id = element['sentence ID']
    if curr_sent_id != sentence_id:
        print(f'sentence ID [{curr_sent_id}] should be different')
        raise ValueError('Incorrect sequence of sentence IDs!')

    sentence_id += 1
