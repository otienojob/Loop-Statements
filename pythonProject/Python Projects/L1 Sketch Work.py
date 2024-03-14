#Prime Numbers between 1 and 100 Using While Statement

num_input=0

print((2**6)*'..')
print("Prime numbers between 1 and 100: \n")

while num_input<=100:
    incr=0
    const_num=2
    if num_input%const_num==0:
        print(f"{num_input} is not a Prime Number")
    const_num+=1


    if incr==0 and num_input!=1:
        print(f"{num_input} is a Prime Number")
    incr+=1
    num_input += 1
print((2**6)*'..')


