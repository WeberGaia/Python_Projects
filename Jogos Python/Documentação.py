"""
1) Print
    1) end='\n' => Quebra de linha
    2) sep é o separador entre os valores, por padrão o separador é um espaço em branco.
    3) print("Tentativa {} de {}".format(rodada,tentativas))
2) Valor das variáveis
    1) int => 54
    2) float => 54.65
    3) str => "Olá mundo"
    4) bool = True or False
3) Condicional
    1) if (condicional):
           print()
        else:
            print()
4) Concatenação de strings e multiplicação de variáveis
    1) a = "olá", b = "mundo", print(a+b) = olamundo
    2)  numero1 = 10
        numero2 = "20"
        produto = numero1 * numero2
        print(produto)
        20202020202020202020 => não aconteceu uma conversão automática/implícita
5) Operadores lógicos
    1) == (igualdade)
    2) >= (maior ou igual)
    3) <= (menor ou igual)
    4) != (diferente)
    5) maior (>)
    6) menor (<)
"""
"""
print("================================")
print("Bem-vindo ao jogo de adivinhação")
print("================================")
secret_num = 22
tentativas = 3
while(tentativas > 0):
    chute = int(input("Digite o seu número: "))
    print(f'Você digitou {chute}')
    if (secret_num == chute):
        print("Você acertou!!!")
    else:
        if (chute > secret_num):
            print("Você errou: Seu chute foi maior que o número secreto!!!")
        elif (chute < secret_num ):
            print("Você errou: Seu chute foi menor que o número secreto!!!")
6) Loops
    1) while()
    2) for variável in range(1,10): => variável assume os valores de range.range(start, stop, [step])
    3) break sai do bloco do laço abruptamente, continue apenas pula para próxima iteração.
7) Interpolação de strings
    1) "Tentativa {} de {}".format(1[0],5[1]); [0] posição zero de um vetor
    2) "R$ {:f}".format(1.58) => R% 1.580000 => R$ {:2f}".format(1.58) = R$ 1.58 => duas casas decimais
    3) "R$ {:7(qtd_caracteres).2f}".format(1.58) = "R$      1.58 => sete caracteres total
    4) "R$ {:07(qtd_caracteres).2f}".format(1.58) => R$ 0001.58 => sete caracteres com o acréscimo de zeros.
    5) formatação de inteiros
        1) "R$ {:07d}.format(4) => R$ 0000004
        2) "data {:2d}/{2d}".format(9,4) => data 9/4
        3) "data {:02d}/{02d}".format(9,4) => data 09/04
"""

rodada = 1
tentativas = 3
secret_num = 60
"""
while(rodada <= tentativas):
    print(f'tentativa {rodada} / {tentativas}')
    print("Tentativa {} de {}".format(rodada,tentativas))
    chute = int(input("Digite o seu número: "))
    print(f'Você digitou {chute}')
    if (secret_num == chute):
        print("Você acertou!!!")
        break
    else:
        if (chute > secret_num):
            print("Você errou: Seu chute foi maior que o número secreto!!!")
        elif (chute < secret_num ):
            print("Você errou: Seu chute foi menor que o número secreto!!!")
    rodada = rodada + 1
print("Fim do jogo")
for rodada in range(1,tentativas+1):
    print(f'tentativa {rodada} / {tentativas}')
    print("Tentativa {} de {}".format(rodada,tentativas))
    chute = int(input("Digite o número entre 1 e 100: "))
    print(f'Você digitou {chute}')
    if(chute < 1 or chute > 100):
        print("Número inválido. Digite um número entre 1 e 100")
        continue
    if (secret_num == chute):
        print("Você acertou!!!")
        break
    else:
        if (chute > secret_num):
            print("Você errou: Seu chute foi maior que o número secreto!!!")
        elif (chute < secret_num ):
            print("Você errou: Seu chute foi menor que o número secreto!!!")
print("Fim do jogo")"""