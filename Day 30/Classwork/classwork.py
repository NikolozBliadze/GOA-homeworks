# Highest and Lowest

# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# Examples
# Input: "1 2 3 4 5" => Output: "5 1"
# Input: "1 2 -3 ...


def high_and_low(numbers):
    nums = [int(x) for x in numbers.split()]
    return f"{max(nums)} {min(nums)}"