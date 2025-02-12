def main():

    text = input("Insira o texto:\n").lower()   # Faz a leitura do texto do standard input
    i = 0   # Para iterar sobre o texto
    length = len (text)
    counter = 0   # Contador usado para armazenar a soma dos dígitos
    digits = ""   # Guarda cada dígito dos números encontrados no texto
    on = True   # Flag para controlar o comportamento de somador (True corresponde a On, False a Off)

    while i < length:   # Percorrer todo o texto
        char = text[i]   # Caracter atual

        if char == '=':
            if digits != "":
                counter += int (digits)   # Caso 'digits' tenha conteúdo, atualiza 'counter' antes de imprimir
                digits = ""
            print (counter)

        elif char == 'o':   # Para procurar por "on" ou "off"
            if i < length - 2 and text[i+1:i+3] == "ff":  # Caso encontre "off"
                on = False
                i += 2   # Salta os dois 'ff' de "Off" pois não será necessário processá-los
            elif i < length - 1 and text[i+1] == 'n':  # Caso encontre "on"
                on = True
                i += 1   # Salta o 'n' de "On" pois não será necessário processá-lo

        if on:   # Se o comportamento estiver ativo
            if char.isdigit():
                digits += char
            elif digits != "":
                counter += int (digits)
                digits = ""
        i += 1



if __name__ == "__main__":
    main()