letters = ['ა', 'ბ', 'გ', 'დ', 'ე', 'ვ', 'ზ', 'თ', 'ი', 'კ', 'ლ', 'მ', 'ნ', 'ო', 'პ', 'ჟ', 'რ', 'ს', 'ტ', 'უ', 'ფ', 'ქ', 'ღ', 'ყ', 'შ', 'ჩ', 'ც', 'ძ', 'წ', 'ჭ', 'ხ', 'ჯ', 'ჰ']

vowels = ['ა', 'ე', 'ი', 'ო', 'უ']

count = 0
for i in range(len(letters)):
    if letters[i] in vowels:
        count += 1

print("ხმოვნების რაოდენობა არის:", count)

print("-----------------------------------")

multiples = []
for number in range(1, 101):
    if number % 5 == 0 or number % 3 == 0:
        multiples.append(number)        
        print("5 და 3_ის ჯერადევია:", multiples)

print("-----------------------------------")

elements = ['ა', 'ბ', '1', 'გ', '2', '3', 'დ', 'ე']
result_string = " ".join(elements)
print("ერთი სტრინგია:", result_string)

print("-----------------------------------")




