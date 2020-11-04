Escolha = input('''Para converter Binário-->Decimal digite 1\nPara converter Decimal-->Binário digite 0 : ''')

if Escolha == ('1'):                                                #A entrada do usuario é transformada em uma string para ser dividida em uma lista dos seus digitos 
    EntradaBinario = input("Digite um número binário: ")            #e então cada um dos digitos e multiplicado por 2 elevado a sua posição de 2**0 a 2**n em um for loop
    decimal = 0                                                     # no qual o expoente é construido com base em seu comprimento com len(EntradaBinario) - 1
    for i in range(len(EntradaBinario)):
        decimal = decimal + int(EntradaBinario[i]) * 2 ** abs((i - (len(EntradaBinario) - 1)))
    print(decimal)
else:
    EntradaDecimal = int(input('Digite um número decimal: '))
    nbin = []
    while (EntradaDecimal) > 0:
        value = int(EntradaDecimal % 2)                               # Enquanto a entrada binaria for maior que zero então value é definido como a sobra da divisão 
        EntradaDecimal = int(EntradaDecimal / 2)                      # e a EntradaDecimal é definida com a divisão  
        nbin.append(value)                                            #  e então o value e adicionado lista  e para respeitar a contagem dos bits de baixo para cima é invertido
    nbin.reverse()                                                    #  assim o loop continua até o satisfazer a condição EntradaDecimal > 0
    for SaidaBinário in nbin:
        print(SaidaBinário, end ='') 
   
