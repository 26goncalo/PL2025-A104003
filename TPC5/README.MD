# Máquina de Vending


## Autor do Trabalho

![Foto](../photo.jpg)

**Nome:** Gonçalo Monteiro Cunha  
**Número de Aluno:** A104003  
**Data:** 13/03/2025  



## Resumo

Neste trabalho implementei um programa que simula uma máquina de *vending*. Existe um *stock* de produtos presente num ficheiro e o utilizador pode ver os produtos existentes, inserir moedas e escolher produtos. Ao sair, é devolvido o troco, caso exista. A aplicação tem em conta vários casos de erro e informa o utilizador sobre os mesmos (ou lida com eles, quando possível).  



## Enunciado

Pediram-te para construir um programa que simule uma máquina de vending.  
A máquina tem um stock de produtos: uma lista de triplos, nome do produto, quantidade e preço.  
```
stock = [
{"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
...
]
```
Podes persistir essa lista num ficheiro em JSON que é carregado no arranque do programa e é atualizado quando o programa termina.  
A seguir apresenta-se um exemplo de uma interação com a máquina, assim que esta é ligada, para que possas perceber o tipo de comandos que a máquina aceita (as linhas iniciadas marcadas com >> representam o input do utilizador):  
```
maq: 2024-03-08, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
>> LISTAR
maq:
cod | nome | quantidade | preço
---------------------------------
A23 água 0.5L 8 0.7
...
>> MOEDA 1e, 20c, 5c, 5c .
maq: Saldo = 1e30c
>> SELECIONAR A23
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Saldo = 60c
>> SELECIONAR A23
maq: Saldo insuficiente para satisfazer o seu pedido
maq: Saldo = 60c; Pedido = 70c
>> ...
...
maq: Saldo = 74c
>> SAIR
maq: Pode retirar o troco: 1x 50c, 1x 20c e 2x 2c.
maq: Até à próxima
```
O stock encontra-se inicialmente armazenado num ficheiro JSON de nome "stock.json" que é carregado em memória quando o programa arranca. Quando o programa termina, o stock é gravado no mesmo ficheiro, mantendo assim o estado da aplicação entre interações.  
Use a imaginação e criatividade e tente contemplar todos os cenários, por exemplo, produto inexistente ou stock vazio.  
Como extra pode adicionar um comando para adicionar alguns produtos ao stock existente (produtos novos ou já existentes).  
Bom trabalho



## Explicação da implementação

Para resolver este problema implementei a função `main`, que trata de toda a lógica e recorre a uma função auxiliar, a `formatar_valor`.  



#### 1. Variáveis

Inicialmente, são declaradas três variáveis na função principal:

- `saldo`: Corresponde ao saldo do utilizador, que vai alterando ao longo do programa, com inserção de moedas e seleção de produtos. O valor inicial é 0;  
- `estado`: String que indica o estado em que a máquina se encontra ("INICIAL", "AGUARDAR_MOEDA" ou "AGUARDAR_SELECAO"). Começa com o valor "INICIAL";  
- `valores`: Dicionário que contém todas as moedas possíveis. As *keys* do dicionário são a representação das moedas para o utilizador (como **1e** ou **50c**) e os *values* do mesmo correspondem aos valores, em cêntimos, das moedas (como 100 ou 50, para o exemplo anterior).  


#### 2. Inicializações e ciclo principal

Para começar, é aberto o ficheiro *JSON* que contém o *stock* dos produtos (o `stock.json`) e lida a lista de produtos para a variável `stock`. Logo de seguida, é atualizado o estado da máquina para "AGUARDAR_MOEDA" e são feitos os *prints* iniciais.  
Depois, entramos num ciclo *while* que serve para ir lendo as opções inseridas pelo utilizador e tratar cada uma delas, sendo que só termina quando este escrever "SAIR".  
Para a opção "LISTAR", simplesmente é feita a impressão dos dados de cada produto em `stock`, formatados de uma forma legível.  
Quanto à opção "MOEDA", é necessário extrair os valores da linha lida, pelo que é usada uma expressão regular para obter a lista de moedas (com o `findall`). Caso a moeda seja válida, o saldo é atualizado com o valor correspondente (recorrendo à lista `valores`). No fim, o saldo é impresso no formato que era pedido e o estado é atualizado, para indicar que a máquina já pode aceitar seleções de produtos.  
Relativamente ao "SELECIONAR", recorro novamente a uma *regex* para obter o código do produto pretendido e é verificado se o mesmo existe, se tem *stock* e se o saldo do utilizador é suficiente para satisfazer o pedido. Em caso positivo, é impressa a indicação do sucesso da operação, o saldo e a quantidade do produto são atualizados e é apresentado o saldo resultante.  
Já relativamente à opção "SAIR", é necessário entregar o troco, pelo que é verificado, da moeda de maior valor para a de menor, qual a quantidade de cada moeda necessária para tal. É indicado ao utilizador que pode retirar o troco, com indicação de quais moedas foram devolvidas, e é atualizado o ficheiro do *stock* para refletir as alterações de quantidades dos produtos.  
Caso a opção inserida não se enquadre em nenhum destes casos, é informado que o comando é inválido.



## Exemplo de utilização do programa

Para utilizar este programa, temos o seguinte comando:  

```sh
python3 maquina_vending.py
```

Depois, basta inserir as opções pretendidas.