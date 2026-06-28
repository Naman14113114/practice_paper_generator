from scrapers.indiabix import IndiaBixScraper
from storage.question_bank import QuestionBank


def main():

    scraper = IndiaBixScraper()
    bank = QuestionBank()

    topic = "probability"

    url = "https://www.indiabix.com/aptitude/probability/"

    print(f"\n[Scrape] Scraping '{topic}'...\n")

    questions = scraper.get_questions(url)

    print(f"[Scrape] Scraped {len(questions)} questions.\n")

    bank.merge(topic, questions)

    print()

    bank.list_topics()

    print("\n[Scrape] Done.")


if __name__ == "__main__":
    main()