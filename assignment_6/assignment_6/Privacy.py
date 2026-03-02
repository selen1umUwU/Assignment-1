import re

def privacy(paragraph):
    hided_paragraph = re.sub(r"\d{10}|\+84\d+","[REDACT]",paragraph)
    return hided_paragraph

info = input("Nhập đoạn văn: ")
print(privacy(info))