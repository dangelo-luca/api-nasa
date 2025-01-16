from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)
NASA_API_KEY = 'UtqRbePvYtWXvJaBwl4U3gyHb5dOj76fajQT4Kkn' #api kei della nasa

@app.route('/nasa')
def nasa():
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}')
    data = response.json() #converte da json a dict python
    return render_template('nasa.html', title=data.get("title"),description=data.get("explanation"), image_url=data.get("url"))

@app.route('/cat')
def cat():
    response = requests.get('https://catfact.ninja/fact') #richiedo i dati
    data = response.json() #converte da json a dict python
    return render_template('cat_fact.html', fact=data.get("fact"))

@app.route('/home')
def home():
    
    return render_template('home.html') 

if __name__ == '__main__':
    app.run(debug=True)