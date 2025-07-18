import matplotlib.pyplot as plt 
import pandas as pa 
import numpy as np 
plt.style.use('ggplot')

#---reading the csv---
data = pa.read_csv("master.csv")


#TODO (num of male ,num of female )->pie chart

num_of_men = len(data[(data['sex']=='male') & (data['suicides_no']!=0)])
num_of_female = len(data[(data['sex']=='female') & (data['suicides_no']!=0)])
the_list1 = [num_of_men,num_of_female]
labels_one = ["num of male ",'num of female ']
explode_list = [0.1,0.1]
colors_list1 = ["#ff91af",'#98cff0']

plt.title("number of suicide with male and female")
plt.pie(the_list1,labels=labels_one,shadow=True,startangle=90,explode=explode_list,colors=colors_list1)
plt.legend()
plt.show()

#TODO the best 10 country of suicide -> bar
top_countries = data.groupby('country')['suicides_no'].sum().sort_values(ascending=False).head(10)
country_list = []
no_suicide =[]
for country,suicide_num in top_countries.items():
    country_list.append(country)
    no_suicide.append(suicide_num)
plt.figure(figsize=(6, 6))  # Make the plot wider
plt.bar(country_list, no_suicide, width=0.75,color = 'b')
plt.xticks(rotation=45, ha='right')  # Rotate labels for readability
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

#TODO the increase of suicide from 1985 to 2016 ->line plot 
year_list = []
num_of_suicide_list=[]
for i in range(1985, 2017):  # Use correct year range
    year_list.append(i)
    num_of_suicide_list.append(len(data[(data["year"] == i) & (data['suicides_no'] != 0)&(data["country"]=='Russian Federation')]))
plt.title("line of increase of num of suicide in Russian Federation")
plt.plot(year_list,num_of_suicide_list,)
plt.xlabel("years")
plt.ylabel("num of suicide")
plt.show()
