print("For Loop using range (5)")
print("--- ---- ----- ----- ---")
for x in range(5):
    print(x)

print("For Loop using range (3:8)")
print("--- ---- ----- ----- -----")
# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
print("For Loop using range (3:8:2)")
print("--- ---- ----- ----- -------")
for x in range(3, 8, 2):
    print(x)

print("For Loop without range")
print("--- ---- ------ -----")
primes = [2, 3, 5, 7]
for i in primes:
    print(i)

print("While Loop")
print("----- ----")

count = 0
while count <= 5:
    print(count)
    count += 1


print("While Loop1")
print("----- -----")
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
        print(count)  #this will not execute

print("While Loop2")
print("----- -----")
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    print("before if %d" %x)
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)


print("Else in While While Loop2")
print("-------------------------")
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

print ("For loop with else")
print("-------------------")
# Prints out 1,2,3,4
for i in range(1, 11):
    if(i%5==0):
        continue
    print(i)
else:
    print("%d is max" %i)


for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")