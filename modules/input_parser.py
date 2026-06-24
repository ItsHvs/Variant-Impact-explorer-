import csv

def load_variants(filepath):
    variants = []

    with open(filepath, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            variants.append({
                "chrom": row["chrom"],
                "pos": int(row["pos"]),
                "ref": row["ref"],
                "alt": row["alt"]
            })
            return variants 


