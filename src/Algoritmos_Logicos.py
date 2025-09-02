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
