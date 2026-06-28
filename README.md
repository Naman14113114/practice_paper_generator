# Practice Paper Generator

A modular Python project for building a local offline question bank by scraping aptitude websites and generating randomized practice papers.

The project is designed to be easily extensible:

* Add new scrapers by implementing a common interface.
* Store questions in reusable JSON banks.
* Generate practice papers from one or multiple topics.
* Keep the system independent of any particular website.

---

## Project Architecture

```
practice_paper_generator/
│
├── data/
│   └── banks/
│       └── *.json              # Question banks stored by topic
│
├── generator/
│   ├── generate.py             # Practice paper generation logic (planned)
│   └── paper.py                # Paper model/utilities (planned)
│
├── scrapers/
│   ├── base.py                 # Abstract scraper interface
│   ├── indiabix.py             # IndiaBix scraper implementation
│   ├── examveda.py             # Future scraper
│   └── __init__.py
│
├── storage/
│   └── question_bank.py        # JSON database manager
│
├── scrape.py                   # Entry point for scraping
├── generate.py                 # Entry point for paper generation (planned)
├── requirements.txt
└── README.md
```

---

# Components

## Scrapers

Responsible for extracting questions from supported websites.

Every scraper inherits from `BaseScraper` and implements:

* `get_questions(url)`

Current implementation:

* IndiaBix

Planned:

* ExamVeda
* Additional aptitude websites

---

## Question Bank

`QuestionBank` manages local storage of questions.

Responsibilities:

* Save question banks
* Load existing banks
* Merge new questions
* Remove duplicates
* List available topics

Each topic is stored independently as:

```
data/banks/
    probability.json
    profit-loss.json
    time-distance.json
```

---

## Question Format

Each scraped question follows a common schema:

```json
{
  "question": "...",
  "options": [
    {
      "letter": "A",
      "text": "..."
    }
  ],
  "answer": "A",
  "source": "IndiaBix",
  "topic_url": "..."
}
```

Using a common schema allows multiple websites to feed the same question bank.

---

## Scraping Workflow

```
scrape.py
      │
      ▼
IndiaBixScraper
      │
      ▼
Extract Questions
      │
      ▼
QuestionBank.merge()
      │
      ▼
JSON Question Bank
```

---

## Planned Paper Generation Workflow

```
Question Banks
      │
      ▼
Question Selection
      │
      ▼
Difficulty Filtering
      │
      ▼
Randomization
      │
      ▼
Practice Paper
```

Future versions will support:

* Multiple topics
* Difficulty balancing
* Randomized ordering
* Answer key generation
* Printable papers
* Custom paper templates

---

# Current Status

Implemented:

* Modular scraper architecture
* IndiaBix scraper
* JSON-based question storage
* Duplicate detection during merge
* Topic-wise question banks

Planned:

* Additional scrapers
* Practice paper generator
* Difficulty classification
* CLI interface
* PDF export
* Configuration system

---

# Installation

```bash
git clone <repository-url>

cd practice_paper_generator

python -m venv .venv

source .venv/bin/activate
# Windows:
# .venv\Scripts\activate

pip install -r requirements.txt
```

---

# Usage

Scrape questions:

```bash
python scrape.py
```

Future:

```bash
python generate.py
```

---

# Design Goals

* Modular architecture
* Easy scraper extension
* Reusable question banks
* Offline-first workflow
* Deterministic JSON storage
* Simple to maintain and extend
