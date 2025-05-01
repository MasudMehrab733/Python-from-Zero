# Print pairs of items from two lists
name = ['John','karim','Amini']
age = [23,21,20]
for name, age in zip(name,age):
    print(f"His name is {name}: and age is {age}.")

print('\n')
# Print index and value from a list
Fruits = ['Apple','Banana','Mango','Cherry']
for Index,fruit in enumerate(Fruits):
    print(f"Index:{Index}, Fruit:{fruit}")

print('\n')
# Create a list of tuples (i, j) where i is even and j is odd
result =[(i,j) for i in range(5) for j in range(5) if i % 2==0 if j % 2 !=0]
print(result)

print('\n')
#Print number 0 to 4 and skip 3
for i in range(10):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)

# Loop through a list and handle division by zero error
print('\n')
numbers = [10, 20, 0, 30]
for number in numbers:
    try:
        result = 100 / number
        print(result)
    except ZeroDivisionError:
        print('Division by zero error')

# Loop through a list and apply a function
print('\n')
def square(x):
    return x*x

numbers =[1,2,3,4]
for number in numbers:
   print(square(number))







