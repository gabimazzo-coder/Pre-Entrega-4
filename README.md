### API Data Extractor & Transformer (Python)

Este es un script básico en Python diseñado para realizar peticiones GET a una API pública (JSONPlaceholder), manejar errores en las peticiones HTTP, transformar la respuesta seleccionando atributos específicos y persistir los datos de manera limpia en un archivo local JSON. 

### 🚀 Requisitos Previos

Asegúrate de tener instalado **Python 3.8 o superior** y Git en tu sistema. 

### 🛠️ Instalación y Configuración

1. **Clona el repositorio** en tu máquina local: 

bash

git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio

Usa el código con precaución.
2. **Crea y activa un entorno virtual** (opcional pero recomendado): 

bash

# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate

Usa el código con precaución.
3. **Instala las dependencias** requeridas: 

bash

pip install -r requirements.txt

Usa el código con precaución.
4. **Configura tus variables de entorno**:
Duplica o crea un archivo llamado .env en la raíz del proyecto y define la URL destino de la API: 

env

API_URL=https://jsonplaceholder.typicode.com/users
API_KEY=tu_credencial_aqui

Usa el código con precaución.

### 💻 Ejecución

Para iniciar el proceso de extracción, transformación y guardado, ejecuta el script principal: 

bash

python main.py

Usa el código con precaución.

Al finalizar la ejecución, verás un archivo generado en la raíz del proyecto llamado data_extracted.json con la información simplificada.


