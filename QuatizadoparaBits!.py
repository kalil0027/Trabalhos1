Escolha = input('Qual converter? niveis de quantização para bits digite 1 \n número de bits para niveis de quantização digite 0: ')
if Escolha == ('1'):
    EntradaNdeQuantização = int(input('Digite o nivel de quantização: '))
    n = 1000.0
    T= n * ((EntradaNdeQuantização ** (1/n)) - 1)                                # Para a segunda opção e usada a formula nQ = 2**n onde nQ é o nivel de quantização e o n é o número de bits
    F= n * ((2 ** (1/n)) - 1)                                                    # Para a segundo opção o n (N) é isolado assim formando T ln/ F ln ln(Logaritmo natural) 
    N = T / F                                                                    # No qual o a função logaritmo é definida por n * ((x ** (1/n)) - 1) 
    print(round(N))                                                              
else:
    EntradaNdeBits = int(input('Digite o número de bits: '))
    SaidaNdeQuantização=2**EntradaNdeBits
    print(SaidaNdeQuantização)


