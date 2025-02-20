# Análise de um dataset de obras musicais


## Autor do Trabalho

![Foto](../photo.jpg)

**Nome:** Gonçalo Monteiro Cunha  
**Número de Aluno:** A104003  
**Data:** 20/02/2025  



## Resumo

Para este trabalho foi desenvolvido um programa que lê e processa um *dataset* (o ficheiro `obras.csv`) sobre obras musicais. A partir deste, produz os seguintes resultados: uma lista ordenada com os compositores musicais existentes no ficheiro; um dicionário que associa a cada período o número de obras nele existentes; e um outro dicionário que relaciona cada período com uma lista dos títulos das obras que a ele pertencem.  
O principal desafio consistia em realizar esta tarefa sem recorrer ao módulo CSV do *Python*.  



## Enunciado

Neste TPC, é proibido usar o módulo CSV do Python;  
Deverás ler o dataset, processá-lo e criar os seguintes resultados:  
1. Lista ordenada alfabeticamente dos compositores musicais;  
2. Distribuição das obras por período: quantas obras catalogadas em cada período;  
3. Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período.  



## Explicação da Implementação

A implementação da minha solução encontra-se na função `main`, que recorre à função auxiliar `parse_entrada`. Ambas estão definidas no ficheiro `obras.py`.  



### Função `parse_entrada`

Esta função é responsável por extrair os dados de uma entrada completa do *dataset*. Estes são guardados num *array* (`campos`), em que cada índice possui o valor do campo correspondente (a primeira posição é para o campo "nome", a segunda para a "descrição", etc.). A separação é feita com base no caracter ';' (o delimitador do CSV) e tem em conta a existência deste caracter no meio das descrições das obras (como este campo aparece sempre entre aspas, é necessário controlar se estamos dentro de aspas para determinar se o ponto e vírgula é um delimitador dos campos ou não).  


#### 1. Variáveis

Esta função auxiliar recorre às seguintes principais variáveis:  

- `campos`: Variável que vai guardando os campos da entrada à medida que são encontrados. Cada campo é adicionado de uma só vez, com recurso à variável `campo_atual`;  
- `campo_atual`: Armazena, caracter a caracter, o conteúdo de um campo. Quando um delimitador é encontrado, é feito um *append* do campo armazenado ao *array* `campos` e a variável é reinicializada;  
- `aspas_flag`: Variável booleana que indica se estamos dentro de um bloco de aspas. Sempre que um caractere de aspas é encontrado, o seu valor é invertido.  


#### 2. Ciclo para percorrer a entrada

A função começa com um ciclo *for* para percorrer a entrada passada como argumento, um caracter de cada vez. De seguida, é verificado se o caracter é o símbolo de aspas e, caso seja, é atualizada a *flag*. Se não for, verifica-se se é um ponto e vírgula (e se aparece fora de aspas) e, em caso positivo, o campo atual é guardado. Caso não estivermos perante nenhum destes casos, o caracter em questão é guardado em `campo_atual`. No final, é atualizada a variável `campos` para guardar o último campo e é retornada essa lista dos campos da entrada recebida.  



### Função `main`

#### 1. Variáveis

Na função principal do programa, temos as variáveis mais relevantes:  

- `campos`: Vai armazenando cada linha do ficheiro até atingir o final de cada entrada do *dataset*;  
- `aspas_flag`: Variável booleana que funciona da mesma forma da da função auxiliar, indicando se estamos dentro de um bloco de aspas ou não;  
- `ponto_virgula_contador`: Serve para controlar se foi atingido o final de uma entrada válida. Para isso, é incrementada sempre que se encontra um delimitador. Se, no final da leitura de uma linha, o seu valor for 6 (pois temos 7 campos, logo são 6 os delimitadores), chegamos ao fim de uma entrada válida (com o número correto de campos);  
- `compositores`: Lista para armazenar todos os compositores musicais do *dataset*, excluindo repetidos;  
- `nr_obras_por_periodo`: Dicionário para relacionar cada período com o número de obras nele existentes;  
- `titulos_obras_por_periodo`: Dicionário que associa a cada período uma lista dos títulos das obras desse período.  


#### 2. Abertura do ficheiro e extração dos dados

Primeiramente, é aberto o ficheiro do *dataset*. As linhas do mesmo são guardadas numa variável, a `linhas`.  
Após isto, é feito um ciclo para percorrer cada linha (menos a primeira, do cabeçalho) e, dentro deste, temos um novo *for* para percorrer cada caracter de cada linha, onde são feitas as verificações dos caracteres. Quando se verifica que se chegou ao final de uma entrada, é chamada a função auxiliar para guardar em `obra` os campos da mesma.  
Com isto, são atribuídos a 3 variáveis os campos correspondentes, que são usados de seguida. Caso o compositor da entrada ainda não existisse, é adicionado a `compositores` (o que evita repetidos); o número de obras para o período em questão é incrementado; e o nome da obra é adicionado ao dicionário, caso ainda não existisse, na posição do período correspondente.  


#### 3. Ordenação e impressão do output

Finalmente, é feita uma ordenação dos dados necessários (os compositores e os títulos para cada período) e são impressos os dados pretendidos, usando uma formatação simples e clara.  



## Exemplo de utilização do programa

De modo a utilizar este programa, o comando a inserir no terminal é:

```sh
python3 obras.py
```

São então apresentados os resultados especificados. Segue um excerto do *output*:

```

Lista ordenada dos compositores musicais:

    Alessandro Stradella
    Antonio Maria Abbatini
    Bach, Johann Christoph
    Bach, Johann Michael
    Bach, Wilhelm Friedemann
    Balbastre, Claude
    Baldassare Galuppi
    Barbara of Portugal
    Benda, Franz
    Bernardo Pasquini
    (...)

--------------------------------------------------------------------------------

Número de obras catalogadas em cada período:

   Barroco: 26
   Clássico: 15
   Medieval: 48
   Renascimento: 41
   Século XX: 18
   Romântico: 19
   Contemporâneo: 7

--------------------------------------------------------------------------------

Lista ordenada dos títulos das obras de cada período:

    Barroco:
       Ab Irato
       Die Ideale, S.106
       Fantasy No. 2
       Hungarian Rhapsody No. 16
       Hungarian Rhapsody No. 5
       Hungarian Rhapsody No. 8
       Impromptu Op.51
       (...)
    Clássico:
       Bamboula, Op. 2
       Capriccio Italien
       Czech Suite
       (...)

```