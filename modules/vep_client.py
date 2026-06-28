import requests 

def annotate_variant(chrom, pos, ref, alt):

    region = f"{chrom}:{pos}-{pos}"
    allele = f"{ref}/{alt}"

    url = (
            f"https://rest.ensembl.org/vep/human/region/{region}"
                f"/{allele}"
                )
    
    headers = {
        "Accept": "application/json"
    }

    print("URL:")
    print(url)
    
    response = requests.get(url, headers=headers)

    print("STATUS:", response.status_code)
    print("TEXT:")
    print(response.text)

    return response.json()

