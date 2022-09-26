def ficha(nome = '<desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


#Programa Principal

n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))

if g.isnumeric():                # Vai checar se o valor digitado for um número inteiro, caso não, ele irá dar o valor 0
    g = int(g)
else:
    gols = 0
if n.strip() == '':              # Se o NOME retirando os espaços for VAZIO, a função vai receber somente os numeros de GOLS                                  
    ficha(gol = g)                 
else:
    ficha(n, g)                  # Caso o G for número inteiro e o N for um valor passado, a ficha receberá os dois valores.
