import json
from Creation import Creation

with open('./prompt/Mary.json','rt') as f:
    des=json.load(f)
with open("./prompt/name_judge.txt",'r') as f:
    name_judge=f.read()

c=Creation(system_msg=name_judge)
sentence_1=f'persona description:{des["Description for the image"]},\n\n name:{des["name1"]}'
sentence_2=f'persona description:{des["Description for the image"]},\n\n name:{des["name2"]}'
score_1=0
score_2=0
for i in range(50):
    r1=c.create(sentence_1)
    r2=c.create(sentence_2)
    print('name1:',r1,'\n')
    print('name2:',r2,'\n')
    score_1+=float(json.loads(r1)["score"])
    score_2+=float(json.loads(r2)["score"])

score_1/=50
score_2/=50
print('score of name 1',score_1)
print('score of name 2',score_2)

