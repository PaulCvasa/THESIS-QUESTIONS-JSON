import json
from random import shuffle


class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    END = "\033[0m"


class Test:

    letter_to_index = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4
    }

    def __init__(self, file_path):
        self.file_path = file_path
        self.questions = self._load_questions()

    def _load_questions(self) -> dict:
        with open(self.file_path) as f:
            f_str = f.read()
        return json.loads(f_str)


def main():
    ti = Test('ads.json')
    keys = list(ti.questions.keys())
    shuffle(keys)
    for key in keys:
        print(key)
        answer_keys = list(ti.questions[key].keys())
        shuffle(answer_keys)
        for (answer_key, letter) in zip(answer_keys, ti.letter_to_index.keys()):
            print(f"    {letter}.{answer_key}")
        input_values = input("Answers: ")

        total_wrong_answers = 0
        for val in input_values:
            idx = ti.letter_to_index[val]
            if not ti.questions[key][answer_keys[idx]]:
                print(f"{Colors.RED}Wrong answer: {answer_keys[idx]}{Colors.END}")
                total_wrong_answers += 1

        if total_wrong_answers == 0:
            print(f"{Colors.GREEN}Correct!{Colors.END}")
        else:
            print("Correct answers: ", end=' ')
            for answer_key in answer_keys:
                if ti.questions[key][answer_key]:
                    print(answer_key, end='; ')
        print(" ")
        print(" ")
        print(" ")


if __name__ == '__main__':
    main()
