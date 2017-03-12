import csv
from collections import defaultdict
import json

data = defaultdict(lambda : defaultdict(lambda : defaultdict(int)))
children = []

with open('../data/complaints.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Sub-product']:
            if 'relief' in row['Company response to consumer']:
                data[row['Product']][row['Sub-product']]['relief'] += 1
            else:
                data[row['Product']][row['Sub-product']]['no_relief'] += 1

    for p, pp in data.iteritems():
        child = {
            'name': p,
            'children': []
        }
        for s, ss in pp.iteritems():
           data[p][s]['ratio'] = ss['relief'] / (ss['relief'] + ss['no_relief'])
           x = data[p][s]
           x['name'] = s
           child['children'].append(x)
        children.append(child)

    tree = {'name': 'complaints', 'children': children}

    print(json.dumps(tree))
