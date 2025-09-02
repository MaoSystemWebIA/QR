"""

from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Función auxiliar para medir texto - DEFINIR PRIMERO
def text_width(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]

# Configuración de imagen
width, height = 600, 400
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)

# Colores
blue = (36, 102, 252)
black = (0, 0, 0)

# Función para rombos
def draw_diamond(x, y, size, color):
    half = size // 2
    points = [(x, y - half), (x + half, y), (x, y + half), (x - half, y)]
    draw.polygon(points, fill=color, outline="black")

# Rombos más juntos
center_x = width // 2
start_y = 80
spacing = 20
sizes = [40, 50, 60]

for i, size in enumerate(sizes):
    y = start_y + i * spacing
    draw_diamond(center_x, y, size, blue)

# Fuentes
try:
    font_big = ImageFont.truetype("arial.ttf", 42)
    font_bold = ImageFont.truetype("arialbd.ttf", 20)
except IOError:
    font_big = ImageFont.load_default()
    font_bold = ImageFont.load_default()

# Texto principal
text_parts = ["MaoSystemWebIA"]
text_y = start_y + len(sizes) * spacing - 10

# Calcular ancho del texto
part_widths = [text_width(draw, part, font_big) for part in text_parts]
total_width = sum(part_widths) - 20  # Kerning negativo
start_x = (width - total_width) // 2

# Dibujar texto
x_offset = start_x
for i, part in enumerate(text_parts):
    color = blue if i == 1 else black
    draw.text((x_offset, text_y), part, fill=color, font=font_big)
    x_offset += part_widths[i] - (10 if i < len(text_parts)-1 else 0)

# Ícono y URL
globe_icon = Image.open(BytesIO(requests.get("https://cdn-icons-png.flaticon.com/512/84/84380.png").content))
globe_icon = globe_icon.resize((24, 24)).convert("RGBA")

url_text = "maosystemwebia.github.io/Landin/"
url_y = text_y + 50
url_width = text_width(draw, url_text, font_bold)
url_x = (width - url_width - 30) // 2

img.paste(globe_icon, (url_x, url_y - 2), globe_icon)
draw.text((url_x + 30, url_y), url_text, fill=blue, font=font_bold)

img.save("maosystemwebia_compacto.png")
print("✅ Logo compacto guardado correctamente")


Programa que cdados tres números
encuentra cuál es el mayor de los tres.

a = int(input("Ingrese un número uno: "))
b = int(input("Ingrese un número dos: "))
c = int(input("Ingrese número tres: "))

mayor = None

if mayor is None or a > mayor:
    mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c
print(f"El número mayor es: {mayor}")


a="artefacto"
n=0
letras=len(a)
while n<=letras-1:
      print(a[n])
      n+=1

#varaible del texto

cadena=""hola muchachos se compro. Otras cosas como muebles."""


