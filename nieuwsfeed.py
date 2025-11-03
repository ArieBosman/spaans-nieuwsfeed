import streamlit as st
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from streamlit_autorefresh import st_autorefresh
import time

# Pagina-instellingen en aangepaste stijl
st.set_page_config(layout="wide")

# Automatische verversing elke 60 seconden
st_autorefresh(interval=60000, limit=None, key="nieuwsfeed")

# Aangepaste stijl: Arial, grotere tekst, minder witruimte
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: Arial, sans-serif;
        font-size: 20px;
        margin-top: -50px;
    }
    h1, h2, h3 {
        font-family: Arial, sans-serif;
    }
    .main {
        max-width: 1400px;
        margin: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Lijst van Spaanse nieuwswebsites
news_sites = [
    "https://elpais.com/",
    "https://www.elmundo.es/",
    "https://www.abc.es/",
    "https://www.lavanguardia.com/",
    "https://www.elperiodico.com/",
    "https://www.elconfidencial.com/",
    "https://www.20minutos.es/",
    "https://www.elespanol.com/",
    "https://www.diariosur.es/",
    "https://www.lavozdegalicia.es/",
    "https://www.marca.com/",
    "https://www.eleconomista.es/"
]

# Bepaal welke site we gebruiken op basis van tijd
index = int(time.time() // 60) % len(news_sites)
selected_site = news_sites[index]

# Headlines ophalen
def get_headlines(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all(['h2', 'h3'])
        return [h.get_text().strip() for h in headlines if h.get_text().strip()]
    except:
        return ["Geen headlines gevonden"]

# Vertalen Spaans → Nederlands
def translate_to_dutch(text):
    try:
        return GoogleTranslator(source='es', target='nl').translate(text)
    except:
        return "Vertaling mislukt"

# Titel en bronvermelding
st.markdown(f"<h2>📰 Live Spaanse Nieuwsfeed met Nederlandse Vertaling</h2>", unsafe_allow_html=True)
st.markdown(f"<p><i>Bron: {selected_site}</i></p>", unsafe_allow_html=True)

# Layout: twee kolommen
col1, col2 = st.columns([1, 1])  # Gelijk verdeeld

with col1:
    st.markdown("### 🇪🇸 Spaans")
    headlines = get_headlines(selected_site)
    for headline in headlines[:5]:
        st.write(f"- {headline}")

with col2:
    st.markdown("### 🇳🇱 Nederlands")
    for headline in headlines[:5]:
        translated = translate_to_dutch(headline)
        st.write(f"- {translated}")