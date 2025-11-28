# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta 
# o abrimos el folder desde visual Studio Code 


# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC4.py
#  PC4.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal, otra donde contaran su experiencia aprendiendo a programar y una tercera donde presentarán sus gráficos.

# Creamos la lista de páginas
paginas = ['Sobre mí', 'Experiencia', 'Gráficos', 'Final']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona la sección que deseas ver', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Sobre mí':

    # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>๋࣭⭑✮💻 Intentando codificar 💻 ๋࣭ ⭑✮</h1>", unsafe_allow_html=True)

    # <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
    # La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
    # el atributo style se utiliza para agregar estilos CSS. 
    # En este caso, el texto está alineado al centro (text-align: center;). 
    # Pueden agregar emojis en el texto de Markdown utilizando códigos de emoji, por ejemplo:
    # <h1 style='text-align: center;'>Aquí escribe un nombre creativo para tu blog 📝</h1>
    # También pueden personalizar el color del texto utilizando el atributo style, por ejemplo:
    # <h1 style='text-align: center; color: blue;'>Nombre de tu blog</h1>
    # El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)

    col3, col4 = st.columns(2)

    col5, col6 = st.columns(2)


    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de perfil
    col2.image("perfil.jpg", caption='Maria Pia Enriquez Jimenez (soy yo!)', width=350)

    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "ellie.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # en este caso "Aquí puedes escribir una etiqueta debajo de la imagen". 
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

    # En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
    # Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
    # ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

    texto_1 = """
    ¡Hola! Mi nombre es Maria Pia Enriquez Jimenez ᓚ₍ ^. .^₎. Soy de Lima, Perú 🦙, estudio Comunicaciones Audiovisuales 🎥 en la Pontificia Universidad Católica del Perú y siempre me ha interesado el cómo las nuevas tecnologías transforman la forma en cómo contamos historias en forma de productos audiovisuales ˙✧˖°📷 ༘ ⋆｡˚. Escogí mi carrera justamente por eso, quiero ser parte de ese proceso creativo que crea productos que impresionen y conecten con la gente 𐀪𐀪. 
    """

    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
    
    # Mostramos el texto
    col1.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_1}</div>", unsafe_allow_html=True)

    texto_2 = """
    Lo que me gusta de mi carrera es que me permiye explorar distintos kenguajes que conforman lo que conocemos de la comunicación₍^. .^₎Ⳋ: lo audiovisual, escrito, digital, etc. También que siempre me reta a aprender cosas nuevas🐱, como en este curso que es donde logré aprender un poco de programación ( ˶°ㅁ°) !!
    """
    col4.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    col3.image("dino.jpg", width=350)

    texto_3 = """
    En un futuro me gustaría aplicar todos los conocimientos que he ido adquiriendo para desarrollarme como profesional ₍⑅ᐢ..ᐢ₎, buscar un trabajo que me haga feliz y con el que pueda llegar a una gran cantidad de personas a las que pueda impactar de buena manera ˚ ༘ 🦕𖦹⋆｡˚.
    """
    
    col5.markdown(f"<div style='text-align: justify; font-size: 19px; '>{texto_3}</div>", unsafe_allow_html=True)
    
    col6.image("harrypotter.jpg", width=350)

    texto = """
    Algunos de mis pasatiempos:
    """
    
    st.markdown(f"<h4 style='text-align: center;'>{texto}</h4>", unsafe_allow_html=True) #con esto he podido hacer un subtitulo, PUEDO HACER MÁS SUBTITULOS CON ESTO AAA

    # ACÁ VOY A PONER LAS IMÁGENES DE LOS PASATIEMPOS - hacer más columnas

    # COLUMNAS PARA LAS FOTOS
    col7, col8, col9 = st.columns(3)
    col10, col11, col12 = st.columns(3)

    col7.image("pelicula.jpg", caption='🍿Ver películas y series🎬', width=222)
    col8.image("libros.jpg", caption='Leer libros📖✨', width=222)
    col9.image("colombia.jpg", caption='Viajar🛫🗺️', width=222)
    col10.image("concierto.jpg", caption='Salir con amigos°📸⋆｡', width=222)
    col11.image("oli.jpg", caption='Mascotitas ᓚ₍ ^. .^₎', width=222)
    col12.image("cofi.jpg", caption='Probar nuevas cosas°☕⋆｡˚', width=222)


    # <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
    # La etiqueta <div> se utiliza para agrupar contenido en HTML. 
    # En este caso, el texto está justificado (text-align: justify;). 
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto} se reemplaza por el valor de la variable texto.

