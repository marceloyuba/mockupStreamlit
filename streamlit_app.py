import streamlit as st
import Functions


st.set_page_config(page_title="Strategic Data Transform", page_icon="scr/fondo.jpg", layout="wide")
           
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

column_widths = [2, 1] 

with st.container():
    col1, col2 = st.columns(column_widths)

    
    with col1:
        imagen = "scr/SDTLogo-blanco.png" 
        st.image(imagen, width=200)
    
    with col2:
        imagen = "scr/logoGreyhound.png"  
        st.image(imagen, width=500)



# ---- HEADER SECTION ----
with st.container():    
    st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h2 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h1 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>p {color: white;}, font=</style>', unsafe_allow_html=True)
    
    st.title("Muestra parcial del Deploy de Strategic Data Transform")
   
    st.subheader("Consultora de informacion de Latino America")
    
    st.subheader("A continuacion mostramos el Deploy de descripcio de el proyecto, endpoints y Dashboard")
   
    st.write("[Nuestro Github >](https://github.com/marceloyuba)")
    st.write("[Nuestro LinkedIn >](https://www.linkedin.com/in/marcelo-yuba-b9a39827b/)")

with st.container():    
    st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h2 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h1 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>p {color: white;}, font=</style>', unsafe_allow_html=True)
    
    st.title("Este sector quedaria reservado para la explicacion del proyecto")
   
    st.subheader("Sobre nuestra Consultora")
          
    st.header("Equipo de trabajo")
    st.subheader("""                
                <ul>
                    <li>Cristian Fontanilla = Data Engeenier</li>
                    <li>Elizabeth Torres = Data Engeenier</li>
                    <li>Ingrid Barrios = Data Analyst</li>
                    <li>Josue Mora = Data Science</li>
                    <li>Marcelo Yuba = Team Leader / Data Analyst</li>
                </ul>
                """)
    st.subheader("EDA")
    
    st.subheader("ETL")
    
    st.subheader("Analisis de los datos")
    
    st.subheader("Stack Tecnologico")

with st.container():    
    st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h2 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h1 {color: white;}, font=</style>', unsafe_allow_html=True)
    
    st.title("Mostramos nuestros resultados")
   
    
def Developer(desarrollador):
    resultadodeveloper = Functions.Developer(desarrollador)
    return resultadodeveloper
st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
st.markdown('<style>h2 {color: white;}, font=</style>', unsafe_allow_html=True)
st.markdown('<style>h1 {color: white;}, font=</style>', unsafe_allow_html=True)
st.subheader("Consulta de puntos mas solicitados en la ciudad")
desarrollador = st.text_input("", "Indique el codigo de la region")
if st.button("Consultar"):
    developer_result = Developer(desarrollador)
    st.write(developer_result)

def UserForGenre(Genero_Especificado):
    resultadoReview = Functions.UserForGenre(Genero_Especificado)
    return resultadoReview
st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
st.markdown('<style>h2 {color: white;}, font=</style>', unsafe_allow_html=True)
st.markdown('<style>h1 {color: white;}, font=</style>', unsafe_allow_html=True)
st.markdown('<style>p {color: white;}, font=</style>', unsafe_allow_html=True)
st.subheader("Calcule que vehiculo es el adecuado para su viaje")

Genero_Especificado = st.text_input("", "Indique el codigo del destino")
if st.button("Consultar_vehiculo"):
    Genero_Especificado = UserForGenre(Genero_Especificado)
    st.write(Genero_Especificado)
st.title("")
def main():
    st.title("Dashboard del PI2 en forma de muestra")
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <iframe width="1240" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiM2NjNDA0YmItMmRhZC00ZDhlLWFmOWYtZTZiMWMxYWY3ODAzIiwidCI6ImUyYjc5Nzc5LTBhODgtNDMzMS05YjQyLTM4NGNkNzFjODVkNyIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
    

if __name__ == "__main__":
    main()

page_bg_img = f"""
<style>

[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://github.com/marceloyuba/mockupStreamlit/blob/main/scr/fondoTaxi.png?raw=true");
background-position: top left;
background-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)