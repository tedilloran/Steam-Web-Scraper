import sys
import xlsxwriter
import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd

def queryByDeveloper(devName):
    return querySteam("https://store.steampowered.com/search/?developer={}&page=".format(devName))

def queryByPublisher(pubName):
    return querySteam("https://store.steampowered.com/search/?publisher={}&page=".format(pubName))

def getGameUrls(soup, queryURL):
    gameURLs = []
    if (len(soup.find('div', {'class': 'search_pagination_right'}).findAll('a', limit=3)) == 0):
        temp = soup.find('div', {'id': 'search_result_container'}).findAll('a', {'class': 'search_result_row'})
        [gameURLs.append(e['href']) for e in temp]
    else:
        lastPage = soup.find('div', {'class': 'search_pagination_right'}).findAll('a', limit=3)[-1].text
        if lastPage =='>':
            lastPage = soup.find('div', {'class': 'search_pagination_right'}).findAll('a', limit=3)[-2].text
        for i in range(1, int(lastPage) + 1):
            response = requests.get("{}{}".format(queryURL, i))
            soup = BeautifulSoup(response.text, 'html.parser')
            temp = soup.find('div', {'id': 'search_result_container'}).findAll('a', {'class': 'search_result_row'})
            [gameURLs.append(e['href']) for e in temp]
    return gameURLs

def filterForTitle(var):
    temp = ['\n', ' ', ', ']
    if var in temp:
        return False
    else:
        return True

def queryGamePageTitle(soup):
    if soup.find('div', {'class': 'apphub_AppName'}) != None:
        return soup.find('div', {'class': 'apphub_AppName'}).text
    elif soup.find('h2', {'class': 'pageheader'}) != None:
        return soup.find('h2', {'class': 'pageheader'}).text
    else:
        print("\033[93m Title not found")
        return "None"

def filterForDev(var):
    temp = ['\n', ' ', '<br/>', ', ']
    if var in temp:
        return False
    elif type(var) == bs4.element.NavigableString:
        return False
    else:
        return True

def queryGamePageDeveloper(soup):
    if soup.find('div', {'id': 'developers_list'}) != None:
        return soup.find('div', {'id': 'developers_list'}).find('a').text
    elif soup.find('div', {'class': 'details_block'}) != None:
        for br in soup.find('div', {'class': 'details_block'}).find('p').findAll('br'):
            br.extract()
        gameDetails = list(filter(filterForDev, list(soup.find('div', {'class': 'details_block'}).find('p'))))
        for index, e in enumerate(gameDetails):
            if e.text == 'Developer:':
                return gameDetails[index + 1].text
    else:
        print("\033[93m Developer not found")
        return "None" 

def queryGamePages(gameURLs):
    results = []
    for gamePage in gameURLs:
        response = requests.get(gamePage)
        soup = BeautifulSoup(response.text, 'html.parser')
        game = {}
        errors = []

        game['URL'] = gamePage
        game['Title'] = queryGamePageTitle(soup)
        try:
            game['Release Date'] = soup.find('div', {'class': 'date'}).text
        except:
            errors.append("Release Date")
            game['Release Date'] = "None"
        game['Developer'] = queryGamePageDeveloper(soup)
        try:
            game['Publisher'] = soup.findAll('div', {'class': 'dev_row'})[-1].find('a').text
        except:
            errors.append("Publisher")
            game['Publisher'] = "None"
        if errors:
            print("\033[93m {} not found - {}".format(", ".join(errors), gamePage))
        else:
            print("\033[94m Finished - {}".format(gamePage))
        results.append(game)
    return results

def querySteam(queryURL):
    response = requests.get("{}1".format(queryURL))
    soup = BeautifulSoup(response.text, 'html.parser')

    if (not soup.find('a', {'class': 'search_result_row'})):
        print("\033[93m No search results")
        return

    dfInput = queryGamePages(getGameUrls(soup, queryURL))

    return pd.DataFrame(dfInput, columns = ["Title","Release Date", "Developer", "Publisher", "URL"])


    # try:
    #     print("\033[94m Writing to 'output.xlsx'...")
    #     writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
    #     df.to_excel(writer, sheet_name='Sheet1', index=False)
    #     writer.save()
    # except:
    #     print("\033[93m Something went wrong - {}".format(sys.exc_info()[0]))
    # else:
    #     print("\033[92m Complete")
 
# Single Page - Clever Endeavour Games
# 2 Pages - Valve
# 8 Pages - Plug In Digital
# queryByPublisher("Valve")

# response = requests.get("https://store.steampowered.com/bundle/234/Portal_Bundle/")
# soup = BeautifulSoup(response.text, 'html.parser')
# queryGamePageDeveloper(soup)