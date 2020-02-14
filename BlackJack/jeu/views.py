from flask import Flask, render_template
from flask_mysqldb import MySQL
from . import models
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'damos02'
app.config['MYSQL_DB'] = 'blackjack'

mysql = MySQL(app)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']



@app.route('/', methods=['GET', 'POST'])

def index():
    
    joueur1 = Joueur()
    joueur1.setNom('Michel') 
        
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO joueur (nom) VALUES (%s)", (joueur1.getNom()))
    mysql.connection.commit()
    cur.close()

    return render_template('index.html')

if __name__ == "__main__":
    app.run()