import json
import re
import os
import requests
from bs4 import BeautifulSoup
import httpx
import csv
import time
from dicts import *

basePath = '//mnt//e//webscr//tradingView//'
payloadsPath = basePath + 'jsonFiles//actualFiles//'
url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-large-cap/'



def extractCatName(country,payloadName):

    """
    Description: Grabs the names of the tables from a fileName.
    country: a string of the name of the country in question
    
    """
    myString = payloadName
    matchAgainst = '{}(.+?)Payload*'.format(country)
    n = re.search(matchAgainst,myString)
    #print(n.group(1))
    return n.group(1)

    
def countryLinksFromStr(containingString):

    """
    Description: This function takes a script that contains markets links and extracts those links
    and edits them to fit them into proper link form
    
    containingString: A string of an HTML script element 
    
    Returns: a list of links for all markets on TradingView
    """
    markets = list(set(re.findall('"url":"/markets/[world-]{0,10}stocks[-/][a-zA-Z-]{0,50}/?',containingString)))
    
    modMarkets = []
    for market in markets:
        modMarkets.append(['https://www.tradingview.com'+market[7:]+'market-movers-large-cap/',market[23:-1]])
    
    print(len(markets))
    
    return(modMarkets)

def countryLinksFromPage(pageLink):
    
    """
    Description:This function extracts the script which contains links to markets and passes it to another which
    extracts the links themselves
    
    pageLink: a link of the page from which we'd like to extract market links 
    
    Returns: A list of links of stock markets pages
    """
    
    page = requests.get(pageLink).text
    parsed = BeautifulSoup(page,'lxml')
    
    #Links are all stored in a script so they can be added and removed when the user hovers over the markets tab
    input_tag = parsed.findAll('script', attrs= {"type" : "application/prs.init-data+json"})
    
    
    for tag in input_tag:
        #only the script that contains the links has the word egypt in it. Could change
        if 'egypt' in str(tag):
            linksString = str(tag)
            
            
    return countryLinksFromStr(linksString)





def craftColumns(myDict, payloadJSON):
    
    """
    myDict: A hardcoded dicitionary that holds payload values and their corresponding manifistation on the page 
    myJSON: a json of the values sent in the payload
    Returns: A list of the column names pulled from the page itself as opposed to keys used to address the API
    """
    
    pageVals = []
    myColumns = payloadJSON['columns']
    
    for row in myColumns:
        
        if row in myDict.values():

            for key,val in myDict.items():
                

                if val == row:
                    pageVals.append(key)

        else:
            pageVals.append(row)

    return pageVals



def createCsv(fileName, country, response, valuesDict, payloadJSON):
    """
    Response: sever's response (JSON)
    fileName: Name of file you'll be creating to write the result to
    Columns: A list that will be written to the first row of the csv
    
    """
    
    columns = craftColumns(valuesDict, payloadJSON)
    if country not in os.listdir(basePath + 'csvs\\'):
        os.mkdir(basePath + 'csvs\\{}'.format(country))

    with open(basePath + 'csvs\\{}\\{}.csv'.format(country, fileName), 'w', newline='') as file:

        
        serverResp = response['data']
        writer = csv.writer(file)
        writer.writerow(columns)

        for i in range(len(serverResp)):

            writer.writerow(serverResp[i]['d'])


        
def countryAllCSVS(payloadsPath, country):
    
    tables = []
    tablesCap = []
    payloads = os.listdir(payloadsPath)
    
    for payload in payloads:
        tableName = extractCatName('canada',payload)
        tablesCap.append(tableName)
        tables.append(tableName.lower())
    
    
    for table in tables:

        for dic in dictsList:

            if dic['title'] == table:
                
                print("{} == {}".format(dic['title'],table))
                payloadString = basePath + "jsonFiles\\ActualFiles\\canada{}Payload.json".format(tablesCap[tables.index(table)])
                resp = getCountryTable((payloadString), country, reqRows = 20000)
                createCsv(country+table.capitalize(), country[1], resp, dic, json.loads(open(basePath + 'jsonFiles\\ActualFiles\\canada{}Payload.json'.format(tablesCap[tables.index(table)])).read()))
    
    


def getAllTablesAllCountries(payloadsPath):
    
    
    """
    DESCRIPTION: This function loops over all the tables for all countries and saves them into csvs in a specified folder 
    """
    
    failed_list = []
    i = 0
    countries =  countryLinksFromPage('https://www.tradingview.com/markets/stocks-usa/market-movers-large-cap/')
    print("There are {} countries\n", format(len(countries)))
    for country in countries:
        i += 1
        print("Doing country number {}".format(i))
        try:
            print("Trying to grab the csvs for {}".format(country[1]))
            countryAllCSVS(payloadsPath, country[1])
            print("SUCCESS\n\n\n")
            time.sleep(1)


        except:
            
            try:
            
                if country[1] == 'usa':
                    countryAllCSVS(payloadsPath, 'america')

                elif country[1] == 'united-kingdom':
                    countryAllCSVS(payloadsPath, 'uk')
                    
                elif country[1] == 'south-africa':
                    countryAllCSVS(payloadsPath, 'rsa')

                elif '-' in country[1]:
                    countryAllCSVS(payloadsPath, country[1].replace('-',''))
                    
                



                    print("WE FAILED")
                    print("The country we failed was: ", country[1])
                    print("\n\n\n")
                    
            except:
                failed_list.append(country)
                
    return failed_list
            
            

    
    
    


def getCountryTable(payloadPath, country, reqRows = 30000):
    
    with open(payloadPath, 'r') as f:
        
        payloadString = f.read()
        payloadString = payloadString.replace("\"range\":[0,100]","\"range\":[0,{}]".format(reqRows))

    conn = http.client.HTTPSConnection("scanner.tradingview.com")
    conn.request("POST", "/{}/scan".format(country), payloadString)
    #print("scanner.tradingview.com"+"/{}/scan".format(country))
    res = conn.getresponse()
    data = res.read()
    
    
    return json.loads(data)            




async def getCountryTableAsync(payloadPath, country, reqRows = 30000):
    
    with open(payloadPath, 'r') as f:
        
        payloadString = f.read()
        payloadString = payloadString.replace("\"range\":[0,100]","\"range\":[0,{}]".format(reqRows))
    
    async with httpx.AsyncClient() as client:

        conn = await client.get("scanner.tradingview.com")
        conn.request("POST", "/{}/scan".format(country), payloadString)
        #print("scanner.tradingview.com"+"/{}/scan".format(country))
        res = conn.getresponse()
        data = res.read()
    
    
    return json.loads(data)            






def main():

    val = countryLinksFromPage(url)
    
    print(val)






main()
