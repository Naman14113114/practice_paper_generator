from pprint import pprint

from scrapers.indiabix import IndiaBixScraper

scraper = IndiaBixScraper()

topics = scraper.discover_topics()

print()

print(f"Total Topics: {len(topics)}")

print()

pprint(topics)