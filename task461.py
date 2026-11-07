underscore_name = input().strip()
words = underscore_name.split('_')
camel_case_name = ""

for word in words:
    if word:
        camel_case_name += word.capitalize()

print(camel_case_name)