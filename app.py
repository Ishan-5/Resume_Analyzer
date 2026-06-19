import streamlit as st

from utils.pdf_parser import extract_resume_text
from utils.embeddings import get_embedding
from utils.scorer import calculate_match_score
from utils.skill_extractor import extract_skills
from utils.prompts import career_analysis_prompt
from utils.llm import ask_llm

st.set_page_config(
    page_title="AI Career Copilot",
    layout="wide"
)

st.title("AI Career Copilot")

resume_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze Resume"):

    if resume_file and job_description:

        with st.spinner("Analyzing..."):

            # Resume Text
            resume_text = extract_resume_text(
                resume_file
            )

            # Embeddings
            resume_embedding = get_embedding(
                resume_text
            )

            jd_embedding = get_embedding(
                job_description
            )

            # Similarity
            score = calculate_match_score(
                resume_embedding,
                jd_embedding
            )

            # Skills
            resume_skills = extract_skills(
                resume_text
            )

            jd_skills = extract_skills(
                job_description
            )

            missing_skills = list(
                set(jd_skills)
                -
                set(resume_skills)
            )

            # LLM Prompt
            prompt = career_analysis_prompt(
                resume_text,
                job_description,
                missing_skills
            )

            report = ask_llm(
                prompt
            )

            st.metric(
                "ATS Match Score",
                f"{score}%"
            )

            st.subheader(
                "Resume Skills"
            )

            st.write(
                resume_skills
            )

            st.subheader(
                "Missing Skills"
            )

            st.write(
                missing_skills
            )

            st.subheader(
                "AI Career Report"
            )

            st.markdown(
                report
            )

    else:

        st.warning(
            "Please upload resume and job description"
        )