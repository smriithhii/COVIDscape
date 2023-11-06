import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#sns.set() to initialize the graphing configuration values 

def dataSetDisp(n):
    path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-25-2020.csv'
    df = pd.read_csv(path)
    #reading and importing a dataset from github
    df.drop(['FIPS', 'Admin2','Last_Update','Province_State', 'Combined_Key'], axis=1, inplace=True)
    #drop function used to drop columns which are uncessary
    df.rename(columns={'Country_Region': "Country"}, inplace=True)    
    #renaming acc to our convenience
    world = df.groupby("Country")['Confirmed','Active','Recovered','Deaths'].sum().reset_index()
    #to sort data acc to the world countries
    if(n==1):
        print(df.head())
        
    elif(n==2):  
        print("*********************************")
        print("\t\t\tARRANGED ")
        print("*********************************")
        print(world.head()) 
        
        #to display the countries in alphabetic arranged order
        
        pchar=eval(input("if you wish to view to the data in pie chart format of:\n1.Arranged\n2.Line graph and scatter graphs: "))
        if(pchar==1):
            print("Enter which of the following piecharts do you wish to view:\n")
            choice=eval(input("1.Confirmed cases pie-chart.\n2.Active cases pie-chart.\n3.Recovered cases pie-chart\
                              \n4.Death cases pie-chart."))
            if(choice==1):
                l1=world['Confirmed'].head(10).tolist()
                print(l1)
                mylabels=world['Country'].head(10).tolist()
                p1=plt.pie(l1,labels=mylabels)
                p1=plt.title("CONFIRMED Alphabetic order-Pie chart")
                plt.show(p1)
                
                #piechart for confirmed cases
                
            elif(choice==2):
                l2=world['Active'].head(10).tolist()
                mylabels=world['Country'].head(10).tolist()
                p1=plt.pie(l2,labels=mylabels)
                p1=plt.title("Alphabetic order-Pie chart-active")
                plt.show(p1)
                
                #piechart for active cases
                
            elif(choice==3):
                l3=world['Recovered'].head(10).tolist()
                mylabels=world['Country'].head(10).tolist()
                p1=plt.pie(l3,labels=mylabels)
                p1=plt.title("Alphabetic order-Pie chart-recovered")
                plt.show(p1)
                
                #pie chart for recovered cases
                
            elif(choice==4):    
                l4=world['Deaths'].head(10).tolist()
                mylabels=world['Country'].head(10).tolist()
                p1=plt.pie(l4,labels=mylabels)
                p1=plt.title("Alphabetic order-Pie chart-deaths")
                plt.show(p1)
                
                #piechart for death cases
                
            else:
                print("Enter a number within 1-4")
        elif(pchar==2):
            print("Line graph analysis of the data:\n")
            v=eval(input("1.Confirmed-Active line graph\n2.Recovered-Death line graph\n3.Confirmed-Active scatter graph\n4.Recovered-death scatter graph:\n"))
            if(v==1):
                
                #various analysis of data using line graph and scatter plots
                
                print("Line graph of Confirmed and Active cases")
                l1=world['Confirmed'].head(15).tolist()
                l2=world['Recovered'].head(15).tolist()
                p1=plt.plot(l1,l2,color='g',linewidth='4.5')
                p1=plt.title("Confirmed-LINE GRAPH")
                p1=plt.xlabel('Confirmed')
                p1=plt.ylabel('Active')
                plt.show(p1)
                
            elif(v==2):
                print("Line graph of Recovered and death cases")
                l1=world['Recovered'].head(15).tolist()
                l2=world['Deaths'].head(15).tolist()
                p1=plt.plot(l1,l2,color='b',linewidth='5.5')
                p1=plt.title("Recovered-death LINE GRAPH")
                p1=plt.xlabel('Recovered')
                p1=plt.ylabel('Death')
                plt.show(p1)
                
            elif(v==3):
                print("Scatter plot of Confirmed and Recovered cases")
                l1=world['Confirmed'].head(20).tolist()
                l2=world['Active'].head(20).tolist()
                p1=plt.scatter(l1,l2,color='y')
                p1=plt.title("Confirmed-Active Scatter GRAPH")
                p1=plt.xlabel('Confirmed')
                p1=plt.ylabel('Active')
                plt.show(p1)
                
            elif(v==4):
                print("Scatter plot of Recovered and death cases")
                l1=world['Recovered'].head(20).tolist()
                l2=world['Deaths'].head(20).tolist()
                p1=plt.scatter(l1,l2,color='r')
                p1=plt.title("Recovered and death Scatter GRAPH")
                p1=plt.xlabel('Recovered')
                p1=plt.ylabel('Deaths')
                plt.show(p1)
                
    elif(n==3):
        
        print("***********************************"*2)
        print("\t\t\tTo display top 20")
        print("***********************************"*2)
        
        top_20 = world.sort_values(by=['Confirmed'], ascending=False).head(20)
        plt.figure(figsize=(12,10))
        plot = sns.barplot(top_20['Confirmed'], top_20['Country'])
        for i,(value,name) in enumerate(zip(top_20['Confirmed'],top_20['Country'])):
            plot.text(value,i-0.05,f'{value:,.0f}',size=10)
            
            #zip function to map values to each other
            
        plt.show()
        
    elif(n==4):
        print("************************************"*2)
        print("\t\t\tPlotting confirmed and active cases for the top 5 countries")
        print("************************************"*2)
        top_5 = world.sort_values(by=['Confirmed'], ascending=False).head()
        plt.figure(figsize=(15,5))
        confirmed = sns.barplot(top_5['Confirmed'], top_5['Country'], color = 'red', label='Confirmed')
        recovered = sns.barplot(top_5['Recovered'], top_5['Country'], color = 'green', label='Recovered') 
        for i,(value,name) in enumerate(zip(top_5['Confirmed'],top_5['Country'])):
            confirmed.text(value,i-0.05,f'{value:,.0f}',size=9)
        for i,(value,name) in enumerate(zip(top_5['Recovered'],top_5['Country'])):
                recovered.text(value,i-0.05,f'{value:,.0f}',size=9)
        plt.legend(loc=4)
        plt.show()
        ch=eval(input("If you wish to view to the data in pie chart format of:\n1.Confirmed\n2.Recovered\n3.Line graph-Confirmed and recovered\n4.Scatter plot of -confirmed and recovered"))
        if(ch==1):
            print("Pie-chart for Confirmed cases only")
            l1=top_5['Confirmed'].tolist()
            mylabels=["US","Brazil","Russia",'United Kingdom','Spain']
            p1=plt.pie(l1,labels=mylabels)
            p1=plt.title("Confirmed-Pie chart")
            plt.show(p1)
            
            #confirmed pie chart for the top 5 countries
            
        elif(ch==2):
            print("Pie chart for Recovered cases only")
            l1=top_5['Recovered'].tolist()
            mylabels=["US","Brazil","Russia",'United Kingdom','Spain']
            p1=plt.pie(l1,labels=mylabels)
            p1=plt.title("Recovered-Pie chart")
            plt.show(p1)
            #confirmed pie chart for recovered cases in top 5 countries
            
        elif(ch==3):
            print("Line graph of Confirmed and recovered cases")
            l1=top_5['Confirmed'].tolist()
            l2=top_5['Recovered'].tolist()
            p1=plt.plot(l1,l2)
            p1=plt.title("Confirmed-LINE GRAPH")
            p1=plt.xlabel('Confirmed')
            p1=plt.ylabel('Recovered')
            plt.show(p1)
            
        elif(ch==4):
            print("Scatter plot of Confirmed and Recovered cases")
            l1=top_5['Confirmed'].tolist()
            l2=top_5['Recovered'].tolist()
            p1=plt.scatter(l1,l2)
            p1=plt.title("Confirmed-LINE GRAPH")
            p1=plt.xlabel('Confirmed')
            p1=plt.ylabel('Recovered')
            plt.show(p1)

