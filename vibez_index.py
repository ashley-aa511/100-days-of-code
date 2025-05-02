import streamlit as st
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

# Sample Gen Z posts
posts = [
    "I’m so broke I just argued with an M-Pesa agent over 5 bob 💀",
    "Soft life is expensive, but so am I 😌",
    "Capitalism is draining me slowly 🥲",
    "Woke up and chose delulu over reality again 💅",
    "Payday and rent are 3 days apart. Make it make sense 😩",
    "I’m manifesting money and it better listen this time 💸"
]

# Analyze sentiment
def get_sentiment(text):
    score = TextBlob(text).sentiment.polarity
    return score

# Label the mood
def label_vibe(score):
    if score < -0.3:
        return "🥶 Crisiscore"
    elif -0.3 <= score < 0.1:
        return "😐 Meh Vibes"
    elif 0.1 <= score < 0.5:
        return "😊 Chill Zone"
    else:
        return "🤑 Soft Life Era"

# Score all posts
data = []
for post in posts:
    score = get_sentiment(post)
    label = label_vibe(score)
    data.append({"Post": post, "Score": round(score, 2), "Vibe": label})

df = pd.DataFrame(data)
average = df["Score"].mean()
overall_vibe = label_vibe(average)
vibe_counts = df["Vibe"].value_counts()

# Streamlit UI
st.set_page_config(page_title="Vibez Index", layout="wide")
st.title("🔥 The Vibez Index – Gen Z Mood Tracker")
st.markdown("Analyzing Gen Z internet posts to see how the vibes are vibing.")

st.metric(label="Weekly Vibez Score", value=f"{average:.2f}")
st.subheader(f"Current Mood: {overall_vibe}")

st.write("### 👀 Analyzed Posts")
st.dataframe(df)

st.line_chart(df["Score"])

# Display pie chart
st.write("### 💫 Mood Distribution")
fig, ax = plt.subplots()
ax.pie(vibe_counts, labels=vibe_counts.index, autopct='%1.1f%%', startangle=90)
st.pyplot(fig)
