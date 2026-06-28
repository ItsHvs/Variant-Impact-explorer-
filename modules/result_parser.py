def parse_result(result):
    if "error" in result:
        return {"error": result["error"]}

    transcript = result[0].get("transcript_consequences", [])
    impact_rank = {
            "HIGH": 4,
            "MODERATE": 3,
            "LOW": 2,
            "MODIFIER": 1
             }
    if not transcript:
        return {"error": "No transcript consequences found"}
    t = max(
        transcript,
        key=lambda x: impact_rank.get(x.get("impact", "MODIFIER"), 0)
        )
    ref_codon, alt_codon = t.get("codons", "N/A/N/A").split("/")
    ref_aa, alt_aa = t.get("amino_acids", "X/X").split("/")
    protein_change = t.get("hgvsp")

    if not protein_change:
        if "protein_start" in t:
            protein_change = (
            f"p.{ref_aa}{t['protein_start']}{alt_aa}"
        )
        else:
            protein_change = "N/A"

    coding_change = t.get("hgvsc")

    if not coding_change:
        if "cds_start" in t:
            coding_change = (
            f"c.{t['cds_start']}{ref_codon}>{alt_codon}"
        )
        else:
            coding_change = "N/A"

    print("Selected transcript:")
    print(t)

    print("Consequence terms =", t.get("consequence_terms"))

    return {
        "gene": t.get("gene_symbol", "N/A"),
        "transcript": t.get("transcript_id", "N/A"),
        "consequence": ", ".join(t.get("consequence_terms", [])),
        "impact": t.get("impact", "N/A"),

        "protein_change": protein_change,
        "coding_change": coding_change,

        "amino_acids": t.get("amino_acids", "N/A"),
        "codon": t.get("codons", "N/A"),

        "sift_prediction": t.get("sift_prediction", "N/A"),
        "sift_score": t.get("sift_score", "N/A"),

        "polyphen_prediction": t.get("polyphen_prediction", "N/A"),
        "polyphen_score": t.get("polyphen_score", "N/A"),

        "biotype": t.get("biotype", "N/A"),

                                                                
        "protein_position": t.get("protein_start", "N/A"),
        "cds_position": t.get("cds_start", "N/A")
     }
    