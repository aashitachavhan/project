import pandas as pd
import matplotlib.pyplot as plt,numpy as np
import mysql.connector
from sqlalchemy import create_engine



def main_menu():
    print("    MAIN MENU    ")
    print("Press 1.Display")
    print("Press 2.Analyze")
    print("Press 3.Visualize")
    print("Press 4.Export to mysql")
    print("Press 5.Exit")
    print("__"*40)
    ch = int(input("Enter your choice from main menu:"))
    if ch == 1:
        display()
        main_menu()
    elif ch == 2:
        analyze()
        main_menu()
    elif ch == 3:
        visualize()
        main_menu()
    elif ch == 4:
        export()
        main_menu()
    elif ch == 5:
        pass
    else:
       print("Your choice is invalid.")
       print("Please enter it again.")
       main_menu()
       
df = pd.read_csv("co-emissions-by-sector.csv")
df = df.fillna(0)
def column_option():
    print("         SECTOR OPTION   ")
    print("Press 1.Building (CAIT, 2020)")
    print("Press 2.Industry (CAIT, 2020)")
    print("Press 3.Land-Use Change and Forestry (CAIT, 2020)")
    print("Press 4.Other Fuel Combustion (CAIT, 2020)")
    print("Press 5.Transport (CAIT, 2020)")
    print("Press 6.Manufacturing & Construction (CAIT, 2020)")
    print("Press 7.Fugitive Emissions (CAIT, 2020)")
    print("Press 8.Electricity & Heat (CAIT, 2020)")
    print("Press 9.All of them")

def visualize_option():
    print("         SECTOR OPTION   ")
    print("Press 1.'Building (CAIT, 2020)'")
    print("Press 2.'Industry (CAIT, 2020)'")
    print("Press 3.'Land-Use Change and Forestry (CAIT, 2020)'")
    print("Press 4.'Other Fuel Combustion (CAIT, 2020)'")
    print("Press 5.'Transport (CAIT, 2020)'")
    print("Press 6.'Manufacturing & Construction (CAIT, 2020)'")
    print("Press 7.'Fugitive Emissions (CAIT, 2020)'")
    print("Press 8.'Electricity & Heat (CAIT, 2020)'")

def option():
    print()
    print("Press 1.If you want to continue with analyze menu.")
    print("Press 2.Go back to main menu.")
    print() 
    o = int(input("Enter choice:"))
    print()
    if o == 1:
        analyze()
    elif o == 2:
        main_menu()
    else:
        print("Invalid choice")
        print("Please enter valid choice")
        option()
        
def d_option():
    print("Press 1.If you want to continue with display menu.")
    print("Press 2.Go back to main menu.")
    print() 
    o = int(input("Enter choice:"))
    print()
    if o == 1:
        display()
    elif o == 2:
        main_menu()
    else:
        print("Invalid choice")
        print("Please enter valid choice")
        d_option()
        
def v_option():
    print()
    print("Press 1.If you want to continue with visualize menu.")
    print("Press 2.Go back to main menu.")
    print() 
    o = int(input("Enter choice:"))
    print()
    if o == 1:
        visualize()
    elif o == 2:
        main_menu()
    else:
        print("Invalid choice")
        print("Please enter valid choice")
        option()
        
def display():
    print()
    column_option()
    print()
    cho = int(input("Enter choice from sector options to display data of given sector:"))
    cn = list(df.columns)
    print()
    if cho == 9:
        print("Display data of all the sectors")
        print()
        print(df.iloc[:,1:])
    else:
        print("Display data of sector",cn[cho+2])
        print()
        print(df.iloc[:,cho+2])
    print("__"*40)
    d_option()
    
