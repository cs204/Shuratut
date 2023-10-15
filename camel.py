camel_case = input("Верблюжий стиль: ")
snake_case = ""
for letter in camel_case:
    if letter.isupper():
        snake_case += "_" + letter.lower()
    else:
        snake_case += letter
snake_case = snake_case.lstrip("_")
print(snake_case)