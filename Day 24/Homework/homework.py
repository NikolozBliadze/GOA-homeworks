def custom_split(input_string):
    result = []
    word = ""
    for char in input_string:
        if char != " ":
            word += char
        else:
            result.append(word)
            word = ""
    if word:
        result.append(word)
    return result

print(custom_split("Hello World Python"))




def custom_join(input_list):
    result = ""
    for i in range(len(input_list)):
        result += input_list[i]
        if i < len(input_list) - 1:
            result += " "
    return result

print(custom_join(['Hello', 'World', 'Python']))





def custom_replace(input_string, old_substring, new_substring):
    result = ""
    i = 0
    while i < len(input_string):
        if input_string[i:i+len(old_substring)] == old_substring:
            result += new_substring
            i += len(old_substring)
        else:
            result += input_string[i]
            i += 1
    return result


print(custom_replace("Hello World", "World", "Python"))





def mini_calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"

print(mini_calculator(10, 5, "add"))



words = input("შეიტანეთ სიტყვები ცალ-ცალკე გაშორებული სივრცით: ").split()

result = " ".join(words)

print("შეერთებული სიტყვები:", result)

