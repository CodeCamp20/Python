import re

text =input("enter the text :\n")

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print("Emails :\n", emails)
