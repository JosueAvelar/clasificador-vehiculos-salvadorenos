import streamlit as st
import keras
import numpy as np
from PIL import Image
import json
from keras.applications.resnet50 import preprocess_input

@st.cache_resource
def load_model():
    model = keras.models.load_model('mi_modelo.keras')
    with open('clases.json') as f:
        class_indices = json.load(f)
    idx_to_class = {v: k for k, v in class_indices.items()}
    return model, idx_to_class

modelo, idx_to_class = load_model()

# Emojis por clase para hacerlo más visual
EMOJIS = {
    "Carro": "🚗",
    "Moto": "🏍️",
    "Bus Salvadoreno": "🚌",
    "Microbus Salvadoreno": "🚐"
}

# UI
st.title("🚦 Clasificador de Vehículos Salvadoreños")
st.write("Subí una imagen de un vehículo y el modelo te dirá qué tipo es.")
st.divider()

uploaded_file = st.file_uploader(
    "Subí tu imagen aquí",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    col1, col2 = st.columns(2)

    with col1:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Imagen subida", use_column_width=True)

    with col2:
        with st.spinner("Analizando imagen..."):
            IMG_SIZE = 160
            img_resized = image.resize((IMG_SIZE, IMG_SIZE))
            img_array  = np.array(img_resized)
            img_array  = preprocess_input(img_array)
            img_array  = np.expand_dims(img_array, axis=0)

            pred = modelo.predict(img_array, verbose=0)[0]

        # Clase ganadora
        idx_ganador   = np.argmax(pred)
        clase_ganador = idx_to_class[idx_ganador]
        emoji_ganador = EMOJIS.get(clase_ganador, "")
        prob_ganador  = pred[idx_ganador]
        nombre_ganador = clase_ganador.replace('_', ' ').title()

        st.subheader("Resultado:")
        st.markdown(f"## {emoji_ganador} {nombre_ganador}")
        st.markdown(f"**Confianza: {prob_ganador:.1%}**")
        st.divider()

        # Barras de probabilidad para todas las clases
        st.subheader("Probabilidades:")
        for idx in pred.argsort()[::-1]:
            nombre = idx_to_class[idx]
            emoji  = EMOJIS.get(nombre, "")
            prob   = pred[idx]
            nombre_limpio = nombre.replace('_', ' ').title()
            st.write(f"{emoji} **{nombre_limpio}**: {prob:.1%}")
            st.progress(float(prob))

st.divider()
st.caption("Desarrollado por Josué Avelar | Diplomado Python Avanzado - UDB | Módulo 4")