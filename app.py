from modules.input_parser import load_variants
from modules.vep_client import annotate_variant

variants = load_variants("data/sample_variants.csv")

for variant in variants:

    result = annotate_variant(
        variant["chrom"],
        variant["pos"],
        variant["ref"],
        variant["alt"]   
    )

    print(result)