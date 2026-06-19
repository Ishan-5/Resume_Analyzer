from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_score(
    resume_embedding,
    jd_embedding
):

    score = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )

    return round(
        float(score[0][0]) * 100,
        2
    )