def inverter_string(string):
    chars = list(string)
    size = len(chars)

    for i in range(size // 2):
        chars[i], chars[size - i - 1] = chars[size - i - 1], chars[i]

    string_invertida = ''.join(chars)

    return string_invertida

string_original = input("Digite algo: ")
string_invertida = inverter_string(string_original)
print("Original:", string_original)
print("Invertida:", string_invertida)