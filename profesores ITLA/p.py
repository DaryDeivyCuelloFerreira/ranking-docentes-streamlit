import streamlit as st
import pandas as pd

# Crear bases de datos
profesores_data = {
    'Carrera': [
        'Desarrollo de Software', 'Desarrollo de Software', 'Desarrollo de Software',
        'Ciberseguridad', 'Ciberseguridad',
        'Inteligencia Artificial', 'Inteligencia Artificial',
        'Simulaciones Interactivas y Videojuegos', 'Simulaciones Interactivas y Videojuegos',
        'Telecomunicaciones', 'Telecomunicaciones',
        'Informática Forense', 'Informática Forense',
        'Energías Renovables', 'Energías Renovables',
        'Redes de Información', 'Redes de Información',
        'Mecatrónica', 'Mecatrónica',
        'Manufactura Automatizada', 'Manufactura Automatizada',
        'Multimedia', 'Multimedia',
        'Sonido', 'Sonido',
        'Analítica y Ciencia de los Datos', 'Analítica y Ciencia de los Datos',
        'Seguridad Informática', 'Seguridad Informática'
    ],
    'Asignatura': [
        'Bases de Datos 1', 'Bases de Datos 2', 'Programación Avanzada',
        'Criptografía', 'Seguridad en Redes',
        'Redes Neuronales', 'Procesamiento de Lenguaje Natural',
        'Diseño de Videojuegos', 'Programación de Simulaciones',
        'Redes de Datos', 'Comunicaciones Ópticas',
        'Informática Forense 1', 'Recuperación de Datos',
        'Energía Solar', 'Energía Eólica',
        'Administración de Redes', 'Seguridad de Redes',
        'Robótica', 'Sistemas Mecatrónicos',
        'Automatización Industrial', 'Control de Producción',
        'Diseño Gráfico', 'Producción Multimedia',
        'Ingeniería de Sonido', 'Técnicas de Grabación',
        'Minería de Datos', 'Análisis Predictivo',
        'Fundamentos de Seguridad', 'Hacking Ético'
    ],
    'Nombre': [
        'María Pérez', 'Juan Gómez', 'Ana Rodríguez',
        'Carlos Ruiz', 'Laura Sánchez',
        'Pedro Martínez', 'Sofía Díaz',
        'Luis Torres', 'Elena Rivas',
        'Fernando Soto', 'Patricia Méndez',
        'Andrés Castillo', 'Natalia Herrera',
        'Julio Morales', 'Carmen Díaz',
        'Adrián Figueroa', 'Verónica Lara',
        'Eduardo Peña', 'Mónica Vásquez',
        'Roberto Salazar', 'Daniela Campos',
        'Silvia Romero', 'Gabriel Álvarez',
        'Oscar Molina', 'Viviana Cruz',
        'Mauricio León', 'Paula Rivera',
        'Ernesto Fuentes', 'Daniela Vega'
    ],
    'Ranking': [
        4.8, 4.5, 4.9,
        4.2, 4.7,
        4.3, 4.6,
        4.5, 4.6,
        4.4, 4.3,
        4.7, 4.6,
        4.2, 4.4,
        4.5, 4.3,
        4.6, 4.7,
        4.5, 4.4,
        4.6, 4.5,
        4.3, 4.4,
        4.7, 4.6,
        4.5, 4.4
    ]
}

# Datos adicionales - INGLÉS
asignaturas_ingles = ['Nivel 1-3', 'Nivel 4-6', 'Nivel 7-9', 'Nivel 10-12', 'Inglés Técnico']
profesores_ingles = ['Lucas González', 'Marina Ríos', 'Andrés Rivas', 'Camila Peña', 'Sebastián Morales']
ranking_ingles = [4.3, 4.5, 4.2, 4.4, 4.6]

asignaturas_humanidades = ['Historia Universal', 'Ética Profesional', 'Filosofía Moderna']
profesores_humanidades = ['Javier Soto', 'Ana Beltrán', 'Luis Fernández']
ranking_humanidades = [4.5, 4.4, 4.3]

# Crear DataFrames
df_tecnicos = pd.DataFrame(profesores_data)
df_ingles = pd.DataFrame({
    'Carrera': ['Inglés'] * 5,
    'Asignatura': asignaturas_ingles,
    'Nombre': profesores_ingles,
    'Ranking': ranking_ingles
})
df_humanidades = pd.DataFrame({
    'Carrera': ['Humanidades'] * 3,
    'Asignatura': asignaturas_humanidades,
    'Nombre': profesores_humanidades,
    'Ranking': ranking_humanidades
})

