from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("NoNinjas.html")

@app.route("/ninja")
def fourNinjas():
    pictureToDisplay = "/static/tmnt.jpg"
    turtleName="All Turtles"
    return render_template("oneNinja.html", pic=pictureToDisplay, name=turtleName)

@app.route("/ninja/<color>")
def ninjaPicker(color):
    print color
    pictureToDisplay = "/static/notapril.jpg"
    turtleName = "Not April"
    # If user visits /ninja/blue, it should only display the Ninja Turtle Leonardo.
    if (color.lower() == 'blue'):
        pictureToDisplay = "/static/leonardo.jpg"
        turtleName = "Leonardo"
    # /ninja/orange - Ninja Turtle Michelangelo.
    if (color.lower() == 'orange'):
        pictureToDisplay = "/static/michelangelo.jpg"
        turtleName = "Michelangelo"
    # /ninja/red - Ninja Turtle Raphael
    if (color.lower() == 'red'):
        pictureToDisplay = "/static/raphael.jpg"
        turtleName = "Raphael"
    # /ninja/purple - Ninja Turtle Donatello
    if (color.lower() == 'purple'):
        pictureToDisplay = "/static/donatello.jpg"
        turtleName = "Donatello"
    # If a user tries to hack into your web app by specifying a color or string
    # combination other than the colors (Blue, Orange, Red, and Purple),
    # example: /ninja/black or /ninja/123, then display the image notapril.jpg
    return render_template("oneNinja.html", pictureToDisplay=pictureToDisplay, turtleName=turtleName)

app.run(debug=True)
