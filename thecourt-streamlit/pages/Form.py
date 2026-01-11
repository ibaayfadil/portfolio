# import streamlit as st  # pip install streamlit

# st.header(":soccer: Register your team here!")


# contact_form = """
# <form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
#      <input type="hidden" name="_captcha" value="false">
#      <input type="text" name="name" placeholder="Your Team Name" required>
#      <input type="email" name="email" placeholder="Your email" required>
#      <textarea name="message" placeholder="Your Player"></textarea>
#      <button type="submit">Send</button>
# </form>
# """

# st.markdown(contact_form, unsafe_allow_html=True)

# # Use Local CSS File
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# local_css("pages/static/style.css")

import streamlit as st

st.header(":soccer: Register your team here!")

# Buat daftar nama tim yang dapat dipilih
team_names = ["Pendekar United", "Bintang Timur Surabaya", "Black Steel FC", "Cosmo JNE FC"
              , "IPC Pelindo", "Unggul FC", "Kancil WHW", "Giga FC"]

# Tampilkan selectbox untuk memilih nama tim
selected_team = st.selectbox("Select Your Team", team_names)

contact_form = f"""
<form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" value="{selected_team}" readonly>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your Player"></textarea>
     <textarea name="message" placeholder="Number Your Player"></textarea>
     <textarea name="message" placeholder="Position Your Player"></textarea>
     <div style="display: flex; flex-direction: column;">
         <div>
             <label for="player_number_1">Player 1 :</label>
             <br>
             <input type="number" name="player_number_1" id="player_number_1" placeholder="Number" required>
             <input type="text" name="player_name_1" placeholder="Name" required>
             <input type="text" name="player_position_1" id="player_position_1" placeholder="Position" required>  
         </div>
         <div>
             <label for="player_number_2">Player 2 :</label>
             <br>
             <input type="number" name="player_number_2" id="player_number_2" placeholder="Number" required>
             <input type="text" name="player_name_2" placeholder="Name" required>
             <select name="player_position_2" id="player_position_2" required>
             <option value="Plank">Forward</option>
             <option value="Anchor">Midfielder</option>
             <option value="Pivot">Defender</option>
             <option value="Goalkeeper">Goalkeeper</option>
             </select>  
         </div>
     </div>
     <br>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("pages/static/style.css")

import streamlit as st
import pandas as pd

file = st.file_uploader("Upload a file", type="csv")

if st.button('Get data'):
    df = pd.read_csv(file)
    # This display will go away with the user's next action.
    st.write(df)

if st.button('Save'):
    # This will always error.
    df.to_csv('data.csv')