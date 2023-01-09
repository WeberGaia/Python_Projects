import forca
import adivinhacao


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        print("Jogando forca: \n")
        forca.jogar()
    elif jogo == 2:
        print("Jogando adivinhação")
        adivinhacao.jogar()


if __name__ == "__main__":   # Se você roda esse arquivo como programa principal, roda a seguinte função
    escolhe_jogo()
"""
Python Avançado
1) A função find encontra a primeira ocorrência do texto que estamos procurando e devolve o índice.
    1.1) O find também aceita um segundo parâmetro, que define a partir de qual posição gostaríamos de começar.
    1.2) find("")
    1.3) https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
    1.4) strip => retira espaços em branco do início e do final. str.strip()
    1.5) O tipo str foi criado de tal maneira que é impossível alterá-lo, qualquer função de alteração devolve uma nova string, que representa a alteração. Esse principio também é chamado de imutabilidade. Strings são imutáveis, são sequências imutáveis!

2) Listas
    2.1) Para verificar se um determinado elemento existe em uma Lista, podemos utilizar o operador in.Ele nos retorna True ou False caso o elemento esteja ou não dentro da lista verificada, tornado este processo de verificação bem simples!
    2.2) E claro, assim como temos a função min() que nos retorna o menor item da Lista, também temos a função max() que nos retorna o maior item da mesma.
    2.3) A função len() retorna a quantidade de itens das listas
    2.4) count() => contar o número de ocorrências de um determinado elemento em uma lista.
    2.5) index() => retorna o índice da primeira ocorrência de um determinado elemento em uma lista
    Uma sequência é nada mais do que um conjunto de valores ordenados. Essa ordem é definida pelo índice.

3) tupla => estrutura de dados imutável
    OBS: Outra diferença é a questão de podermos alterar a sequência ou não. Listas podem ser alteradas, podendo adicionar ou remover elementos. Tuples, uma vez criadas, não podem ser alteradas. Tuples são imutáveis .
    OBS2: Entre essas sequências, list é a única que é mutável. tuple, str e range são imutáveis.
    OBS3:Não falamos explicitamente que range é imutável, mas saiba que ele se comporta como tuples e strs.
    OBS4:Posso guardar dados de uma tupla dentro de uma lista
    OBS5: tupla[primeiro elemento][segundo elemento]
    OBS6: Transformando uma lista para tupla -> declarar a lista dentro da função tuple() e vice e versa.
    OBS7: set => não podem existir elementos duplicados. colecao = {11122233344, 22233344455, 33344455566}
    colecao.add(44455566677)
    É importante notar que o set não é uma sequência, pois não tem um índice
    Um set é uma coleção não ordenada de elementos. Cada elemento é único, isso significa que não existem elementos duplicados dentro do set.

4) Dicionários => sempre um nome associado com a idade. Sempre temos um par de valores
    nome : idade
    Nesse par, temos no lado esquerdo a chave e no lado direito o valor. Isso é importante pois usamos a chave para recuperar um valor e assim resolvemos nosso problema
    
5) Compreensão de lista
    lista = ["_" for var1 in var2] => Usa o "_" para cada var1 dentro de var2
    pares = [x(1º:conteúdo da lista) for x in inteiros if x % 2 == 0] ->

6) Leitura e escrita de arquivos
    open("nome_arquivo", "modo de trabalho (w,r,a(append))")
    Além do r, w e a existe o modificador b que devemos utilizar quando queremos trabalhar no modo binário.
    file.read()
    file.strip() => Usado também para eliminar o \n dentro de um arquivo
    .readline() => Lê apenas a linha do arquivo
    Pois o comando read() lê o arquivo inteiro de uma vez, colocando o ponteiro de leitura no final do mesmo. Se chamarmos a função read() novamente, como o ponteiro de leitura está no final, nada será lido.
    with => Função deve ser usada junto do open() para que o python se encarregue de fechar o arquivo, caso dê erro
    
7) Funções
    7.1) def nome_da_funcao(): => definição de função
    7.2) Em Python, a convenção é criarmos funções no padrão snake_case, isto é, cada palavra é iniciada com letras minúsculas e separadas por um underscore (_).
    
8) Boas práticas de código

"""