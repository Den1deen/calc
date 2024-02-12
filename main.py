import re

def main():
    pattern = re.compile(r'^([1-9]|10)([+\-*/])([1-9]|10)$')
    expression = input('Введите выражение: ')
    if pattern.fullmatch(expression):
        print(int(eval(expression)))
    else:
        print("throws Exception")



main()