def analyze():
    print()
    print("         ANALYZE DATA    ")
    print("Press 1.Describe data")
    print("Press 2.Country wise co2 emission ")
    print("Press 3.Year wise co2 emission")
    print("Press 4.Average co2 emission")
    print("Press 5.Minimum and maximum co2 emission")
    print("Press 6.Total co2 emission")
    print("Press 7.Average co2 emission in a year of a particular country ")
    print("Press 8.Total co2 emission in a year of a particular country")
    print("Press 9.Display code of a country")
    print("Press 10.Display data of co2 emission in a year of a particular country")
    print("Press 11.Go back to main menu")
    print("__"*40)
    ch = int(input("Enter your choice from analyze data:"))
    print()
    if ch == 1:
        print("         DESCRIBE DATA")
        print()
        print("Describe data of:")
        print()
        column_option()
        print("__"*40)
        cho = int(input("Enter choice from given sector options:"))
        cn = list(df.columns)
        print()
        if cho == 9:
            print("Describe data of all the sectors")
            print()
            print(df.describe().iloc[:,1:])
        else:
            print("Describe data of sector",cn[cho+2])
            print()
            print(df.describe().iloc[:,cho])
        print("__"*40)
        option()
        
    elif ch == 2:
        print("         COUNTRY WISE CO2 EMISSION")
        print()
        cdf = df.groupby("Entity")
        c = cdf.groups.keys()
        print(c)
        print()
        country = input("Enter country from given above:")
        countrydf = cdf.get_group(country)
        print()
        print("Country wise co2 emission in:")
        print()
        column_option()
        print("__"*40)
        cn = list(df.columns)
        cho =int(input("Enter your choice from given sector option:"))
        print()
        if cho == 9:
            print("Country wise co2 emission in all the give sectors in a country",country)
            print()
            print(countrydf.iloc[:,2:])
        else:
            print("Country wise co2 emission from" ,cn[cho+2],"sector in the country",country,"is:")
            print()
            print(countrydf.iloc[:,[2,cho+2]])
        print("__"*40)
        option()
        
    elif ch == 3:
        print("         YEAR WISE CO2 EMISSION")
        print()
        year = int(input("Enter year between 1990 to 2016:"))
        ydf = df.groupby("Year")
        yeardf = ydf.get_group(year)
        print()
        print("Year wise co2 emission in:")
        print()
        column_option()
        print("__"*40)
        cn = list(df.columns)
        cho =int(input("Enter your choice from given sector option:"))
        print()
        if cho == 9:
            print("Year wise co2 emission in all the give sectors in year",year)
            print()
            print(yeardf)
        else:
            print("Year wise co2 emission from" ,cn[cho+2],"sector in a year",year,"is:")
            print()
            print(yeardf.iloc[:,[0,cho+2]])
        print("__"*40)
        option()
        
    elif ch == 4:
        print("            AVERAGE CO2 EMISSION")
        print()
        print("Press 1.Year wise average")
        print("Press 2.Country wise average")
        print()
        c = int(input("Enter choice from above:"))
        print()
        if c == 1:
            year = int(input("Enter year between 1990 to 2016:"))
            ydf = df.groupby("Year")
            yeardf = ydf.get_group(year)
            print()
            print("Year wise average co2 emission in:")
            print()
            column_option()
            print("__"*40)
            cho =int(input("Enter your choice from given sector option:"))
            print()
            if cho == 9:
                print("Average co2 emission in all the give sectors in year",year)
                print()
                print(yeardf.mean(numeric_only = True)[1:])
            else:
                print("Average co2 emission from" ,yeardf.mean(numeric_only = True).index[cho],"sector in a year",year,"is:")
                print()
                print(yeardf.mean(numeric_only = True).iloc[cho])
        else:
            cdf = df.groupby("Entity")
            c = cdf.groups.keys()
            print(c)
            print()
            country = input("Enter country from given above:")
            countrydf = cdf.get_group(country)
            print()
            print("Country wise average co2 emission in:")
            print()
            column_option()
            print("__"*40)
            cho =int(input("Enter your choice from given sector option:"))
            print()
            if cho == 9:
                print("Average co2 emission from",country,"in all the given sectors from year 1990-2016 is :")
                print()
                print(countrydf.mean(numeric_only = True)[1:])
            else:
                print("Average co2 emission from" ,countrydf.mean(numeric_only = True).index[cho],"sector in the country",country,"from year 1990-2016 is:")
                print()
                print(countrydf.mean(numeric_only = True).iloc[cho])
        print("__"*40)
        option()
        
    elif ch == 5:
        print("         MINIMUM AND MAXIMUM CO2 EMISSION")
        print()
        print("Press 1. Year wise maximum")
        print("Press 2. Year wise minimum")
        print("Press 3. Country wise maximum")
        print("Press 4. Country wise minimum")
        print()
        c = int(input("Enter choice from above:"))
        print()
        if c == 1:
            year = int(input("Enter year between 1990 to 2016:"))
            ydf = df.groupby("Year")
            yeardf = ydf.get_group(year)
            print()
            print("Year wise maximum co2 emission in:")
            print()
            column_option()
            print("__"*40)
            cho =int(input("Enter your choice from given sector option:"))
            print()
            if cho == 9:
                print("Maximum co2 emission in all the give sectors in year",year)
                print()
                print(yeardf.max(numeric_only = True)[1:])
            else:
                print("Maximum co2 emission from" ,yeardf.max(numeric_only = True).index[cho],"sector in a year",year,"is:")
                print()
                print(yeardf.max(numeric_only = True).iloc[cho])
        elif c == 2:
            year = int(input("Enter year between 1990 to 2016:"))
            ydf = df.groupby("Year")
            yeardf = ydf.get_group(year)
            print()
            print("Year wise minimum co2 emission in:")
            print()
            column_option()
            print("__"*40)
            cho =int(input("Enter your choice from given sector option:"))
            print()
            if cho == 9:
                print("Minimum co2 emission in all the give sectors in year",year)
                print()
                print(yeardf.min(numeric_only = True)[1:])
            else:
                print("Minimum co2 emission from" ,yeardf.min(numeric_only = True).index[cho],"sector in a year",year,"is:")
                print()
                print(yeardf.min(numeric_only = True).iloc[cho])
        elif c == 3:
            cdf = df.groupby("Entity")
            c = cdf.groups.keys()
            print(c)
            print()
            country = input("Enter country from given above:")
            countrydf = cdf.get_group(country)
            print()
            print("Country wise maximum co2 emission in:")
            print()
            column_option()
            print("__"*40)
            cho =int(input("Enter your choice from given sector option:"))
            print()
            if cho == 9:
                print("Maximum co2 emission from",country,"in all the given sectors:")
                print()
                print(countrydf.max(numeric_only = True)[1:])
            else:
                print("Maximum co2 emission from" ,countrydf.max(numeric_only = True).index[cho],"sector in the country",country,"is:")
                print()
                print(countrydf.max(numeric_only = True).iloc[cho])
        elif c == 4:
            cdf = df.groupby("Entity")
            c = cdf.groups.keys()
            print(c)
            print()
            country = input("Enter country from given above:")
            countrydf = cdf.get_group(country)
            print()
            print("Country wise minimum co2 emission in:")
            print()
            column_option()
            print("__"*40)
            cho =int(input("Enter your choice from given sector option:"))
            print()
            if cho == 9:
                print("Minimum co2 emission from",country,"in all the given sectors:")
                print()
                print(countrydf.min(numeric_only = True)[1:])
            else:
                print("Minimum co2 emission from" ,countrydf.min(numeric_only = True).index[cho],"sector in the country",country,"is:")
                print()
                print(countrydf.min(numeric_only = True).iloc[cho])
        else:
            print("Invalid choice")
        print("__"*40)
        option()
        
    elif ch == 6:
        print("                TOTAL CO2 EMISSION")
        print()
        print("Press 1.Year wise total")
        print("Press 2.Country wise total")
        print()
        c = int(input("Enter choice from above:"))
        print()
        if c == 1:
            year = int(input("Enter year between 1990 to 2016:"))
            ydf = df.groupby("Year")
            yeardf = ydf.get_group(year)
            print()
            print("Year wise total co2 emission in:")
            print()
            column_option()
            print("__"*40)
            cho =int(input("Enter your choice from given sector option:"))
            print()
            if cho == 9:
                print("Total co2 emission in all the give sectors in year",year)
                print()
                print(yeardf.sum(numeric_only = True)[1:])
            else:
                print("Total co2 emission from" ,yeardf.sum(numeric_only = True).index[cho],"sector in a year",year,"is:")
                print()
                print(yeardf.sum(numeric_only = True).iloc[cho])
        else:
            cdf = df.groupby("Entity")
            c = cdf.groups.keys()
            print(c)
            print()
            country = input("Enter country from given above:")
            countrydf = cdf.get_group(country)
            print()
            print("Country wise total co2 emission in:")
            print()
            column_option()
            print("__"*40)
            cho =int(input("Enter your choice from given sector option:"))
            print()
            if cho == 9:
                print("Total co2 emission from",country,"in all the given sectors from year 1990-2016 is :")
                print()
                print(countrydf.sum(numeric_only = True)[1:])
            else:
                print("Total co2 emission from" ,countrydf.sum(numeric_only = True).index[cho],"sector in the country",country,"from year 1990-2016 is:")
                print()
                print(countrydf.sum(numeric_only = True).iloc[cho])
        print("__"*40)
        option()
        
    elif ch == 7:
        print("        AVERAGE CO2 EMISSION IN A YEAR OF A PARTICULAR COUNTRY ")
        print()
        year = int(input("Enter year between 1990 to 2016:"))
        ydf = df.groupby("Year")
        yeardf = ydf.get_group(year)
        print()
        yeardf.index = yeardf.Entity
        print(list(yeardf.index))
        print()
        country = input("Enter country from given above:")
        print()
        print("Average co2 emission in",country,"in year",year,"from all sectors is :")
        print()
        print(yeardf.loc[country,"Building (CAIT, 2020)":].mean())
        print("__"*40)
        option()
        
    elif ch == 8:
        print("           TOTAL CO2 EMISSION IN A YEAR OF A PARTICULAR COUNTRY ")
        print()
        year = int(input("Enter year between 1990 to 2016:"))
        ydf = df.groupby("Year")
        yeardf = ydf.get_group(year)
        print()
        yeardf.index = yeardf.Entity
        print(list(yeardf.index))
        print()
        country = input("Enter country from given above:")
        print()
        print("Total co2 emission in",country,"in year",year,"from all sectors is :")
        print()
        print(yeardf.loc[country,"Building (CAIT, 2020)":].sum())
        print("__"*40)
        option()
        
    elif ch == 9:
        print("          DISPLAY CODE OF THE COUNTRY ")
        print()
        ydf = df.groupby("Year")
        yeardf = ydf.get_group(1990)
        print()
        yeardf.index = yeardf.Entity
        print(list(yeardf.index))
        print()
        country = input("Enter country from given above:")
        print()
        print(yeardf.loc[country,"Code"])
        print("__"*40)
        option()
        
    elif ch == 10:
        print("    DISPLAY DATA OF CO2 EMISSION IN A YEAR OF A PARTICULAR COUNTRY ")
        print()
        year = int(input("Enter year between 1990 to 2016:"))
        ydf = df.groupby("Year")
        yeardf = ydf.get_group(year)
        print()
        yeardf.index = yeardf.Entity
        print(list(yeardf.index))
        print()
        country = input("Enter country from given above:")
        print()
        print("Data of",country,"in year",year)
        print()
        print(yeardf.loc[country])
        print("__"*40)
        option()
        
    elif ch == 11:
        main_menu()
    else :
        print("Invalid choice")
        print("Please enter valid choice")
        print("__"*40)
        analyze()