elif  pagina_seleccionada == 'Experiencia':

    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>Yo intentando programar ≽^- ˕ -^≼</h1>", unsafe_allow_html=True)

    # En esta sección debes describir y comentar tu experiencia aprendiendo a programar
    # ¿Cómo te sentiste al principio?, 
    # ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
    # ¿Qué te gustaría hacer con la programación en el futuro? 

    st.markdown(f"<h4 style='text-align: center;'>🪐¿Cómo me sentí al principio?🪐</h4>", unsafe_allow_html=True) #con esto he podido hacer un subtitulo, PUEDO HACER MÁS SUBTITULOS CON ESTO AAA
    texto_4 = """
    Al principio estaba un poco insegura sobre el curso /ᐠ-˕-マ, ya que nunca había comprendido cómo es que funcionaba la programación, aunque he visto videos en el que han programado antes🦖. Pero más que nada me daba curiosidad el aprender a programar ᨐฅ y cómo lo iban a abordar en clase.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4}</div>", unsafe_allow_html=True)


    st.markdown(f"<h4 style='text-align: center;'>☁️Cositas que me ha enseñado el programar☁️</h4>", unsafe_allow_html=True) #con esto he podido hacer un subtitulo, PUEDO HACER MÁS SUBTITULOS CON ESTO AAA
    texto_5 = """
    🦕Una de las cosas que la programación me ha enseñado es buscar el resolver problemas desde diferentes perspectivas, buscar dividir las cosas en pasos pequeños, con patrones y sobre todo el tener paciencia al no poder resolver algo a la primera.🦕
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px'>{texto_5}</div>", unsafe_allow_html=True)


    st.markdown(f"<h4 style='text-align: center; '>🐕¿Qué me gusta de programar y lo que me gustaría hacer con este conocimiento en el futuro?🐕</h4>", unsafe_allow_html=True)
    texto_6 = """
    Me gusta el poder armar un programa desde cero y poder añadir diferentes ideas que se me pueden ocurrir🦖🎀. El crear un programa de un interés propio es bastante increíble ฅ^._.^ฅ.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px'>{texto_6}</div>", unsafe_allow_html=True)
    texto_7 = """
    Me gustaría aplicar la programación para proyectos futuros🐈, como una página web para promocionar algún producto o servicio (˶ᵔ ᵕ ᵔ˶), o el crear programas interactivos para el disfrute del público, tal vez incluso el aprender a programar videojuegos◝(ᵔᗜᵔ)◜🐈‍⬛.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px'>{texto_7}</div>", unsafe_allow_html=True)


    # <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el texto está justificado (text-align: justify;).
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto_2.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto_2} se reemplaza por el valor de la variable texto.

    # Agregamos un subtítulo para el video
    st.markdown("<h2 style='text-align: center;'>Mi primer video intentando explicar un poco de Python (╥‸╥)</h2>", unsafe_allow_html=True)
    
    # <h2 style='text-align: center;'>Aquí escribe un nombre creativo para presentar tu video</h2>: Esta es una cadena de código HTML.
    # La etiqueta <h2> se utiliza para un encabezado de segundo nivel en una página web.
    # El texto está centrado (text-align: center;).
    # El texto dentro de las etiquetas <h2> ("Aquí escribe un nombre creativo para presentar tu video") es el contenido del encabezado.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.
    # Por ejemplo, puedes agregar un emoji de video 🎥 

    # Agregamos un video realizado en las practicas anteriores
    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
    
    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E"): Esta línea está mostrando un video en la aplicación web.
    # La función video toma como primer argumento la URL del video que se desea mostrar.
    # En este caso, la URL es "https://www.youtube.com/watch?v=X_Z7d04x9-E".
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.

    st.image("imagen_video.png", caption='Diferencias entre las declaraciones condicionales if-elif-else ( - ~ - )' , width=705)
    # O creamos un botón para ir al enlace del video con button
    st.markdown(f"<div style='text-align: center;'><a href='https://drive.google.com/file/d/1xdcc5xcp43zDlFBLc0Y2rCbxJJYUq4Pf/view?usp=sharing' target='_blank'><button>¡VER VIDEO AQUÍ!</button></a></div>", unsafe_allow_html=True) 

    # <div style='text-align: center;'><a href='https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link' target='_blank'><button>Ver video</button></a></div>:
    # Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el contenido está centrado (text-align: center;).
    # La etiqueta <a> se utiliza para crear un enlace.
    # El atributo href especifica la URL a la que se dirige el enlace.
    # En este caso, la URL es 'https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link'.
    # El atributo target='_blank' indica que el enlace se abrirá en una nueva pestaña del navegador.
    # La etiqueta <button> se utiliza para crear un botón.
    # El texto dentro de las etiquetas <button> ("Ver video") es el contenido del botón.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.
    
