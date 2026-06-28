from scrapers.indiabix import IndiaBixScraper
from storage.question_bank import QuestionBank


# =====================================================
# Available Scrapers
# =====================================================

SCRAPERS = {
    "indiabix": IndiaBixScraper(),
}


# =====================================================
# Topics
# =====================================================

TOPICS = {
    "indiabix": {

        "problems_on_trains":
            "https://www.indiabix.com/aptitude/problems-on-trains/",

        "time_and_work":
            "https://www.indiabix.com/aptitude/time-and-work/",

        "profit_and_loss":
            "https://www.indiabix.com/aptitude/profit-and-loss/",

        "problems_on_ages":
            "https://www.indiabix.com/aptitude/problems-on-ages/",

        "average":
            "https://www.indiabix.com/aptitude/average/",

        "permutation_and_combination":
            "https://www.indiabix.com/aptitude/permutation-and-combination/",

        "problems_on_hcf_and_lcm":
            "https://www.indiabix.com/aptitude/problems-on-hcf-and-lcm/",

        "square_root_and_cube_root":
            "https://www.indiabix.com/aptitude/square-root-and-cube-root/",

        "chain_rule":
            "https://www.indiabix.com/aptitude/chain-rule/",

        "alligation_or_mixture":
            "https://www.indiabix.com/aptitude/alligation-or-mixture/",

        "stocks_and_shares":
            "https://www.indiabix.com/aptitude/stocks-and-shares/",

        "bankers_discount":
            "https://www.indiabix.com/aptitude/bankers-discount/",

        "time_and_distance":
            "https://www.indiabix.com/aptitude/time-and-distance/",

        "simple_interest":
            "https://www.indiabix.com/aptitude/simple-interest/",

        "partnership":
            "https://www.indiabix.com/aptitude/partnership/",

        "calendar":
            "https://www.indiabix.com/aptitude/calendar/",

        "area":
            "https://www.indiabix.com/aptitude/area/",

        "numbers":
            "https://www.indiabix.com/aptitude/numbers/",

        "decimal_fraction":
            "https://www.indiabix.com/aptitude/decimal-fraction/",

        "surds_and_indices":
            "https://www.indiabix.com/aptitude/surds-and-indices/",

        "pipes_and_cistern":
            "https://www.indiabix.com/aptitude/pipes-and-cistern/",

        "logarithm":
            "https://www.indiabix.com/aptitude/logarithm/",

        "probability":
            "https://www.indiabix.com/aptitude/probability/",

        "odd_man_out_and_series":
            "https://www.indiabix.com/aptitude/odd-man-out-and-series/",

        "height_and_distance":
            "https://www.indiabix.com/aptitude/height-and-distance/",

        "compound_interest":
            "https://www.indiabix.com/aptitude/compound-interest/",

        "percentage":
            "https://www.indiabix.com/aptitude/percentage/",

        "clock":
            "https://www.indiabix.com/aptitude/clock/",

        "volume_and_surface_area":
            "https://www.indiabix.com/aptitude/volume-and-surface-area/",

        "problems_on_numbers":
            "https://www.indiabix.com/aptitude/problems-on-numbers/",

        "simplification":
            "https://www.indiabix.com/aptitude/simplification/",

        "ratio_and_proportion":
            "https://www.indiabix.com/aptitude/ratio-and-proportion/",

        "boats_and_streams":
            "https://www.indiabix.com/aptitude/boats-and-streams/",

        "races_and_games":
            "https://www.indiabix.com/aptitude/races-and-games/",

        "true_discount":
            "https://www.indiabix.com/aptitude/true-discount/"
    }
}


# =====================================================
# Scrape One Topic
# =====================================================

def scrape_topic(website, topic):

    print("\n========================================")
    print(f"Website : {website}")
    print(f"Topic   : {topic}")
    print("========================================\n")

    scraper = SCRAPERS[website]
    bank = QuestionBank()

    url = TOPICS[website][topic]

    questions = scraper.scrape_topic(url)

    bank.merge(topic, questions)

    print(f"\nFinished '{topic}'.\n")


# =====================================================
# Scrape All Topics
# =====================================================

def scrape_all_topics(website):

    topics = TOPICS[website]

    print("\n========================================")
    print(f"Scraping ALL {len(topics)} topics")
    print("========================================\n")

    for i, topic in enumerate(topics, start=1):

        print(f"\n[{i}/{len(topics)}] {topic}")

        scrape_topic(
            website,
            topic
        )

    print("\n========================================")
    print("Finished all topics.")
    print("========================================\n")


# =====================================================
# Main
# =====================================================

def main():

    WEBSITE = "indiabix"

    # ---------------------------------
    # Choose Mode
    # ---------------------------------

    MODE = "topic"
    # MODE = "all_topics"

    # ---------------------------------
    # Topic to scrape
    # ---------------------------------

    TOPIC = "probability"

    if MODE == "topic":

        scrape_topic(
            WEBSITE,
            TOPIC
        )

    elif MODE == "all_topics":

        scrape_all_topics(
            WEBSITE
        )

    else:

        print("Unknown mode.")


if __name__ == "__main__":
    main()