import streamlit as st
import Functions

st.set_page_config(page_icon="scr/fondo.jpg", layout="wide")
           
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

# ---- HEADER SECTION ----
with st.container():    
    st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.subheader("Hola, soy Marcelo Yuba :wave:")
    st.markdown('<style>h1 {color: white;}</style>', unsafe_allow_html=True)
    st.title("Un Data Analyst  y Data Scientist de Buenos Aires, Argentina")
    st.write(
        "Soy un apasionado en el analisis de datos usando, Power BI y Python, tratando de forma mas eficiente,  obtener resultados para tu negocio."
    )
    st.write("[Mi Github >](https://github.com/marceloyuba)")
    st.write("[Mi LinkedIn >](https://www.linkedin.com/in/marcelo-yuba-b9a39827b/)")

def Developer(desarrollador):
    resultadodeveloper = Functions.Developer(desarrollador)
    return resultadodeveloper

st.markdown(""" 
    <html>
        <body>
            <h2>INSTRUCCIONES</h2>
            <p>            
                Ingrese el destino a donde quiere ir
                 
            </p>      
        </body>
    </html>
    """, unsafe_allow_html=True)

desarrollador = st.text_input("Ingrese el destino a donde quiere ir", "Brooklyn")
if st.button("Consultar"):
    developer_result = Developer(desarrollador)
    st.write(developer_result)







page_bg_img = f"""
<style>

[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://github.com/marceloyuba/PorfolioIngles/blob/main/scr/fondoTaxi.png?raw=true");
background-position: top left;
background-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)