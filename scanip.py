import requests
import folium
import webbrowser
# Debe instalar pip install requests
# Debe instalar pip install Jinja2
# pip install folium
# Debe instarlar pip install requests folium
def obtener_informacion_ip(public_ip):
    url = f"http://ip-api.com/json/{public_ip}"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos

def crear_mapa(ciudad):
    m = folium.Map(location=[0, 0], zoom_start=2)  # Mapa inicial con un zoom bajo

    # Agrega un marcador en la ubicación de la ciudad
    folium.Marker(
        location=[ciudad['lat'], ciudad['lon']],
        popup=ciudad['city'],
        icon=folium.Icon(icon='cloud')
    ).add_to(m)

    # Guarda el mapa como archivo HTML
    m.save('mapa.html')

if __name__ == "__main__":
    public_ip = input("Ingresa la dirección IP pública que deseas consultar: ")
    informacion = obtener_informacion_ip(public_ip)

    if informacion["status"] == "success":
        print("Información de la IP pública:")
        print(f"IP: {informacion['query']}")
        print(f"País: {informacion['country']}")
        print(f"Región: {informacion['regionName']}")
        print(f"Ciudad: {informacion['city']}")
        print(f"Código Postal: {informacion['zip']}")
        print(f"Proveedor de Internet: {informacion['isp']}")

        # Crea un mapa y guárdalo como HTML
        crear_mapa(informacion)
        print("Mapa generado como 'mapa.html'. Abriendo en el navegador...")
        
        # Abre el mapa en el navegador web predeterminado
        webbrowser.open('mapa.html', new=2)
    else:
        print("No se pudo obtener información para la IP proporcionada.")
