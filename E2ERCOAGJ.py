try:
    import requests
except ImportError:
    os.system("pip install requests")
    print("Installing requests...")
    print("Ejecuta de nuevo el programa")
    exit()


try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    os.system("pip install Beautifulsoup4")
    print("Installing BeautifulSoup...")
    print("Ejecuta de nuevo el programa")
    exit()

try:
    import webbrowser
except ImportError:
    os.system("pip install webbrowser")
    print("Installing webbbrowser...")
    print("Ejecuta de nuevo el programa")
    exit()

"""Erick Rosales Camarillo, Olaf Aliber Garcia Juarez
El script nos pide el rango de las paginas que deseas buscar,
despues pide que ingreses las siglas de una facultad,
y de acuerdo al rango de paginas busca si se menciona
dicha facultad y se nos abrira en el navegador las paginas"""

print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango, finRango = finRango, inicioRango
for i in range(inicioRango, finRango, 1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get(url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content, "html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content, "html.parser")
                parrafos = soup2.select("p")
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo", url2)
                        webbrowser.open(url2)
                        break
