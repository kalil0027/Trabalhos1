Escolha = input('''Para converter Binário-->Decimal digite 1\nPara converter Decimal-->Binário digite 0 : ''')

if Escolha == ('1'):
    EntradaBinario = input("Digite um número binário: ")
    decimal = 0
    for i in range(len(EntradaBinario)):
        decimal = decimal + int(EntradaBinario[i]) * 2 ** abs((i - (len(EntradaBinario) - 1)))
    print(decimal)
else:
    EntradaDecimal = int(input('Digite um número decimal: '))
    nbin = []
    while (EntradaDecimal) > 0:
        value = int(EntradaDecimal % 2)
        EntradaDecimal = int(EntradaDecimal / 2)
        nbin.append(value)
    nbin.reverse()
    for SaidaBinário in nbin:
        print(SaidaBinário, end ='')