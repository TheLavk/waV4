from flask import Flask, render_template
from random import choice

app = Flask(__name__)
#v produkci smazat!
app.debug = True


@app.route("/")
def vyber():

    return render_template ("vyber.html")

@app.route('/kamen')
def kamen():
    hrac = "Kámen"
    pocitac = choice(["Kámen", "Nůžky", "Papír"])
    if pocitac == "Kámen":
        skore = "REMÍZA"
    if pocitac == "Nůžky":
        skore = "VÝHRA"
    if pocitac == "Papír":
        skore = "PROHRA"
    return render_template ("hra.html", pocitac=pocitac, hrac=hrac, skore=skore)

@app.route('/nuzky')
def nuzky():
    hrac = "Nůžky"
    pocitac = choice(["Kámen", "Nůžky", "Papír"])
    if pocitac == "Kámen":
        skore = "PROHRA"
    if pocitac == "Nůžky":
        skore = "REMÍZA"
    if pocitac == "Papír":
        skore = "VÝHRA"
    return render_template ("hra.html", pocitac=pocitac, hrac=hrac, skore=skore)

@app.route('/papir')
def papir():
    hrac = "Papír"
    pocitac = choice(["Kámen", "Nůžky", "Papír"])
    if pocitac == "Kámen":
        skore = "VÝHRA"
    if pocitac == "Nůžky":
        skore = "PROHRA"
    if pocitac == "Papír":
        skore = "REMÍZA"
    return render_template ("hra.html", pocitac=pocitac, hrac=hrac, skore=skore)



if __name__ == '__main__':
    app.run()
