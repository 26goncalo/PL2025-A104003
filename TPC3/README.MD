# Conversor de MarkDown para HTML


## Autor do Trabalho

![Foto](../photo.jpg)

**Nome:** Gonçalo Monteiro Cunha  
**Número de Aluno:** A104003  
**Data:** 27/02/2025  



## Resumo

Este trabalho consistiu em desenvolver um programa simples que converte a sintaxe básica de *MarkDown* para *HTML*. O programa desenvolvido lê um ficheiro `.md` (no caso o `exemplo.md`) a converter e produz o ficheiro `output.html`.  



## Enunciado

Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:  

Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"  
In: `# Exemplo`  
Out: `<h1>Exemplo</h1>`  

Bold: pedaços de texto entre "**":  
In: `Este é um **exemplo** ...`  
Out: `Este é um <b>exemplo</b> ...`  

Itálico: pedaços de texto entre "*":  
In: `Este é um *exemplo* ...`  
Out: `Este é um <i>exemplo</i> ...`  

Lista numerada:  
In:  
```sh
1. Primeiro item  
2. Segundo item  
3. Terceiro item  
```
Out:  
```sh
<ol>  
<li>Primeiro item</li>  
<li>Segundo item</li>  
<li>Terceiro item</li>  
</ol>  
```

Link: [texto](endereço URL)  
In: `Como pode ser consultado em [página da UC](http://www.uc.pt)`  
Out: `Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>`  

Imagem: ![texto alternativo](path para a imagem)  
In: `Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...`  
Out: `Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...`  



## Explicação da Implementação

Para o problema em questão, implementei toda a lógica na função `main` presente em `conversor.py`.  



#### 1. Variáveis

As variáveis declaradas inicialmente foram:  

- `ficheiro_md`: Corresponde ao caminho (ou apenas o nome) para o ficheiro `.md` a converter, indicado pelo utilizador ao correr o programa;  
- `html_linhas`: Lista que guardará, linha a linha, o resultado da conversão;  
- `dentro_lista`: *Flag* que controla se estamos dentro de uma lista ou não.  


#### 2. Abertura do ficheiro, ciclo para efetuar conversão e criação do output

Inicialmente, é necessário abrir o ficheiro *MarkDown* a converter. As linhas deste são armazenadas em `conteudo_md`.  
De seguida, temos o ciclo que percorre cada linha e vai substituindo a sintaxe *MD* por *HTML*. Esta substituição é feita recorrendo a expressões regulares, definidas para cada caso da sintaxe pretendida. Para negrito, itálico, imagem e *link* foi necessário que os grupos de captura usados não fossem *greedy*, de modo a funcionar em situações "aninhadas", com mais do que um caso na mesma linha.  
É também importante notar a ordem em que algumas operações são verificadas, como a conversão de negrito ser feita antes da de itálico e a de imagem vir antes da dos *links*. Isto foi feito para garantir que não haviam conflitos entre as expressões regulares e que uma não atuava antes da pretendida. A principal função usada foi a `sub` do módulo `re`, tendo também recorrido à `match` para verificar em que caso se inseriam as linhas.  
No caso especial das listas, a abordagem foi ligeiramente mais complexa pois foi necessário verificar, recorrendo a uma variável booleana, se nos encontrávamos dentro da lista, a fim de saber em que ponto inserir o inicializador da lista (o `<ol>`) e o terminador (`</ol>`).  
No final do ciclo, é atualizada a variável `html_linhas` com a linha convertida.  
Depois disto, é colocado em `conteudo_md` todo o resultado da conversão e escrito no ficheiro de *output* (que é criado caso não exista).  



## Exemplo de utilização do programa

Para executar este programa, deve-se utilizar este comando:

```sh
python3 conversor.py <ficheiro MD a converter>
```

substituindo `<ficheiro MD a converter>` pelo nome ou caminho do ficheiro *Markdown* a converter.

Para utlizar o ficheiro de exemplo fornecido, que contém todos os exemplos da sintaxe possível de converter e vários casos especiais, o comando será:

```sh
python3 conversor.py exemplo.md
```

O ficheiro *HTML* resultante da conversão é então gerado na mesma pasta do ficheiro original. Apresenta-se de seguida o *output* para o ficheiro fornecido:

```
<h1>Exemplo de header 1</h1>

<h2>Exemplo de header 2</h2>

<h3>Exemplo de header 3</h3>

Este é um <b>exemplo de texto</b> a negrito.

Este é um <i>exemplo de texto</i> em itálico.

Este é um exemplo de uma linha com texto <i>em itálico</i> e <b>a negrito</b>, mais <b>do que uma</b> vez na <i>mesma</i> linha.

Texto <b>em <i>itálico</i> dentro de</b> negrito.

<ol>
<li>Primeiro item de uma lista</li>
<li>Segundo item da lista</li>
<li>Terceiro item da lista</li>
</ol>

<ol>
<li>Elemento 1 de uma segunda lista</li>
<li>Elemento 2 da 2ª lista</li>
</ol>

Este é um exemplo de um <a href="http://www.google.pt">link</a>

Isto é um exemplo de uma imagem: <img src="https://www.eng.uminho.pt/SiteAssets/Logo.PNG" alt="imagem"/>

Este é um exemplo de <a href="http://www.google.pt">um link</a> seguido de <a href="http://www.google.pt">outro link</a>.

Isto é um exemplo de uma imagem: <img src="https://www.eng.uminho.pt/SiteAssets/Logo.PNG" alt="imagem"/> seguida de outra imagem: <img src="https://www.eng.uminho.pt/SiteAssets/Logo.PNG" alt="imagem dois"/>.
```