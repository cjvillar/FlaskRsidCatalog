from flask import Flask, render_template, redirect, url_for, request, session
from requests.api import get
app = Flask(__name__)

from litvar_api import litvar_url

@app.route('/')
def home():
    return render_template('home_page.html')


@app.route('/rsID/', methods=['GET','POST'])
def rsID():
    if request.method == "POST":
        rsid = request.form['rs']
        get_id_response = litvar_url(rsid)
        return render_template('rsID.html',get_id_response = litvar_url(rsid))
    else:
        return render_template('rsID.html')
    
if __name__ == '__main__':
    app.run(debug=True)

