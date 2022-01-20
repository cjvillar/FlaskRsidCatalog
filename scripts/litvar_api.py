import json
import requests
import argparse
import sqlite3

def check_list(rs):
    rs_ids = []
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    for row in cur.execute('SELECT rs_id from variant'):
        rs_ids.append(row[0]) 
    if rs not in rs_ids:  
        rs_ids.append(rs)
        return rs_ids
    else: 
        return "Already in list"

def litvar_url(rs):
    rs_ids = []
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    for row in cur.execute('SELECT rs_id from variant'):
        clean_id = row[0].strip('##')
        rs_ids.append(clean_id)    
    if rs not in rs_ids:
        try:
            url=("https://www.ncbi.nlm.nih.gov/research/bionlp/litvar/api/v1/entity/litvar/{}%23%23".format(rs))
            response = requests.get(url)
            data = response.json() 
            rs_id = data["id"]
            gene = data["gene"]
            diseases = data["diseases"]
            return rs_id,diseases, response,gene, data.keys()
        except:
            None
    else:
        return None

        
    

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('rs')
    arguments = parser.parse_args()
    rs = arguments.rs
    print(litvar_url(rs))
    
    
