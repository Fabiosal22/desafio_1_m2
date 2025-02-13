# Missão 1: Restaurando as Regras Escolares-----------------------------------------------------------
nota = input("Digite sua Nota: ")
if nota >= '6':
    print("Aprovado!")
else:
    print("Reprovado!")


# Missão 2: O Sistema Eleitoral Secreto---------------------------------------------------------------
idade = input("Digite sua idade: ")
if idade >= '16':
    print("Você pode votar!")
else:
    print("Você ainda não pode votar.")

# Missão 3: Recuperando o Sistema de Notas------------------------------------------------------------
nota = input("Digite sua nota: ")

if nota >= '90':
    print("Parabéns, você tirou A!")
elif '80' <= nota <= '89':
    print("Muito bem, você tirou B.")
elif '70' <= nota <= '79':
    print("Bom trabalho, você tirou C.")
elif '60' <= nota <= '69':
    print("Fique atento, você tirou D.")
else:
    print("Estude um pouco mais, você tirou F.")

# Missão 4: Restaurando a Identificação de Números----------------------------------------------------


def somar_numeros(num1, num2):
    return f"A soma de {num1} + {num2} é {num1 + num2}"


n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

resultado = somar_numeros(n1, n2)
print(resultado)


# Missão 5: Recuperando o Cofre de Segurança------------------------------------------------------
senha = input('Digite a senha:')
if senha == "Python123":
    print("Acesso permitido!")
else:
    print("Senha incorreta!")


# Missão 6: Reforçando a Segurança e a Contagem do Sistema----------------------------------------

contador = 1
while contador <= 10:
    print(contador)
    contador += 1
    print('Arquivos verificados!')
    print("nenhum erro encontrado!")


# Missão 7: Organizando a Lista--------------------------------------------------------------------

numeros = [8, 3, 10, 1, 5]
numeros.sort()
print(numeros)


# Missão 8: Acessando os Registros de Alunos------------------------------------------------------

alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
print(f"O primeiro aluno é {alunos[0]} e o último aluno é {alunos[-1]}")


# Missão 9: Calculando Dobro de um Número---------------------------------------------------------
def dobro(numero1):
    return numero1


n1 = int(input("Digite um numero:"))

resultado = dobro(f" O dobro de {n1} é {n1 + n1}")
# ou
# resultado = dobro(f" O dobro de {n1} é {n1 *2}")
print(resultado)

# Missão 10: Contando Letras-----------------------------------------------------------------------


def contar_letras(nome):
    return nome


digite_nome = input("Digite seu nome e saiba quantas letras ele tem:")
contagem = (f"O nome {digite_nome} tem {len(digite_nome)} letras.")
print(contagem)


# Mensagem Final!
print("🔹 Você restaurou a escola Vai na Web! 🎉 Agora, você se tornou um(a) verdadeiro(a) programador(a) FullStack lendário(a)!!! 🚀")
