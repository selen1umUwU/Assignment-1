def Uni_codes(code):
    if len(code) != 6:
        return False 
    part_1 = code[:3]
    if not (part_1.isalpha() and part_1.isupper()):
        return False
    part_2 = code[3:]
    if not part_2.isdigit():
        return False
    
    return True

info = input("Nhập mã lớp học: ")
print(Uni_codes(info))
    