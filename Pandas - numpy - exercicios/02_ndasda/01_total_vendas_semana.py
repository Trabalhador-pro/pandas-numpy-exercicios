## Case 1

# Você trabalha com uma pequena loja online.  
# O dono te passou a quantidade de vendas feitas em 5 dias:

# - segunda: 12  
# - terça: 15  
# - quarta: 9  
# - quinta: 18  
# - sexta: 20  

# Sua tarefa é criar um código usando NumPy que:

# - importe o numpy como np  
# - crie um array com esses valores  
# - mostre o array  
# - mostre o total de vendas da semana usando NumPy  

# %%
# Importando o Numpy e criando uma array
import numpy as np

# Vendas da semana (segunda a sexta)
vendas = np.array([12, 15, 9, 18, 20])

# Exibindo os valores
print("Vendas por dia:", vendas)

# Calculando o total da semana
total_semana = np.sum(vendas)

# Exibindo o total
print("Total da semana:", total_semana)
