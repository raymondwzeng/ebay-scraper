from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import csvprocess

headers = ['Name', 'List_Price', 'Price_With_Shipping', 'URL']

#Strips the extra items out of the price string, allowing it to be parsed as a float.
def strip_extra(amount):
    numResult = 0.0
    if(amount == 'Free shipping'):
        return numResult
    try:
        numResult = float(amount.replace('$','').replace(',','').replace('+','').replace('shipping', ''))
    except ValueError:
        print("Error parsing amount as float.")
    return numResult

#Process -> Turn the raw HTML, run the string comparison and output all the items sorted by name, input parameters, listing price, shipping price and URL.
def process(itemName, html, parameters):
    listings = [] 
    for item in html.find_all('div', {'class': 's-item__info clearfix'}): #Item box
        shipping = item.find('span', {'class': 's-item__shipping s-item__logisticsCost'})
        if(shipping != None):
            shippingPrice = strip_extra(item.find('span', {'class': 's-item__shipping s-item__logisticsCost'}).text)
        else:
            shippingPrice = 0.0
        price = strip_extra(item.find('span', {'class': 's-item__price'}).text)
        name = item.find('h3', {'class': 's-item__title'}).text.upper() or "N/A" #Turning to upper case so we don't run into capitalization issues.
        itemForSale = {
            'Name': name,
            'List_Price': price,
            'Price_With_Shipping': price + shippingPrice,
            'URL': item.find('a', {'class': 's-item__link'})['href'],
        }
        for parameter in parameters: #For each category
            itemForSale[parameter] = None
            for search in parameters[parameter]: #For each value of said category
                if(search in name): #If a value is found, set that to the parameter that we're looking for.
                    itemForSale[parameter] = search
                    #print("Found item: " + search + " in " + name)
                    break
        listings.append(itemForSale)
    csvprocess.processIntoCSV(listings, headers, itemName+".csv")


def scrape(url):
    response = None
    try:
        response = BeautifulSoup(requests.get(url).text, "html.parser")
    except:
        print("Error while processing URL.")
        exit()
    if(response != None): #We got the the pure HTML data!
        print("Success!")
        return response


def main():
    itemName = input("Enter the item name of a given product: ") #e.g. "GTX 1060"
    eBayName = itemName.replace(' ', '+')
    soldURL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + eBayName + "&rt=nc&LH_Sold=1&LH_Complete=1" #Produces a URL of sold items.
    endingSoonURL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + eBayName + "&_sacat=27386&_sop=1" #Produces a URL of items that are ending auction soon, we do this because there's no point in bidding early as prices are 99% going to increase.
    
    finalDict = {}
    #Parameters that I need at the end -> Average rolling price for specific combination, Volume, Profit and Profit margin ()

    parameters = input("List the parameters that you want to search for: ") #e.g. "Manufacturer, Capacity" -> Should be lists
    for parameter in parameters.split(' '):
        headers.append(parameter) #Add parameter as part of CSV
        items = input("List the search terms to scrape for parameter " + parameter + " (Note: May not be completely accurate): ").split(' ')
        finalDict[parameter] = items
    
    #Input: Manufacturer, Capacity
    # For each input, ask for a list of items, these will be the terms searched for from the item name
    # e.g. "ASUS, ZOTAC, 3GB, 4GB, etc." -> This is the main part that requires manual labor. There's no way to automate this...right?
    process(itemName + '-sold', scrape(soldURL), finalDict)

main() #Execute main