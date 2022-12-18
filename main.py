#Importing Required Libraries

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

#Creating Variables to store data
country = []
no_of_projects = []

def scraper():

    #Creating scaper to scrap data

    url = 'https://opentender.eu/start'
    request = requests.get(url=url).text
    soup = bs(request,'html.parser')

    #Extracting the required data

    list_tenders = soup.find_all('li', class_ = 'portal-link')
    
    #Storing the extracted data

    for tender in list_tenders:
        country_name = tender.find('a').text
        country.append(country_name)
        no_of_tenders = tender.find('div').text
        no_of_projects.append(no_of_tenders)

    #Creating dataframe to save the extracted data in required formate

    df = pd.DataFrame(list(zip(country,no_of_projects)),columns=['Country Name','No of Tenders'])
    df.to_excel('output.xlsx',index=False)

scraper()
