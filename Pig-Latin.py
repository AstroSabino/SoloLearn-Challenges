# Thaina's Pig Latin

sentence = input()


sentence = sentence.split(" ")
piglatin = list()

for i in range(len(sentence)):
    for j in range(len(sentence[i])) :
        if j != 0:
            piglatin += sentence[i][j]
    piglatin += sentence[i][0] + 'ay '
print(''.join(piglatin))
