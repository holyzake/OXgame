import pickle
try:
    with open('score.txt','rb') as file:
        score = pickle.load(file)
except:
    score = 0
print  "your score is",+score

score=10020
with open('score.txt','wb') as file:
    pickle.dump(score,file)
