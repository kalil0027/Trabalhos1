Escolha = input('Qual converter? niveis de quantização para bits digite 1 \n número de bits para niveis de quantização digite 0: ')
if Escolha == ('1'):
    EntradaNdeQuantização = int(input('Digite o nivel de quantização: '))
    n = 1000.0
    T= n * ((EntradaNdeQuantização ** (1/n)) - 1)
    F= n * ((2 ** (1/n)) - 1)
    N = T / F
    print(round(N))
else:
    EntradaNdeBits = int(input('Digite o número de bits: '))
    SaidaNdeQuantização=2**EntradaNdeBits
    print(SaidaNdeQuantização)


