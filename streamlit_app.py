import streamlit as st
import Functions


st.set_page_config(page_title="Strategic Data Transform", page_icon="scr/fondo.jpg", layout="wide")
           
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")
with st.container():
    st.title("Analisis estrategico de inserción de mercado")
    st.title("")
    st.image("https://github.com/marceloyuba/mockupStreamlit/blob/main/scr/logos.png?raw=true")

  
with st.container():
    st.markdown(
    """
    <style>
        a {
            color: red; /* Cambia el color del texto del enlace a rojo */
        }
    </style>
    """,
    unsafe_allow_html=True
   )
    st.markdown('<style>h4{color: white;}, font=</style>', unsafe_allow_html=True)    
    st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h2 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h1 {color: white;}, font=</style>', unsafe_allow_html=True)
     
    st.header("Nuestro Cliente")
    st.markdown(""" 
                #### Empresa líder en el mercado de transporte de pasajeros de media y larga distancia, con una larga trayectoria, paso a manos de Flix North America y Juntos, FlixBus, Greyhound y sus socios continúan ofreciendo una experiencia de autobús interurbano de clase mundial inteligente, ecológica y moderna, brindando la mejor opción asequible para aún más personas que viajan por los Estados Unidos.
                  """)       
     
    st.header("Nuestra mision")
    st.markdown("""
                #### Desde la expansión en 2021, Nuestro cliente analiza nuevos mercados fuera del transporte de buses, por eso nos encomendó analizar la inserción al negocio de los viajes en automóviles, analizando a su competidores directos (Taxis, Uber, Lyft) y comenzando por la ciudad de Nueva York, ya que la misma tiene una de las redes mas complejas de transporte en todo el pais, nuestro trabajo es analizar si es viable el ingreso al sistema cumpliendo con las regulaciones impuestas por el gobierno respecto a tener una ciudad libre de emisiones contaminantes""") 
    
    st.subheader("Datos relevantes del proyecto")
    st.write("[Nuestros datos >](https://dashboardsiniestrosviales.observablehq.cloud/documentaci-n/)")
    
    st.header("Equipo de trabajo")
    st.write("##")
    st.markdown(""" 
                #### Cristian Fontanilla = Data Engeenier
                
                #### Elizabeth Torres = Data Engeenier
                
                #### Ingrid Barrios = Data Analyst
                
                #### Josue Mora = Data Science
                
                #### Marcelo Yuba = Team Leader / Data Analyst
                  """)

with st.container():    
    st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h2 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h1 {color: white;}, font=</style>', unsafe_allow_html=True)
    
    st.markdown(""" 
                # Mostramos nuestros resultados""")
   
    
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
       <iframe title="DatasetMockup" width="1240" height="1000" src="https://app.powerbi.com/view?r=eyJrIjoiZjRmOWFiOWUtZmE4Yy00MDcwLTllNjktNjE5NTcwZDY3OTJlIiwidCI6ImUyYjc5Nzc5LTBhODgtNDMzMS05YjQyLTM4NGNkNzFjODVkNyIsImMiOjR9&pageName=ReportSection10f0c58045468d53ab10" frameborder="0" allowFullScreen="true"></iframe></div>
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