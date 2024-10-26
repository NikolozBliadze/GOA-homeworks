for i in range(1, 51, 2):
    print(i)



i = 0 
x = 10

while i < x:
    print("*" * x)
    i += 1



for num1 in range(3):
    for num2 in range(3):
        print(num1, num2)


username = input("შეიყვანეთ მომხმარებლის სახელი: ")
password = input("შეიყვანეთ პაროლი: ")
confrim_password = input("გაიმეორეთ პაროლი: ")

if password == confrim_password:
    print("რეგისტრაცია წარმატებულია")
else:
     print("პაროლი არასწორია. სცადეთ თავიდან")