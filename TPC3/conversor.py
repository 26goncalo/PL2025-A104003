import re, sys


def main(args):
    ficheiro_md = args[1]   # Nome ou caminho para o ficheiro .md a converter
    html_linhas = []
    dentro_lista = False   # Flag para controlar se estamos dentro de uma lista
    
    with open(ficheiro_md, 'r', encoding='utf-8') as f:
        conteudo_md = f.readlines()
    
    if conteudo_md:
        for linha in conteudo_md:
            linha = linha.strip()
            
            #Cabeçalhos
            if re.match(r'^###', linha):   # Se a linha começa por ###
                linha = re.sub(r'^### (.*)', r'<h3>\1</h3>', linha)
            elif re.match(r'^##', linha):   # Se a linha começa por ##
                linha = re.sub(r'^## (.*)', r'<h2>\1</h2>', linha)
            elif re.match(r'^#', linha):   # Se a linha começa por #
                linha = re.sub(r'^# (.*)', r'<h1>\1</h1>', linha)

            # Negrito
            linha = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', linha)

            # Itálico
            linha = re.sub(r'\*(.*?)\*', r'<i>\1</i>', linha)

            # Lista Numerada
            if re.match(r'^\d+\.\s', linha):  # Linha começa com número e ponto (ou seja, é uma entrada de uma lista)
                if not dentro_lista:
                    html_linhas.append("<ol>")   # Inicializador da lista
                    dentro_lista = True
                linha = re.sub(r'^\d+\.\s(.*)', r'<li>\1</li>', linha)
            else:
                if dentro_lista:
                    html_linhas.append("</ol>")   # Se a linha não é uma lista mas a anterior era, adiciona o terminador
                    dentro_lista = False

            # Imagem
            linha = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', linha)

            # Link
            linha = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', linha)


            html_linhas.append(linha)
        
        if dentro_lista:
            html_linhas.append('</ol>')   # Se o ficheiro terminar com uma lista

    conteudo_md = "\n".join(html_linhas)
    
    with open("output.html", 'w', encoding='utf-8') as output:
        output.write(conteudo_md)

    print("Conversão efetuada com sucesso!")




if __name__ == "__main__":
    main(sys.argv)