import pandas as pd
import statsmodels.formula.api as smf



final_sample_a = pd.read_csv('baseline_a.csv')
final_sample_a['month_str'] = pd.Categorical(final_sample_a.month)
final_sample_a['week_str'] = pd.Categorical(final_sample_a.week)
model_a = smf.ols('rate ~ wk_flag*index_flag + month_str + week_str + city + city_name', data=final_sample_a).fit()

final_sample_b = pd.read_csv('baseline_b.csv')
final_sample_b['month_str'] = pd.Categorical(final_sample_b.month)
final_sample_b['week_str'] = pd.Categorical(final_sample_b.week)
model_b = smf.ols('rate ~ wk_flag*index_flag + month_str + week_str + city + city_name', data=final_sample_b).fit()


final_sample_c = pd.read_csv('baseline_c.csv')
final_sample_c['month_str'] = pd.Categorical(final_sample_c.month)
final_sample_c['week_str'] = pd.Categorical(final_sample_c.week)
model_c = smf.ols('rate ~ wk_flag*index_flag + month_str + week_str + city + city_name', data=final_sample_c).fit()

final_sample_d = pd.read_csv('baseline_d.csv')
final_sample_d['month_str'] = pd.Categorical(final_sample_d.month)
final_sample_d['week_str'] = pd.Categorical(final_sample_d.week)
model_d = smf.ols('rate ~ wk_flag*index_flag + month_str + week_str + city + city_name', data=final_sample_d).fit()

final_sample_e = pd.read_csv('baseline_e.csv')
final_sample_e['month_str'] = pd.Categorical(final_sample_e.month)
final_sample_e['week_str'] = pd.Categorical(final_sample_e.week)
model_e = smf.ols('rate ~ wk_flag*index_flag + month_str + week_str + city + city_name', data=final_sample_e).fit()

final_sample_f = pd.read_csv('baseline_f.csv')
final_sample_f['month_str'] = pd.Categorical(final_sample_f.month)
final_sample_f['week_str'] = pd.Categorical(final_sample_f.week)
model_f = smf.ols('rate ~ wk_flag*index_flag + month_str + week_str + city + city_name', data=final_sample_f).fit()