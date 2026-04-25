edad=17

if edad==18:
    print("mayor de edad")
elif edad<18:
    print("Niño")
else:
    print("muy viejo XD")

spam = 0
while spam < 5:  # Continue while spam is less than 5
    print('Hello, world.')
    spam = spam + 1  # Increment counter to avoid infinite loop

print("")

for i in range(5):
    print(f'Will stop at 5! or 4? ({i})')

print("")

for i in range(3, -2, -1):
    print(i)