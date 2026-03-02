import re

def sum_nums(numbers):
    find_nums = re.findall(r"\d+",numbers)
    total = 0
    for num_str in find_nums:
        num_int = int(num_str) 
        total = total + num_int
    return total

info = input("Nhập chuỗi: ")
print(sum_nums(info))