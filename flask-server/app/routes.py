from flask import Blueprint, request, jsonify, g
from .recommender import update_preferences, recommend_songs

main = Blueprint('main', __name__)

@main.route("/swipe", methods=["POST"])
def swipe():
    data = request.json # get the data sent in the request body as json
    user_id = data.get("user_id")
    song_id = data.get("song_id")
    liked = data.get("liked")

    if liked:
        #save the song to the user's favorites
        g.cursor.execute("INSERT INTO saved_songs (user_id, song_id) VALUES (%s, %s)", (user_id, song_id))

    update_preferences(user_id, song_id, liked) # tell the model about the preference
    g.db.commit() # save changes

    return jsonify({"message": "Swipe recorded"}), 200

@main.route("/get_users_faves", methods=["GET"])
def get_users_faves():
    user_id = request.args.get("user_id") # take the userid from the query string

    g.cursor.execute("SELECT songs.* FROM saved_songs JOIN songs ON saved_songs.song_id = songs.id WHERE saved_songs.user_id = %s", (user_id, ))
    rows = g.cursor.fetchall() # fetch all of the mtching songs

    songs = []
    for row in rows:
        song = {
            "id": row[0],
            "title": row[1],
            "artist": row[2]
        }
        songs.append(song)

    return jsonify({"user_id": user_id, "saved_songs": songs}), 200

@main.route("/get_song", methods=["GET"])
def get_song():
    user_id = request.args.get("user_id")

    recommendation = recommend_songs() # TO DO: add arguments

    return recommendation