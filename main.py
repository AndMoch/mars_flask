from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def tagline():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    prom = [
      "Человечество вырастает из детства.", "Человечеству мала одна планета.",
      "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!",
      "Присоединяйся!"
    ]
    return '</br>'.join(prom)


@app.route("/image_mars")
def image_mars():
    return f"""<!doctype html>
                  <html lang="en">
                    <head>
                      <meta charset="utf-8">
                      <title>Привет, Марс!</title>
                    </head>
                    <body>
                      <h1>Жди нас, Марс!</h1>
                      <img src={url_for('.static', filename='img/mars.jpg')}>
                    </body>
                  </html>"""


@app.route("/promotion_image")
def promotion_image():
    return f"""<!doctype html>
                  <html lang="en">
                    <head>
                      <meta charset="utf-8">
                      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                      <link rel="stylesheet" 
                      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                      integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                      crossorigin="anonymous">
                      <link rel="stylesheet" href={url_for('.static', filename='css/style.css')}>
                      <title>Колонизация</title>
                    </head>
                    <body>
                      <h1>Жди нас, Марс!</h1>
                      <img src={url_for('.static', filename='img/mars.jpg')}>
                      <div class="alert alert-dark" role="alert">
                        Человечество вырастает из детства.
                      </div>
                      <div class="alert alert-success" role="alert">
                        Человечеству мала одна планета.
                      </div>
                      <div class="alert alert-secondary" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                      </div>
                      <div class="alert alert-warning" role="alert">
                        И начнем с Марса!
                      </div>
                      <div class="alert alert-danger" role="alert">
                        Присоединяйся!
                      </div>
                    </body>
                  </html>"""


@app.route("/choice/<planet_name>")
def choice(planet_name):
    return f"""<!doctype html>
                  <html lang="en">
                    <head>
                      <meta charset="utf-8">
                      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                      <link rel="stylesheet" 
                      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                      integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                      crossorigin="anonymous">
                      <title>Варианты выбора</title>
                    </head>
                    <body>
                      <h1>Мое предложение: {planet_name}</h1>
                      <div class="alert alert-light" role="alert">
                        Эта планета близка к Земле;
                      </div>
                      <div class="alert alert-success" role="alert">
                        На ней много необходимых ресурсов
                      </div>
                      <div class="alert alert-secondary" role="alert">
                        На ней есть вода и атмосфера;
                      </div>
                      <div class="alert alert-warning" role="alert">
                        На ней есть небольшое магнитное поле;
                      </div>
                      <div class="alert alert-danger" role="alert">
                        Наконец, она просто красива!
                      </div>
                    </body>
                  </html>"""


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f"""<!doctype html>
                  <html lang="en">
                    <head>
                      <meta charset="utf-8">
                      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                      <link rel="stylesheet" 
                      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                      integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                      crossorigin="anonymous">
                      <title>Варианты выбора</title>
                    </head>
                    <body>
                      <h1>Результаты отбора</h1>
                      <h2>Претендента на участие в миссии {nickname}:</h2>
                      <div class="alert alert-success" role="alert">
                        Поздравляем! Ваш рейтинг после {level} этапа отбора
                      </div>
                      <div class="alert alert-light" role="alert">
                        составляет {rating}!
                      </div>
                      <div class="alert alert-warning" role="alert">
                        Желаем удачи!
                      </div>
                    </body>
                  </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)