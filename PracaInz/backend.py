class Question():
    def __init__(self, image, answer, correct_answer, bad_answer):
        self.answer = answer
        self.image = image
        self.correct_answer = correct_answer
        self.bad_answer = bad_answer
    
with open('odp.txt') as f:
    for line in f:
        abc = line
        print(abc,end='')
print('')
pytania = []

with open('odp.txt') as f:
    for line in f:
        S = line.split()
        image = S[0]
        answer = S[1]
        correct_answer = S[2]
        bad_answer = [3] 
        pytania.append(Question(image, answer, correct_answer, bad_answer))
print('')
for i in range(len(pytania)):
    print(pytania[i].image, pytania[i].answer, sep=" ")

f = open("odp.txt", "a")
f.write("\n")
for i in range(len(pytania)):
    f.write(pytania[i].image +" " + pytania[i].answer)
    f.write("\n")
f.close()

