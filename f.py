from flask import Flask, request, jsonify, send_file
import qrcode
import io



app = Flask(__name__)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.get_json()

    # Перевірка, чи передано поле "text"
    if not data or 'text' not in data:
        return jsonify({"error": "Поле 'text' обов'язкове"}), 400

    text = data['text']
    
    # Генерація QR-коду
    qr = qrcode.make(text)
    img_io = io.BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)

    # Повернення QR-коду як зображення
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)