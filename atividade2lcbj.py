import os
os.system('cls')

Tot_folha = 0
Tot_pecas = 0 
Media_m = 0 
Media_f = 0 
Cont_m = 0 
Cont_f = 0 
sm = 724

for i in range(1, 15 + 1):
    Num_op = int(input('Digite o número do operário: '))
    Pecas_op = int(input('Digite a quantidade de peças que o operário produziu: '))
    Sexo_op = str(input('Digite o sexo do operário (M/F): '))
    
    while Sexo_op != 'M' and Sexo_op != 'm' and Sexo_op != 'F' and Sexo_op != 'f':
        Sexo_op = str(input('Digite o sexo do operário (M/F): '))
    
    if Pecas_op <= 30:
        Salario_op = sm
    elif Pecas_op > 30 and Pecas_op <= 35:
        Salario_op = sm + ((Pecas_op - 30) * 3 / 100 * sm)
    else:
        Salario_op = sm + ((Pecas_op - 30) * 5 / 100 * sm)
    
    print(f'O número do operário é: {Num_op}')
    print(f'O salário do operário é de: R${Salario_op :.2f}')
    Tot_folha = Tot_folha + Salario_op 
    Tot_pecas = Tot_pecas + Pecas_op
    
    if Sexo_op == 'M' or Sexo_op == 'm':
        Media_m = Media_m + Pecas_op
        Cont_m = Cont_m + 1
    else:
        Media_f = Media_f + Pecas_op
        Cont_f = Cont_f + 1
    
    if i == 1 or Salario_op > Salario_maior:
        Salario_maior = Salario_op
        Num_maior = Num_op


if Cont_m != 0:
    Media_m = Media_m / Cont_m

if Cont_f != 0:
    Media_f = Media_f / Cont_f
print(f'O total da folha de pagamento da fábrica foi de: R${Tot_folha :.2f}\nO número total de peças fabricadas no mês foi de: {Tot_pecas}\nA média de peças fabricadas pelos homens foi de: {Media_m}\nA média de peças fabricadas pelas mulheres foi de: {Media_f}\nO numero do/a operário/a de maior salário é: {Num_maior}')
