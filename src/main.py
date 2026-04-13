"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8,
            "valence": 0.9,
            "danceability": 0.7,
            "tempo_bpm": 120,
            "acousticness": 0.3,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35,
            "valence": 0.6,
            "danceability": 0.5,
            "tempo_bpm": 80,
            "acousticness": 0.8,
        },
        "Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9,
            "valence": 0.5,
            "danceability": 0.6,
            "tempo_bpm": 145,
            "acousticness": 0.2,
        },
    }

    for profile_name, user_prefs in profiles.items():
        print(f"\n=== {profile_name} ===\n")

        recommendations = recommend_songs(user_prefs, songs, k=5)

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()