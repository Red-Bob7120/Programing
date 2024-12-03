from scipy import stats
from statsmodels.formula.api import ols,glm

red_wine_quality = wine.loc[wine['type']=='red','quality']
white_wine_quality = wine.loc[wine['type']=='white','quality']
stats.ttest_ind(red_wine_quality,white_wine_quality,equal_var=False)

Rformula ='quality ~ fixed_acidity+volatile_acidity+citric_acid+residual_sugar+chlorieds + free_sulfur_dioxide + totoal_sulfur_dioxide + density + pH + sulphates + alcohol'
regressinon_result =ols(Rformula,data=wine).fit()
regressinon_result.summary()