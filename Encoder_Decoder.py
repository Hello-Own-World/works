alphabet = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'ґ': 5,
            'д': 6, 'е': 7, 'є': 8, 'ж': 9, 'з': 10,
            'и': 11, 'і': 12, 'ї': 13, 'й': 14, 'к': 15,
            'л': 16, 'м': 17, 'н': 18, 'о': 19, 'п': 20,
            'р': 21, 'с': 22, 'т': 23, 'у': 24, 'ф': 25,
            'х': 26, 'ц': 27, 'ч': 28, 'ш': 29, 'щ': 30,
            'ь': 31, 'ю': 32, 'я': 33}
reversed_alphabet = {v : k for (k, v) in alphabet.items()}
phrase = str(input("Введіть фразу:"))

print(phrase)
lst = phrase.split()

lst2 = []
lst3 = []
lst4 = []

print(lst)

for x in lst:
    lst2.append(alphabet[x])    # convert letters into numbers
print(lst2)

key3 = int(input("key:"))   # for encode enter key; for decode enter opposite to key


print(key3)
for x in lst2:
    numb = x + key3
    if numb > 33:
        numb = numb - 33        # change numbers
    if numb <= 0:
        numb = 33 + numb
    lst3.append(numb)

for x in lst3:
    lst4.append(reversed_alphabet[x])       # changed numbers into changed message
print(lst4)