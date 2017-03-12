import csv
from collections import defaultdict
import json

data = defaultdict(lambda : defaultdict(lambda : defaultdict(int)))
tree = [{
    'name': 'Complaints',
    'id': 1
}]

with open('../data/complaints.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if 'relief' in row['Company response to consumer']:
            data[row['Product']][row['Sub-product']]['relief'] += 1
        else:
            data[row['Product']][row['Sub-product']]['no_relief'] += 1

    parent = 2
    id = 100
    for p, pp in data.iteritems():
        size = 0
        for s, ss in pp.iteritems():
            _sum = 0
            _count = 0
            if (s):
                _sum += ss['relief']
                _count += ss['relief'] + ss['no_relief']
                data[p][s]['ratio'] = 1.0 * ss['relief'] / (ss['relief'] + ss['no_relief'])
                subSize = ss['relief'] + ss['no_relief']
                size += subSize
                tree.append({
                    'id': id,
                    'name': s,
                    'size': subSize,
                    'parent': parent,
                    'percent': data[p][s]['ratio']
                })
                id += 1
        tree.append({
            'id': parent,
            'name': p,
            'size': size,
            'parent': 1,
            'percent': 1.0 * _sum / _count if _count else 0
        })
        parent += 1

    print(json.dumps(tree))
