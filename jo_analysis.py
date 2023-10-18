# %%
import pandas as pd
from  jolibhw3 import module1

data = pd.read_csv('sample_diabetes_mellitus_data.csv')
data.head()

# %%
# Clean data
data = module1.remove_nan(data, ['age', 'gender', 'ethnicity'])
data = module1.fillmean_nan(data, ['height', 'weight'])

# %%
# Calculating the mean diabetes_mellitus for each ethnicity
# mean_diabetes_mellitus = data.groupby('ethnicity')['diabetes_mellitus'].mean()
# data['ethn_value'] = data['ethnicity'].map(mean_diabetes_mellitus)
data = module1.mean_encoding(data, 'ethnicity', 'diabetes_mellitus')

gender_map = {'M': 0, 'F': 1}
data = module1.mapping(data, 'gender', gender_map)

# %%
# Predicting values
feat_col = ['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure',
            'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']
data = module1.predict_model(data, feat_col, 'diabetes_mellitus')

# %%
