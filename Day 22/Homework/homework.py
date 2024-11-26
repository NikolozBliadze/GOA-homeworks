list_of_names = ["დავითი", "ნიკა", "ნიკა", "ელენე", "ნიკა", "ქეთი"]
targrt_name = "ნიკა"
count = list_of_names.count(targrt_name)
print(f"სახელი {targrt_name} სიაში მეორდება {count}_ჯერ")




numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)




list_of_numbers = [1, 2, 3]
length = len(list_of_numbers)
repeated_list = list_of_numbers * length
print(repeated_list)



list_of_numbers1 = ["nika", "luka"]
len_list_of_numbers1 = len(list_of_numbers1)
res = list_of_numbers1 * len_list_of_numbers1
print(res)


languages = ["პითონი", "ჯავა", "პითონი", "ცეფი", "რუბი", "პითონი"]
count = languages.count("პითონი")
languages.remove("პითონი")
print(f"პითონის რაოდენობა: {count}")
print("განახლებული სია:", languages)