def main1():
    
    print("\t\t*******************************")
    print("\t\t\t\tCOVID ANALYSIS\t\t")
    print("\t\t*******************************")    
    n=1
    while(n != 0):
        print("1.to display dataset\n2.to arrange alphabetical order\n3.Display top 20")
        print("4.top 5 confirmed and recovered:\n")
        n=eval(input())
        dataSetDisp(n)
main1()
def dataSetDisp2(n):
    
    df1 = pd.read_csv(r"C:\Users\smrit\OneDrive\Desktop\python packAGE\uk data\overview_2022-06-17.csv")  
    df1.drop(['areaCode', 'areaName', 'areaType'], 
         axis='columns', 
         inplace=True)
    print(df1.head().to_string())
    print(df1.tail().to_string())
    df1['date'] = pd.to_datetime(df1['date'])
    if(n==1):
      
        # df2 = df2.head(321)
        # print(df2.sample(10).to_string())
        
        print(df1)
    elif(n==2):
        print("data from 15-2-2020 to 31-12-2020")
        df1.sort_values(by=["date"], 
                ignore_index=True, 
                inplace=True)
        
# Want to select 2020-02-15 to 2020-12-31 dates
# Set up a mask to indicate the date election

        date_mask = (df1['date'] > '2020-02-14') & (df1['date'] <= '2020-12-31')
        