else:

    # Agregamos un título para la página de gráficos
    st.markdown("<h1 style='text-align: center;'>Algunos de mis gráficos -> los bonitos (•˕ •マ.ᐟ</h1>", unsafe_allow_html=True)

    # Creamos una lista de gráficos
    graficos = ['Gráfico de barras Tarjetas Rojas en La Liga', 'Gráfico de Resultados de Celta como visitante', 'Gráfico de Resultados de Celta como local', 'WordCloud Paro', 'Mapa Películas']

    # Creamos un cuadro de selección en la página de gráficos
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # El cuadro de selección se crea con la función selectbox.
    # El primer argumento es el texto que se muestra en el cuadro de selección.
    # El segundo argumento es una lista de opciones que se pueden seleccionar.
    # En este caso, las opciones son los elementos de la lista graficos.
    # La opción seleccionada se asigna a la variable grafico_seleccionado.
    # La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
    

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Gráfico de barras Tarjetas Rojas en La Liga':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
        st.image("LaLiga_promedio_tarjetas_rojas_equipo_local.png", caption='Promedio de tarjetas rojas en La Liga', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico de Resultados de Celta como visitante':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
        st.image("pastel_celta_visitante.png", caption='Resultados partidos Celta como visitante', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico de Resultados de Celta como local':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
        st.image("pastel_celta_local.png", caption='Resultados partidos Celta como local', width=500)
        pass
    elif grafico_seleccionado == 'WordCloud Paro':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
        st.image("wordcloud_paro.png", caption='WordCloud sobre el texto del Paro', width=500)
        pass
    elif grafico_seleccionado == 'Mapa Películas':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu mapa</div>", unsafe_allow_html=True)
        # Si "mapa_cusco.html" es un archivo HTML (no una imagen), debes mostrarlo con st.components.v1.html
        import streamlit.components.v1 as components
        with open("mapa_pelis.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass

    # if grafico_seleccionado == 'Gráfico de barras verticales de lenguas aisladas':
    # st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
    # st.image("aisladas_base_datos.png", caption='Gráfico de lenguas aisladas', width=500): Esta línea está mostrando una imagen en la aplicación web.
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar.
    # En este caso, la imagen es "aisladas_base_datos.png".
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen,
    # en este caso "Gráfico de lenguas aisladas".
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 500 píxeles.

    # elif grafico_seleccionado == 'mapa_cusco':
    # import streamlit.components.v1 as components
    # with open("mapa_cusco.html", "r", encoding="utf-8") as f:
    #     html_content = f.read()
    # components.html(html_content, height=500): Esta línea está mostrando un archivo HTML en la aplicación web.
    # La función components.html toma como primer argumento el contenido HTML que se desea mostrar.
    # En este caso, el contenido HTML se lee desde el archivo "mapa_cusco.html".
    # El argumento height se utiliza para especificar la altura del contenido HTML, en este caso 500 píxeles.
    
    # Si no tenemos el archivo HTML, podemos agregar el código para crear el mapa de Cusco directamente en Streamlit.
    # Primero debes crear el diccionario de coordenadas del mapa de Cusco.
    # Luego debes crear el mapa utilizando la librería folium y streamlit-folium.
    # pip install folium
    # pip install streamlit-folium
        #import folium
        #from streamlit_folium import st_folium

        # Mostrar el mapa en Streamlit
        #st_folium(mapa_cusco, width=700, height=500)


    
