from flask import Flask, url_for, render_template

app = Flask(__name__, static_folder="static", static_url_path="/static")


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/<title>')
def main_custom_title(title):
    return render_template("base.html", title=title)


@app.route('/index')
def tagline():
    return "И на Марсе будут яблони цвести!"


@app.route('/index/<title>')
def index_custom_title(title):
    return render_template("base.html", title=title)


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


@app.route("/carousel")
def carousel():
    return f"""<!doctype html>
                      <html lang="en">
                        <head>
                          <meta charset="utf-8">
                          <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                          <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                          <title>Пейзажи Марса</title>
                        </head>
                        <body>
                          <h1>Пейзажи Марса</h1>
                            <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                              <div class="carousel-inner">
                                <div class="carousel-item active">
                                  <img class="d-block w-100" src="{url_for('.static', filename='img/1.jpg')}" alt="First slide">
                                </div>
                                <div class="carousel-item">
                                  <img class="d-block w-100" src="{url_for('.static', filename='img/2.jpg')}" alt="Second slide">
                                </div>
                                <div class="carousel-item">
                                  <img class="d-block w-100" src="{url_for('.static', filename='img/3.jpg')}" alt="Third slide">
                                </div>
                              </div>
                              <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="sr-only"></span>
                              </a>
                              <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="sr-only"></span>
                              </a>
                            </div>
                            <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
                    </body>
                  </html>"""


@app.route("/training/<prof>")
def training(prof):
    return render_template("training.html", prof=prof)


@app.route("/list_prof/<list>")
def list_prof(list):
    return render_template("job_list.html", list=list)


@app.route("/answer")
def answer():
    param = {'title': "Анкета",
             'surname': "Watny",
             'name': "Mark",
             'education': "выше среднего",
             'profession': "штурман марсохода",
             'sex': "male",
             'motivation': "Всегда мечтал застрять на Марсе!",
             'ready': "True"}
    return render_template("auto_answer.html", **param)


@app.route("/auto_answer")
def auto_answer():
    param = {'title': "Анкета",
             'surname': "Watny",
             'name': "Mark",
             'education': "выше среднего",
             'profession': "штурман марсохода",
             'sex': "male",
             'motivation': "Всегда мечтал застрять на Марсе!",
             'ready': "True"}
    return render_template("auto_answer.html", **param)


@app.route("/distribution")
def distribution():
    members = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тэдди Сандерс', 'Шон Бин']
    return render_template("on_the_board.html", members=members)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)