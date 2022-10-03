import requests
import pandas as pd
import numpy as np
import json
import plotly.express as px
import seaborn as sns
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)


response = requests.get('http://127.0.0.1:5000').json()
print(response)

# response_pd = requests.get('http://127.0.0.1:5000/pandas').json()
# df = pd.DataFrame(response_pd, columns=['id', 'name', 'hire_date', 'gender', 'age', 'salary', 'manager_id', 'department_id'])
# print(df.loc[2:8, "name":"age"]) # вывод определенных строк и определенных столбцов
# print(df[(df["gender"] == 'F') & (df["salary"] < 55000)]) # фильтрация по определенным значениям столбцов
# salary = df[(df["gender"] == 'F') & (df["salary"] < 55000)]
# print(salary.sort_values(by = ["salary"])) # сортировка
# print(df.drop("manager_id", axis=1)) # удаление столбца
# df["profit"] = df["salary"] * 1.2 # добавление столбца
# print(df)
# df.rename(columns={"profit":"profits"}, inplace=True) # изменение имени столбца
# print(df.describe()) # статистическая информация по всему датафрейму
# print(df.groupby("gender").agg({"name":['count']})) # групировка с подсчетом людей в разрезе полов
# print(df.fillna('unknown')) # заполнение нулей значением по умолчанию

# Построение графиков

# df_graf = df[["salary", "age", "id"]]
#
# sns.barplot(x="salary", y="age", palette='hls', data=df)
# plt.show()

# frame2 = sns.countplot( x='gender', data=df)
# plt.show()

# heatmap = sns.heatmap(df_graf.corr(), vmin=-1, vmax=1, annot=True, cmap='BrBG')
# heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':18}, pad=12)
# plt.show()

# sns.scatterplot(data=df, x="salary", y="age")
# plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')
#
# x = df['salary']
# y = df['age']
# z = df['id']
#
# ax.set_xlabel("salary")
# ax.set_ylabel("age")
# ax.set_zlabel("people")
#
# ax.scatter(x, y, z)
#
# plt.show()

# sns.scatterplot(data=df, x="age", y="salary", hue="name", size=10)
# plt.show()