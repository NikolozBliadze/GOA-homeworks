# numb = [1,23,4,5,5,6,6,1212312,31,4,5,12,3]
# # classworck
# # ცოფების სია გაქვს გადმოცელი
# # შეცვალოთ მხოლოდ კენტი რიცხვები და მივანიჭოთ "კენტი"

# for i in range(len(numb)):
#     print(numb[i])


numb = [1, 23, 4, 5, 5, 6, 6, 1212312, 31, 4, 5, 12, 3]

for i in range(len(numb)):
    if numb[i] % 2 != 0:
        numb[i] = "კენტი" 

print(numb)


