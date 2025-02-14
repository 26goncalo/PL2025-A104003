# Somador On/Off

## Autor do Trabalho

![Foto](../photo.jpg)

**Nome:** Gonçalo Monteiro Cunha  
**Número de Aluno:** A104003  
**Data:** 14/02/2025  

## Resumo

Este trabalho consistiu em desenvolver um programa que, dado um texto, soma todas as sequências de dígitos (com um ou mais elementos) nele presentes. É ainda possível desativar e reativar esta funcionalidade, escrevendo em qualquer parte do texto **off** e **on**, respetivamente, e obter o resultado a qualquer momento, inserindo **=**.

## Enunciado

Somador on/off: criar um programa em Python (sem usar expressões regulares) que...
1. Some todas as sequências de dígitos que encontre num texto;
2. Sempre que encontrar a string "Off" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
3. Sempre que encontrar a string "On" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
4. Sempre que encontrar o caráter "=", o resultado da soma é colocado na saída.
5. No fim, coloca o valor da soma na saída.


## Explicação da Implementação

Para resolver este problema, implementei apenas uma função, a `main`, presente no ficheiro `somador.py`.  

#### 1. Variáveis

Comecei por declarar as variáveis necessárias:  

- `text`: corresponde ao texto que vai ser inserido pelo utilizador e lido do *standard input*, sendo aplicada a função `lower` para que a procura das palavras "on" e "off" seja tratada de uma forma mais simples, de modo a atender a qualquer combinação de maiúsculas e minúsculas;  
- `i`: variável para iterar sobre o texto;  
- `length`: número de caracteres do texto;  
- `counter`: variável que vai servir de somador, armazenando a soma dos valores que vai encontrando;  
- `digits`: serve para guardar as sequências de dígitos do texto. Caso vários algarismos apareçam seguidos (ex.: `a20b`), devem ser tratados como um único número (no exemplo, o número **vinte**), sendo necessário ir armazenando os algarismos;  
- `on`: *flag* que controla se o comportamento da soma está ativo (caso tenha encontrado anteriormente um "on") ou inativo (caso tenha encontrado um "off").  

#### 2. Ciclo para percorrer o texto

O programa é bastante simples, consistindo apenas num ciclo *while* para percorrer a *string* lida. Neste, é avaliado cada caracter do texto e verificado em que situação se insere:  

- Caso seja um `=`, é impresso para o terminal o valor atual da soma, verificando se existia algum valor armazenado na variável `digits` que ainda não tinha sido somado. É também reiniciada a variável `digits`;  

- Se for um `o`, é verificado se os caracteres seguintes são dois 'ff' ou se o seguinte é um 'n', para verificar de uma forma mais eficiente se estamos perante um "off" ou um "on". Perante cada um dos casos, a *flag* `on` é alterada e o índice `i` atualizado de modo a ignorar os caracteres seguintes da palavra encontrada;  

- Caso o comportamento da soma esteja ativo, se o caracter for um dígito é adicionado à variável que guarda os algarismos dos números que serão somados; se não for e se a variável `digits`tiver um número, este é então somado (quando encontramos um caracter não numérico, significa que o número completo já foi identificado e pode ser somado).  

Por último, é impresso o resultado final, tendo em atenção o caso em que o texto termina com um número, no qual é necessário atualizar a variável `counter` com o valor armazenado em `digits`.  

#### 3. Exemplo de utilização do programa

Para se utilizar este programa, basta escrever, num terminal:

```sh
python3 somador.py
```

De seguida, a aplicação irá pedir o texto a utilizar. No final, pressionando a tecla **ENTER**, o(s) resultado(s) será(ão) apresentado(s).

- Exemplo de texto:

```sh
abc2dOff4=oN100pdsl=1nc30oFfsdsa255nc=pa
```

- Output para o exemplo:
```
2       # Soma até ao primeiro =, ignorando '4' que surge após um "off"
102     # Soma até ao segundo =, adicionando '100' que vem após "on" (2 + 100)
133     # Soma final, até ao terceiro =, adicionando '1' e '30' e ignorando '255' após o "off" (102 + 1 + 30)
```