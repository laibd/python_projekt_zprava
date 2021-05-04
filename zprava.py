import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel("zkusebni_zprava.xlsx", skiprows=3)
colors=["teal","lime","aqua","magenta","gold","orange","red"]
#%%

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
testy = ["T1","T2","T3"]
studenti = [data["T1"].count(),data["T2"].count(),data["T3"].count()]
ax.bar(testy,studenti)
plt.ylabel("Počet studentů")
plt.xlabel("Termíny")
plt.title("Početní zastoupení studentů na jednotlivých termínech")
plt.show()
#%%

for i,prvek in enumerate(data["Záp."]):
    if prvek == "F":
            data["Konečné známky"]=data["Záp."].replace("F",data["Změnil"])
           
for i,prvek in enumerate(data["Konečné známky"]):
    if prvek == "F":
        data["Konečné známky"]=data["Konečné známky"].replace("F",data["Změnil.1"])
data["Konečné známky"].fillna("F",inplace = True)
data
#%%
konecneznamky=data.groupby("Konečné známky").count()["Jméno"].plot.bar(title="Přehled konečných známek",rot=0)
#%%
znamkyCel=data.groupby("Konečné známky").count()["Jméno"].plot.pie(title="Procentuální zastoupení konečných známek",colors=colors,legend=True,autopct='%0.1f%%').axis('equal')
#%%
znamkyT1=data.groupby("Záp.").count()["T1"].plot.pie(title="Procentuální zastoupení známek na prvním termínu",colors=colors,legend=True,autopct='%0.1f%%').axis('equal')
#%%
znamkyT2=data.groupby("Změnil").count()["T2"].plot.pie(title="Procentuální zastoupení známek na druhém termínu",colors=colors,legend=True,autopct='%0.1f%%').axis('equal')
#%%
znamkyT3=data.groupby("Změnil.1").count()["T3"].plot.pie(title="Procentuální zastoupení známek na třetím termínu",colors=colors,legend=True,autopct='%0.1f%%').axis('equal')
#%%
pre=pd.crosstab(index=data["Omezení"], columns=data["Záp."], values=data["Poř."], aggfunc="count")
pre.plot.bar(title="Početní zastoupení známek z jednotlivých ročníků a specializací",color=colors,legend=True,width=0.9,stacked=True)
#%%
prehled=pd.crosstab(index=data["T1"], columns=data["Záp."], values=data["Poř."], aggfunc="count")
prehled.plot.bar(title="Známky na T1",color=colors,legend=True,width=1)
#%%
prehled2=pd.crosstab(index=data["T2"], columns=data["Změnil"], values=data["Poř."], aggfunc="count")
prehled2.plot.bar(title="Známky na T2",color=colors,legend=True,width=1)
#%%
prehled3=pd.crosstab(index=data["T3"], columns=data["Změnil.1"], values=data["Poř."], aggfunc="count")
prehled3.plot.bar(title="Známky na T3",color=colors,legend=True,width=1)