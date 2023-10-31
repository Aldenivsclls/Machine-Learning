#questao 7
#ANTONIO ALDENI ALVES VASCONCELOS FILHO

import pandas as pd
df = pd.read_csv('dados.csv')
coluna_idade = df['idade']
df_filtrado = df[df['idade'] > 30]
