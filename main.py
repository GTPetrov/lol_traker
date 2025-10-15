from flask import Flask, render_template, request
from riot_api.variables import get_player_data



app = Flask(__name__)


@app.route("/", methods=["GET","POST"])

def main():
    puuid = None
    error = None
    if request.method == "POST":
        player_name = request.form.get("player_name")
        player_tag = request.form.get("player_tag")

        data=get_player_data(player_name,player_tag)

        if data:
            puuid = data.get("puuid")
        else:
            error = "Couldnt get player data"

    return render_template("index01.html", puuid=puuid, error=error)

if __name__ == "__main__":
    app.run(debug=True)