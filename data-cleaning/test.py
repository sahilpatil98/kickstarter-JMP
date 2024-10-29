import json
from flatten_json import flatten
import pandas as pd


TEST_PATH = '/Users/sahil/kickstarter-JMP/Data/test_copy.jsonl'
#TEST_PATH = '/Users/sahil/kickstarter-JMP/Data/Kickstarter_2016-03-22T07_41_08_591Z.json'
data2 = []

with open(TEST_PATH, 'r') as file:
    for line in file:
        data2.append(flatten(json.loads(line)['data']))

df2 = pd.DataFrame(data2)

unique_creator_ids = [765699764]
for id in unique_creator_ids:
    one_person = df2[(df2['creator_id'] == id)].drop_duplicates(subset='id')
    break
        
print(one_person)