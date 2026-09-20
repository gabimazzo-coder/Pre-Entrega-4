### API Data Extractor & Transformer (Python)

Este es un script básico en Python diseñado para realizar peticiones GET a una API pública (JSONPlaceholder), manejar errores en las peticiones HTTP, transformar la respuesta seleccionando atributos específicos y persistir los datos de manera limpia en un archivo local JSON. 

### 🚀 Requisitos Previos

Tener instalado **Python 3.8 o superior** y Git en tu sistema. 
Yo lo corri en Colab

### 🛠️ Instalación y Configuración

python -m venv venv
venv\Scripts\activate


4. **Configurar tus variables de entorno**:
Crear un archivo llamado .env en la raíz del proyecto y define la URL destino de la API: 

API_URL=https://jsonplaceholder.typicode.com/users

### 💻 Ejecución

Para iniciar el proceso de extracción, transformación y guardado, se ejecuta el script principal: 



python main.py


Al finalizar la ejecución,se genera un archivo en la raíz del proyecto llamado data_extracted.json con la información simplificada.


