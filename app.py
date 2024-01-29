from flask import Flask, render_template
from flask_bootstrap import Bootstrap 

app = Flask(__name__) 

bootstrap = Bootstrap(app) 

Einkaufsliste = [  

    {'name': 'Ochse', 'anzahl':'2'},

    {'name': 'Birne', 'anzahl':'2'},

    {'name': 'Banane', 'anzahl':'2'},

    {'name': 'Hackfleisch', 'anzahl':'2'},

    {'name': 'Kackfleisch', 'anzahl':'2'}
] 

app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'lux'

@app.route('/einkaufsliste')
def einkaufsliste():
    return render_template('index.html', einkaufsliste = Einkaufsliste)

@app.route('/laender')
def laender():
    return render_template('staftlandfluss.html', einkaufsliste = Einkaufsliste)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/v-bucks') 
def login(): 
    return render_template('login.html') 

if __name__ == '__main__':  

    app.run(debug=True)