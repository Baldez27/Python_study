def tabuada():
    n1 = int(input('Digite um número que queira saber a tabuada: '))
    for i in range(1, 11):
        print(f"{n1} x {i} = {n1*i}")
    
print(tabuada())
