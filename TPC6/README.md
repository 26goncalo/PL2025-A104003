# Analisador Sintático: recursivo descendente


## Autor do Trabalho

![Foto](../photo.jpg)

**Nome:** Gonçalo Monteiro Cunha  
**Número de Aluno:** A104003  
**Data:** 23/03/2025  



## Resumo

Este trabalho consistiu em implementar um parser recursivo descendente para reconhecer expressões matemáticas simples e calcular o seu valor.



## Enunciado

Baseado nos materiais fornecidos na aula, cria um parser LL(1) recursivo descendente que reconheça expressões aritméticas e calcule o respetivo valor.  

Exemplos de algumas frases:  

```
2+3
67-(2+3*4)
(9-2)*(13-4)
```



## Explicação da implementação

A implementação deste problema foi relativamente simples, tendo sido necessário criar os analisadores léxico e sintático para a linguagem em questão. Isto foi feito num mesmo ficheiro, o `recursivo_descendente.py`, estando separadas as partes léxica e sintática. Recorri à biblioteca *ply*, nomeadamente aos módulos *lex* e *yacc*.  

Na parte do analisador léxico, inicialmente defini os *tokens* necessários e as expressões regulares para os *tokens* simples. Depois, defini as funções necessárias (para o **NUM** e para o **ERROR**). Finalmente, é chamada a função `lex`.  

De seguida, na parte sintática, foram implementadas as regras de produção, cada uma na sua função, tratando a lógica necessária conforme o caso. A seguir a isto, tenho um comentário representativo destas mesmas regras, chamo o `yacc` e crio a lógica principal, com um ciclo *while* para reconhecer e processar cada linha inserida, assim como imprimir o resultado.  



## Exemplo de utilização do programa

O comando para executar o programa é:  

```sh
python3 recursivo_descendente.py
```

Depois, o utilizador pode ir inserindo expressões, uma a uma, e, caso sejam válidas, é apresentado o seu resultado. Caso contrário, é indicado que ocorreu um erro. Para sair, basta clicar no *Enter*.