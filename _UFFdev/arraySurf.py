scores = []

results = open("resultadoss")
for line in results:
    (name,score) = line.split()
    scores.append(float(score))
scores.sort()
scores.reverse()

print (scores)
results.close()
