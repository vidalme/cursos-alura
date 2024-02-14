'''
def a():
    print('sou a')


def b():
    print('sou b')
    a()

def c():
    print('sou c')
    b()

c()

waves = ['Pavones','Jeffreys Bay','Puerto Escondido','Anchor Point','Pasta Point','Arugam Bay','Lance’s Right','Pipeline']

print(waves)
print('--------------')
print(waves[1])
print(waves[-1])
print(waves[-2])
print('--------------')
print(max(waves))
print(min(waves))
print('--------------')
waves[3] = 'Uluwatu'
print(waves)

print(waves)

waves[4:7] = ['Superbanks','Teahupo’o','Desert Point']
barrels = waves[4:-1]
barrels.append('Backdoor')
barrels.insert(0,'Praia do futuro')

print(barrels)
print(waves)

ceara = ['Cumbuco','Icarai', 'Iguape']
waves.extend(ceara)
print(waves)


ceara = ['Cumbuco','Icarai', 'Iguape']
eu = 'Andre'
print(eu.replace('A','O'))
print(eu)

estado = 'Ceara'

print(estado[1] )


inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)

impares =  [ n for n in inteiros if n%2!=0 ] 

print(pares)
print(impares)
'''

doc = open('file1.txt','a')
doc.write('oi bom dia \n')
doc.close()
