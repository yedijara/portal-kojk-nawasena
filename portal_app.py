
import streamlit as st
import os
import base64

st.set_page_config(layout="wide")

# Background image encoded
def get_base64_bg(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_base64 = get_base64_bg("images/bg-ai.png")

# CSS: vivid animated gradient overlay
st.markdown(f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bg_base64}");
        background-size: cover;
        background-position: center top;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .gradient-overlay {{
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        z-index: 0;
        background: linear-gradient(135deg,
            rgba(255, 0, 255, 0.25),
            rgba(0, 255, 255, 0.25),
            rgba(0, 0, 255, 0.25));
        background-size: 300% 300%;
        animation: gradientShift 18s ease infinite;
        pointer-events: none;
        filter: blur(10px);
    }}
    @keyframes gradientShift {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    .main, .block-container {{
        position: relative;
        z-index: 1;
    }}
    .glass-card {{
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(0,0,0,0.3);
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
        z-index: 1;
    }}
    .glass-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 0 25px rgba(0,0,0,0.6);
    }}
    </style>
    <div class="gradient-overlay"></div>
''', unsafe_allow_html=True)

# Title
st.markdown('''
<h1 style='text-align: center;
            color: white;
            text-shadow: 2px 2px 4px #000;
            position: relative;
            z-index: 1;'>KOJK: NAWASENA</h1>
''', unsafe_allow_html=True)
st.write("")
st.write("")

# Card data
cards = [
    {"title": "Slider Prediksi", "image": "images/ai.png", "url": "https://example.com/simulasi"},
    {"title": "Peta AFI UFI", "image": "images/inklu.png", "url": "https://example.com/data"},
    {"title": "Peta NTL", "image": "images/lampu.png", "url": "https://example.com/peta"},
    {"title": "Klasifikasi", "image": "images/regstrat.png", "url": "https://example.com/ipm"},
    {"title": "Strategic Guide", "image": "images/benchmark.png", "url": "https://example.com/laporan"},
]

# Base64 encode image
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Render card
def display_card(card):
    if os.path.exists(card["image"]):
        encoded_img = get_base64_image(card["image"])
        st.markdown(f'''
            <a href="{card["url"]}" target="_blank" style="text-decoration: none;">
                <div class="glass-card">
                    <img src="data:image/png;base64,{encoded_img}"
                         style="width: 100%; max-width: 400px; height: 250px;
                                object-fit: cover; border-radius: 8px;" />
                    <h4 style="margin-top: 10px; color: white; text-shadow: 1px 1px 2px #000;">
                        {card["title"]}
                    </h4>
                </div>
            </a>
        ''', unsafe_allow_html=True)
    else:
        st.error(f"Gambar tidak ditemukan: {card['image']}")

# Display in 3-column layout
cols = st.columns(3)
for idx, card in enumerate(cards):
    with cols[idx % 3]:
        display_card(card)
