import statistics


wights= input("Enter bottle weights (grams, space separated):").split()

wights=[float(x) for x in wights]
var=statistics.variance(wights)
print("variance is = ", var)

threshold = 2.0
if var > threshold:
    print("Production unstable ")
else:
    print("Production stable ")

