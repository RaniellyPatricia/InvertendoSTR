def inverter_string(s):
    inverted = ""
    for i in range(len(s) - 1, -1, -1):
        inverted += s[i]
    return inverted

string_original = "Hello, world!"
string_invertida = inverter_string(string_original)
print("Invertida:", string_invertida)