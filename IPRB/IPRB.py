import math
k = 27
m = 22
n = 17
pop = float(k + m + n)

# probabilidade de selecionar dois indivíduos homo dominante
prob_1 = (1 / pop) * (1 / (pop - 1)) * \
    math.factorial(k) / math.factorial(k - 2)

# probabilidade de selecionar um homo dominante e um hetero
prob_2 = ((1 / pop) * (1 / (pop - 1))) * k * m * 2

# probabilidade de selecionar dois indivíduos hetero e
# e obter um indivíduo com o alelo dominante
prob_3 = ((1 / pop) * (1 / (pop - 1))) * 0.75 * \
    math.factorial(m) / math.factorial(m - 2)

# probabilidade de selecionar um homo dominante e outro homo recessivo
prob_4 = ((1 / pop) * (1 / (pop - 1))) * k * n * 2

# probabilidade de selecionar um hetero e um homo recessivo e obter um
# indivíduo com o alelo dominante
prob_5 = ((1 / pop) * (1 / (pop - 1))) * 0.5 * m * n * 2

# printa a probabilidade do evento
print prob_1 + prob_2 + prob_3 + prob_4 + prob_5


############################################################
# outra possibilidade, muito mais simples, sugerida por um
# usuário no fórum do Rosalind

# k =
# m =
# n =
# def firstLaw(k,m,n):
# N = float(k+m+n)
# return(1 - 1/N/(N-1)*(n*(n-1) + n*m + m*(m-1)/4.))
# print firstLaw(k,m,n)
