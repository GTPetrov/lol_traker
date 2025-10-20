from flask import Flask, render_template, request
from riot_api.variables import get_player_data , server_data, get_rank



app = Flask(__name__)


@app.route("/", methods=["GET","POST"])

def main():
    puuid = None
    error = None
    game_tag = None
    game_name = None
    server=None
    rank=None

    if request.method == "POST":
        player_name = request.form.get("player_name")
        player_tag = request.form.get("player_tag")
        region = request.form.get("region")

        data = get_player_data(player_name, player_tag, region)

        if data:
            puuid = data.get("puuid")
            game_name = data.get("gameName")
            game_tag = data.get("tagLine")
            #getting region data
            server_data1 = server_data(puuid, region)
            server = server_data1.get("region")

            #getting rank data
            rank_data = get_rank(puuid, region)
            rank = rank_data.get("tier")
           

        else:
            error = "Couldnt get player data"


    return render_template("index01.html", puuid=puuid, error=error, game_name=game_name, game_tag=game_tag, server=server, rank=rank)



if __name__ == "__main__":
    app.run(debug=True)