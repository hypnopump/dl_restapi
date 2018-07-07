a = {1: "a"}

b = {}

for el in a:
	b[el] = a[el]

a[1] = "ba"
print(b)