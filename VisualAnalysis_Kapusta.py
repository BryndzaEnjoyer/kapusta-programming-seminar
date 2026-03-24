

import openpyxl as xl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt

data = pd.read_csv(r"C:\Users\Lukas\Documents\GitHub\kapusta-programming-seminar\kaviaren_data.csv", sep=';', decimal=',')
order = [10, 11, 12, 1, 2, 3,]

#functionality
#1. boxplot graph: montly profit for each month + total average and median for comparison 
#2. multi-bar chart graph: average profit per day type of day for each month + total average profit for that month
#3. violin graph: distribution of profit for each day + color seperation for what type of day it was + total average and median for comparison
#4. line + bar graph: average sales of all products combined except for cakes and extras + second and third line just for the cakes and extras. Then a bar graph for motnhly total profit

def month():
    data.columns = data.columns.str.strip()
    data['Deň'] = pd.to_datetime(data["Deň"],format="%d.%m.",errors="coerce")
    return data['Deň'].dt.month

def boxplot_graph_simple(data):

    sns.boxplot(x=month(), y="Čistý zisk", data=data,order=order)
    plt.axhline(data["Čistý zisk"].mean(), color='r', linestyle='--', label='Average Profit')
    plt.axhline(data["Čistý zisk"].median(), color='g', linestyle='--', label='Median Profit')
    plt.legend()
    plt.title("Monthly Profit Boxplot")
    plt.show()
    
def boxplot_graph(data):

    data = data[data['Čistý zisk'] > -100]
    data = data[data['Typ dňa'].isin(["druhý", "prvý"])]
    sns.boxplot(x=month(), y="Čistý zisk", data=data,order=order,hue='Typ dňa')
    plt.title("Priemerný denný profit v prvý a druhý deň")
    plt.xlabel("Mesiac")
    plt.show()

def multibar_graph_og(data):
    data = data[data['Čistý zisk'] > -100]
    data = data[data['Typ dňa'].isin(["druhý", "prvý"])]
    overall_median = data["Čistý zisk"].median()
    overall_mean = data["Čistý zisk"].mean()
    data['Mesiac'] = pd.to_datetime(data["Deň"], format="%d.%m.", errors="coerce").dt.month
    monthly_avg = data.groupby(['Mesiac', 'Typ dňa' ])['Čistý zisk'].mean().reset_index()

    sns.barplot(data=monthly_avg, x='Mesiac', y='Čistý zisk', hue='Typ dňa', order=order, hue_order=['prvý', 'druhý'], errorbar="sd")
    
    plt.axhline(overall_mean, color='red', linestyle='--', label=f'Mean: {overall_mean:.2f}')   
    plt.axhline(overall_median, color='green', linestyle='--', label=f'Median: {overall_median:.2f}')
    
    plt.legend()
    plt.show()

def multibar_graph(data):

    data['Mesiac'] = pd.to_datetime(data["Deň"], format="%d.%m.", errors="coerce").dt.month
    collumns=['Čistý zisk',"Absolutná zmena","príliv kapitálu"]
    shownData = data.groupby('Mesiac')[collumns].sum().reset_index()
    
    data_plot = shownData.melt(id_vars='Mesiac', value_vars=collumns,var_name='cats',value_name="euro")
    
    sns.barplot(data=data_plot, x='Mesiac', y="euro",hue='cats', estimator=sum, order=order)
    čpOverall_mean = shownData["Čistý zisk"].mean()
    azOverall_mean = shownData["Absolutná zmena"].mean()
    pkOverall_mean = shownData["príliv kapitálu"].mean()
    
    plt.axhline(čpOverall_mean, color='blue', linestyle='--', label=f'priemerný čistý zisk: {čpOverall_mean:.2f}')
    plt.axhline(azOverall_mean, color='orange', linestyle='--', label=f'priemerná absolutná zmena: {azOverall_mean:.2f}')
    plt.axhline(pkOverall_mean, color='green', linestyle='--', label=f'priemerný príliv kapitálu: {pkOverall_mean:.2f}')
    plt.legend()
    plt.title("Celkový príliv kapitálu, absolutná zmena a čistý zisk za mesiac")
    plt.show()

   
def violin_graph():
    sns.violinplot(data=data, x="Čistý zisk", density_norm="count", inner="quart")
    sns.scatterplot(data=data,x="Čistý zisk", y=0, hue="Typ dňa")
    plt.xlabel("Čistý zisk")
    plt.ylabel("Počet")
    plt.title("Distribúcia rôznych typov dni na základe čistého zisku")
    mean_by_day = data.groupby('Typ dňa')['Čistý zisk'].mean()

    
    plt.axvline(mean_by_day["prvý"], color='orange', linestyle='--', label=f'priemerný čistý zisk za prvý deň: {mean_by_day["prvý"]:.2f}')
    plt.axvline(mean_by_day["druhý"], color='blue', linestyle='--', label=f'priemerný čistý zisk za druhý deň: {mean_by_day["druhý"]:.2f}')
    plt.axvline(mean_by_day["DOD"], color='green', linestyle='--', label=f'priemerný čistý zisk za DOD: {mean_by_day["DOD"]:.2f}')
    plt.legend()
    plt.show()  
   
def barAndLineGraph(data):
    
    data['Mesiac'] = pd.to_datetime(data["Deň"], format="%d.%m.", errors="coerce").dt.month
    #three lines
    mainProducts=["Palacinky","nutella","Toasty","espresso","capuchino"]
    extras=["ginger shot","espresso tonic","club mathe","speciality","Cold brew","Batch brew", "espresso sunrise"]
    #cakes
    
    #dataMainProducts = data.groupby('Mesiac')[mainProducts].mean().reset_index().sum(axis=1)
    #dataExtras = data.groupby('Mesiac')[extras].mean().reset_index().sum(axis=1)
    #cakes= data.groupby('Mesiac')["#koláčov"].mean().reset_index()
    #
    #fixedData= pd.concat([dataMainProducts,dataExtras, cakes], axis=1)
    
    data['Mesiac'] = pd.Categorical(data['Mesiac'], categories=order, ordered=True)
    data = data.sort_values('Mesiac')
    data["Hlavné produkty"]=data[mainProducts].sum(axis=1)
    data["Extra nápoje"]=data[extras].sum(axis=1)
    lines= ["Hlavné produkty","Extra nápoje","#koláčov"]
    lineData = data.groupby('Mesiac')[lines].mean().reset_index()
        
    #sns.barplot(data=data, x='Mesiac', y="Čistý zisk", estimator=sum, order=order)   
    sns.lineplot(data=lineData)
    plt.xlabel("Mesiac")
    plt.ylabel("Počet")
    plt.title("Priemerný počet predaných produktov za deň")
    plt.show()
    
barAndLineGraph(data)
boxplot_graph(data)
multibar_graph(data)
violin_graph()
