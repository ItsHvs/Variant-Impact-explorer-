from modules.input_parser import load_variants

variants = load_variants("data/sample_variants.csv")

for variant in variants:
    print(variant)