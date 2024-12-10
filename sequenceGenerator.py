from itertools import islice

def A061418_gen(start):
    a = start
    while True:
        yield a
        a += a >> 1

results = []
for start in range(0, 500):
    sequence = list(islice(A061418_gen(start), start+1)) 
    results.append(sequence[start])
for ele in results:
    print(" ",ele)

