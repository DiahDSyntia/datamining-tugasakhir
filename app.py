from flask import Flask, render_template, request, redirect
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        with open('knn_pickle', 'rb') as r:
            model = pickle.load(r)

        usia = float(request.form['age'])
        jenis_kelamin = float(request.form['gender'])
        totalbillirubin = float(request.form['totalbillirubin'])
        directbillirubin = float(request.form['directbillirubin'])
        alkalinephosphotase = float(request.form['alkalinephosphotase'])
        alamineaminotransferase = float(request.form['alamineaminotransferase'])
        aspartateaminotransferase = float(request.form['aspartateaminotransferase'])
        totalproteins = float(request.form['totalproteins'])
        albumin = float(request.form['albumin'])
        albuminglobulinratio = float(request.form['albuminglobulinratio'])

        datas = np.array((usia, jenis_kelamin, totalbillirubin, directbillirubin, alkalinephosphotase, alamineaminotransferase, aspartateaminotransferase, totalproteins, albumin, albuminglobulinratio))
        datas = np.reshape(datas, (1, -1))

        return render_template('hasil.html',)

    else:
        return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)