def parse_entrada (entrada):   # Função auxiliar que separa os campos de 'entrada', tendo em conta as aspas, e guarda-os no array 'campos'
    campos = []
    campo_atual = []
    aspas_flag = False   # "Flag" para ignorar os casos em que aparece um delimitador (;) na descrição das obras (que vêm dentro de aspas)

    for char in entrada:
        if char == '"':
            aspas_flag = not aspas_flag
        elif char == ';' and not aspas_flag:   # Caso encontre um ; que não esteja dentro de aspas
            campos.append("".join(campo_atual).strip())   # Guarda o campo atual em 'campos'
            campo_atual = []
        else:
            campo_atual.append(char)   # Vai guardando, caracter a caracter, o campo que está a ler

    if campo_atual:
        campos.append("".join(campo_atual).strip())   # Guarda o último campo

    return campos



def main():
    campos = ""
    aspas_flag = False
    ponto_virgula_contador = 0

    compositores = []   # Lista para armazenar os compositores musicais
    nr_obras_por_periodo = {}   # Dicionário para relacionar cada período com o número de obras nele existentes
    titulos_obras_por_periodo = {}   # Dicionário que associa a cada período uma lista dos títulos das obras desse período

    with open("obras.csv", "r", encoding="utf-8") as f:
        linhas = f.readlines()

    for linha in linhas[1:]:   # Ignora o cabeçalho

        for char in linha:
                if char == '"':
                    aspas_flag = not aspas_flag
                elif char == ";" and not aspas_flag:
                    ponto_virgula_contador += 1

        campos += linha   # 'campos' vai guardando cada linha do ficheiro até atingir o final da entrada

        if ponto_virgula_contador == 6:   # Caso tenha chegado ao final de uma entrada válida
            obra = parse_entrada(campos)

            compositor = obra[4].strip()   # O 5º campo (indíce 4) do ficheiro csv corresponde ao compositor
            periodo = obra[3].strip()   # O 4º campo (índice 3) corresponde ao período
            nome = obra[0].strip()   # O 1º campo (índice 0) corresponde ao nome da obra

            if compositor not in compositores:
                compositores.append(compositor)   # Adiciona o compositor da entrada atual à lista dos compositores, caso não existisse

            nr_obras_por_periodo[periodo] = nr_obras_por_periodo.get(periodo, 0) + 1   # Atualiza o número de obras para o período em questão

            if periodo not in titulos_obras_por_periodo:
                titulos_obras_por_periodo[periodo] = []
            titulos_obras_por_periodo[periodo].append(nome)   # Adiciona o nome da obra obtido ao dicionário, na posição do período correspondente

            campos = ""
            ponto_virgula_contador = 0

    compositores.sort()   # Ordena a lista dos compositores

    for periodo in titulos_obras_por_periodo:
        titulos_obras_por_periodo[periodo].sort()   # Ordena a lista dos títulos das obras para cada período

    # Impressão do output
    print("\nLista ordenada dos compositores musicais:\n")
    for compositor in compositores:
        print ("   ", compositor)

    print ("\n--------------------------------------------------------------------------------\n")

    print("Número de obras catalogadas em cada período:\n")
    for periodo in nr_obras_por_periodo:
        print("   " + periodo + ": " + str(nr_obras_por_periodo[periodo]))

    print ("\n--------------------------------------------------------------------------------\n")
        
    print("Lista ordenada dos títulos das obras de cada período:\n")
    for periodo in titulos_obras_por_periodo:
        print ("   ", periodo + ":")
        for obra in titulos_obras_por_periodo[periodo]:
            print ("      ", obra)
    
    print ("")


if __name__ == "__main__":
    main()