"""
#numero veces 
veces=0
letra="o"
punto="."

n=0
contando=len(cadena)
while n<=contando-1:
    if cadena[n]==letra or cadena==[n]:
       veces+=1
    n+=1

print("veces que aparece la 'o' , veces que aparece el '.'")
       

n=0

palabra=input("ingrese palabra ")


vocales="aeiou"
contador_vocales=0


while n<=len(palabra)-1:
    if palabra[n] in vocales:
        contador_vocales+=1
    n+=1
       
print("las vocales que tiene la palabra son:", contador_vocales)


lista=[2,5,90,23,45,87,54,11,38]

elemento=2

for l in range(len( lista)):
    if lista[l]==elemento:
        print(f"el elemento {lista[l]} está en la ppsición: {l}")
        print("El",elemento, "esta en la posición ", l+1)


tablas de multiplicar:


p=(int(input("Ingrese un número:")))
for n in range(1,11):   
    mult=n*p
    print(p,"*", n, "=" , p * n )
    #diferencia de print y de formatos el recomendado es:
    print(f"{p} * {n} = {p * n}")

bucle infinito
ctrl+c


                       ejercicio de simulación:


Descripción detallada:

1. Selección de opciones:
Los jugadores se enfrentan y, al mismo tiempo, cada uno
elige una de las tres opciones:

Piedra: Se representa con el puño cerrado.
Papel: Se representa con la mano extendida, 
Tijera: dos dedos con la mano abierta en forma de tijera 



4. Desarrollo del juego:
El juego puede continuar por un número determinado de
rondas o hasta que un jugador alcance un cierto número de victorias.

El concurso de piedra papel o tijera todas las apuestas que se
hagan tienes un minuto para ganarle a su contrincate.
el que gana 100 puntos y el que pierde los pierde todos.
















import time
import random

puntos=0

inicio=time.time()

while True:
       print("*******CONCURSO MATEMATICO******")
       print("Haz todas las opciones que puedas/n"
            "Tienes 10 segundos de tiempo"
            "*********************************")
       print("Estamos jugando y el tiempo se acaba en este instante")
       n1=random.randint(1,9)
       n2=random.randint(1,9)
       op=random.choice(["+","*"])
       final=time.time()
       
       if op=="+":
          res=n1+n2
          respuesta=(int(input(str(n1)+""+op+""+str(n2)+"=")))
       if respuesta==res:
          puntos+=1       
          print(n1,op,n2,"correcto tienes",puntos, end="")
       

          
       elif op=="*":
            res=n1*n
            respuesta=(int(input(str(n1)+""+op+""+str(n2)+"=")))
            print(n1,op,n2,end="")
       if respuesta==res:
          puntos+=1       
          print(n1,op,n2,"correcto tienes",puntos, end="")

       tiempo_final=inicio-final

       if final-inicio>=2:
          print("se acabo el tiempo.")
          break
       
      
print("fin del juego",final,puntos)


}
Sistema de Gestión de Estudiantes
Desarrolla un programa en Python que permita gestionar información de estudiantes.
El sistema debe:

Requisitos:

1. Almacenar información de estudiantes (nombre, edad, calificaciones)
2. Calcular el promedio de calificaciones de cada estudiante
3. Determinar si un estudiante está aprobado (promedio ≥ 6.0)
4. Mostrar estadísticas generales del grupo
5. Buscar estudiantes por nombre

6.  Estructuras de datos a utilizar:
7.  Listas para almacenar múltiples estudiantes
8.  Diccionarios para representar cada estudiante
9.  Tuplas para datos inmutables (como rangos de calificación)
10. Sets para manejar materias únicas





promedio=0


while True:
    try:
        print("Ingresa los siguientes datos:")
        nombre = input("Ingresa nombre: ")
        edad = int(input("Ingresa edad: "))
        calificacion = float(input("Ingresa calificación: "))
        
        print(f"\nDatos ingresados:")
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"Calificación: {calificacion}")
        break  # ← IMPORTANTE: Salir del ciclo cuando todo esté correcto
        
    except ValueError:
        print("Error: Debes ingresar números válidos para edad y calificación\n")

programa dónde jugamos a que pase el tiempo .





import time
import random


#programa donde jugamos a que pase e tiempo.


print("******* CONCURSO MATEMÁTICO *********")
print("                                     ")
print("                                     ")
print(" Haz todas las operaciones que puedas")
print("     Tienes 10 segundos de tiempo    ")
print()
print("*************************************")


pulsa=input("Para empezar pulsa 'Enter':")
print()


inicio=time.time() 



while True:      
      
       a=random.randint(1,9)
       b=random.randint(1,9)
       op=random.choice(["+","-","*","/"])  
              
       if op=="+":
          resultado=a+b
          respuestas=(int(input(str(a) + "" + op + ""+ str(b) + "")))
          print(a,op,b, end=" ")
          
          

       elif  op=="-":
             resultado=a-b
             respuestas=(int(input(str(a) + "" + op + ""+ str(b) + "")))
             print(a,op,b, end="")
                   


       elif  op=="*":
             resultado=a*b
             respuestas=(int(input(str(a) + "" + op + ""+ str(b) + "")))
             print(a,op,b, end="")   
          
          

       elif op=="/":
            resultado=a/b
            respuestas=(int(input(str(a) + "" + op + ""+ str(b) + "")))
            print(a,op,b, end="")

       respuestas=(int(input("=")))

       if respuesta==resultado:
          puntos+=1
          print("Correcto. Tienes ",puntos,"puntos")

       else:
           print("Correcto , Tienes", puntos, "puntos")
              
       final=time.time()

       if final-inicio>=3:

          print("Se acabo el tiempo.")

          break
              


print(f"se acabo el tiempo {final-inicio},")



import time

print("MEMORIZA LOS COLORES:")

print("\n⏰ Tienes 5 segundos para memorizar...")

#  Medir tiempo de memorización REAL
inicio = time.time()  # Iniciar cronómetro
time.sleep(5)         # 5 segundos para memorizar
final = time.time()   # Finalizar cronómetro

# Mensajes después de memorizar
print("... Preparado ...")
time.sleep(0.5)
print("... Listo .......")
time.sleep(0.5)
print(".....Ya .........")

# Calcular tiempo transcurrido
tiempo = final - inicio

# f-string correcta
print(f"El tiempo de memorización fue: {tiempo:.3f} segundos")



import time

print("\n⏰ Tienes 1 min: segundos para memorizar...")
print("\n⏰azul","\n⏰amarillo","\n⏰griz","\n⏰negro","\n⏰cafe")
inicio=time.time()
time.sleep(9.5)
print()

while True:
       
       final=time.time()
       tiempo=final-inicio
       break

print(f"el tiempo transcurrido:{tiempo:.2f} segundos")


import time

inicio=time.time()

print("tienes 3 segundos para recordarlo:")
colores_recordado=[]
colores=["amarillo","azul","griz","rosado"]

for c in colores:       
       time.sleep(0.3)       
       print(c)
       final=time.time()   

       
       
color=input("ingrese colores: ")       
colores_recordado.append(color)
print("colores recordados",colores_recordado)

"""
import qrcode
from PIL import Image, ImageDraw, ImageFont
import argparse
import os

