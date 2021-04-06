import requests
import pandas as pd
import json
from pandas.io.json import json_normalize
from flask import Flask, request, render_template, session, redirect
app = Flask(__name__)
@app.route("/")
def test():
    global result
    dataget = requests.get('https://reqres.in/api/products')
    s = dataget.json()
    data=list(s.items())[4][1]
    result = pd.json_normalize(data)
    return render_template('product.html', column_names=result.columns.values, row_data=list(result.values.tolist()), zip=zip)   
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
