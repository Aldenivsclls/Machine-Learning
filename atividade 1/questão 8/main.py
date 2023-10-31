#questao 8
#ANTONIO ALDENI ALVES VASCONCELOS FILHO

import pandas as pd
df = pd.DataFrame({'A': [1, 2, np.nan, 4, 5], 'B': [np.nan, 2, 3, np.nan, 5]})
df['A'].fillna(df['A'].mean(), inplace=True)


