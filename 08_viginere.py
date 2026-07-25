alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
de_stand = {"a" : 0.0651, "b" : 0.0189, "c" : 0.0306, "d" : 0.0508, "e" : 0.1740, "f" : 0.0166, "g" : 0.0301, "h" : 0.0476, "i" : 0.0755, "j" : 0.0027, "k" : 0.0121, "l" : 0.0344, "m" : 0.0253, "n" : 0.0978, "o" : 0.0251, "p" : 0.0079, "q" : 0.0002, "r" : 0.0700, "s" : 0.0727, "t" : 0.0615, "u" : 0.0435, "v" : 0.0067, "w" : 0.0189, "x" : 0.0003, "y" : 0.0004, "z" : 0.0113}

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
        elif elem == "ä" or elem == "ü" or elem == "ö" or elem == "ß":

            if elem == "ä": sub_elem1 = "a"; sub_elem2 = "e"
            elif elem == "ü": sub_elem1 = "u"; sub_elem2 = "e"
            elif elem == "ö": sub_elem1 = "o"; sub_elem2 = "e"
            else: sub_elem1 = "s"; sub_elem2 = "s"

            output_list.append(rotate(sub_elem1, key_list[n], mode))
            if n == len(key_list) - 1:
                n = 0
            else:
                n+=1

            output_list.append(rotate(sub_elem2, key_list[n], mode))
            if n == len(key_list) - 1:
                n = 0
            else:
                n+=1
        else:
            continue
    output = ''.join(str(x) for x in output_list)
    return output

def get_spalten(input_list, n):
    spalten_ges = []
    for u in range(n):
        spalte_current = []
        for i in range(len(input_list) // n):
            spalte_current.append(input_list[u + i * n])
        spalten_ges.append(spalte_current)
    #return [input_list[u::n] for u in range(n)]
    return spalten_ges


#def clear_list(input_list):
#    i=0
#    while i < len(input_list):
#        if (input_list[i] not in alph):
#            del input_list[i]
#            i-=1
#        i+=1
#    return input_list


def ic_find_keylength(input_list):
    n = 2
    keylength_list = []
    spalten_ges = get_spalten(input_list, n)
    while (len(input_list) / n) >= 20:
        spalten_ges = get_spalten(input_list, n)
        print(n, " = N")
        for spalte in spalten_ges:
            already_processed = []
            sum_char = 0
            for char in spalte:
                if char in already_processed:
                    continue
                else:
                    freq_char = spalte.count(char)
                    already_processed.append(char)
                    sum_char += freq_char * (freq_char - 1)
            ic = sum_char / (len(spalte) * (len(spalte) - 1))
            if ic < 0.06:
                print("break", ic)
                break
        if ic >= 0.06:
            keylength_list.append(n)
            print("IC ok:", ic, keylength_list)
        n+=1
    return keylength_list

def get_key(input_list, keylength):
    spalten_ges = get_spalten(input_list, keylength)
    key_char_list = []
    for spalte in spalten_ges:
        smallest_chi = 1000000000000000
        smallest_chi_index = 0
        alph_distr = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, 
                          "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

        for elem in spalte:
            alph_distr[elem] += 1

        for i in range(26):
            chi = 0
            for buchstabe, freq in de_stand.items():
                letter_index = alph.index(buchstabe)
                observed = alph_distr[alph[(letter_index + i) % 26]]
                expected = freq * len(spalte)
                chi += (observed - expected)**2 / expected

            if chi < smallest_chi:
                smallest_chi = chi
                smallest_chi_index = i

        key_char_list.append(alph[smallest_chi_index])
        print(smallest_chi, key_char_list)
    key = ''.join(str(x) for x in key_char_list)
    return key
        
def find_key(text):
    input_list = list(text.lower())
    keylength_list = ic_find_keylength(input_list)
    print("keys", keylength_list)
    feedb = "n"
    while feedb != "j":
        try:
            keylength = keylength_list[0]
        except:
            break
        key = get_key(input_list, keylength)
        text_encr = ''.join(str(x) for x in input_list)
        output = convert(text_encr, key, False)
        feedb = input(f"Ist das der Originaltext ('j'/'n'): {output}")
        if feedb == "j":
            print(f"Der Schlüssel lautet {key}.")
            break
        elif feedb == "n":
            del keylength_list[0]
        else:
            print("Falsche Eingabe")
            feedb = "n"
    if feedb == "n":
        print("Zu kurzer Text oder zu langer Schlüssel. Schlüssel konnte nicht gefunden werden")




#main

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
        find_key(text)
    else:
        print("Falsche Eingabe.")
else:
    print("Falsche Eingabe.")



