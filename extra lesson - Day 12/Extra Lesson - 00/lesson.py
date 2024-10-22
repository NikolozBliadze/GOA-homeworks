name = "Two Tower"
result = ""
for i in name:
    result += i 
    print(i) 


n = int(input("შეიყვანეთ ციფრი: "))

if n % 2 == 0:
    print("ლუწი")
else:
    print("კენტი")


for n in range(1, 101):
    if n % 2 == 0:
        print(n, "ლუწი")
    else:
        print(n, "კენტი")

        #

