from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import json
import sqlite3

app = Flask(__name__, static_folder='.')
CORS(app)

# Configuración de OpenAI (reemplaza con tu API key válida)
OPENAI_API_KEY = "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"

# Rutas para todas las páginas
@app.route('/')
def presentacion():
    return send_from_directory('.', 'presentacion-orbix-optimized.html')

@app.route('/presentacion')
def presentacion_page():
    return send_from_directory('.', 'presentacion-orbix-optimized.html')

@app.route('/orbix-sitio')
def orbix_sitio():
    return send_from_directory('orbix-sitio', 'index.html')

@app.route('/orbix-sitio/')
def orbix_sitio_index():
    return send_from_directory('orbix-sitio', 'index.html')

@app.route('/orbix-sitio/paginas/<path:filename>')
def orbix_paginas(filename):
    return send_from_directory('orbix-sitio/paginas', filename)

@app.route('/orbix-sitio/assets/<path:filename>')
def orbix_assets(filename):
    return send_from_directory('orbix-sitio/assets', filename)

@app.route('/aenki')
def aenki():
    return send_from_directory('.', 'aenki.html')

@app.route('/sentinel')
def sentinel():
    return send_from_directory('.', 'Maqueta Sentinel.html')

@app.route('/portafolio')
def portafolio():
    return send_from_directory('.', 'index-Portafolio.html')

@app.route('/blog')
def blog():
    return send_from_directory('.', 'blog.html')

@app.route('/documentos')
def documentos():
    return send_from_directory('.', 'documentos.html')

@app.route('/contacto-chat')
def contacto_chat():
    return send_from_directory('.', 'index chat y contacto.html')

@app.route('/chat')
def chat():
    return send_from_directory('.', 'index chat y contacto.html')

# SEO Files
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml', mimetype='application/xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory('.', 'robots.txt', mimetype='text/plain')

# Servir archivos estáticos
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

# Inicializar base de datos SQLite
def init_db():
    conn = sqlite3.connect('contactos.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL,
            mensaje TEXT NOT NULL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/contacto', methods=['POST'])
def contacto():
    data = request.json
    nombre = data.get('nombre')
    correo = data.get('correo')
    mensaje = data.get('mensaje')
    # Guardar en la base de datos
    conn = sqlite3.connect('contactos.db')
    c = conn.cursor()
    c.execute('INSERT INTO contactos (nombre, correo, mensaje) VALUES (?, ?, ?)', (nombre, correo, mensaje))
    conn.commit()
    conn.close()
    print(f"Nuevo contacto: {nombre} <{correo}>: {mensaje}")
    return jsonify({'success': True, 'msg': '¡Gracias por contactarnos! Pronto te responderemos.'})

@app.route('/chat', methods=['POST'])
def chat_api():
    data = request.json
    user_message = data.get('mensaje')
    
    print(f"Mensaje recibido: {user_message}")
    
    # Intentar usar OpenAI directamente con requests
    try:
        headers = {
            'Authorization': f'Bearer {OPENAI_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'model': 'gpt-3.5-turbo',
            'messages': [
                {
                    'role': 'system', 
                    'content': 'Eres la IA asistente de Orbix, una empresa innovadora de desarrollo tecnológico. Orbix se especializa en: desarrollo web moderno, aplicaciones móviles, inteligencia artificial, soluciones cloud, experiencias inmersivas, y consultoría digital. Responde de forma profesional, amigable y enfocada en cómo Orbix puede ayudar al usuario con sus proyectos tecnológicos.'
                },
                {
                    'role': 'user', 
                    'content': user_message
                }
            ],
            'max_tokens': 200,
            'temperature': 0.7
        }
        
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers=headers,
            json=payload,
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            respuesta = result['choices'][0]['message']['content'].strip()
            print(f"✅ Respuesta de OpenAI: {respuesta}")
            return jsonify({'respuesta': respuesta})
        else:
            print(f"❌ Error OpenAI: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"❌ Excepción OpenAI: {str(e)}")
    
    # Respuestas locales inteligentes como fallback
    print("🔄 Usando respuestas locales...")
    
    user_lower = user_message.lower()
    
    # Respuestas específicas por palabras clave
    if any(word in user_lower for word in ['hola', 'saludos', 'buenos', 'hi', 'hello']):
        respuesta = '¡Hola! 👋 Soy la IA de Orbix. Estamos especializados en desarrollo web, aplicaciones móviles y soluciones tecnológicas innovadoras. ¿En qué proyecto puedo ayudarte?'
    elif any(word in user_lower for word in ['servicios', 'que hacen', 'especialidades']):
        respuesta = 'Orbix ofrece: 🌐 Desarrollo Web, 📱 Apps Móviles, 🤖 Inteligencia Artificial, ☁️ Soluciones Cloud, 🎮 Experiencias Inmersivas, y 💼 Consultoría Digital.'
    elif any(word in user_lower for word in ['precios', 'costo', 'cuanto', 'cotización']):
        respuesta = '💰 Nuestros precios son competitivos y se adaptan a cada proyecto. Te recomiendo contactar a nuestro equipo para una cotización personalizada.'
    elif any(word in user_lower for word in ['web', 'página', 'sitio', 'website']):
        respuesta = '🌐 ¡Excelente! El desarrollo web es una de nuestras especialidades. Creamos sitios modernos, responsivos y optimizados. ¿Tienes algún proyecto web en mente?'
    elif any(word in user_lower for word in ['app', 'aplicación', 'móvil', 'mobile']):
        respuesta = '📱 Las aplicaciones móviles son el futuro. En Orbix desarrollamos apps nativas e híbridas para iOS y Android. ¿Qué tipo de app necesitas?'
    elif any(word in user_lower for word in ['ia', 'inteligencia', 'artificial', 'ai', 'bot']):
        respuesta = '🤖 ¡La IA es fascinante! Implementamos soluciones de inteligencia artificial para automatizar procesos y mejorar la experiencia del usuario. ¿Te interesa integrar IA en tu proyecto?'
    elif any(word in user_lower for word in ['portafolio', 'trabajos', 'proyectos']):
        respuesta = '🎯 Te invito a visitar nuestra sección de Portafolio donde podrás ver proyectos como Eternityzone.info y CoopeAvatar City.'
    elif any(word in user_lower for word in ['tecnologias', 'lenguajes', 'herramientas']):
        respuesta = '⚡ Trabajamos con: Python, JavaScript, React, Flask, AI/ML, Unity, Blender, y las últimas tecnologías web.'
    elif any(word in user_lower for word in ['tiempo', 'duración', 'cuando']):
        respuesta = '⏱️ Los tiempos de desarrollo varían según el proyecto. Un sitio web básico puede tomar 2-4 semanas, mientras que aplicaciones complejas pueden requerir 2-6 meses.'
    else:
        respuesta = '🤖 ¡Hola! Soy la IA de Orbix. Puedo ayudarte con información sobre desarrollo web, apps móviles, inteligencia artificial, y nuestros servicios tecnológicos. ¿En qué proyecto estás pensando?'
    
    print(f"📝 Respuesta local: {respuesta}")
    return jsonify({'respuesta': respuesta})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)