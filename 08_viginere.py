alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def rotate(text_char, key_char, mode):
    key_index = alph.index(key_char)
    old_index = alph.index(text_char)
    if mode:
        new_index = (old_index + key_index) % 26
    else:
        new_index = (old_index - key_index) % 26
    return alph[new_index]

def convert(text, key, mode):
    input_list = list(text.lower())
    output_list = []
    key_list = list(key.lower())
    n = 0
    for elem in input_list:
        if elem in alph:
            output_list.append(rotate(elem, key_list[n], mode))
            if n == len(key_list) - 1:
                n = 0
            else:
                n+=1
        else:
            output_list.append(elem)
    output = ''.join(str(x) for x in output_list)
    return output

def find_key(text):
    return 0

ins = input("Möchten sie ver- oder entschlüsseln? ('en'/'de')")

if ins == "en":
    text = input("Geben Sie den zu verschlüsselnden Text ein:")
    key = input("Geben Sie den Schlüssel ein:")
    print(convert(text, key, True))
elif ins == "de":
    text = input("Geben Sie den verschlüsselten Text ein:")
    key_mode = input("Haben Sie den Schlüssel? ('j'/'n')")
    if key_mode == "j":
        key = input("Geben Sie den Schlüssel ein:")
        print(convert(text, key, False))
    elif key_mode == "n":
        print(find_key(text))
    else:
        print("Falsche Eingabe.")
else:
    print("Falsche Eingabe.")



