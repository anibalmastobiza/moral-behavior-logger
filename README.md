Moral Behavior Logger
Esta es una demo de una aplicación web simple construida con Streamlit para registrar conductas morales basadas en la Teoría de los Fundamentos Morales (Moral Foundations Theory) de Jonathan Haidt. Permite a los usuarios describir una conducta, calificarla en seis fundamentos morales (escala 1-5) y almacenar los datos en una base de datos Supabase para análisis posterior (datos persistentes).
Funcionalidades

Registro de descripciones de conductas morales (accesible para todos).
Calificación en fundamentos: Care/Harm, Equality, Proportionality, Loyalty, Authority, Purity.
Visualización de registros (solo para administradores con contraseña).
Exportación a CSV para análisis (solo para administradores con contraseña).

Instalación y Ejecución Local

Clona el repositorio: git clone https://github.com/tu-usuario/moral-behavior-logger.git
Instala dependencias: pip install -r requirements.txt
Configura variables de entorno: Crea un archivo .env con SUPABASE_URL=tu-url y SUPABASE_KEY=tu-key, luego carga con dotenv si es necesario (o ejecútalo manualmente).
Ejecuta la app: streamlit run streamlit_app.py
Abre en tu navegador (generalmente http://localhost:8501).

Despliegue en Streamlit Community Cloud

Ve a share.streamlit.io.
Inicia sesión con GitHub y selecciona este repositorio.
Configura: Branch "main", Archivo "streamlit_app.py".
En "Advanced settings" > "Secrets", agrega:SUPABASE_URL = "https://mvuwuphcfkdinxtvblfy.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im12dXd1cGhjZmtkaW54dHZibGZ5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTQ2OTkzMDksImV4cCI6MjA3MDI3NTMwOX0.LbZoA0g9FET3U7zVC7AxccxWyehD9a7de7jfyHtR5so"


Haz clic en "Deploy". Obtendrás un enlace público para ver la app (e.g., https://tu-app.streamlit.app).
Opcional: Agrega el enlace aquí tras desplegar: [Insertar enlace].

Ejecución en GitHub Codespaces

Abre el repo en Codespaces (botón "Code" > "Open with Codespaces").
Espera la configuración automática (via devcontainer.json).
Configura variables de entorno en Codespaces (en terminal: export SUPABASE_URL=https://mvuwuphcfkdinxtvblfy.supabase.co y export SUPABASE_KEY=tu-key).
En la terminal: streamlit run streamlit_app.py
Abre el puerto 8501 en el navegador (ve a la pestaña Ports).

Análisis de Datos
Los datos se almacenan en Supabase (persisten). Exporta a CSV desde la app (solo admin) y analiza con Python:
import pandas as pd
df = pd.read_csv('moral_behaviors.csv')
print(df['care'].mean())  # Ejemplo: promedio de 'Care'

Notas

Datos persistentes vía Supabase (plan gratuito). Configura las credenciales como variables de entorno.
La funcionalidad de "Ver Registros" y "Exportar a CSV" está protegida por una contraseña de administrador (definida en el código).
Basado en MFQ-2; consulta referencias para validez: Moral Foundations Questionnaire.

Licencia: MIT
