from typing import List

def read_lines(file_path: str) -> list:
    questions = list()
    with open(file_path) as file:
        for line in file:
            questions.append(line.strip())
    return questions

def write_lines(file_path: str, lines: List[str]) -> bool:
    try:
        with open(file_path, "w+") as file:
            file.writelines(line + '\n' for line in lines)
            return True
    except:
        return False
