
import streamlit as st
from streamlit.hello.utils import show_code

st.set_page_config(page_title="Strategic Data Transform", page_icon="scr/fondo.jpg", layout="wide")
           
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

with st.container():
    
    st.image("scr/titulo.png",use_column_width=True, output_format='auto')
    st.title("")
    st.image("scr/logo.png", use_column_width=True, output_format='auto')


with st.container():
    
    st.markdown('<style>h4{color: white;}, font=</style>', unsafe_allow_html=True)    
    st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h2 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h1 {color: white;}, font=</style>', unsafe_allow_html=True)
    
column_widths = [2, 1]
with st.container():
     
    col1, col2 = st.columns(column_widths)   
    
    with col1:
        st.title("Nuestro Cliente")
        st.markdown(""" 
                #### Empresa líder en el mercado de transporte de pasajeros de media y larga distancia, con una larga trayectoria, paso a manos de Flix North America y Juntos, FlixBus, Greyhound y sus socios continúan ofreciendo una experiencia de autobús interurbano de clase mundial inteligente, ecológica y moderna, brindando la mejor opción asequible para aún más personas que viajan por los Estados Unidos.
                  """) 
    
    with col2:
        imagen = "scr/cliente.png"  
        st.image(imagen, width=500, use_column_width=True, output_format='auto')        

st.title("")
st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    
with st.container():
    col1, col2 = st.columns(column_widths)
    
    with col1:
        st.title("Nuestra mision")        
        st.markdown("""
                #### Desde la expansión en 2021, Nuestro cliente analiza nuevos mercados fuera del transporte de buses, por eso nos encomendó analizar la inserción al negocio de los viajes en automóviles, analizando a su competidores directos (Taxis, Uber, Lyft) y comenzando por la ciudad de Nueva York, ya que la misma tiene una de las redes mas complejas de transporte en todo el pais, nuestro trabajo es analizar si es viable el ingreso al sistema cumpliendo con las regulaciones impuestas por el gobierno respecto a tener una ciudad libre de emisiones contaminantes""") 
        
    with col2:
        imagen = "scr/mision.png"  
        st.image(imagen, width=500, use_column_width=True, output_format='auto')

      
with st.container():    
    st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h2 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h1 {color: white;}, font=</style>', unsafe_allow_html=True)
st.title("")
st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    
def main():    

    st.title("Dashboard de analisis de insercion de mercado")
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
       <iframe title="DatasetMockup" width="1300" height="860" src="https://app.powerbi.com/view?r=eyJrIjoiZjRmOWFiOWUtZmE4Yy00MDcwLTllNjktNjE5NTcwZDY3OTJlIiwidCI6ImUyYjc5Nzc5LTBhODgtNDMzMS05YjQyLTM4NGNkNzFjODVkNyIsImMiOjR9&pageName=ReportSection10f0c58045468d53ab10" frameborder="0" allowFullScreen="true"></iframe>
       </div>
        """,
        
        unsafe_allow_html=True
    )
    st.title("")
    st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)   
    st.title("Calculador de vehiculos")
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
       <iframe title="DatasetMockup" width="1300" height="860" src="https://app.powerbi.com/view?r=eyJrIjoiMjM3OGExNjItNTBmZS00MDhmLThmYzYtNDFlMTYzNWZmYWEyIiwidCI6ImUyYjc5Nzc5LTBhODgtNDMzMS05YjQyLTM4NGNkNzFjODVkNyIsImMiOjR9" frameborder="10" allowFullScreen="true"></iframe>
       </div>
        """,
        
        unsafe_allow_html=True
        
        
    )
        
if __name__ == "__main__":
    main()

st.title("")
st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    
with st.container():
    
    st.header("Contactanos!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/strategicdatatransform@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Nombre" required>
        <input type="email" name="email" placeholder="E-mail" required>
        <textarea name="message" placeholder="Tu consulta" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()




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