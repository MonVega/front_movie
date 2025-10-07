import streamlit as st
from api import get_movie_prediction  

st.markdown(
    """
    <div style="background-color:#4CAF50;padding:20px;border-radius:12px;box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
        <h1 style="color:white;text-align:center;margin:0;">Movie Rating Predictor 🎬</h1>
        <p style="color:white;text-align:center;margin-top:5px;">¡Predice la calificación de tu película favorita!</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")  # espacio
st.write("Ingresa el título y la descripción de la película:")

# ---------------- SESSION STATE ----------------
if "prediction" not in st.session_state:
    st.session_state.prediction = None
if "input1" not in st.session_state:
    st.session_state.input1 = ""
if "input2" not in st.session_state:
    st.session_state.input2 = ""

# ---------------- INPUTS ----------------
st.markdown(
    """
    <div style="padding:10px; background-color:#f0f2f6; border-radius:10px; box-shadow: 1px 1px 5px rgba(0,0,0,0.1);">
    """,
    unsafe_allow_html=True
)

text1 = st.text_area("Título de la película:", height=100, key="input1")
st.write("")  # espacio
text2 = st.text_area("Descripción de la película:", height=150, key="input2")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FUNCIONES ----------------
def clear_all():
    st.session_state.input1 = ""
    st.session_state.input2 = ""
    st.session_state.prediction = None

def make_prediction():
    if text1.strip() and text2.strip():
        pred = get_movie_prediction(text1, text2)
        if pred is not None:
            st.session_state.prediction = pred
        else:
            st.error("No se pudo obtener la predicción de la API")
    else:
        st.warning("Debes ingresar ambos campos.")

st.write("")  
col1, col2 = st.columns(2)

with col1:
    st.button("Predecir", on_click=make_prediction, key="predict_btn", help="Haz clic para predecir la calificación")

with col2:
    st.button("Limpiar", on_click=clear_all, key="clear_btn", help="Haz clic para limpiar los campos y la predicción")

st.write("")  


if st.session_state.prediction is not None:
    score = st.session_state.prediction
    if score <= 1:
        icon = "❌"  # tach
        color = "#f44336"  # rojo
        bg_color = "#ffe6e6"
    elif 1 < score <= 3:
        icon = "✅"  # paloma
        color = "#4CAF50"  # verde
        bg_color = "#e6ffe6"
    else:
        icon = "⭐"  # estrella
        color = "#ff9800"  # naranja
        bg_color = "#fff3e6"

    st.markdown(
        f"""
        <div style="padding:15px; background-color:{bg_color}; border-radius:10px; 
                    border: 2px solid {color}; box-shadow: 1px 1px 8px rgba(0,0,0,0.1); text-align:center;">
            <h3 style="margin:0;color:{color};">Score: {score:.2f} {icon}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")  


st.markdown(
    """
    <hr>
    <div style="text-align:center; color:gray; font-size:12px; margin-top:20px;">
        Hecho con ❤️ por tu equipo de Movies
    </div>
    """,
    unsafe_allow_html=True
)