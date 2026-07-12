de_distr = ['e', 'n', 'i', 's', 'r', 'a', 't', 'd', 'h', 'u', 'l', 'c', 'g', 'm', 'o', 'b', 'w', 'f', 'k', 'z', 'p', 'v', 'j', 'y', 'x', 'q']
en_distr = ['e', 't', 'a', 'o', 'n', 'i', 'h', 's', 'r', 'l', 'd', 'u', 'c', 'm', 'w', 'y', 'f', 'g', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alph_cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


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
            if alph_distr[alph_sort[w+v]] > biggest_num:
                biggest_num = alph_distr[alph_sort[w+v]]
                biggest_elem = alph_sort[w+v]
                biggest_ind = w+v
        swap_elem = alph_sort[v]
        alph_sort[v] = biggest_elem
        alph_sort[biggest_ind] = swap_elem
    print(alph_distr)
    print(alph_sort)
    return alph_sort

def decrypt(input_text, alph_sort):
    input_list = list(input_text)
    output_list = []
    for elem in input_list:
        if (elem not in alph) and (elem not in alph_cap):
            output_list.append(elem)
            continue
        if (lang != "de") and (lang != "en"):
            print("Falsche Eingabe")
            break
        if elem.isupper():
            exec(f"output_list.append(alph_cap[alph.index({lang}_distr[alph_sort.index(elem.lower())])])")
        elif elem.islower():
            exec(f"output_list.append({lang}_distr[alph_sort.index(elem)])")

    output = ''.join(str(x) for x in output_list)
    return output




lang = input("Sprache des Texts? (de/en)")
text = input("Zu entschlüsselnden Text eingeben:")

sorted = find_distribution(text)
print(decrypt(text, sorted))