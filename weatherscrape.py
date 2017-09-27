import bs4, requests

def getWeather(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#wwaleft > ul > li:nth-child(1) > a')
    return elems[0].text.strip()

temp = getWeather('http://www.weather.gov/')
print(temp)