def crear_logo_hamburguesa(tamanio):
    """Crear un logo simple de hamburguesa para el QR"""
    img = Image.new('RGB', (tamanio, tamanio), color='white')
    draw = ImageDraw.Draw(img)
    
    # Dibujar una hamburguesa simple
    margen = tamanio // 4
    
    # Pan superior (círculo amarillo)
    draw.ellipse([margen, margen, tamanio-margen, tamanio-margen], fill='#F9D423', outline='#D4A017')
    
    # Carne (círculo marrón)
    draw.ellipse([margen+5, tamanio//2-5, tamanio-margen-5, tamanio//2+15], fill='#8B4513', outline='#654321')
    
    # Lechuga (círculo verde)
    draw.ellipse([margen+10, tamanio//2-15, tamanio-margen-10, tamanio//2+5], fill='#32CD32', outline='#228B22')
    
    return img

def crear_qr_menu_hamburguesas(nombre_restaurante, enlace_menu, nombre_archivo):
    """Crear QR para menú digital de hamburguesas"""
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=12,
        border=4,
    )
    
    qr.add_data(enlace_menu)
    qr.make(fit=True)
    
    # Crear imagen con colores temáticos
    img = qr.make_image(fill_color="#8B4513", back_color="#FFFDD0")
    img = img.convert('RGB')
    
    # Añadir logo de hamburguesa en el centro
    logo = crear_logo_hamburguesa(60)
    pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
    img.paste(logo, pos)
    
    # Añadir texto descriptivo
    ancho, alto = img.size
    nueva_img = Image.new('RGB', (ancho, alto + 60), color='white')
    nueva_img.paste(img, (0, 0))
    
    draw = ImageDraw.Draw(nueva_img)
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except:
        font = ImageFont.load_default()
    
    texto = f"Menú {nombre_restaurante}"
    texto_ancho = draw.textlength(texto, font=font)
    draw.text(((ancho - texto_ancho) / 2, alto + 15), texto, fill="#8B4513", font=font)
    
    texto_scan = "Escanea con tu cámara"
    texto_scan_ancho = draw.textlength(texto_scan, font=font)
    draw.text(((ancho - texto_scan_ancho) / 2, alto + 40), texto_scan, fill="black", font=font)
    
    nueva_img.save(nombre_archivo, format='PNG')
    print(f"✅ QR menú creado: {nombre_archivo}")
    print(f"📁 Archivo guardado en: {os.path.abspath(nombre_archivo)}")
    
    return nueva_img

def crear_qr_promocion(nombre_restaurante, texto_promocion, nombre_archivo):
    """Crear QR para promociones especiales - VERSIÓN CORREGIDA"""
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=12,
        border=4,
    )
    
    qr.add_data(texto_promocion)
    qr.make(fit=True)
    
    # Colores llamativos para promociones
    img = qr.make_image(fill_color="#FF4500", back_color="#FFFFE0")
    img = img.convert('RGB')
    
    # Añadir texto
    ancho, alto = img.size
    nueva_img = Image.new('RGB', (ancho, alto + 80), color='white')
    nueva_img.paste(img, (0, 0))
    
    draw = ImageDraw.Draw(nueva_img)
    try:
        font_titulo = ImageFont.truetype("arial.ttf", 20)
        font_texto = ImageFont.truetype("arial.ttf", 14)
    except:
        font_titulo = ImageFont.load_default()
        font_texto = ImageFont.load_default()
    
    # Título
    titulo = f"🎉 Oferta {nombre_restaurante}"
    titulo_ancho = draw.textlength(titulo, font=font_titulo)
    draw.text(((ancho - titulo_ancho) / 2, alto + 10), titulo, fill="#FF4500", font=font_titulo)
    
    # Instrucción
    instruccion = "Escanea para ver la promoción"
    instruccion_ancho = draw.textlength(instruccion, font=font_texto)
    draw.text(((ancho - instruccion_ancho) / 2, alto + 50), instruccion, fill="black", font=font_texto)
    
    # ✅ LÍNEA CRÍTICA: Guardar como IMAGEN PNG
    nueva_img.save(nombre_archivo, format='PNG')
    
    print(f"✅ QR promoción creado: {nombre_archivo}")
    print(f"📏 Tamaño del archivo: {os.path.getsize(nombre_archivo)} bytes")
    
    return nueva_img

def main():
    """Función principal"""
    parser = argparse.ArgumentParser(description='Generador de QR para Hamburgueserías')
    parser.add_argument('--mi_hamburguesas', '-n', required=True, help='Nombre de tu hamburguesería')
    parser.add_argument('--menu', '-m', help='Enlace al menú digital (opcional)')
    
    args = parser.parse_args()
    
    # Crear directorio de salida
    os.makedirs("qrs_hamburgueseria", exist_ok=True)
    
    nombre_archivo_base = args.mi_hamburguesas.lower().replace(' ', '_')
    
    # Crear QR del menú si se proporciona enlace
    if args.menu:
        qr_menu = crear_qr_menu_hamburguesas(
            args.mi_hamburguesas, 
            args.menu, 
            f"qrs_hamburgueseria/menu_{nombre_archivo_base}.png"
        )
    else:
        print("ℹ️  No se proporcionó enlace de menú, creando solo QR de promoción")
    
    # Crear QR de promoción (siempre se crea)
    qr_promocion = crear_qr_promocion(
        args.mi_hamburguesas,
        "¡Disfruta de nuestras hamburguesas artesanales! Visítanos pronto.",
        f"qrs_hamburgueseria/promo_{nombre_archivo_base}.png"
    )
    
    # Mostrar mensaje de éxito
    print("\n" + "🎉" * 20)
    print("✅ ¡QRs GENERADOS EXITOSAMENTE!")
    print("🎉" * 20)
    print(f"📋 Hamburguesería: {args.mi_hamburguesas}")
    print(f"📁 Carpeta de guardado: {os.path.abspath('qrs_hamburgueseria')}")
    print(f"🔍 Para ver los QR: Abre los archivos .png en la carpeta")
    
    # Verificar que los archivos son imágenes reales
    try:
        ruta_promo = f"qrs_hamburgueseria/promo_{nombre_archivo_base}.png"
        tamaño = os.path.getsize(ruta_promo)
        print(f"📏 Tamaño del QR de promoción: {tamaño} bytes")
        
        if tamaño > 1000:  # Si tiene más de 1KB, es una imagen real
            print("✅ El archivo es una imagen PNG válida")
            # Abrir la imagen
            img = Image.open(ruta_promo)
            img.show()
        else:
            print("❌ El archivo es demasiado pequeño, puede estar corrupto")
            
    except Exception as e:
        print(f"❌ Error al verificar el archivo: {e}")

if __name__ == "__main__":
    main()
