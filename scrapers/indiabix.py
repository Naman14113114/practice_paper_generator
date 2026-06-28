import requests
from bs4 import BeautifulSoup

from scrapers.base import BaseScraper

class IndiaBixScraper(BaseScraper):
    def __init__(self):
        super().__init__("IndiaBix")
        self.base_url = "https://www.indiabix.com"

    def get_page(self, url):
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"Failed with {response.status_code}")

        return BeautifulSoup(response.text, "lxml")
    def get_questions(self, url):

        soup = self.get_page(url)

        question_blocks = soup.find_all("div", class_="bix-div-container")

        questions = []

        for block in question_blocks:

            question_div = block.find("div", class_="bix-td-qtxt")

            if question_div is None:
                continue

            question_text = question_div.get_text(" ", strip=True)

            options = []

            option_rows = block.find_all(
                "div",
                class_="d-flex flex-row align-items-top bix-opt-row"
            )

            for row in option_rows:

                # -------------------
                # Option Letter
                # -------------------

                span = row.find("span")

                classes = span.get("class", [])

                letter = ""

                for cls in classes:
                    if cls.startswith("option-svg-letter-"):
                        letter = cls[-1].upper()

                # -------------------
                # Option Value
                # -------------------

                table = row.find("table", class_="ga-tbl-answer")

                if table:

                    nums = table.find_all("td")

                    if len(nums) == 2:
                        value = f"{nums[0].get_text(strip=True)}/{nums[1].get_text(strip=True)}"
                    else:
                        value = table.get_text(" ", strip=True)

                else:
                    value = row.get_text(" ", strip=True)

                options.append({
                    "letter": letter,
                    "text": value
                })

            answer = block.find("input", id=lambda x: x and x.startswith("hdnAnswer_"))

            answer_letter = answer["value"] if answer else None

            questions.append({
                "question": question_text,
                "options": options,
                "answer": answer_letter,
                "source": "IndiaBix",
                "topic_url": url
            })

        return questions