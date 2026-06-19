import pandas as pd

skills = pd.read_csv(
    "data/skills.csv",
    header=None
)[0].tolist()

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in skills:

        if skill.lower() in text:

            found.append(skill)

    return list(set(found))

def get_missing_skills(
    resume_skills,
    jd_skills
):

    return list(
        set(jd_skills)
        -
        set(resume_skills)
    )