import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

# 데이터 읽기 및 처리
red_df = pd.read_csv("C:\Programing\BigData\data\data\winequality-red.csv", sep=';', header=0, engine='python')
white_df = pd.read_csv("C:\Programing\BigData\data\data\winequality-white.csv", sep=';', header=0, engine='python')

# 타입 컬럼 추가
red_df.insert(0, column='type', value='red')
white_df.insert(0, column='type', value='white')

# 데이터 합치기
wine = pd.concat([red_df, white_df])
wine.columns = wine.columns.str.replace(' ', '_')

# 회귀분석 모델 적합
Rformula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'
regression_result = ols(Rformula, data=wine).fit()

# 회귀 요약 출력
print(regression_result.summary())

# 부분회귀 플롯 시각화
fig = plt.figure(figsize=(20, 15))
fig.suptitle('Partial Regression Plots', fontsize=16)
sm.graphics.plot_partregress_grid(regression_result, fig=fig)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
