import openpyxl as xl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Load data





data = pd.read_csv(r"C:\Users\Lukas\Documents\GitHub\kapusta-programming-seminar\filtrovanie_maraton.csv")
#print("Number of people still running: ",len(data))

def occurences(kat,val):
    return data[kat].value_counts().get(val,0)
def umiestnenie(kat,um):
    return data[data[kat]==um]

a=0
for i in data["Strata"]:
    if i=="---":
        a+=1

def thelastthing(data):

    # Columns we want
    time_cols = ['10 km', '21,1 km', '31,1 km', 'Čas']
    
    # Convert time columns to minutes
    for col in time_cols:
        data[col] = pd.to_timedelta(data[col], errors="coerce").dt.total_seconds() / 60
    
    # Compute mean time per category
    mean_times = data.groupby("Kategórie")[time_cols].mean().reset_index()
    
    # Reshape for seaborn
    mean_long = mean_times.melt(
        id_vars="Kategórie",
        value_vars=time_cols,
        var_name="Distance",
        value_name="Mean Time (minutes)"
    )
    
    # Keep correct order on x-axis
    order = ['10 km', '21,1 km', '31,1 km', 'Čas']
    mean_long["Distance"] = pd.Categorical(mean_long["Distance"], categories=order, ordered=True)
    
    # Plot
    plt.figure(figsize=(10,6))
    
    sns.scatterplot(
        data=mean_long,
        x="Distance",
        y="Mean Time (minutes)",
        hue="Kategórie",
        s=80
    )
    
    sns.lineplot(
        data=mean_long,
        x="Distance",
        y="Mean Time (minutes)",
        hue="Kategórie",
        legend=False
    )
    
    plt.xticks(rotation=45)
    plt.title("Average Intermediate Times per Category")
    plt.xlabel("Distance")
    plt.ylabel("Mean Time (minutes)")
    plt.tight_layout()
    plt.show()
    
thelastthing(data)
#nationalites
def piechartnat():
    c=0
    rest=0
    narnum_dict={}

    nationalities = data['Nár.'].unique()
    for nat in nationalities:
        c=occurences("Nár.",nat)
        if c<(data['Štrat. číslo'].notna().sum())/100*2:
            rest+=c
        else:
            narnum_dict[nat]=c
        c=0
    narnum_dict["others"]=rest
    plt.pie(narnum_dict.values(), labels=narnum_dict.keys(), autopct='%1.1f%%')
    plt.show()
#piechartnat()
def barchartnat():
    c=0
    rest=0
    narnum_dict={}

    nationalities = data['Nár.'].unique()
    for nat in nationalities:
        c=occurences("Nár.",nat)
        if c<(data['Štrat. číslo'].notna().sum())/100*2:
            rest+=c
        else:
            narnum_dict[nat]=c
        c=0
    narnum_dict["others"]=rest
    plt.bar(narnum_dict.keys(), narnum_dict.values())
    plt.xlabel('Nationality')
    plt.ylabel('number of runners')
    plt.show()
#barchartnat()
def timetosec(kat):
    categories={}
    a=[]

    for i in kat:
        NOTcategories=umiestnenie("Kategórie",i)
        a = pd.to_timedelta(NOTcategories["Čas"], errors="coerce").dt.total_seconds()/60       
        categories[i]=a
        a=[]
    return categories




   
#kat=["10 km","21,1 km","31,1 km"]
kat=data["Kategórie"].unique()

#scttar graph where 1 point represents average time of a category for 10km, 21.1km and 31.1km
#sns.scatterplot(data=  )




sns.kdeplot(data=pd.DataFrame(timetosec(kat)), fill=True, common_norm=False, alpha=0)
plt.xlabel("Time in minutes")
plt.axvline(umiestnenie("Priezvisko","SZÉKELY")["Čas"].apply(lambda x: pd.to_timedelta(x, errors="coerce").total_seconds()/60).iloc[0], color="red", label="Ondro Szekeli", zorder=99)
plt.text(umiestnenie("Priezvisko","SZÉKELY")["Čas"].apply(lambda x: pd.to_timedelta(x, errors="coerce").total_seconds()/60).iloc[0], 0.02, "Ondro Szekeli", rotation=90, color="red")
plt.show()
#print(kat)
#print("check this: ",umiestnenie("Priezvisko","SZÉKELY"))
sns.boxplot(data=pd.DataFrame(timetosec(kat)), orient="h")
plt.show()
sns.violinplot(data=pd.DataFrame(timetosec(kat)), orient="h" )
plt.xlabel("Time in minutes")
plt.ylabel("Category")

plt.scatter(umiestnenie("Priezvisko","SZÉKELY")["Čas"].apply(lambda x: pd.to_timedelta(x, errors="coerce").total_seconds()/60), "M hlavná kategória",s=100, color="red", label="Ondro Szekeli", zorder=99)
plt.show()
quit()     
        
    
print("Total number of runners: ", data['Štrat. číslo'].notna().sum())
print("Number of people disqulafied or still runnig: ",a)
print("Number of Kenyan runners: ", occurences("Nár.","KEN"))
print("Number of Czech runners: ", occurences("Nár.","CZE"))
print("73rd place in main category M: ", umiestnenie("Kategórie","M hlavná kategória")[umiestnenie("Kategórie","M hlavná kategória")["poradie v kategórii"]==73])
try: 
    print("73rd place in main category Ž: ", umiestnenie("Kategórie","Ž hlavná kategória").iloc[72]["Meno"],umiestnenie("Kategórie","Ž hlavná kategória").iloc[72]["Priezvisko"])   
except IndexError:
    print("There are less than 73 runners in main category Ž")
print("Number of unique clubs: ", len(umiestnenie("Kategórie","Ž hlavná kategória")))
v= umiestnenie("Kategórie","M hlavná kategória")
print(v[v["poradie v kategórii"]==73])
#Kto bol 73. v kategórii:  M hlavná kategória
#print(np.unique(data['Klub']))

w=umiestnenie("Kategórie","Z 40-49 rokov")
print("Oldest runner in W40-49: ",w[w["Roč."]==w["Roč."].min()]) 
m=umiestnenie("Klub","---")

print("A guy from 1950: \n",data.loc[(data["Roč."]==1950) &  (data["Klub"]!="---"), ["Meno","Priezvisko"]].iloc[0]) 
print("number of people from 1966: ", occurences("Roč.",1966))
print("number of people from 1966: ", len(umiestnenie("Roč.",1966)))
print("Marathon Club Žitný Ostrov: ", umiestnenie("Klub","Marathon Club Žitný Ostrov").iloc[0]["poradie v kategórii"])
print("Number of people from Marathon Club Žitný Ostrov: ", umiestnenie("Klub","Marathon Club Žitný Ostrov"))