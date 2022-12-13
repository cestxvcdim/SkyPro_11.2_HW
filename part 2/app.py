from utils import *
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main_page():
    info: list[dict[str, int | str]] = load_candidates_from_json()
    return render_template('list.html', info=info)


@app.route('/candidate/<int:x>')
def search_by_candidate_id(x):
    info: dict[str, int | str] | str = candidate(x)
    if type(info) == str:
        return f'<h1>{info}</h1>'
    return render_template('card.html', info=info)


@app.route('/search/<candidate_name>')
def search_by_candidate_name(candidate_name: str):
    info: list[dict[str, int | str]] | str = get_candidates_by_name(candidate_name)
    if type(info) == str:
        return f'<h1>{info}</h1>'
    return render_template('search_names.html', info=info)


@app.route('/skill/<skill_name>')
def search_by_candidates_skill(skill_name: str):
    info: list[dict[str, int | str]] | str = get_candidates_by_skill(skill_name)
    skill: str = skill_name
    if type(info) == str:
        return f'<h1>{info}</h1>'
    return render_template('search_skills.html', info=info, skill=skill)


app.run()
