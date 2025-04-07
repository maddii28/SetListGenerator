from flask import Blueprint, request, jsonify, g
from .recommender import update_preferences

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