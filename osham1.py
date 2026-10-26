import re
with open ("file.txt", "r") as file:
  text=file.read()

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(pattern, text)
print("Email addresses found:")
for email in emails:
    print(email)
