nota = input("Digite sua nota: ")

if nota >= '90':
    print("Parabéns, você tirou A!")   # and e >=
elif nota >= '80' and nota <= '89':
    print("Muito bem, você tirou B.")
elif '70' <= nota <= '79':
    print("Bom trabalho, você tirou C.")
elif '60' <= nota <= '69':
    print("Fique atento, você tirou D.")
else:
    print("Estude um pouco mais, você tirou F.")
