import streamlit as st
import base64
import os
import subprocess
import sys

# Tự động cài thư viện nếu thiếu
try:
    from streamlit_extras.switch_page_button import switch_page
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit-extras"])
    from streamlit_extras.switch_page_button import switch_page

# Cấu hình trang
st.set_page_config(page_title="Sleep Health", layout="wide", initial_sidebar_state="collapsed")

# Google Fonts
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Lato&family=Playfair+Display&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Thiết lập nền có overlay
def set_background_with_overlay(image_file):
    if not os.path.exists(image_file):
        st.warning(f"Ảnh nền '{image_file}' không tìm thấy. Sử dụng nền mặc định.")
        return
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    css = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(
            rgba(255, 246, 240, 0.85),
            rgba(255, 246, 240, 0.85)
        ),
        url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        animation: fadeIn 1.5s ease-in-out;
    }}
    .block-container {{
        max-width: 900px;
        margin: 0 auto;
        padding: 2rem !important;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 1rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        animation: slideUp 1s ease-in-out;
    }}
    .navbar {{
        position: fixed;
        top: 0; left: 0; width: 100%;
        padding: 1rem 2rem;
        background-color: rgba(255, 246, 240, 0.95);
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(200,180,170,0.5);
        animation: fadeInDown 1s ease;
    }}
    .navbar-title {{
        font-family: 'Playfair Display', serif;
        color: #a66f6f;
        font-size: 1.8rem;
        letter-spacing: 0.5px;
    }}
    .navbar-link {{
        font-family: 'Lato', sans-serif;
        color: #7a5c61;
        text-decoration: none;
        font-weight: 500;
        padding: 0.2rem 0.5rem;
        border-radius: 0.4rem;
        transition: background 0.3s ease;
    }}
    .navbar-link:hover {{
        background: rgba(122,92,97,0.1);
    }}
    </style>
    <div class="navbar">
        <div class="navbar-title">🛌 Sleep Health</div>
        <div><a class="navbar-link" href="?reset=true">🔙 Back to Welcome</a></div>
    </div>
    """
    st.markdown(css, unsafe_allow_html=True)

# Giao diện chào mừng
def show_landing():
    st.markdown("""
        <div class="hero">
            <h1>Welcome to Sleep Health & Lifestyle</h1>
            <p>🧠 <strong>Sleep matters.</strong><br>
            Sleep plays a vital role in our cognitive performance, emotional balance, and overall health.</p>
            <p>📚 <strong>About this project:</strong><br>
            Final project for <em>Business IT – Python for Data Science</em>.</p>
            <p>💡 <strong>What you'll gain:</strong><br>
            Learn about the relationship between sleep quality and lifestyle habits.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3, 2, 3])
    with col2:
        if st.button("🚀 Let's Start", use_container_width=True):
            st.session_state.started = True
            st.rerun()

# Chuyển sang trang chính
def show_main_app():
    switch_page("homepage")

# Chạy chính
def main():
    set_background_with_overlay("cafe.jpg")  # Nên đặt ảnh cafe.jpg cùng thư mục

    if st.query_params.get("reset") == "true":
        st.session_state.started = False
        st.query_params.clear()

    if "started" not in st.session_state:
        st.session_state.started = False

    if not st.session_state.started:
        show_landing()
    else:
        show_main_app()

main()
