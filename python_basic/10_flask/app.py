from flask import Flask,request,redirect,render_template
import sqlite3
import os, pickle
from PIL import Image
import numpy as np

app = Flask(__name__)
path = os.path.dirname(__file__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inputform', methods=['GET','POST'])
def inputform():
    if request.method == 'GET':
        return render_template('inputform.html')
    else:
        #db에 데이터 입력
        conn = sqlite3.connect(path + '/customer.db')
        cur = conn.cursor()
        cur.execute('''create table if not exists customer
                        (name text,
                        email text,
                        tel text,
                        address text,
                        gender text)''')
        conn.commit()
        data=[request.form['name'],request.form['email'],request.form['tel'],request.form['address'],request.form['gender']]
        cur.execute('insert into customer values(?,?,?,?,?)',data)
        conn.commit()
        conn.close()
        return redirect('/')

@app.route('/customerlist')
def customerlist():
    conn = sqlite3.connect(path + '/customer.db')
    cur = conn.cursor()
    cur.execute('select * from customer order by name')
    data = cur.fetchall()
    return render_template('customerlist.html',data=data)

@app.route('/mnist', methods=['GET','POST'])
def mnist():
    if request.method == 'GET':
        return render_template('mnist_form.html')
    else:
        f = request.files['file']
        mnistpath = path+'/static/upload/'+f.filename
        f.save(mnistpath)
        img = Image.open(mnistpath).convert('L')
        img = np.resize(img,(1,784))
        img = 255-img
        f1 = open(path+'/model','rb')
        model = pickle.load(f1)
        data = model.predict(img)
        print(data)
        return render_template('mnist_result.html',data = data[0],path=f.filename)


if __name__ == '__main__':
    app.run(debug=True,port=80)