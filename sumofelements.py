def sum(*num):
    s=0
    for i in range (len(num)):
        s=s+num[i]

    return s
print(sum(9,2,3,3,3))

