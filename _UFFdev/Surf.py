highscore = 0
results = open("resultadoss")
for line in results:
    (name,score) = line.split()
    if float(score) > highscore:
        highscore = float(score)
results.close()
print(highscore)