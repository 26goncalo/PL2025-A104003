# Analisador Léxico


## Autor do Trabalho

![Foto](../photo.jpg)

**Nome:** Gonçalo Monteiro Cunha  
**Número de Aluno:** A104003  
**Data:** 03/03/2025  



## Resumo

Para este TPC foi desenvolvido um analisador léxico para uma dada linguagem de *query*, que converte uma string numa sequência de *tokens*. Para isto, um programa lê cada linha do *input* nessa linguagem, separa os *tokens* e imprime as informações de cada um, como a categoria em que se enquadram, o valor que foi capturado, o número da linha e os índices onde cada um começa e acaba.  



## Enunciado

Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:
```
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000  
```



## Explicação da implementação

Para este problema, apenas foi implementada uma função, a `tokenize`, e foi incluída uma pequena lógica de leitura de input, tratamento do número da linha e chamada da função, na `main`.  



#### 1. Variáveis

É definida a variável principal, a `token_specification`, que é uma lista de tuplos (em que o primeiro elemento é o nome/categoria do *token* e o segundo é a expressão regular para o captar), e outras variáveis, como `tok_regex`, `reconhecidos` e `mo`.  


#### 2. Ciclo principal

A lógica da função consiste essencialmente no ciclo *for* que percorre os *match objects*. É criado um dicionário de cada *match* e verificada cada entrada do mesmo, inserindo, no final, o *token* `t` em `reconhecidos`, que é a variável a ser retornada. Caso o *token* seja um *SKIP*, apenas é ignorado e caso não se tenha inserido em nenhum dos outros casos, o *token* é considerado um erro.  



## Exemplo de utilização do programa

De modo a colocar o programa a correr, deve-se fazer:

```sh
python3 analisador_lexico.py 
```

O programa fica então à espera que sejam inseridas linhas e, para cada uma delas, apresenta o resultado.

Exemplos:

```
# DBPedia: obras de Chuck Berry

('COMMENT', '# DBPedia: obras de Chuck Berry', 1, (0, 31))


select ?nome ?desc where {

('KEYWORD', 'select', 2, (0, 6))
('ID', '?nome', 2, (7, 12))
('ID', '?desc', 2, (13, 18))
('KEYWORD', 'where', 2, (19, 24))
('LBRACE', '{', 2, (25, 26))


?s foaf:name "Chuck Berry"@en .

('ID', '?s', 3, (0, 2))
('PREFIX', 'foaf', 3, (3, 7))
('COLON', ':', 3, (7, 8))
('TYPE', 'name', 3, (8, 12))
('STRING', '"Chuck Berry"', 3, (13, 26))
('TAG', '@en', 3, (26, 29))
('DOT', '.', 3, (30, 31))
```