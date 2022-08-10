def makeArrayConsecutive2(statues):
    sortd = sorted(statues)
    
    extras = 0
    
    for index, item in enumerate(sortd):
        try:
            diff = sortd[index+1] - item
            if diff > 1:
                extras += diff -1
        except:
            continue
    return extras

print(makeArrayConsecutive2([6, 2, 3, 8])) #3
print(makeArrayConsecutive2([6, 3])) #2