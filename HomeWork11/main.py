from flask import Flask, render_template
from utils import *
app = Flask(__name__)

@app.route('/')
def main_page():
    candidates = load_candidates_from_json('candidates.json')
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<x>')
def candidate_page(x):
    candidate_data  = get_candidate(int(x))
    return render_template('single.html', candidate_data=candidate_data)

@app.route('/search/<name>')
def search_candidates(name):
    length = len(get_candidates_by_name(name))
    return render_template('candidate_name.html', candidates_data=get_candidates_by_name(name), length=length)

@app.route('/skills/<skill>')
def skills_data(skill):
    len_ = len(get_candidates_by_skill(skill))
    return render_template('search.html', candidate_skills=get_candidates_by_skill(skill), len_=len_, skill=skill)


app.run()