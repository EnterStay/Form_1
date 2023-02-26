from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Форма для участия в суперсекретной миссии</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email"
                                     aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="name" class="form-control"
                                     id="name" placeholder="Введите имя" name="name">
                                     <input type="surname" class="form-control"
                                     id="surname" placeholder="Введите фамилию" name="surname">
                                    <div class="form-group">
                                        <label for="classSelect">Ваше образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Специальное</option>
                                          <option>Профессиональное</option>
                                          <option>Я уже смешарик</option>
                                        </select>
                                     </div>
                                     <p>Кем вы работали?</p>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="pilot" name="pilot">
                                        <label class="form-check-label" for="pilot">Пилот</label>
                                    </div>
                                    <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="engine" name="engine">
                                        <label class="form-check-label" for="engine">Инженер</label>
                                    </div>
                                    <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="healer" name="healer">
                                        <label class="form-check-label" for="healer">Врач</label>
                                    </div>
                                    <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="meteo" name="meteo">
                                        <label class="form-check-label" for="meteo">Метеоролог</label>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему решили принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['pilot'])
        print(request.form['engine'])
        print(request.form['healer'])
        print(request.form['meteo'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
