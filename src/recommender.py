import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        scored: List[Tuple[Song, float]] = []

        for song in self.songs:
            score = 0.0

            if song.genre == user.favorite_genre:
                score += 2.0

            if song.mood == user.favorite_mood:
                score += 1.5

            energy_score = 1 - abs(song.energy - user.target_energy)
            score += 1.5 * energy_score

            if user.likes_acoustic:
                acoustic_score = song.acousticness
            else:
                acoustic_score = 1 - song.acousticness
            score += 0.75 * acoustic_score

            scored.append((song, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return [song for song, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons: List[str] = []

        if song.genre == user.favorite_genre:
            reasons.append("genre matches your preference")

        if song.mood == user.favorite_mood:
            reasons.append("mood matches your preference")

        if abs(song.energy - user.target_energy) <= 0.2:
            reasons.append("energy is close to your target")

        if user.likes_acoustic and song.acousticness >= 0.6:
            reasons.append("it has an acoustic feel you may like")
        elif not user.likes_acoustic and song.acousticness <= 0.4:
            reasons.append("it is less acoustic, which matches your preference")

        if not reasons:
            reasons.append("it is one of the closest overall matches in the catalog")

        return ", ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    ## TODO: Implement CSV loading logic
    songs: List[Dict] = []

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    # TODO: Implement scoring logic using your Algorithm Recipe from Phase 2.
    # Expected return format: (score, reasons)
    score = 0.0
    reasons: List[str] = []

    if song["genre"] == user_prefs.get("genre"):
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs.get("mood"):
        score += 1.5
        reasons.append("mood match (+1.5)")

    energy_score = 1 - abs(song["energy"] - user_prefs.get("energy", song["energy"]))
    energy_points = 1.5 * energy_score
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    valence_score = 1 - abs(song["valence"] - user_prefs.get("valence", song["valence"]))
    valence_points = 1.0 * valence_score
    score += valence_points
    reasons.append(f"valence similarity (+{valence_points:.2f})")

    dance_score = 1 - abs(song["danceability"] - user_prefs.get("danceability", song["danceability"]))
    dance_points = 1.0 * dance_score
    score += dance_points
    reasons.append(f"danceability similarity (+{dance_points:.2f})")

    acoustic_score = 1 - abs(song["acousticness"] - user_prefs.get("acousticness", song["acousticness"]))
    acoustic_points = 0.75 * acoustic_score
    score += acoustic_points
    reasons.append(f"acousticness similarity (+{acoustic_points:.2f})")

    tempo_gap = abs(song["tempo_bpm"] - user_prefs.get("tempo_bpm", song["tempo_bpm"]))
    tempo_score = 1 - min(tempo_gap / 100, 1)
    tempo_points = 0.75 * tempo_score
    score += tempo_points
    reasons.append(f"tempo similarity (+{tempo_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    scored_songs: List[Tuple[Dict, float, str]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda x: x[1], reverse=True)
    return scored_songs[:k]

