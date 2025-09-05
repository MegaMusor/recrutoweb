from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    # Получаем параметры из GET-запроса
    name = request.args.get('name', 'Recruto')
    message = request.args.get('message', 'Давай дружить')

    # Формируем ответ
    response = f"Hello {name}! {message}!"
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)