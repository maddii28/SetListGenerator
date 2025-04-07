#contains recommendation logic

def update_preferences(user_id, song_id, liked):
    print(f"User {user_id} {'liked' if liked else 'disliked'} song {song_id}")