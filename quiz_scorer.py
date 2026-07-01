from quiz_data import QUIZ_QUESTIONS

_Q_MAP = QUIZ_QUESTIONS


def enrich_and_score(raw_answers: list[dict]) -> dict:

    print(f"\n[DEBUG 1] RAW ANSWERS RECEIVED: {raw_answers}")
    print(f"[DEBUG 2] _Q_MAP KEYS: {list(_Q_MAP.keys())[:5]}") 

    enriched     = []
    cat_totals   = {"programming": 0, "maths": 0, "analysis": 0, "communication": 0}
    cat_counts   = {"programming": 0, "maths": 0, "analysis": 0, "communication": 0}

    domain_scores = {}
    domain_counts = {}

    for ans in raw_answers:
        q_idx  = ans.get("question_id") 
        o_idx  = ans.get("option_index")
        q_def  = _Q_MAP.get(q_idx)

        print(f"[DEBUG 3] Checking Answer -> q_idx: {q_idx}, o_idx: {o_idx}, Found q_def: {q_def is not None}")

        if q_def is None or o_idx is None:
            continue

        options = q_def["options"]
        if not (0 <= o_idx < len(options)):
            continue

        opt    = options[o_idx]
        score  = opt["score"]
        domain = opt["domain"]
        cat    = q_def["category"]

        enriched.append({
            "q_index":      q_idx,
            "option_index": o_idx,
            "score":        score,
            "category":     cat,
            "domain":       domain,
        })

        if cat in cat_totals:
            cat_totals[cat] += score
            cat_counts[cat] += 1

        if domain != "general":
            domain_scores[domain] = domain_scores.get(domain, 0) + score
            domain_counts[domain] = domain_counts.get(domain, 0) + 1

    normalized_domains = {}

    for d in domain_scores:
        avg_score = domain_scores[d] / domain_counts[d]
        normalized_domains[d] = round(avg_score, 2)

    print("\n===== DOMAIN DEBUG =====")
    print("RAW DOMAIN SCORES:", domain_scores)
    print("NORMALIZED DOMAIN SCORES:", normalized_domains)

    if normalized_domains:      
        dominant_domain = max(normalized_domains, key=normalized_domains.get)
    else:
        dominant_domain = "backend"

    print("SELECTED DOMAIN (soft):", dominant_domain)
    print("========================\n")
    
    # this converts category totals to a 0-100 scale based on how many questions were answered in that category
    def to_100(cat):
        count = cat_counts[cat]
        if count == 0:
            return 50
        return round((cat_totals[cat] / (count * 10)) * 100, 1)

    prog_score = to_100("programming")
    math_score = to_100("maths")
    anal_score = to_100("analysis")
    comm_score = to_100("communication")

    problem_solving = round((prog_score + math_score + anal_score) / 3, 1)
    creativity = round((anal_score + comm_score) / 2, 1)
    leadership = round((comm_score * 0.7 + anal_score * 0.3), 1)

    print("\n===== FINAL SCORES =====")
    print("Programming:", prog_score)
    print("Math:", math_score)
    print("Analytics:", anal_score)
    print("Communication:", comm_score)
    print("Problem Solving:", problem_solving)
    print("Creativity:", creativity)
    print("Leadership:", leadership)
    print("========================\n")

    return {
        "enriched_answers": enriched,
        "prog_score": prog_score,
        "math_score": math_score,
        "anal_score": anal_score,
        "comm_score": comm_score,
        "problem_solving": problem_solving,
        "creativity": creativity,
        "leadership": leadership,
        "domain": dominant_domain,
    }