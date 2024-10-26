age = int(input("შეიყვანეთ თქვენი წლოვანება: "))
is_teenager = 13 < age < 19
print(f"თქვენ ხართ თინეიჯერი: {is_teenager}")


grade = int(input("ნუგზარის ნიშანი (1-10): "))

is_A = grade >= 9
is_B = 8 <= grade < 9
is_C = 7 <= grade < 8
is_D = 6 <= grade < 7
is_F = grade < 6

print(f"is_A: {is_A}")
print(f"is_B: {is_B}")
print(f"is_C: {is_C}")
print(f"is_D: {is_D}")
print(f"is_F: {is_F}")


true_var = True
false_var = False

print(f"True and False: {true_var and false_var}")
print(f"True or False: {true_var or false_var}")
print(f"not True: {not true_var}")
print(f"not False: {not false_var}")


x = int(input("შეიყვანეთ პირველი რიცხვი: "))
y = int(input("შეიყვანეთ მეორე რიცხვი: "))

print(f"x == y: {x == y}")
print(f"x < y: {x < y}")
print(f"x > y: {x > y}")
print(f"x <= y: {x <= y}")
print(f"x >= y: {x >= y}")
print(f"x != y: {x != y}")


x = int(input("შეიყვანეთ პირველი რიცხვი: "))
y = int(input("შეიყვანეთ მეორე რიცხვი: "))

print(f"x == y: {x == y}")
print(f"x < y: {x < y}")
print(f"x > y: {x > y}")
print(f"x <= y: {x <= y}")
print(f"x >= y: {x >= y}")
print(f"x != y: {x != y}")


a = int(input("შეიყვანეთ a: "))
b = int(input("შეიყვანეთ b: "))
c = int(input("შეიყვანეთ c: "))

is_a_greatest = a > b and a > c
is_b_middle = (b > a and b < c) or (b > c and b < a)
is_c_least = c < a and c < b

print(f"is_a_greatest: {is_a_greatest}")
print(f"is_b_middle: {is_b_middle}")
print(f"is_c_least: {is_c_least}")


score = int(input("შეიყვანეთ ქულა (0-100): "))

is_pass = score >= 50
is_high_pass = 75 <= score < 90
is_perfect = score == 100
is_failing = score < 50

print(f"is_pass: {is_pass}")
print(f"is_high_pass: {is_high_pass}")
print(f"is_perfect: {is_perfect}")
print(f"is_failing: {is_failing}")


P = True
Q = False

P_and_not_Q = P and not Q
not_P_and_Q = not P and Q
P_xor_Q = (P or Q) and not (P and Q)

print(f"P_and_not_Q: {P_and_not_Q}")
print(f"not_P_and_Q: {not_P_and_Q}")
print(f"P_xor_Q: {P_xor_Q}")