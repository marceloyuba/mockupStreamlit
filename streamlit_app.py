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
  
    st.markdown(""" # Strategic Data Transform""")
   
    st.subheader("Consultora de informacion de Latino America")
    
    st.subheader("A continuacion mostramos el Deploy de descripcio de el proyecto, endpoints y Dashboard")
   
    st.write("[Nuestro Github >](https://github.com/marceloyuba)")
    st.write("[Nuestro LinkedIn >](https://www.linkedin.com/in/marcelo-yuba-b9a39827b/)")

with st.container():
    st.markdown('<style>h4{color: white;}, font=</style>', unsafe_allow_html=True)    
    st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h2 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h1 {color: white;}, font=</style>', unsafe_allow_html=True)
    
    
    st.title("Este sector quedaria reservado para la explicacion del proyecto")
   
    st.header("Sobre Nosotros")
    st.markdown("""
                #### Strategic Data Transform es una consultora de información, para generar estrategias de negocios, basado en datos. Se basa en un tipo de negocio B2B, como empresa, ofrecer servicios a otras empresas, que estén dentro de la esfera del IT, tanto como empresas no relacionadas a la actividad y tengan necesidades de analizar sus datos y que permita poder desarrollar mejor sus actividades, teniendo conciencia de donde se encuentran las fallas en relación con cómo administran su información de negocio. 

                #### Nuestra propuesta de valor: Dashboards de alto impacto: Dados los conocimientos técnicos, pero a su vez visuales, gracias a técnicas de diseño gráfico y publicidad, la idea es hacer dashboards de un gran impacto visual como a la vez completamente funcionales, interactivos e intuitivos para el usuario. En la actualidad se muestran muchas métricas y gráficos de manera apilada, sin dejar espacios libres, haciéndolos densos para ser leídos e interpretados. Nuestra idea es usar gráficos que sean más originales, respetando su imagen corporativa, pero un poco más desafiantes que paneles convencionales, que simplemente sean funcionales.
                """)    
    st.header("Equipo de trabajo")
    st.write("##")
    st.markdown(""" 
                #### Cristian Fontanilla = Data Engeenier
                
                #### Elizabeth Torres = Data Engeenier
                
                #### Ingrid Barrios = Data Analyst
                
                #### Josue Mora = Data Science
                
                #### Marcelo Yuba = Team Leader / Data Analyst
                  """)
    st.header("Nuestro Cliente")
    st.markdown(""" 
#### La marca icónica de Greyhound es sinónimo de viajes asequibles de larga distancia en América del Norte con una red única.
#### Fundada en 1914, Greyhound Lines, Inc. es el proveedor más grande de transporte interurbano en autobús, sirviendo 2300 destinos en América del Norte con una flota moderna y respetuosa con el medio ambiente. Se ha convertido en un símbolo estadounidense, brindando viajes seguros, agradables y asequibles a casi 16 millones de pasajeros cada año en los Estados Unidos y Canadá. El perro de carrera de Greyhound es una de las marcas más reconocidas a nivel mundial.
#### Si bien Greyhound es bien conocida por su servicio de pasajeros programado regularmente, la compañía también ofrece una serie de otros servicios para sus clientes. Greyhound brinda paquetes chárter para empresas, convenciones, escuelas y otros grupos a precios competitivos.
#### En 2010 la compañía lanzó su servicio premium de ciudad a ciudad, Greyhound Express, y desde entonces expandió rápidamente el popular servicio a más de 135 mercados en América del Norte. También opera Greyhound Connect, un servicio que conecta comunidades rurales con destinos de Greyhound más grandes en los Estados Unidos.
#### Además, Greyhound tiene alianza con varias compañías de autobuses independientes en los Estados Unidos. Esas empresas brindan servicios complementarios a los horarios existentes de Greyhound y llegan a muchas de las ciudades más pequeñas en el sistema de rutas nacionales de Greyhound.
#### Los pasajeros de Amtrak usan Greyhound para hacer conexiones a ciudades que no cuentan con el servicio ferroviario Thruway de Amtrak al comprar un boleto para la conexión de autobús de Amtrak junto con la compra de su boleto de tren. Los pasajeros también pueden comprar un boleto de autobús directamente con Greyhound.
#### Flix SE adquirió Greyhound Lines Inc. el 21 de octubre de 2021. Habiendo estado presente en el mercado norteamericano con sus servicios FlixBus desde 2018, la compra de Greyhound reunió a dos líderes en la industria de autobuses interurbanos, combinando la tecnología global innovadora de FlixBus y la experiencia en movilidad compartida con la presencia y experiencia icónicas a nivel nacional de Greyhound. Desde julio de 2022, la entidad con sede en Dallas Flix North America, Inc. ("Flix North America") supervisa las operaciones de Greyhound y FlixBus en América del Norte.
#### Juntos, FlixBus, Greyhound y sus socios continúan ofreciendo una experiencia de autobús interurbano de clase mundial inteligente, ecológica y moderna, brindando la mejor opción asequible para aún más personas que viajan por los Estados Unidos.
#### Desde la expansión en 2021, Nuestro cliente analiza nuevos mercados fuera del transporte de buses, por eso nos encomendó analizar si es viable ingresar al negocio de los viajes en automóviles, para eso usamos como marco de referencia los transportes ya existentes y posibles competidores.
                  """)        
    
    
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