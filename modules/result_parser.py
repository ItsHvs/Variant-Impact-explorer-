def parse_result(result):
    if "error" in result:
        return {"error": result["error"]}

    transcript = result[0].get("transcript_consequences", [])

    if not transcript:
        return {"error": "No transcript consequences found"}
    
    t = transcript [0]

    return {
    "gene": t.get("gene_symbol", "N/A"),
    "transcript": t.get("transcript_id", "N/A"),
    "consequense": ", ".join(t.get(" consequence_terms", [])),
    "impact": t.get("impact", "N/A"),
    "protein_change": t.get("hgvsp", "N/A"),
    "coding_change": t.get("hgvsc", "N/A"),
    "amino_acids": t.get("amino_acids", "N/A"),
    "codon": t.get("codons", "N/A")
    
    }