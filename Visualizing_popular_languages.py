import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib import style
style.use('seaborn-darkgrid')

df=pd.read_csv('data.csv', index_col=0)

c=Counter()
for lang in df["LanguagesWorkedWith"]:
    c.update(lang.split(';'))


languages=[]
lang_count=[]

for i in c.most_common(12):
    languages.append(i[0])
    lang_count.append(i[1])

languages.reverse()
lang_count.reverse()

plt.barh(languages, lang_count)     #horizontal bar-graph

plt.title('Most popular languages')
plt.xlabel('no. of people')

plt.tight_layout()
plt.show()
