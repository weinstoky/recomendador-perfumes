import streamlit as st

st.set_page_config(
    page_title="Recomendador de Perfumes", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar session state para preferencias
if 'historial_ph' not in st.session_state:
    st.session_state.historial_ph = []
if 'perfumes_favoritos' not in st.session_state:
    st.session_state.perfumes_favoritos = []

# Función para aplicar fondo de color según categoría
def set_background(color):
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """, unsafe_allow_html=True)

# Encabezado
st.markdown("<h1 style='text-align:center; color:#4B0082;'>✨ Recomendador de Perfumes ✨</h1>", unsafe_allow_html=True)
st.write("Descubre tu fragancia ideal según tu pH, la ocasión y el mejor lugar para aplicarla.")

# Sidebar para preferencias guardadas
with st.sidebar:
    st.markdown("###  Tus Preferencias")
    
    if st.session_state.historial_ph:
        st.markdown("**Últimos pH consultados:**")
        for ph_hist in st.session_state.historial_ph[-5:]:
            st.text(f"pH {ph_hist}")
    
    if st.session_state.perfumes_favoritos:
        st.markdown("** Perfumes Favoritos:**")
        for fav in st.session_state.perfumes_favoritos:
            st.text(f"• {fav}")
        if st.button(" Limpiar favoritos"):
            st.session_state.perfumes_favoritos = []
            st.rerun()

# Barra de pH
ph = st.slider("Selecciona tu pH de piel", 0.0, 14.0, 5.5, 0.1)

# Guardar pH en historial
if ph not in st.session_state.historial_ph:
    st.session_state.historial_ph.append(ph)

# Definir categorías según pH
if ph <= 3.0:
    color = "#87CEEB"
    tipo = "Fragancias frescas y acuáticas"
    descripcion = "Tu piel es muy ácida. Los aromas frescos y acuáticos duran más y se sienten ligeros."
    estacion = " Primavera /  Verano"
    perfumes = [
        {
            "nombre": "Acqua di Gio - Giorgio Armani",
            "ocasión": "Uso diario",
            "lugar": "Muñecas y cuello",
            "notas_top": "Bergamota, Neroli, Mandarina",
            "notas_corazon": "Jazmín, Calone, Romero",
            "notas_base": "Ámbar, Cedro, Almizcle",
            "precio": "$95 USD"
        },
        {
            "nombre": "Nautica Voyage",
            "ocasión": "Días calurosos",
            "lugar": "Cuello y pecho",
            "notas_top": "Manzana verde, Hoja de loto",
            "notas_corazon": "Mimosa, Menta acuática",
            "notas_base": "Cedro, Almizcle, Ámbar",
            "precio": "$25 USD"
        },
        {
            "nombre": "Issey Miyake L'Eau d'Issey",
            "ocasión": "Oficina o citas",
            "lugar": "Muñecas y cuello",
            "notas_top": "Limón, Bergamota, Yuzu",
            "notas_corazon": "Lirio, Nuez moscada",
            "notas_base": "Sándalo, Cedro, Almizcle",
            "precio": "$75 USD"
        }
    ]
elif 3.0 < ph <= 4.5:
    color = "#98D8C8"
    tipo = "Fragancias cítricas y aromáticas"
    descripcion = "Tu piel es ácida. Los aromas cítricos y aromáticos resaltan mejor y se perciben frescos."
    estacion = " Primavera"
    perfumes = [
        {
            "nombre": "Versace Pour Homme",
            "ocasión": "Día casual",
            "lugar": "Muñecas y cuello",
            "notas_top": "Limón, Bergamota, Neroli",
            "notas_corazon": "Cedro, Salvia, Ámbar",
            "notas_base": "Almizcle, Ámbar gris",
            "precio": "$85 USD"
        },
        {
            "nombre": "Dolce & Gabbana Light Blue",
            "ocasión": "Trabajo o eventos diurnos",
            "lugar": "Cuello y muñecas",
            "notas_top": "Toronja, Bergamota, Enebro",
            "notas_corazon": "Pimienta, Romero, Palo de rosa",
            "notas_base": "Almizcle, Roble, Incienso",
            "precio": "$92 USD"
        },
        {
            "nombre": "Calvin Klein Eternity",
            "ocasión": "Eventos formales",
            "lugar": "Cuello y pecho",
            "notas_top": "Mandarina, Lavanda, Limón",
            "notas_corazon": "Jazmín, Albahaca, Salvia",
            "notas_base": "Sándalo, Ámbar, Vetiver",
            "precio": "$68 USD"
        }
    ]
elif 4.5 < ph <= 5.5:
    color = "#B8D4E3"
    tipo = "Fragancias frescas y especiadas"
    descripcion = "Tu pH ligeramente ácido permite que los aromas frescos y especiados se mantengan todo el día."
    estacion = " Verano"
    perfumes = [
        {
            "nombre": "Bleu de Chanel",
            "ocasión": "Trabajo o días calurosos",
            "lugar": "Muñecas y cuello",
            "notas_top": "Limón, Menta, Pomelo",
            "notas_corazon": "Jengibre, Nuez moscada, Jazmín",
            "notas_base": "Incienso, Cedro, Sándalo",
            "precio": "$150 USD"
        },
        {
            "nombre": "Paco Rabanne 1 Million",
            "ocasión": "Fiestas y salidas nocturnas",
            "lugar": "Cuello y muñecas",
            "notas_top": "Pomelo, Menta, Sangre de dragón",
            "notas_corazon": "Rosa, Canela, Especias",
            "notas_base": "Cuero, Ámbar, Madera",
            "precio": "$95 USD"
        },
        {
            "nombre": "Hugo Boss Bottled",
            "ocasión": "Oficina y reuniones",
            "lugar": "Pecho y cuello",
            "notas_top": "Manzana, Limón, Ciruela",
            "notas_corazon": "Canela, Geranio, Clavel",
            "notas_base": "Sándalo, Cedro, Vetiver",
            "precio": "$78 USD"
        }
    ]
elif 5.5 < ph <= 6.5:
    color = "#C4B896"
    tipo = "Fragancias amaderadas y frescas"
    descripcion = "Tu pH equilibrado permite que fragancias amaderadas y frescas se mantengan perfectas."
    estacion = " Primavera /  Otoño"
    perfumes = [
        {
            "nombre": "Dior Sauvage",
            "ocasión": "Día a día",
            "lugar": "Muñecas y cuello",
            "notas_top": "Bergamota de Calabria, Pimienta",
            "notas_corazon": "Lavanda, Pimienta Sichuan",
            "notas_base": "Ámbar gris, Cedro, Vetiver",
            "precio": "$155 USD"
        },
        {
            "nombre": "Jean Paul Gaultier Le Male",
            "ocasión": "Cenas y citas",
            "lugar": "Cuello y pecho",
            "notas_top": "Menta, Lavanda, Bergamota",
            "notas_corazon": "Canela, Comino, Flor de naranjo",
            "notas_base": "Vainilla, Tonka, Sándalo",
            "precio": "$98 USD"
        },
        {
            "nombre": "Montblanc Explorer",
            "ocasión": "Eventos sociales",
            "lugar": "Muñecas y cuello",
            "notas_top": "Bergamota, Pimienta rosa",
            "notas_corazon": "Cuero, Vetiver",
            "notas_base": "Pachulí, Ámbar, Madera de cachemira",
            "precio": "$72 USD"
        }
    ]
elif 6.5 < ph <= 7.5:
    color = "#C9A66B"
    tipo = "Fragancias amaderadas y especiadas"
    descripcion = "Tu piel ligeramente alcalina resalta aromas cálidos y especiados con elegancia."
    estacion = " Otoño /  Invierno"
    perfumes = [
        {
            "nombre": "Yves Saint Laurent La Nuit de L'Homme",
            "ocasión": "Eventos nocturnos",
            "lugar": "Cuello y muñecas",
            "notas_top": "Cardamomo, Bergamota",
            "notas_corazon": "Lavanda, Cedro",
            "notas_base": "Vetiver, Cumarín",
            "precio": "$128 USD"
        },
        {
            "nombre": "Tom Ford Noir Extreme",
            "ocasión": "Cenas elegantes",
            "lugar": "Detrás de las orejas y cuello",
            "notas_top": "Mandarina, Neroli, Azafrán",
            "notas_corazon": "Kulfi, Rosa, Nuez moscada",
            "notas_base": "Vainilla, Sándalo, Ámbar",
            "precio": "$175 USD"
        },
        {
            "nombre": "Armani Code",
            "ocasión": "Salidas nocturnas",
            "lugar": "Muñecas y pecho",
            "notas_top": "Bergamota, Limón",
            "notas_corazon": "Flor de olivo, Guayaco",
            "notas_base": "Tabaco, Cuero, Tonka",
            "precio": "$105 USD"
        }
    ]
else:
    color = "#8B7355"
    tipo = "Fragancias intensas y orientales"
    descripcion = "Tu pH muy alcalino favorece aromas intensos y sofisticados para ocasiones especiales."
    estacion = " Invierno"
    perfumes = [
        {
            "nombre": "Tom Ford Oud Wood",
            "ocasión": "Eventos nocturnos exclusivos",
            "lugar": "Cuello y muñecas",
            "notas_top": "Cardamomo, Pimienta rosa",
            "notas_corazon": "Oud, Sándalo, Vetiver",
            "notas_base": "Ámbar, Vainilla, Tonka",
            "precio": "$295 USD"
        },
        {
            "nombre": "Creed Aventus",
            "ocasión": "Cenas formales",
            "lugar": "Detrás de las orejas y pecho",
            "notas_top": "Piña, Grosella negra, Manzana",
            "notas_corazon": "Abedul, Pachulí, Jazmín",
            "notas_base": "Almizcle, Roble, Vainilla",
            "precio": "$445 USD"
        },
        {
            "nombre": "Viktor & Rolf Spicebomb",
            "ocasión": "Fiestas o reuniones importantes",
            "lugar": "Cuello y muñecas",
            "notas_top": "Bergamota, Toronja, Pimienta rosa",
            "notas_corazon": "Canela, Azafrán, Chile",
            "notas_base": "Tabaco, Cuero, Vetiver",
            "precio": "$125 USD"
        }
    ]

# Aplicar fondo
set_background(color)

# Mostrar tipo y descripción en panel grande
st.markdown(f"<div style='background-color:rgba(255,255,255,0.8); padding:30px; border-radius:20px; margin-bottom:20px;'>", unsafe_allow_html=True)
st.subheader(f" Tipo de fragancia recomendada: {tipo}")
st.write(descripcion)
st.markdown(f"**Mejor temporada:** {estacion}")
st.markdown("</div>", unsafe_allow_html=True)

# Mostrar perfumes en columnas con tarjetas mejoradas
st.markdown("###  Perfumes sugeridos para ti:")
cols = st.columns(3)
for i, p in enumerate(perfumes):
    with cols[i]:
        st.markdown(f"""
        <div style='background-color:rgba(255,255,255,0.9); padding:20px; border-radius:15px; margin-bottom:10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        """, unsafe_allow_html=True)
        
        st.markdown(f"### {p['nombre']}")
        st.markdown(f"** Precio:** {p['precio']}")
        st.markdown(f"** Ocasión:** {p['ocasión']}")
        st.markdown(f"** Aplicación:** {p['lugar']}")
        
        with st.expander(" Ver notas de fragancia"):
            st.markdown(f"**Notas superiores:** {p['notas_top']}")
            st.markdown(f"**Notas de corazón:** {p['notas_corazon']}")
            st.markdown(f"**Notas de base:** {p['notas_base']}")
        
        # Enlaces de compra
        st.markdown("** Comprar en:**")
        link_col1, link_col2, link_col3 = st.columns(3)
        with link_col1:
            st.markdown(f"[Amazon](https://www.amazon.com/s?k={p['nombre'].replace(' ', '+')})", unsafe_allow_html=True)
        with link_col2:
            st.markdown(f"[Sephora](https://www.sephora.com/search?keyword={p['nombre'].replace(' ', '+')})", unsafe_allow_html=True)
        with link_col3:
            st.markdown(f"[Ulta](https://www.ulta.com/search?q={p['nombre'].replace(' ', '+')})", unsafe_allow_html=True)
        
        # Botón para agregar a favoritos
        if p['nombre'] not in st.session_state.perfumes_favoritos:
            if st.button(f" Agregar a favoritos", key=f"fav_{i}"):
                st.session_state.perfumes_favoritos.append(p['nombre'])
                st.rerun()
        else:
            st.success(" En favoritos")
        
        st.markdown("</div>", unsafe_allow_html=True)

# Comparador de precios
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("###  Comparador de Precios")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div style='background-color:rgba(255,255,255,0.8); padding:15px; border-radius:10px; text-align:center;'>
        <h4> Amazon</h4>
        <p>Envío gratis con Prime</p>
    </div>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown(f"""
    <div style='background-color:rgba(255,255,255,0.8); padding:15px; border-radius:10px; text-align:center;'>
        <h4> Sephora</h4>
        <p>Muestras gratis incluidas</p>
    </div>
    """, unsafe_allow_html=True)
    
with col3:
    st.markdown(f"""
    <div style='background-color:rgba(255,255,255,0.8); padding:15px; border-radius:10px; text-align:center;'>
        <h4> Ulta Beauty</h4>
        <p>Puntos de recompensa</p>
    </div>
    """, unsafe_allow_html=True)

# Consejos adicionales
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("###  Consejos de Aplicación")

tips_col1, tips_col2 = st.columns(2)
with tips_col1:
    st.markdown("""
    <div style='background-color:rgba(255,255,255,0.8); padding:20px; border-radius:10px;'>
        <h4> Puntos de Pulso</h4>
        <ul>
            <li>Detrás de las orejas</li>
            <li>Interior de muñecas</li>
            <li>Detrás de las rodillas</li>
            <li>Interior de los codos</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tips_col2:
    st.markdown(f"""
    <div style='background-color:rgba(255,255,255,0.8); padding:20px; border-radius:10px;'>
        <h4> Mejor Momento</h4>
        <ul>
            <li>Después de la ducha</li>
            <li>Sobre piel hidratada</li>
            <li>No frotar, solo aplicar</li>
            <li>Evitar joyería directa</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Mensaje final
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'> Tu fragancia ideal refleja tu estilo único </h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666;'>Recuerda: cada piel es diferente, ¡prueba antes de comprar!</p>", unsafe_allow_html=True)
