from modules.input_parser import load_variants
from modules.result_parser import parse_result
from modules.vep_client import annotate_variant

csv_path = input("Enter CSV file path: ")
variants = load_variants(csv_path)

for variant in variants:

    result = annotate_variant(
        variant["chrom"],
        variant["pos"],
        variant["ref"],
        variant["alt"]   
    )

    parsed = parse_result(result)

    for key, value in parsed.items():
        print(f"{key}: {value}")