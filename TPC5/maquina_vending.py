from datetime import date
import json, re



def formatar_valor(valor):   # Função que retorna uma string com a formatação correta do valor recebido como argumento, convertido de cêntimos
    euros = valor // 100
    cents = valor % 100
    if euros > 0:   # Se o valor tem pelo menos 1 euro
        if cents > 0:   # Se o valor tem pelo menos 1 cêntimo
            return f"{euros}e{cents}c"
        else:
            return f"{euros}e"
    else:   # Se o valor tem apenas cêntimos
        return f"{cents}c"



def main():
    
    saldo = 0   # Saldo em cêntimos
    estado = "INICIAL"
    valores = {"2e": 200, "1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}   # Valores possíveis das moedas, em cêntimos
    
    with open('stock.json', 'r', encoding='utf-8') as file:
        stock = json.load(file)["stock"]   # Lê o stock do ficheiro json

    estado = "AGUARDAR_MOEDA"
    print(f"{date.today()}, Stock carregado, Estado atualizado.")
    print("Bom dia. Estou disponível para atender o seu pedido.\n")

    while True:
        opcao = input().strip()

        if opcao == "LISTAR":
            print(f"{'COD':^7}|{'NOME':^35}|{'QUANTIDADE':^12}|{'PREÇO':^9}")   # Formatação do output
            print("------------------------------------------------------------------")
            for produto in stock:
                print(f"{produto['cod']:^7}|{produto['nome']:^35}|{produto['quant']:^12}|{produto['preco']:^9}")   # Formatação do output
            print()
        
        elif opcao.startswith("MOEDA"):   # Ex.: MOEDA 2e, 1e, 50c, 5c.
            moedas = re.findall(r'\d+[ec]', opcao[6:])   # Lista de moedas. Ex.: [2e, 1e, 50c, 5c]
            for moeda in moedas:
                valor = valores.get(moeda, 0)   # 'valor' está em cêntimos. O valor default caso não encontre a moeda na lista é 0
                if valor == 0:   # Caso a moeda não exista
                    print("Foi inserida uma moeda inválida.")
                    continue
                else:
                    saldo += valor
            print(f"Saldo = {formatar_valor(saldo)}")
            estado = "AGUARDAR_SELECAO"   # Altera o estado para indicar que já pode ser feita uma seleção de produto
            print()
        
        elif (match := re.match(r'SELECIONAR (\w+)', opcao)):   # Ex.: SELECIONAR A23
            if estado != "AGUARDAR_SELECAO":
                print("Por favor, insira moedas primeiro.")
                print()
                continue
            cod_prod = match.group(1)
            produto = None
            for p in stock:
                if p["cod"] == cod_prod:
                    produto = p
                    break
            if not produto:
                print("Produto inexistente.")
                print()
                continue
            if produto["quant"] == 0:
                print(f"O produto {produto['nome']} está esgotado.")
                print()
                continue
            preco = round(produto["preco"] * 100)   # Preço do produto em cêntimos
            if saldo < preco:
                print("Saldo insuficiente para satisfazer o seu pedido.")
                print(f"Saldo = {formatar_valor(saldo)}; Pedido = {formatar_valor(preco)}")
                print()
                continue
            print(f"Pode retirar o produto dispensado \"{produto['nome']}\".")
            saldo -= preco
            produto["quant"] -= 1   # A quantidade é também atualizada em 'stock'
            print(f"Saldo = {formatar_valor(saldo)}")
            print()

        elif opcao == "SAIR":
            troco = saldo   # Troco em cêntimos
            if troco == 0:
                print("Não há troco a entregar.")
            else:
                moedas_list = [200, 100, 50, 20, 10, 5, 2, 1]   # Valores das moedas em cêntimos
                troco_partes = []   # Lista para armazenar as partes do troco
                for moeda in moedas_list:
                    if troco >= moeda:
                        quant = troco // moeda
                        troco %= moeda
                        if moeda >= 100:   # Se a moeda era de euro
                            valor_formatado = f"{moeda//100}e"
                        else:   # Se a moeda era de cêntimos
                            valor_formatado = f"{moeda}c"
                        troco_partes.append(f"{quant}x {valor_formatado}")
                if len(troco_partes) == 1:
                    troco_str = troco_partes[0] + "."
                else:
                    troco_str = ", ".join(troco_partes[:-1]) + " e " + troco_partes[-1] + "."
                print("Pode retirar o troco:", troco_str)
            with open('stock.json', "w", encoding="utf-8") as f:   # Mantém os acentos
                json.dump({"stock": stock}, f, indent=4, ensure_ascii=False)   # Atualiza o ficheiro de stock
            print("Até à próxima.")
            break

        else:
            print("Comando não reconhecido.")
            print()



if __name__ == "__main__":
    main()