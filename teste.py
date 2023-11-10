# b = input("Digite um número: ")
# input(b + 5)

# nascimento = int(input("Ano de Nascimento:"))
# ano = int(input("Ano atual:"))
# idade = ano - nascimento
# print(idade)

# print(4*3/2)

# b = int(input(20))
# a = int(input(10))
# d = int(input(25))

# print = (-b + sqrt(d))/2*a
# se chover saio com guarda-chuva
# se não não saio com guarda chuva
# idade = int(input("Digite sua idade: "))
# if idade > 18:
#     print("É maior de idade")
# elif idade ==18:
#     print("Acabou de fazer 18 anos")
# else:
#     print("É menor de idade")

# idade = int(input("Digite sua idade: "))
# print("maior de idade") if idade >=18 else print("é menor de idade")
# ano_n = int(input("Digite seu ano de nascimento: "))
# ano_a = int(input("Ano atual: "))
# if ano_a - ano_n >= 18: 
#     print("maior de idade. Digite o título: ")
# else: print("menor de idade.")

# a = 1
# while a < 5: 
#     print("teste") 
#     a = a + 1

# a = ["Marcio", "Raphael", "Lilian"]
# for a in a:
#     print(a)

# a = "descomplica"
# for a in a :
#     print(a)

# a = []
# b = 1
# print(a)
# while b <=3:
#     a.append(input("Digite um nome de aluno:"))
#     b = b + 1
# print(a)

# a = ["marcio", "bruna"]
# a.insert(1,"Hellen")
# print(a)
# a.remove("marcio")
# print(a)

#preciso lançar um laço aqui.
#tirar a média de cada aluno
#para cada aluno é necessário fazer a média, se maior que 6 passou.

# aluno   = []
# cpf     = []
# email   = [] 
# mat     = [] 
# nota1   = []
# nota2   = []
# nota3   = []
# b = 1
# print(aluno)
# while b <=1: 
#     aluno.append(input("Aluno: "))
#     cpf.append(input("CPF: "))
#     email.append(input("E-mail: "))
#     mat.append(input("Nº Matrícula: "))
#     nota1.append(input("Nota 1: "))
#     nota2.append(input("Nota 2: "))
#     nota3.append(input("Nota 3: "))
#     b = b + 1

# a = 1
# while a <= 5:
#     print(a)
# # a = a +1 

# def soma(a, b):
#     c = a + b
#     if c % 2 == 0:
#         return "Par"
#     else:
#         return "Impar"
# print(soma(4,9))
# print(soma(4,10))
# print(soma(13,9))



# nasc = int(input("Ano de nascimento: "))
# ano = int(input("Ano atual: "))
# idade = ano - nasc
# print("Você tem", idade, "anos")
# if idade < 18 :
#     print("Você não pode dirigir")
# else:
#     print("Você pode dirigir")
# print("Obrigado por participar da nossa campanha")

# def contagem(a):
#         b = a + 1
#         return b 
# print(contagem(9), ",", contagem(8), ",", contagem(7), ",",contagem(6), end = "")









# def fatorial(n):
#     if n == 1:
#         return 1
#     return  n * fatorial (n - 1)
# valor = int(input("Digite o fatorial: "))
# print(fatorial(valor))

# def fatorial(n):
#     if n == 1:
#         return 1
#     return  n * fatorial (n - 1)
# n = int(input("Digite o fatorial: "))
# print(fatorial(n))

# def f(a,b,c):
#     v = a * b * c
#     return v
# print(f(1,2,3))

# # def contagem(a):
# #         b = a + 1
# #         return b 
# # print(contagem(9), ",", contagem(8), ",", contagem(7), ",",contagem(6), end = "")

# a = (1,2,3)
# a.insert(4)
# print(a)

# #Como saber se um determinado valor existe em uma tupla
# tupla = (1,2,3,4,5,6,7,8,9,0)
# if 8 in tupla: 
#     print("Existe")
# else:
#     print("não exite")

# #Para criar dicionários dentro de uma lista basta utilizar os dois pontos :
# #Dicionários são nomenclaturas que damos para comportar outros nomes;
# #Como fazer: ao efetuar a lista adicione dois pontos e o elemento interno. 
# #No exemplo abaixo quando eu peço para printar lista e coloco conchetes ele sugere Nome ou Sobrenome.
# lista  = {"Nome":"Raphael", "Sobrenome":"Neves"}
# print(lista["Nome"], lista["Sobrenome"])


# a = {1,3,5, 6}
# b = {2,4,6}
# print(b.inssubset(a))
#Desafio: 
#1 - Criar com input e laço de repetição um cadastro de 5 nomes diferentes; 
#2 - Mostrar a lista;
#3 - Verificar se na lista tem o nome descomplica; 

# lista = []
# for a in range(5):
#     lista.append(input("Nome: "))
# print(lista)

# if "Descomplica" in lista:
#     print("Sim, Descomplica está na lista")
# else: 
#     print("Não, Descomplica não está na lista", lista)

#Codigo para importar um código de outro arquivo 'from', 'novo = nome do arquivo', 'import', 'PessoaCadastrada = classe importada'
# from novo import PessoaCadastrada
# pessoa = PessoaCadastrada("Raphael", 29)
# print(pessoa.nome)
# # print(pessoa.idade)
# # pessoa.exibir("Raphael",  29)

# # from novo import Pessoa
# # p = Pessoa()
# # print(p.caminhar(12))

# conteudo = open("arquivo.txt", "r")
# print(conteudo.read())
# # conteudo.write("Eu estou aprendento Python\n")
# # conteudo.write("para quebrar a linha no arquivo novo utilize contrabarra e N juntos\n")
# # conteudo.close()

# import requests
# ler = requests.get("https://wiki.sj.ifsc.edu.br/images/4/4a/Ecoshower.txt")
# print(ler)

# # with open("arquivo_txt","wb") as arquivo:
# #     arquivo.write(ler.content)

# a = int(input("Digite um número: "))
# b = int(input("Digite outro número: "))

# while b == 0:
#     b = int(input("Digite outro número: "))
#     resultado = a /b
#     print(resultado)


# if b == 0: 
#     print("não é possível dividir por 0")
# else: 
def somar_numeros(a,b)
    print(somar_numeros(3,5))