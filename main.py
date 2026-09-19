import os
import json
import requests
from dotenv import load_dotenv

# 1. Configuración de Seguridad: Cargar variables de entorno
load_dotenv()
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY") # Listo para usarse si la API lo requiere

def extract_and_transform():
    if not API_URL:
        print("Error: API_URL no configurada en el archivo .env")
        return

    print(f"Iniciando petición GET a: {API_URL}...")
    
    try:
        # 2. Extracción: Realizar la petición HTTP
        response = requests.get(API_URL, timeout=10)
        
        # Manejo de códigos de error HTTP (404, 500, etc.)
        response.raise_for_status() 
        
        data = response.json()
        print("✓ Extracción exitosa.")

        # 3. Transformación Básica: Limpieza de campos innecesarios
        # De cada usuario, solo conservaremos: id, name, username, email y company_name
        cleaned_data = []
        for user in data:
            clean_user = {
                "id": user.get("id"),
                "name": user.get("name"),
                "username": user.get("username"),
                "email": user.get("email"),
                "company_name": user.get("company", {}).get("name") # Campo anidado
            }
            cleaned_data.append(clean_user)
            
        print("✓ Transformación completada (Campos innecesarios eliminados).")

        # 4. Persistencia: Guardar en data_extracted.json
        output_filename = "data_extracted.json"
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(cleaned_data, f, indent=4, ensure_ascii=False)
            
        print(f"✓ Persistencia completada. Archivo guardado como: '{output_filename}'")

    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP ocurrido: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error de conexión: {conn_err}")
    except requests.exceptions.Timeout:
        print("La petición ha superado el tiempo de espera límite.")
    except Exception as err:
        print(f"Ocurrió un error inesperado: {err}")

# Ejecutar el script
if __name__ == "__main__":
    extract_and_transform()

