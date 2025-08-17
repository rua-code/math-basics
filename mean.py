import statistics

lst=input("enter values").split()
lst=[int(x) for x in lst]
print("Mean:", statistics.mean(lst))