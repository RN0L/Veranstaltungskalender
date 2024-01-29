from flask import Flask, render_template
from flask_bootstrap import Bootstrap 

app = Flask(__name__) 

bootstrap = Bootstrap(app) 


app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'lux'

@app.route('/einkaufsliste')
def einkaufsliste():
    return render_template('index.html', einkaufsliste = Einkaufsliste)



if __name__ == '__main__':  

    app.run(debug=True)