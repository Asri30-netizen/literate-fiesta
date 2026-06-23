import os
import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Srivastava Studios Lobby", page_icon="🎮")

# --- Title Header ---
st.title("🎮 Untitled Bounce Game")
st.subheader("Presented by Srivastava Studios")
st.subheader("*This is an AI made page, the real game is made by me*")
st.write("Welcome to the **Untitled Bounce Game** home page!")

# --- Download Section ---
st.info(
    "Because this game uses Pygame and Tkinter desktop windows, you must download and run the game folder locally on your computer."
)

zip_path = "Untitled_Bounce_Game.zip"

if os.path.exists(zip_path):
    with open(zip_path, "rb") as file:
        st.download_button(
            label="📥 Download Game Installer (Windows)",
            data=file,
            file_name="Untitled_Bounce_Game.zip",
            mime="application/zip",
        )
else:
    st.warning(
        "Game file zip bundle not uploaded yet. Upload your zip file to GitHub to activate this download button."
    )
