for num in range(1, 51, 2):
    print(num)

size = 5  # კვადრატის ზომა
for i in range(size):
    print('*' * size)


width = 7  # მართკუთხედის სიგანე
height = 4  # მართკუთხედის სიმაღლე

for i in range(height):
    print('*' * width)



for num1 in range(1, 4):  # გარეთა ლუპი
    for num in range(1, 4):  # შიდა ლუპი
        print(f"num1: {num1}, num: {num}")


users = []  # რეგისტრირებულ მომხმარებლების სია

while True:
    username = input("გთხოვთ შეიყვანოთ მომხმარებლის სახელი: ")
    password = input("გთხოვთ შეიყვანოთ პაროლი: ")
    email = input("გთხოვთ შეიყვანოთ ელექტრონული ფოსტის მისამართი: ")

    users.append({
        'username': username,
        'password': password,
        'email': email
    })

    another = input("გინდათ კიდევ ერთ მომხმარებლის რეგისტრირება? (yes/no): ")
    if another.lower() != 'yes':
        break

print("რეგისტრირებული მომხმარებლები:")
for user in users:
    print(user)
