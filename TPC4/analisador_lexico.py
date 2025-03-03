import sys, re


def tokenize(linha, n):

    token_specification = [
        ('COMMENT', r'^#.*'),        # Comentário (linha começada por #)
        ('ID',      r'\?\w+'),       # ?nome, ?desc, ?s, ?w
        ('LBRACE',  r'\{'),          # {
        ('RBRACE',  r'\}'),          # }
        ('COLON',   r'\:'),          # :
        ('DOT',     r'\.'),          # .
        ('PREFIX',  r'\w+(?=:)'),    # dbo, foaf
        ('TYPE',    r'(?<=:)\w+'),   # MusicalArtist, name, artist, abstract
        ('STRING',  r'"[^"]+"'),     # "Chuck Berry"
        ('TAG',     r'@\w+'),        # @en
        ('NUM',     r'\d+'),         # 1000
        ('KEYWORD', r'[a-zA-Z]+'),   # select, where, a, LIMIT
        ('NEWLINE', r'\n'),          # Line endings
        ('SKIP',    r'[ \t]+'),      # Skip over spaces and tabs
        ('ERRO',    r'.')            # Any other character
    ]

    tok_regex = '|'.join([f'(?P<{id}>{expreg})' for (id, expreg) in token_specification])
    
    reconhecidos = []
    mo = re.finditer(tok_regex, linha)
    
    for m in mo:
        dic = m.groupdict()

        if dic['COMMENT']:
            t = ("COMMENT", dic['COMMENT'], n, m.span())
        elif dic['ID']:
            t = ("ID", dic['ID'], n, m.span())
        elif dic['LBRACE']:
            t = ("LBRACE", dic['LBRACE'], n, m.span())
        elif dic['RBRACE']:
            t = ("RBRACE", dic['RBRACE'], n, m.span())
        elif dic['COLON']:
            t = ("COLON", dic['COLON'], n, m.span())
        elif dic['DOT']:
            t = ("DOT", dic['DOT'], n, m.span())
        elif dic['PREFIX']:
            t = ("PREFIX", dic['PREFIX'], n, m.span())
        elif dic['TYPE']:
            t = ("TYPE", dic['TYPE'], n, m.span())
        elif dic['STRING']:
            t = ("STRING", dic['STRING'], n, m.span())
        elif dic['TAG']:
            t = ("TAG", dic['TAG'], n, m.span())
        elif dic['NUM']:
            t = ("NUM", int(dic['NUM']), n, m.span())
        elif dic['KEYWORD']:
            t = ("KEYWORD", dic['KEYWORD'], n, m.span())
        elif dic['SKIP']:
            pass
        else:
            t = ("ERRO", m.group(), n, m.span())
        if not (dic['SKIP'] or dic['NEWLINE']):
            reconhecidos.append(t)
        
    return reconhecidos



if __name__ == '__main__':
    n_linha = 0
    for linha in sys.stdin:
        print()
        n_linha += 1
        for tok in tokenize(linha, n_linha):
            print(tok)
        print("\n")