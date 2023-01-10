import json

def load_candidates_from_json(path):
    with open(path, 'r') as candidates:
     return json.load(candidates)


def get_candidate(candidate_id):
    return [i for i in load_candidates_from_json('candidates.json') if i['id'] == candidate_id][0]


def get_candidates_by_name(candidate_name):
    return [i for i in load_candidates_from_json('candidates.json') if candidate_name in i['name']]

def get_candidates_by_skill(skill_name):
    return [i for i in load_candidates_from_json('candidates.json') if skill_name.lower() in i['skills'].lower()]


print(get_candidates_by_skill("python"))