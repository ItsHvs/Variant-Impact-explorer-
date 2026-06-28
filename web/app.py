import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request
from modules.input_parser import load_variants
from modules.vep_client import annotate_variant
from modules.result_parser import parse_result
import json

print("Starting Flask app...")

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    uploaded_file = request.files["csv_file"]

    filepath = "sample_variants.csv"

    uploaded_file.save(filepath)

    variants = load_variants(filepath)

    results = []

    for variant in variants:

        result = annotate_variant(
            variant["chrom"],
            variant["pos"],
            variant["ref"],
            variant["alt"]
        )

        parsed = parse_result(result)

        print("PARSED RESULT:")
        print(parsed)

        results.append(parsed)

    return render_template(
         "result.html",
          results=results
    )
    
    print("__name__ =", __name__)

if __name__ == "__main__":
    print("Launching Flask...")
    app.run(host="0.0.0.0", port=5000, debug=True)