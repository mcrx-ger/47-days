alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alph_cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def rotate(input_text, rot_num):
    input_list = list(input_text)
    output_list = []
    for input_elem in input_list:
        if input_elem in alph_cap:
            alph_index = alph_cap.index(input_elem)
            new_index = (alph_index + rot_num) % 26
            output_list.append(alph_cap[new_index])
        elif input_elem in alph:
            alph_index = alph.index(input_elem)
            new_index = (alph_index + rot_num) % 26
            output_list.append(alph[new_index])
        else:
            output_list.append(input_elem)
    output = ''.join(str(x) for x in output_list)
    return output

def find_distribution(input_text):
    alph_distr = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, 
                  "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    input_list = list(input_text.lower())
    for input_elem in input_list:
        try:
            alph_distr[input_elem] += 1
        except:
            continue
    alph_sort = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for v in range(26):
        biggest_elem = ""
        biggest_num = -1
        biggest_ind = 0
        for w in range(26-v):
            if alph_distr[alph_sort[w]] > biggest_num:
                biggest_num = alph_distr[alph_sort[w]]
                biggest_elem = alph_sort[w]
                biggest_ind = w
        swap_elem = alph_sort[25-v]
        alph_sort[25-v] = biggest_elem
        alph_sort[biggest_ind] = swap_elem
    print(alph_distr)
    print(alph_sort)
    return alph_sort

def decrypt(text):
    alph_sort = find_distribution(text)
    for h in range(26):
        new_rot_num = 26 - ((alph.index(alph_sort[25-h])) - 4)
        print(new_rot_num)
        output_text = rotate(text, new_rot_num)
        print(output_text)
        fb = input("Ist dies das Original? (j/n)")
        if fb == "j":
            break
        elif fb == "n":
            continue
        else:
            print("Falsche Eingabe")
            break

mode = input("Verschlüsseln oder entschlüsseln? ('encr'/'decr')")

if mode == "encr":
    text = input("Zu verschlüsselnden Text eingeben:")
    rot_num = input("Rotationszahl eingeben:")
    output = rotate(text, int(rot_num))
    print(output)

elif mode == "decr":
    text = input("Zu entschlüsselnden Text eingeben:")
    decrypt(text)

else:
    print("Falsche Eingabe")