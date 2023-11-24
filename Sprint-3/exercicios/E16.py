a = "1,3,4,6,10,76"

a = a.split(",")
a = [int(i) for i in a]

print(sum(a))