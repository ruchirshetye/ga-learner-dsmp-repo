# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path)

data['Gender'].replace('-','Agender')
gender_count = data['Gender'].value_counts()

plt.bar(gender_count.index,gender_count)
#path of the data file- path

#Code starts here 




# --------------
#Code starts here
alignment = data.Alignment.value_counts()
print(alignment.index)
plt.pie(alignment,labels = alignment.index)


# --------------
#Code starts here
sc_df = data[['Strength','Combat']]

sc_covariance = sc_df['Strength'].cov(sc_df['Combat'])
sc_strength =  sc_df.Strength.std()
sc_combat =  sc_df.Combat.std()
sc_pearson = sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)

ic_df = data[['Intelligence','Combat']]

ic_covariance = ic_df['Intelligence'].cov(ic_df['Combat'])
ic_intelligence  =  ic_df.Intelligence .std()
ic_combat =  ic_df.Combat.std()
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)



# --------------
#Code starts here

total_high = data['Total'].quantile(0.99)

super_best = data[data['Total']>total_high]

super_best_names = list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
fig, (ax_1,ax_2,ax_3)  = plt.subplots(3,1, figsize = (10,15))

ax_1.boxplot(data['Intelligence'])
ax_1.set_title('Intelligence')

ax_2.boxplot(data['Speed'])
ax_2.set_title('Speed ')

ax_3.boxplot(data['Power'])
ax_3.set_title('Power')



