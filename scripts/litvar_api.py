import json
import requests
import argparse

def litvar_url(rs):
    url=("https://www.ncbi.nlm.nih.gov/research/bionlp/litvar/api/v1/entity/litvar/{}%23%23".format(rs))
    response = requests.get(url)
    data = response.json()
    json_keys = data.keys()
    rs_id = data["id"]
    gene = data["gene"]
    diseases = data["diseases"]
    
    return rs_id,diseases, response,gene, data.keys()


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('rs')
    arguments = parser.parse_args()
    rs = arguments.rs
    print(litvar_url(rs))