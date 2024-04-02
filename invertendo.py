def inverter_string(s):
    inverted = ""  # Uma string vazia para armazenar a string invertida

    for i in range(len(s) - 1, -1, -1):# Loop que itera sobre os caracteres da string original de trás para frente
        inverted += s[i]  # Adiciona o caractere atual à string invertida
    return inverted  

string_original = "Hello, world!"
string_invertida = inverter_string(string_original)
print("Invertida:", string_invertida)