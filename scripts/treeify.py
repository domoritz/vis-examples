import csv
from collections import defaultdict
import json

products = defaultdict(lambda : defaultdict(int))
sub_products = defaultdict(lambda : defaultdict(int))

with open('../data/complaints.csv') as f:
    reader = csv.DictReader(f)
    count = 0
    relief = 0
    for row in reader:
        prod = row['Product']
        sub = row['Sub-product']
        products[prod]['count'] += 1
        count += 1
        if (sub):
            sub_products[sub]['prod'] = prod
            sub_products[sub]['count'] += 1

        if 'relief' in row['Company response to consumer']:
            products[prod]['relief'] += 1
            relief += 1
            if (sub):
                sub_products[sub]['relief'] += 1


    tree = [{
        'name': 'Complaints',
        'id': 1,
        'relief': 1.0 * relief / count
    }]

    id = 2
    for p, pp in products.iteritems():
        pp['id'] = id
        id += 1

        tree.append({
            'name': p,
            'size': pp['count'],
            'id': pp['id'],
            'relief': 1.0 * pp['relief'] / pp['count'],
            'parent': 1
        })
    
    for p, pp in sub_products.iteritems():
        tree.append({
            'name': p,
            'size': pp['count'],
            'id': id,
            'parent': products[pp['prod']]['id'],
            'relief': 1.0 * pp['relief'] / pp['count']
        })
        id += 1

    print(json.dumps(tree))
