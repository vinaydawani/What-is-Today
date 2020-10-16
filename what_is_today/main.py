import rumps
import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://nationaltoday.com/what-is-today/"


def get_data(soup2):
    """Gets the data from HTML and arranges in a DataFrame.

    Parameters
    ----------
    soup2 : [BeautifulSoup Object]
        [BS4 object with website HTML]

    Returns
    -------
    df : [Pandas DataFrame Object]
        [DataFrame of name, location and content of the website events]
    """
    event_location = []
    event_header = []
    event_content = []
    date = ""

    # Scrapes the content from HTML
    headdd = soup2.find_all("div", class_="holiday-title")
    loccc = soup2.find_all("div", class_="holiday-location")
    cont1 = soup2.find_all("div", class_="holiday-content")[0].text.strip()[:-4]
    cont2 = soup2.find_all("div", class_="holiday-excerpt")

    event_content.clear()
    event_header.clear()
    event_location.clear()

    # for name, loc in zip(headdd, loccc):
    #     event_header.append(name.text)
    #     event_location.append(loc.text)

    # Extracts text from the soup objects and stores them in lists
    event_header = [x.text for x in headdd]
    event_location = [x.text for x in loccc]

    event_content.append(cont1)
    for string in cont2:
        event_content.append(string.text.strip()[:-9])

    event_header[0] = event_header[0].split("–")[0][:-1]

    event_header = [x.strip() for x in event_header]
    event_location = [x.strip() for x in event_location]
    event_content = [x.strip() for x in event_content]

    # A dataFrame to conviniently transfer data
    df = pd.DataFrame(
        {
            "Name": [x.strip() for x in event_header],
            "location": [x.strip() for x in event_location],
            "content": [x.strip() for x in event_content],
        }
    )

    return df


if __name__ == "__main__":
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    df = get_data(soup)

    menu = []

    for x in df.itertuples():
        x = list(x)
        menu.append(f"[{x[2]}] {x[1]}")

    app = rumps.App("Today")
    app.menu = menu

    app.run()
