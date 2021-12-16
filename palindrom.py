text = input()
# 1.объеденить без пробелов "".join - соединяет строки вместе с разделителем (добавляет разделитель в "")
text = "".join(text.split())
# 2. (text.split())разбивает стоку на части по разделителю и возвращает эти части СПИСКОМ!
# print(text)

def is_palindrom(text):
    first = 0 # индекс первого элемента
    last = len(text) - 1 # индекс последнего элемента
    while first < last:
        if text[first] != text[last]:
            print("This is not a palindrom")
            break
        first+=1
        last -=1
    else:
        print("This is a palindrom")

is_palindrom(text)