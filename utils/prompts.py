def career_analysis_prompt(
    resume,
    jd,
    missing_skills
):

    return f"""
You are an expert AI career coach.

Analyze this resume against
the job description.

Resume:
{resume}

Job Description:
{jd}

Missing Skills:
{missing_skills}

Provide:

1. Resume Summary

2. Strengths

3. Weaknesses

4. Improvement Suggestions

5. 30-Day Learning Roadmap

6. Interview Questions

7. Project Suggestions
"""