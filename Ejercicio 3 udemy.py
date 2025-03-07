import pandas as pd

Rank = [1,2,3,4,5,6,7,8,9,10]
Country = ["China", "India", "United States", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico"]
Region = ["Asia", "Asia", "Americas", "Asia", "Asia", "Americas", "Africa", "Asia", "Europe", "Americas"]
Sub_Region = ["Eastern Asia", "Southern Asia", "Northern Asia", "Southern Asia", "Southern Asia", "Southern America", "Western Africa", "Southern Asia", "Eastern Europe", "Central America"]
Population = [1412600000, 1386946912, 333073186, 271350000, 225200000, 214231641, 211401000, 172062576, 14171015, 126014024]
indice = [0,1,2,3,4,5,6,7,8,9]

Population_1 = {"Rank": Rank, "Country":Country, "Region": Region, "Sub Region": Sub_Region, "Population": Population}
poblacion = pd.DataFrame(data=Population_1, index=indice)
print (poblacion)
# groupby
print (poblacion.groupby(by="Region"))
# Suma 
print (poblacion.groupby(by="Region").sum())
# groupby-Suma 
print (poblacion [["Region", "Population"]].groupby(by="Region").sum())
# Maximo 
print (poblacion [["Region", "Population"]].groupby(by="Region").max())