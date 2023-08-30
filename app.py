from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json  # Получение данных в формате JSON

    # Вывод данных в консоль для отображения
    print("Пришедшие данные:", data)

    # Здесь обработайте данные по вашим требованиям

    response = {'message': 'Данные успешно приняты'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