# Select all the rows that meet the mask search criteria

        df1 = df1.loc[date_mask]
        print(df1)
        
    elif(n==3):
        print("No of null values/ NaN: ")
        is_null_count = df1.isnull().sum()
        print(is_null_count)

def main2():
    
    print("**************************************"*2)
    print("\t\t\tUK COVID REPORT ANALYSIS")
    print("**************************************"*2)
    
    #this main function focuses mainly on uk's covid report analysis 
    
    n=1
    while(n!=0):
        print("\n\n\n1.Display\n2.Sorted date arrangement\n3.To display only no of nullvalues\n")
        n=eval(input())
        dataSetDisp2(n)
       
main2()    
        
def main3():
    print("***************************"*3)
    print("\t\t\t\tUK covid data analysis and Google mobility data analysis")
    print("\t\t\t\t\tA comparitive analysis")
    print("***************************"*3)
    print('-' * 25)
    df1 = pd.read_csv(r"C:\Users\smrit\OneDrive\Desktop\python packAGE\uk data\overview_2022-06-17.csv")
    print(df1.head().to_string())
    print(df1.tail().to_string())
    
    # Drop columns that don't provide any additional data
    
    df1.drop(['areaCode', 'areaName', 'areaType'], axis='columns', inplace=True)
    
    # Set the date column to be a datetime column
    
    df1['date'] = pd.to_datetime(df1['date'])
    df1.sort_values(by=["date"], ignore_index=True, inplace=True)
    date_mask = (df1['date'] > '2020-02-14') & (df1['date'] <= '2020-12-31')
    df1 = df1.loc[date_mask]
    print(df1.head().to_string())
    print(df1.tail().to_string())
    
    #printing all the rows that meet the mask criteria 
    # Find how many null values for column and printing 
    #increase the readability , cause of presence of NaN's 
    
    is_null_count = df1.isnull().sum()
    
    print(is_null_count)
    # Remove columns with no data in them
    df1.drop(['newPeopleVaccinatedFirstDoseByPublishDate',
              'newPeopleVaccinatedSecondDoseByPublishDate'],
             axis='columns',
             inplace=True)
    # Select a random sample of 10 rows form the DataFrame
    #selecting 10 random rows so that we cn have a simpler set of data with 
    #most meaningful information only
    
    print(df1.sample(10).to_string())
    print('-' * 25)
    
    # Load the google Mobility data for the UK which was taken from uk royal health website
    df2 = pd.read_csv(r"C:\Users\smrit\OneDrive\Desktop\python packAGE\regional mobility\2020_AE_Region_Mobility_Report.csv")
    #google mobility datasets are datsets that are updated periodically w.r.t changes 
    # Drop columns that don't provide any additional data
    
    df2.drop(['country_region_code',
              'country_region',
              'sub_region_1',
              'sub_region_2',
              'metro_area',
              'iso_3166_2_code',
              'census_fips_code',
              'place_id'],
             axis='columns',
             inplace=True)
    df2['date'] = pd.to_datetime(df2['date'])
    df2.rename(columns={'retail_and_recreation_percent_change_from_baseline': 'retail_and_recreation_change'}, inplace=True)
    
    #renaming it for better readability
    # Pick up the first 322 rows
    
    df2 = df2.head(321)
    print(df2.sample(10).to_string())
    print('-' * 25)
    # Can now concatenate them together into a single dateset
    #we could either use merge or join function that is in built in pandas 
    
    df3 = pd.merge(df1, df2, on='date')
    print(df3.sample(10).to_string())
    print(df3.corr().to_string())
    
    #to plot the relationships between data from uk govern 
    #and covid mobility dataset
    #Lets compare the hospital cases against retail and recreation change
    
    df4 = pd.concat([df3['date'],
                      df3['hospitalCases'],
                      df3['retail_and_recreation_change']], axis=1)
    
    axis1 = df4.plot(x="date", y="hospitalCases", legend=False)
    axis2 = axis1.twinx()
    df4.plot(x="date", y="retail_and_recreation_change", ax=axis2, legend=False, color="r")
    axis1.figure.legend()
    plt.show()
    
    #figure 1

    df5 = pd.concat([df3['date'],
                     df3['hospitalCases'].rolling(7).mean(),
                     df3['retail_and_recreation_change'].rolling(7).mean()], axis=1)
    ax1 = df5.plot(x="date", y="hospitalCases", legend=False, color="b")
    
    #rolling() function and then taking the mean of the rolling values. 
    
    ax2 = ax1.twinx()
    df5.plot(x="date", y="retail_and_recreation_change", ax=ax2, legend=False, color="r")
    ax1.set_ylabel('cases', color='b')
    ax2.set_ylabel('% change from baseline', color='r')
    ax1.figure.legend()
    plt.show()
    
    #figure 2 

main3()    
    