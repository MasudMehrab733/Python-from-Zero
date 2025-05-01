for i in range(1,10):
    print(i, end=' ')


fruits = ['Apple','Banana','Cherry']
for fruit in fruits:
        print(fruit)
print()

word = "Python"
for letter in word:
    print(word, end=' ')

print('\n')
# print even numbers from 0 to 9
for i in range(10):
  if i%2 ==0:
    print(i, end=' ')

print('\n')
#Print key and values
person = {'name':'Alice','Age':23}
for key,values in person.items():
    print(f"{key}:{values}")

print('\n')
# Stop loop when i equals 5
for i in range(10):
    if i ==5:
        break
    print(i, end=' ')


print('\n')
# continue loop when i equals 5
for i in range(10):
    if i ==5:
        continue
    print(i, end=' ')

print('\n')
# Print a 3x3 grid
for i in range(5):
    for j in range(5):
        print(f"{i}{j}", end=' ')
print('\n')
# Print numbers from 0 to 9 and then a message
for i in range(10):
    print(i)
else:
    print("Print the numbers!")

print('\n')
square = [x**2 for x in range(5)]
print(square)

#Neasted for loop with conditional
print('\n')
for i in range(10):
    for j in range(5):
        if i ==j:
            print("*", end=' ')
        else:
            print("#", end=' ')
        print()
#Loop through a list of Dictionary
students = [{'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 22}]
for student in students:
    for key, value in student.items():
        print(f'{key}: {value}')









