from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def render_home():
    return render_template("homepage.html")


@app.route("/anime-detail/<id>")
@app.route("/anime/<id>")
def anime_detail_page():
    return


@app.route("/addanime")
def add_anime_page():
    return


@app.route("/browse")
def browse_page():
    return



if (__name__ == "__main__") :
    app.run