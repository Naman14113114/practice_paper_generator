import json
from pathlib import Path


class QuestionBank:

    def __init__(self):
        self.data_dir = Path("data/banks")
        self.data_dir.mkdir(parents=True, exist_ok=True)

        print(f"[QuestionBank] Data directory: {self.data_dir.resolve()}")

    def save(self, topic, questions):

        file_path = self.data_dir / f"{topic}.json"

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(questions, f, indent=4, ensure_ascii=False)

        print(f"[QuestionBank] Saved {len(questions)} questions -> {file_path.name}")

    def load(self, topic):

        file_path = self.data_dir / f"{topic}.json"

        if not file_path.exists():
            print(f"[QuestionBank] No existing bank for '{topic}'.")
            return []

        with open(file_path, "r", encoding="utf-8") as f:
            questions = json.load(f)

        print(f"[QuestionBank] Loaded {len(questions)} questions from {file_path.name}")

        return questions

    def merge(self, topic, new_questions):

        existing_questions = self.load(topic)

        existing_texts = {
            q["question"] for q in existing_questions
        }

        added = 0

        for question in new_questions:

            if question["question"] not in existing_texts:
                existing_questions.append(question)
                existing_texts.add(question["question"])
                added += 1

        self.save(topic, existing_questions)

        print(f"[QuestionBank] Added {added} new question(s).")

    def exists(self, topic):

        file_path = self.data_dir / f"{topic}.json"

        return file_path.exists()

    def list_topics(self):

        topics = sorted(
            file.stem
            for file in self.data_dir.glob("*.json")
        )

        print(f"[QuestionBank] Available topics: {topics}")

        return topics