def visualize():
    print()
    print("        VISUALIZE DATA       ")
    print("Press 1. To visualize country wise")
    print("Press 2. To visualize year wise")
    print()
    ch = int(input("Enter your choice from visualize data:"))
    print()
    if ch == 1:
        print("press 1.For Line chart")
        print("press 2.For bar graph")
        print("press 3.For pie chart")
        ch = int(input("Enter your choice from charts :"))
        print()
        cdf = df.groupby("Entity")
        c = cdf.groups.keys()
        print(c)
        print()
        country = input("Enter country from given above:")
        countrydf = cdf.get_group(country)
        print()
        dfcolumn = list(countrydf.columns)
        print()
        if ch == 1:
            print("Line chart of country between year and sector")
            print()
            visualize_option()
            print("__"*40)
            cho =int(input("Enter your choice from given sector option:"))
            plt.plot(countrydf.iloc[:,[2]],countrydf.iloc[:,[cho+2]],"r*",linestyle = "-")
            plt.xlabel("Year")
            plt.ylabel(dfcolumn[cho+2])
            plt.title("co2 emission in {} from sector {} ".format(country,dfcolumn[cho+2]))
            plt.show()
        elif ch == 2:
            print("Bar graph of country between year and sector")
            print()
            visualize_option()
            print("__"*40)
            c =int(input("Enter sector name of your choice from given sector option:"))
            plt.bar(countrydf["Year"],countrydf.iloc[:,c+2])
            plt.xlabel("Year")
            plt.ylabel(dfcolumn[c+2])
            plt.title("co2 emission in {} from sector {} ".format(country,dfcolumn[c+2]))
            plt.show()
        elif ch == 3:
            print("Pie chart of sector of a country of different years")
            print()
            visualize_option()
            print("__"*40)
            c =int(input("Enter sector name of your choice from given sector option:"))
            plt.pie(countrydf.iloc[:,c+2],labels=countrydf["Year"],autopct="%5.2f%%")
            plt.title("co2 emission from sector {} of country {}".format(dfcolumn[c+2],country))
            plt.show()
        print("__"*40)
        v_option()
            
    if ch == 2:
        print("press 1.For Line chart")
        print("press 2.For bar graph")
        print("press 3.For pie chart")
        ch = int(input("Enter your choice from analyze data:"))
        print()
        year = int(input("Enter year between 1990 to 2016:"))
        ydf = df.groupby("Year")
        yeardf = ydf.get_group(year)
        print()
        dfcolumn = list(yeardf.columns)
        print()
        if ch == 1:
            print("Line chart of year between country and sector")
            print()
            visualize_option()
            print("__"*40)
            cho =int(input("Enter your choice from given column option:"))
            row = int(input("Enter row number from which you want to plot line chart of 10 rows:"))
            plt.plot(yeardf.iloc[row:row+10,0],yeardf.iloc[row:row+10,[cho+2]],"r*",linestyle = "-")
            plt.xlabel("country")
            plt.ylabel(dfcolumn[cho+2])
            plt.title("co2 emission from sector {} in year {}".format(dfcolumn[cho+2],year))
            plt.show()
        elif ch == 2:
            print("Bar graph of year between country and sector")
            print()
            visualize_option()
            print("__"*40)
            c =int(input("Enter sector name of your choice from given sector option:"))
            row = int(input("Enter row number from which you want to plot line chart of 10 rows:"))
            plt.bar(yeardf.iloc[row:row+10,0],yeardf.iloc[row:row+10,c+2])
            plt.xlabel("Country")
            plt.ylabel(dfcolumn[c+2])
            plt.title("co2 emission from sector {} in year {}".format(dfcolumn[c+2],year))
            plt.show()
        elif ch == 3:
            print("Pie chart of country between year and sector")
            print()
            visualize_option()
            print("__"*40)
            c =int(input("Enter sector name of your choice from given sector option:"))
            row = int(input("Enter row number from which you want to plot line chart of 10 rows:"))
            plt.pie(yeardf.iloc[row:row+10,c+2],labels=yeardf.iloc[row:row+10,0],autopct="%1.1f%%")
            plt.title("co2 emission from sector {} in year {}".format(dfcolumn[c+2],year))
            plt.show()
        print("__"*40)
        v_option()


def export():
    engine = create_engine("mysql+pymysql://root:aashita01@localhost/mgmt")
    conn = engine.connect()
    df.to_sql("co2_emission",conn,if_exists="replace")
    print()
    print("Exported to mysql")
    print()
    

    
print("                      WELCOME             ")
print("__"*40)
print("NAME : AASHITA CHAVHAN")
print("CLASS : XII 'A' ")
print("SUBJECT : INFORMATICS PRACTICES (065)")
print("TOPIC : CO2 AND GREENHOUSE GAS EMISSION")
print("__"*40)
main_menu()














