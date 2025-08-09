import streamlit as st
import pandas as pd
import datetime
import os
from supabase import create_client, Client

# Cargar credenciales de Supabase desde variables de entorno
SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')

# Verificar que las credenciales estén presentes
if not SUPABASE_URL or not SUPABASE_KEY:
    st.error("Error: Las credenciales de Supabase no están configuradas. Por favor, contacta al administrador.")
    st.stop()

try:
    # Inicializar cliente Supabase
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception as e:
    st.error(f"Error al conectar con Supabase: {str(e)}")
    st.stop()

# Interfaz de la app
st.title('Registrador de Conductas Morales')

# Sección de autenticación para admin
st.subheader('Acceso Administrador')
admin_password = st.text_input('Ingresa la contraseña de administrador:', type='password')
is_admin = admin_password == 'admin123'  # Cambia 'admin123' por tu contraseña deseada

# Sección para registrar conducta (visible para todos)
st.subheader('Registrar Conducta')
st.write('Describe una conducta moral y califícala en los fundamentos morales (escala 1-5: bajo a alto respaldo).')

description = st.text_area('Descripción de la conducta:')

care = st.slider('Cuidado/Daño (Care/Harm): ¿Involucra compasión o prevención de daño?', 1, 5, 3)
equality = st.slider('Igualdad (Equality): ¿Promueve igualdad o evita discriminación?', 1, 5, 3)
proportionality = st.slider('Proporcionalidad (Proportionality): ¿Se basa en méritos o justicia proporcional?', 1, 5, 3)
loyalty = st.slider('Lealtad (Loyalty): ¿Fortalece lazos grupales o evita traición?', 1, 5, 3)
authority = st.slider('Autoridad (Authority): ¿Respeta jerarquías o tradiciones?', 1, 5, 3)
purity = st.slider('Pureza (Purity): ¿Evita contaminación o promueve santidad?', 1, 5, 3)

if st.button('Registrar Conducta'):
    if description:
        timestamp = datetime.datetime.now().isoformat()
        data = {
            "timestamp": timestamp,
            "description": description,
            "care": care,
            "equality": equality,
            "proportionality": proportionality,
            "loyalty": loyalty,
            "authority": authority,
            "purity": purity
        }
        try:
            response = supabase.table('behaviors').insert(data).execute()
            if response.data:
                st.success('Conducta registrada exitosamente.')
            else:
                st.error('Error al registrar: ' + str(response.error))
        except Exception as e:
            st.error(f'Error al conectar con Supabase: {str(e)}')
    else:
        st.error('Por favor, ingresa una descripción.')

# Sección para admin (visible solo con contraseña correcta)
if is_admin:
    st.subheader('Panel de Administrador')
    if st.button('Ver Registros'):
        try:
            response = supabase.table('behaviors').select('*').execute()
            if response.data:
                df = pd.DataFrame(response.data)
                st.dataframe(df)
            else:
                st.error('Error al cargar registros: ' + str(response.error))
        except Exception as e:
            st.error(f'Error al conectar con Supabase: {str(e)}')

    if st.button('Exportar a CSV'):
        try:
            response = supabase.table('behaviors').select('*').execute()
            if response.data:
                df = pd.DataFrame(response.data)
                csv_path = 'moral_behaviors.csv'
                df.to_csv(csv_path, index=False)
                with open(csv_path, 'rb') as f:
                    st.download_button('Descargar CSV', f, file_name=csv_path)
                os.remove(csv_path)  # Limpia el archivo temporal
            else:
                st.error('Error al exportar: ' + str(response.error))
        except Exception as e:
            st.error(f'Error al conectar con Supabase: {str(e)}')
