print("* Bem vindo ao ambiente de testes *")
print("")

## ENCONTRAR ERROS E OPÇÕES PARA SUAS SOLUÇÕES NOS CÓDIGOS ABAIXO

# Comparando variáveis int 

"""minha_idade = 24
idade_namorado = 25

if(minha_idade == idade_namorado)
    print('temos idades iguais')
else:
    print('temos idades diferentes')"""

# Comparação de variáveis estranha

"""numero1 = 10
numero2 = 10
if(numero1 = numero2):
    print("São números iguais")"""

# Somar string com int
"""idade1 = 10
idade2 = "20"
print(idade1 + idade2)

idade1 = 10
idade2 = int("20")
print(idade1 + idade2)"""

# Concatenando strings

"""nome = "Nico"
sobrenome = "Steppat"
#print(nome,sobrenome)
print(nome,sobrenome, sep="_")
#print(nome + " " + sobrenome)"""

## Usando o elif c/ lógica errada

##idade_str = input("Digite sua idade: ")
##idade = int(idade_str)

##if (idade > 18):
##    print("Você é maior de idade.")
##else:
##    if (idade < 12):
##        print("Você é uma criança.")
##    elif (idade > 12):
##        print("Você é um adolescente.")"""

## Usando o elif corretamente c/ operadores de comparação

"""idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade >= 18):
    print("Você é maior de idade.")
else:
    if (idade <= 12):
        print("Você é uma criança.")
    elif (idade >= 13):
        print("Você é um adolescente.")"""

## Corrigir o código

##usuario = input("Informe o usuário do sistema!")

##if(usuario == "Flávio"):
##    print("Seja bem-vindo Flávio!")
##else(usuario == "Douglas"):
##    print("Seja bem-vindo Douglas!")
##else(usuario == "Nico"):
##    print("Seja bem-vindo Nico")
##else:
##    print("Usuário não identificado!")

## código correto

"""usuario = input("Informe o usuário do sistema: ")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif (usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")"""

## Testando formatações

"""Em 2017 o Carnaval acontece em fevereiro do dia 24 até o dia 28"

dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017

#print("Em" ano, "o carnaval acontece em", mes, "do dia", dia_ini, "até o dia", dia_fim)
print("Em {} o carnaval acontece em {} do dia {} até o dia {}.".format(ano,mes,dia_ini,dia_fim))"""

# Usando laços com for 

"""contador = 1 
for contador in range(1,11,3):
    print(contador)"""

# Trocando a posição de strings

"""print("Tentativa {1} de {0}".format("Cordeiro","Leonardo"))"""

# DUVIDA

"""import random
aleatorio = int(random.random() * 101); # multiplicando 1 * 101 será 101 e não 100 como maior valor?
                                NÃO, porque é menor que 1, então jamais existirá 1 * 101, no máximo 0,9999999 * 101
print(aleatorio)"""

"""Correto! A função random.random() sempre nos retorna um número entre 0.0 e algum valor menor 1.0, 
multiplicando por 101 obteremos um número entre 0.0 e algum valor menor de 100.0. 
A função int() faz o trabalho de cortar as partes decimais deste número e obtemos o que queremos!"""

## Sorteio livros entre 3 alunos

"""import random

sorteado = random.randrange(0,4)

print(sorteado)

if sorteado == 1:
    print( "Paulo")
elif sorteado == 2:
    print("Juliana")
else:
    print("Tamires") # neste caso como não há elif sorteado igual a 3 associado a Tamires, seria injusto. """

# Usando a função abs

""""pontos_perdidos = (21 - 32) / 3
print("Pontos perdidos: {:7.2f}".format(pontos_perdidos))"""

# Usando indices

"""numeros = [10, 20, 30, 40, 50]

for i in range(len(numeros)):
    print("O elemento na posição", i, "é", numeros[i])


frase = "Olá, mundo!"

for i in range(len(frase)):
    print("O caractere na posição", i, "é", frase[i])"""

# Função count em listas, usa-se colchetes
# A função del também é uma função built-in, mas só funciona para sequências mutáveis como listas. 

"""valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores.count(4))"""

# Usando tuplas (são imutáveis), usa-se parenteses. Também são imutáveis as sequências do tipo str e range
# Funções built-ins: len, min e max, funcionam em listas imutáveis como as tuplas. 

"""dias = ("Seg", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
print(len(dias))
print(dias)
print(dias[3])"""

# Converter lista em tupla e vice versa

"""instrutor1 = ("Nico", 39)
instrutor2 = ("Flávio", 37)

instrutor1 = ("Nico", 39)
instrutor2 = ("Flávio", 37)
instrutores = [instrutor1, instrutor2]

print(instrutores)

print(instrutores[0][1])

linhas = []
linhas.append("linha 1")
linhas.append("linha 2")
linhas.append("linha 3")

linhas_tuple = tuple(linhas)
type(linhas_tuple)

print(linhas_tuple)

linhas_list = list(linhas_tuple)
type(linhas_list)

print(linhas_list)"""

# Usando set, não permite-se valores duplicados 
# Set não usa índices para identificar a posição, é uma coleção não ordenada de elementos. 

"""colecao = {11122233344, 22233344455, 33344455566}
colecao.add(44455566677) #vai adicionar pois não existe ainda"""

# Usando dictionary, é como um set mas sempre em pares de infos. 

instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
print(instrutores['Flavio'])