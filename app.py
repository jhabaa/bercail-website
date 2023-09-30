from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/review')
def review():
    return render_template('reviews.html')

@app.route('/traitement', methods=['POST'])
def traitement():
    note = request.form['note']
    avis = request.form['avis']

    # Créez une nouvelle ligne CSV avec les données
    nouvelle_ligne = f'{note},{avis}\n'

    # Ouvrir le fichier CSV en écriture (créer s'il n'existe pas)
    with open(os.path.join(app._static_folder, 'avis.csv'), 'a') as fichier_csv:
        fichier_csv.write(nouvelle_ligne)

    # Rediriger vers la page d'accueil
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host="0.0.0.0")