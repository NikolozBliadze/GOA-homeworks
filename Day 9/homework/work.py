


celsius = float(input("შეიყვანეთ ტემპერატურა ცელსიუსში: "))  # მომხმარებლის შეყვანა
fahrenheit = (celsius * 9/5) + 32  # ცელსიუსიდან ფარენჰეიტში გადაყვანის ფორმულა
print(f"{celsius}°C არის {fahrenheit}°F.")  # შედეგის ბეჭდვა





a = 10
b = 20

# 1. ნაკლებია
print(a < b)  # True

# 2. მეტია
print(b > a)  # True

# 3. ტოლია
print(a == 10)  # True


x = True
y = False

# 1. ლოგიკური AND
print(x and y)  # False

# 2. ლოგიკური OR
print(x or y)  # True

# 3. ლოგიკური NOT
print(not x)  # False


rows = 5
for i in range(1, rows + 1):
    print("<3 " * i)  # " <3" სიმბოლოების რაოდენობის გაზრდა თითოეულ იტერაციაზე

age = int(input("რამდენი წლის ხარ? "))  # მომხმარებლის ასაკის შეყვანა
if age == 20:
    print(True)  # თუ ასაკი არის 20, True დააბრუნებს
else:
    print(False)  # სხვა შემთხვევაში False
