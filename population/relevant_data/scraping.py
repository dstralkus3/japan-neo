
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pickle

#########
# UTILS #
#########

def change_key(dict, key, new_key):
    """
    given a dictionary, key and new key, where the key is contained in the dict,
    replaces with new key and same value. Returns None
    """
    holder = dict[key]
    del dict[key]
    dict[new_key] = holder

################
# WEB SCRAPING #
################

def scrape_prefecture_city_data():
    """
    Returnns a dictionary with prefectures as keys and a list of cities as values corresponding to the cities
    contained in that prefecture
    """
    # Retrieve content
    url = "https://en.wikipedia.org/wiki/List_of_cities_in_Japan"
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")

    # Initialize container list and scrape html content
    container_list = []
    for table in soup.findAll('table'):
        if table.get('class') == ['wikitable', 'sortable']:
            tbody = table.find('tbody')
            for tr in tbody.findAll('tr'):
                td_element = tr.findAll('td')
                parsed = []
                for elt in td_element:
                    a_element = elt.find('a')
                    if a_element:
                        title = a_element.get('title')
                        href = a_element.get('href')
                        if title:
                            parsed.append(title)
                            if 'Prefecture' in title:
                                continue
                            else:
                                new_url = "https://en.wikipedia.org" + href
                                response = requests.get(new_url)
                                new_content = response.content
                                lat_lon_soup = BeautifulSoup(new_content, "html.parser")
                                div = lat_lon_soup.find('div', {'class' :'vector-body-before-content'})
                                span = div.find('span', {'class': 'geo'})
                                if span != None:
                                    lat_lon = span.text.replace(' ', '')
                                    parsed.append(lat_lon.split(';'))

                if parsed != None:
                    container_list.append(parsed)
            break

    return container_list

def parse_scraped_prefecture_data():
    """
    Reads from pickle to parse prefecture_city_list to create a python dictionary 
    containing relevant information
    """
    with open('./population/relevant_data/pickleFiles/pickledData.pkl', 'rb') as file:
        data_list = pickle.load(file)

    prefecture_dict = {}
    for elt in data_list['prefecture_city_list']:
        if len(elt) < 3:
            continue
        city, coords, prefecture = elt[0], elt[1], elt[2]
        if ',' in city:
            city = city.split(',')[0]
        if 'Prefecture' in prefecture:
            prefecture = prefecture.split(' ')[0]

        if type(prefecture) == str:
            if prefecture in prefecture_dict:
                prefecture_dict[prefecture].append([city, coords])
            else:
                prefecture_dict[prefecture] = [city, coords]

    return prefecture_dict

def scrape_prefecture_pop_and_area_dict():
    """
    Reads from a csv file and gives a dictionary with prefectures as keys
    and number of people in that prefecture as values.
    """
    df = pd.read_csv('./population/relevant_data/japanDemographics.csv')
    prefecture_pop_dict = {}
    prefecture_area_dict = {}
    for index, row in df.iterrows():
        prefecture = row['Prefecture']
        num_people = int(row['Americans'])
        prefecture_pop_dict[prefecture] = num_people
        # Scrapes web for prefecture area
        url = "https://en.wikipedia.org/wiki/List_of_Japanese_prefectures_by_area"
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find('table', {'class': ['wikitable', 'sortable']})
        tbody = table.find('tbody')
        for tr in tbody.findAll('tr'):
            tds = tr.findAll('td')
            counter = 0
            area = None
            prefect = None
            for td in tds:
                if counter == 0:
                    counter += 1
                    continue
                if counter == 1:
                    counter += 1
                    prefect = td.text
                    continue
                if counter == 2:
                    counter += 1
                    continue
                if counter == 3:
                    area = td.text
                    break
            prefecture_area_dict[prefect] = area

    # Fix inconsistencies between two dictionaries
    del prefecture_pop_dict['Total']
    del prefecture_area_dict['Japan']
    del prefecture_area_dict[None]

    change_key(prefecture_pop_dict, 'Hokkaidō', 'Hokkaido')
    change_key(prefecture_pop_dict, 'Hyōgo', 'Hyogo')
    change_key(prefecture_pop_dict, 'Kōchi', 'Kochi')
    change_key(prefecture_pop_dict, 'Ōita', 'Oita')

    for key, val in prefecture_area_dict.items():
        prefecture_area_dict[key] = prefecture_area_dict[key].replace(',', '')
    return prefecture_pop_dict, prefecture_area_dict

if __name__ == '__main__':
    pass