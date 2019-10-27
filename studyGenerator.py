# coding = utf-8

def triangles():
    line = [1]
    while True:
        yield line
        temp = [line[j] + line[j+1] for j in range(len(line) - 1)]
        line = [1] + temp + [1]



n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 100:
        break

for t in results:
    print(t)