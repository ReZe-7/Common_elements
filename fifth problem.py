x = list(range(1,12))
y = list(range(4,19))
z = []
print(f"List 1: {x}\nList 2: {y}")
for us in x:
    if us in y:
        z.append(us)
print(f"Common Elements : {z}")