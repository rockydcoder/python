answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
f = open('answers.txt', 'r')
response = []
incorrect = []
for line in f:
    response.append(line[0])
f.close()
counter = 0
for i in range(0,19):
    if answers[i] == response[i]:
        counter+=1
    else:
        incorrect.append(i+1)
if counter >= 15:
    print "Driver has passed"
else:
    print "Driver has failed"
print "Number of correct questions = ", counter
print "Number of incorrect questions = ", (20-counter)
print incorrect