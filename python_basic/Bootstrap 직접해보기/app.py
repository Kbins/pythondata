import sqlite3
from flask import Flask,request, render_template, redirect
import os

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
        #db 입력
        conn = sqlite3.connect(path+'/signup.db')
        cur = conn.cursor()
        cur.execute('''create table if not exists signup(
                        num integer,
                        name text,
                        email text,
                        tel text,
                        address text,
                        brith text,
                        gender text
                    )''')
        conn.commit()
        data=[request.form['num'],request.form['name'],request.form['email'],request.form['tel'],request.form['address'],request.form['birth'],request.form['gender']]
        cur.execute('insert into signup values (?,?,?,?,?,?,?)',data)
        conn.commit()
        conn.close()
        return redirect('/')

@app.route('/signuplist')
def signuplist():
        conn = sqlite3.connect(path+'/signup.db')
        cur = conn.cursor()
        cur.execute('select * from signup order by name')
        data = cur.fetchall()
        return render_template('signuplist.html', data=data)

@app.route('/delsignuplist', methods=['GET','POST'])
def delsignuplist(num):
        conn = sqlite3.connect(path+'/signup.db')
        cur = conn.cursor()

        for i in data:
            if i ==num :
                cur.execute('delete from signup where name = ?',(num,))
                data = cur.fetchall()
            else:
                pass

        conn.commit()
        conn.close()

        return render_template('signuplist.html', data=data)



if __name__ =='__main__':
    app.run(debug=True, port=80)