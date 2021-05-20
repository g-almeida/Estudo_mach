highscore = 0
dicSurf = {}
results = open("resultadoss")
for line in results:
    (name,score) = line.split()
    dicSurf[float(score)] = name
results.close()
print(dicSurf)
print(sorted(dicSurf, reverse = True))

'''c = 1

for cada in sorted(dicSurf.keys(), reverse=True):
    print(f'{c} lugar: surfista {dicSurf[cada]} tirou {cada} pontos!')
    c += 1
    if c == 4:
        break'''