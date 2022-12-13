import json


def load_candidates_from_json() -> list[dict[str, int | str]]:
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def candidate(candidate_id: int) -> dict[str, int | str] | str:
    candidates: list[dict[str, int | str]] = load_candidates_from_json()
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate
    return 'Wrong id'


def get_candidates_by_name(candidate_name: str) -> list[dict[str, int | str]] | str:
    candidates: list[dict[str, int | str]] = load_candidates_from_json()
    result: list = []
    for candidate in candidates:
        names: list[str] = candidate['name'].split()
        for item in names:
            if item in candidate_name.title():
                result.append(candidate)
    if len(result) == 0:
        return 'Wrong name'
    return result


def get_candidates_by_skill(skill_name: str) -> list[dict[str, int | str]] | str:
    candidates: list[dict[str, int | str]] = load_candidates_from_json()
    result: list = []
    for candidate in candidates:
        skills: str = candidate['skills']
        skills: list[str] = skills.lower().split(', ')
        if skill_name.lower() in skills:
            result.append(candidate)
    if len(result) == 0:
        return 'Not found'
    return result
