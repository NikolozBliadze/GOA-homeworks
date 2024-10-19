current_year = 2024  
birth_year = int(input("შეიყვანეთ დაბადების წელი: "))
age = current_year - birth_year
print(f"თქვენი წლოვანება არის: {age}")


length = float(input("შეიყვანეთ ოთკუთხედის სიგრძე: "))
width = float(input("შეიყვანეთ ოთკუთხედის სიგანე: "))
area = length * width
perimeter = 2 * (length + width)
print(f"ოთკუთხედის ფართობი არის: {area}")
print(f"ოთკუთხედის პერიმეტრი არის: {perimeter}")


distance_km = float(input("შეიყვანეთ მანძილი სახლიდან სკოლამდე კილომეტრებში: "))
distance_m = distance_km * 1000
distance_cm = distance_m * 100
distance_mm = distance_cm * 10
print(f"მანძილი სახლიდან სკოლამდე: {distance_m} მეტრი, {distance_cm} სანტიმეტრი, {distance_mm} მილიმეტრი")


name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input("შეიყვანეთ თქვენი გვარი: ")
parent_name = input("შეიყვანეთ მშობლის სახელი: ")
parent_surname = input("შეიყვანეთ მშობლის გვარი: ")
fav_color = input("საყვარელი ფერი: ")
fav_car = input("საყვარელი მანქანა: ")
hobbies = input("3 საყვარელი ჰობი: ")
print(f"{name} {surname}-ის მშობელია {parent_name} {parent_surname}, მისი საყვარელი ფერია {fav_color}, მას უყვარს {fav_car}, მისი ჰობიებია: {hobbies}.")


number = int(input("შეიყვანეთ ორნიშნა რიცხვი: "))
tens = number // 10
units = number % 10
digit_sum = tens + units
print(f"ციფრების ჯამი არის: {digit_sum}")

