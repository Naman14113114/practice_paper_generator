from abc import ABC, abstractmethod


class BaseScraper(ABC):

    def __init__(self, name):
        self.name = name

        print(f"[{self.name}] Scraper initialized.")

    @abstractmethod
    def get_questions(self, url):
        pass