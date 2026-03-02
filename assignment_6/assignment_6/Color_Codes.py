import re 

def color_codes(code):
    if re.fullmatch(r"^#[a-fA-F0-9]{6}$", code):
        return True
    return False

info = input("Nhập mã màu: ")
if (color_codes(info)) == True:
    print("valid Color Code")
else:
    print("Not valid Color Code")