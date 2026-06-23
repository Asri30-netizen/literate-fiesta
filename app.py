import streamlit as st
import os

st.set_page_config(page_title="Srivastava Studios Lobby", page_icon="🎮")

# --- Title Header ---
st.title("🎮 Untitled Bounce Game")
st.subheader("Presented by Srivastava Studios")

# --- Interactive Sidebar Info ---
st.sidebar.header("Game Navigation")
page = st.sidebar.radio("Go to:", ["Home & Downloads", "How To Play", "Update Log", "Credits"])

if page == "Home & Downloads":
    st.write("Welcome to the **Untitled Bounce Game** home page!")
    st.info("Because this game uses Pygame and Tkinter desktop windows, you must download and run the game folder locally on your computer.")
    
    zip_path = "Untitled_Bounce_Game.zip"
    
    if os.path.exists(zip_path):
        with open(zip_path, "rb") as file:
            st.download_button(
                label="📥 Download Game Installer (Windows)",
                data=file,
                file_name="Untitled_Bounce_Game.zip",
                mime="application/zip"
            )
    else:
        st.warning("Game file zip bundle not uploaded yet. Upload your zip file to GitHub to activate this download button.")

elif page == "How To Play":
    st.header("🕹️ How to Play")
    st.markdown("""
    - Use **Up/Down Arrow keys** or **W/S** to control your slider paddle.
    - Bounce the ball back into play to increase your score survival rating.
    - **Do not** let the bouncing entity bypass your boundary line!
    - *Warning:* Glitched Hoverball features unpredictable physics routines!
    """)

elif page == "Update Log":
    st.header("📜 System Log Updates")
    st.write("**Update 1.1.1** (May 30th): Single Player Creation")
    st.write("**Update 1.1.2** (June 2nd): Game Menu Creation")
    st.write("**Update 1.2.0** (June 2nd): Hoverball Added")

elif page == "Credits":
    st.header("👥 Production Credits")
    st.write("- **Lead Developer:** Aarush Srivastava")
    st.write("- **Studio Environment:** Srivastava Studios")
    st.caption("Special thanks to Jason R. Briggs for design patterns.")
