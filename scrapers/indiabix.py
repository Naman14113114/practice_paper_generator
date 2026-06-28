import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from scrapers.base import BaseScraper


class IndiaBixScraper(BaseScraper):

    def __init__(self):
        super().__init__("IndiaBix")
        self.base_url = "https://www.indiabix.com"

    # --------------------------------------------------
    # HTTP
    # --------------------------------------------------

    def get_page(self, url):

        print(f"[{self.name}] GET {url}")

        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(
                f"[{self.name}] HTTP {response.status_code}"
            )

        return BeautifulSoup(response.text, "lxml")

    # --------------------------------------------------
    # Pagination
    # --------------------------------------------------

    def get_page_urls(self, start_url):

        print(f"[{self.name}] Discovering pages...")

        soup = self.get_page(start_url)

        urls = {start_url}

        nav = soup.find(
            "nav",
            attrs={"aria-label": "Page navigation"}
        )

        if nav:

            for link in nav.find_all("a", class_="page-link"):

                href = link.get("href")

                if not href:
                    continue

                if href == "#":
                    continue

                urls.add(
                    urljoin(self.base_url, href)
                )

        urls = sorted(urls)

        print(f"[{self.name}] {len(urls)} page(s) discovered.")

        return urls

    # --------------------------------------------------
    # Single Page
    # --------------------------------------------------

    def get_questions(self, url):

        soup = self.get_page(url)

        blocks = soup.find_all(
            "div",
            class_="bix-div-container"
        )

        questions = []

        for block in blocks:

            question_div = block.find(
                "div",
                class_="bix-td-qtxt"
            )

            if question_div is None:
                continue

            question_text = question_div.get_text(
                " ",
                strip=True
            )

            options = []

            option_rows = block.find_all(
                "div",
                class_="d-flex flex-row align-items-top bix-opt-row"
            )

            for row in option_rows:

                span = row.find("span")

                letter = ""

                if span:

                    for cls in span.get("class", []):

                        if cls.startswith(
                            "option-svg-letter-"
                        ):
                            letter = cls[-1].upper()

                table = row.find(
                    "table",
                    class_="ga-tbl-answer"
                )

                if table:

                    nums = table.find_all("td")

                    if len(nums) == 2:

                        value = (
                            f"{nums[0].get_text(strip=True)}/"
                            f"{nums[1].get_text(strip=True)}"
                        )

                    else:

                        value = table.get_text(
                            " ",
                            strip=True
                        )

                else:

                    value = row.get_text(
                        " ",
                        strip=True
                    )

                options.append({

                    "letter": letter,
                    "text": value

                })

            answer = block.find(

                "input",

                id=lambda x:
                x and x.startswith("hdnAnswer_")

            )

            answer_letter = (
                answer["value"]
                if answer
                else None
            )

            questions.append({

                "question": question_text,
                "options": options,
                "answer": answer_letter,
                "source": "IndiaBix",
                "topic_url": url

            })

        print(
            f"[{self.name}] {len(questions)} question(s)"
        )

        return questions

    # --------------------------------------------------
    # Whole Topic
    # --------------------------------------------------

    def scrape_topic(self, start_url):

        all_questions = []

        pages = self.get_page_urls(start_url)

        for i, page in enumerate(pages, start=1):

            print(
                f"\n[{self.name}] "
                f"Page {i}/{len(pages)}"
            )

            all_questions.extend(
                self.get_questions(page)
            )

        print(
            f"\n[{self.name}] "
            f"Collected {len(all_questions)} questions."
        )

        return all_questions
    
        
    # --------------------------------------------------
    # Discover Topics
    # --------------------------------------------------

    def discover_topics(self):

        print(f"\n[{self.name}] Discovering topics...")

        soup = self.get_page(
            "https://www.indiabix.com/aptitude/"
        )

        wrapper = soup.find(
            "div",
            class_="topics-wrapper"
        )

        if wrapper is None:
            raise Exception(
                "Could not locate topics-wrapper."
            )

        topics = {}

        for link in wrapper.find_all("a"):

            name = link.get_text(
                " ",
                strip=True
            )

            href = link.get("href")

            if not name:
                continue

            if not href:
                continue

            key = (
                name.lower()
                .replace("&", "and")
                .replace("'", "")
                .replace(".", "")
                .replace(",", "")
                .replace("-", "_")
                .replace(" ", "_")
            )

            topics[key] = href

        print(
            f"[{self.name}] Found {len(topics)} topics."
        )

        return topics