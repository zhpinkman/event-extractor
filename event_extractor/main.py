from typing import List
import requests
from bs4 import BeautifulSoup
import re


class Event_extractor:
    """

    """

    @staticmethod
    def get_usual_events(year: int, month: str) -> List[str]:
        """
        Get the list of events in the specified year and month

        provide month in the string format like "june", "july"
        """
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

        url = f"https://www.onthisday.com/events/date/{year}/{month}"
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')

        events = []

        for element in soup.find_all("li", class_="event"):

            events.append(element.get_text())

        return events

    @staticmethod
    def get_special_events(year: int, month: str, term: str) -> List[str]:
        """
        Get the list of events in the specified year and month

        Provide month in the string format like "june", "july", and the term from the list ["Historic Event", "Sports History", "FIFA World Cup", "Film & TV History", "Film Premier", "Music History"]
        """
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

        url = f"https://www.onthisday.com/events/date/{year}/{month}"
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')

        events = []

        for element in soup.find_all("div", class_="section section--highlight section--poi"):
            title = re.search(r'<span .*>(.*)</span>',
                              str((element.find_all("span", class_="poi__heading-txt"))[0])).group(1)
            if title == term:
                content = element.find_all("p")[0].get_text()
                events.append(content)

        return events