# FUNCIONES

def preparar_tabla(df):
    df_ordenado = df.sort_values(by='Ranking', ascending=False).reset_index(drop=True)
    df_ordenado['Ranking'] = df_ordenado['Ranking'].round(1)

    medallas = []
    for ranking in df_ordenado['Ranking']:
        if ranking >= 4.8:
            medallas.append('🥇 Oro')
        elif 4.6 <= ranking < 4.8:
            medallas.append('🥈 Plata')
        elif 4.4 <= ranking < 4.6:
            medallas.append('🥉 Bronce')
        else:
            medallas.append('-')
    df_ordenado['Medalla'] = medallas
    return df_ordenado[['Carrera', 'Nombre', 'Asignatura', 'Ranking', 'Medalla']]

def aplicar_estilos(df):
    def estilo_medalla(val):
        if val == '🥇 Oro':
            return 'background-color: gold; color: black; font-weight: bold'
        elif val == '🥈 Plata':
            return 'background-color: silver; color: black; font-weight: bold'
        elif val == '🥉 Bronce':
            return 'background-color: #cd7f32; color: white; font-weight: bold'
        else:
            return ''
    return df.style.applymap(estilo_medalla, subset=['Medalla'])

# INTERFAZ

st.title('🏅 Ranking de Rendimiento Docente')

st.markdown("""
> Este ranking tiene como finalidad brindar a los estudiantes información confiable sobre los docentes más destacados,
> ayudándolos a elegir con mayor certeza a aquellos profesores que puedan contribuir a una mejor experiencia académica
> y un ambiente de aprendizaje más positivo.
""")

# Sidebar
st.sidebar.header("Navegación")
seccion = st.sidebar.radio('Seleccione una sección:', ['Seleccione una opción', 'Técnicos', 'Inglés', 'Humanidades'])

# Mostrar tabla según sección
if seccion == 'Técnicos':
    carrera_tecnica = st.sidebar.selectbox('Seleccione una carrera técnica:', sorted(df_tecnicos['Carrera'].unique()))
    if carrera_tecnica:
        df_filtrado = df_tecnicos[df_tecnicos['Carrera'] == carrera_tecnica]

        asignaturas = sorted(df_filtrado['Asignatura'].unique())
        asignatura_tecnica = st.sidebar.selectbox('Seleccione una asignatura:', ['Todas'] + list(asignaturas))
        if asignatura_tecnica != 'Todas':
            df_filtrado = df_filtrado[df_filtrado['Asignatura'] == asignatura_tecnica]

        busqueda = st.sidebar.text_input('Buscar profesor por nombre')
        if busqueda:
            df_filtrado = df_filtrado[df_filtrado['Nombre'].str.contains(busqueda, case=False)]

        if not df_filtrado.empty:
            tabla = preparar_tabla(df_filtrado)
            st.dataframe(
                aplicar_estilos(tabla).format({'Ranking': '{:.1f}'})
            )

elif seccion == 'Inglés':
    asignatura_ingles_sel = st.sidebar.selectbox('Seleccione un nivel de Inglés:', ['Todas'] + asignaturas_ingles)
    busqueda = st.sidebar.text_input('Buscar profesor por nombre')

    df_filtrado = df_ingles
    if asignatura_ingles_sel != 'Todas':
        df_filtrado = df_filtrado[df_filtrado['Asignatura'] == asignatura_ingles_sel]
    if busqueda:
        df_filtrado = df_filtrado[df_filtrado['Nombre'].str.contains(busqueda, case=False)]

    if not df_filtrado.empty:
        tabla = preparar_tabla(df_filtrado)
        st.dataframe(
            aplicar_estilos(tabla).format({'Ranking': '{:.1f}'})
        )

elif seccion == 'Humanidades':
    asignatura_human_sel = st.sidebar.selectbox('Seleccione una asignatura de Humanidades:', ['Todas'] + asignaturas_humanidades)
    busqueda = st.sidebar.text_input('Buscar profesor por nombre')

    df_filtrado = df_humanidades
    if asignatura_human_sel != 'Todas':
        df_filtrado = df_filtrado[df_filtrado['Asignatura'] == asignatura_human_sel]
    if busqueda:
        df_filtrado = df_filtrado[df_filtrado['Nombre'].str.contains(busqueda, case=False)]

    if not df_filtrado.empty:
        tabla = preparar_tabla(df_filtrado)
        st.dataframe(
            aplicar_estilos(tabla).format({'Ranking': '{:.1f}'})
        )
