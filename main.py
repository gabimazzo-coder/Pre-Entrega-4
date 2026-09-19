import os
import json
import requests
from dotenv import load_dotenv

# 1. Inicialización y Configuración de Seguridad
load_dotenv()
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY") # Listo para usar en headers si tu API lo requiere

def main():
    if not API_URL:
        print("❌ Error: API_URL no está configurada en el archivo .env")
        return

    print(f"🚀 Iniciando extracción desde: {API_URL}...")

    # 2. Extracción (Petición GET con control de errores)
    try:
        # En APIs con llave usarías: headers={"Authorization": f"Bearer {API_KEY}"}
        response = requests.get(API_URL, timeout=10)
        
        # Lanza una excepción si el código de estado es un error (404, 500, etc.)
        response.raise_for_status() 
        
        raw_data = response.json()
        print("✅ Datos extraídos correctamente.")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ Error HTTP ocurrido: {http_err}")
        return
    except requests.exceptions.RequestException as err:
        print(f"❌ Error de conexión: {err}")
        return
    except ValueError:
        print("❌ Error: La respuesta de la API no contiene un JSON válido.")
        return

    # 3. Transformación Básica
    # Filtramos la estructura para conservar solo id, nombre y email de los usuarios
    cleaned_data = []
    for item in raw_data:
        cleaned_item = {
            "id": item.get("id"),
            "name": item.get("name"),
            "email": item.get("email")
        }
        cleaned_data.append(cleaned_item)
    
    print(f"🧹 Transformación completada. Registros procesados: {len(cleaned_data)}")

    # 4. Persistencia
    output_filename = "data_extracted.json"
    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(cleaned_data, f, indent=4, ensure_ascii=False)
        print(f"💾 Datos guardados exitosamente en '{output_filename}'.")
    except IOError as e:
        print(f"❌ Error al guardar el archivo: {e}")

if __name__ == "__main__":
    main()
