# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeMatch Recommender 1.0  

---

## 2. Intended Use  

This recommender is designed to suggest songs from a small dataset based on a user’s preferences for genre, mood, and musical features such as energy, valence, danceability, tempo, and acousticness.

It is intended for classroom exploration to demonstrate how recommendation systems work. It assumes that a user’s taste can be represented as a combination of categorical preferences (genre, mood) and numeric targets (energy, tempo, etc.), which is a simplification of real-world behavior.

This system should not be used for real-world recommendations, as it relies on a small dataset and simplified assumptions about user preferences.

---

## 3. How the Model Works  

The model assigns a score to each song based on how well it matches the user’s preferences.

It considers both categorical features (genre and mood) and numeric features (energy, valence, danceability, tempo, acousticness). Genre and mood give fixed points when they match the user’s preferences. Numeric features are scored based on how close the song’s values are to the user’s target values.

All these contributions are combined into a final score. Songs are then ranked from highest to lowest score, and the top results are returned as recommendations.

---

## 4. Data  

The model uses a small dataset of songs stored in a CSV file. The dataset includes features such as genre, mood, energy, tempo (BPM), valence, danceability, and acousticness.

The dataset includes a mix of genres like pop, lofi, rock, ambient, and jazz, and moods such as happy, chill, intense, and focused. 

Because the dataset is small and manually created, it does not fully represent the diversity of real-world music preferences and may reflect a limited range of styles and tastes.

---

## 5. Strengths  

The recommender performs well when there are strong matches between user preferences and song attributes.

- It correctly ranks songs that match both genre and mood at the top.
- Numeric features help capture the overall “vibe” of a song.
- It can still suggest reasonable alternatives when exact matches are not available.
- The scoring system is transparent, and explanations clearly show why songs were recommended.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

The model has several limitations:

- It relies on a small dataset, which limits diversity.
- It does not consider lyrics, user history, or cultural context.
- It may over-prioritize genre or mood depending on the weights used.
- It assumes all users can be represented with the same type of profile.
- It can produce cross-genre recommendations when numeric similarity outweighs categorical matches.

These limitations could lead to filter bubbles or less personalized recommendations in a real-world setting.

---

## 7. Evaluation  

No need for numeric metrics unless you created some.

I evaluated the recommender using three user profiles: High-Energy Pop, Chill Lofi, and Intense Rock.

For High-Energy Pop, Sunrise City ranked highest, which matched expectations because it aligned with both genre and mood and had similar numeric features.

For Chill Lofi, Library Rain and Midnight Coding ranked highest, reflecting the low-energy, high-acousticness profile.

For Intense Rock, Storm Runner ranked first, which made sense because it matched both genre and mood and had high energy and tempo.

I also tested changing the genre weight from 2.0 to 0.5. This caused more cross-genre recommendations to appear, showing that the system becomes more flexible but less aligned with strict genre preferences when weights are adjusted.

---

## 8. Future Work  

If I continued developing this recommender, I would:

- Add more songs to improve diversity
- Incorporate user listening history or feedback
- Improve explanation detail and clarity
- Introduce diversity constraints to avoid repetitive recommendations
- Explore machine learning approaches to learn feature weights automatically

---

## 9. Personal Reflection  

This project helped me understand how recommender systems translate user preferences into ranked results using relatively simple logic.

One interesting takeaway was how sensitive the system is to feature weights. Small changes in weights can significantly change the behavior of the recommendations, shifting from strict matching to more flexible, vibe-based suggestions.

It also showed me that even simple algorithms can feel effective, but they rely heavily on design decisions and assumptions about users. This made me think more critically about how real-world recommendation systems balance accuracy, variation, and fairness.

During this project, I also used AI tools like Copilot to help generate and refine parts of the implementation, such as loading data and structuring the scoring logic. While this sped up development, I needed to carefully review and adjust the generated code to ensure it matched my intended design and algorithm. This helped me understand that AI tools are useful for acceleration, but still require human oversight to ensure correctness and alignment with the problem.