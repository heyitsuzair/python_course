import os

if not os.path.exists('data'):
    os.mkdir('data')

for i in range(100):
    if not os.path.exists(f'data/day{i+1}'):
        os.mkdir(f'data/day{i+1}')
    # os.mkdir(f'data/day{i+1})
