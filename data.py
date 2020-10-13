from bs4 import BeautifulSoup
import requests

def scrape_poll_data():
    pollster_data_array = []

    URL = 'https://projects.fivethirtyeight.com/polls/president-general/'

    page = requests.get(URL)
    # print(page.content)
    soup = BeautifulSoup(page.content, 'html.parser')
    rows = soup.find_all(class_='visible-row')

    for r in rows:
        date = r.find(class_='date-wrapper').text
        # print(date, '\n')

        pollster_container = r.find(class_='pollster-container')

        pollster_links = pollster_container.find_all("a")

        pollster_name = pollster_links[-1].text  # Accesses lasta element of the link array.

        # print(pollster_name)
        sample_size = r.find(class_='sample').text
        leader = r.find(class_='leader').text
        net = r.find(class_='net').text

        # print(sample_size, leader,net,'\n')

        # Getting the percent favorable for Trump and Biden

        values = r.find_all(class_='value')

        # If the other value is hidden by the "more" button

        if len(values) == 1:
            next_slbling = r.findNext("tr")
            value = next_slbling.find(class_="value")
            values.append(value)

        trump_fav = values[0].find(class_="heat-map").text
        biden_fav = values[1].find(class_="heat-map").text
        # print('values', len(values),'\n')
        pollster_data = {
            "date":date,
            "pollster_name":pollster_name,
            "sample_size":sample_size,
            "leader":leader,
            "net":net,
            "trump_fav":trump_fav,
            "biden_fav":biden_fav
        }

        pollster_data_array.append(pollster_data)

    print(len(pollster_data_array),"from data.py")
    return pollster_data_array



scrape_poll_data()