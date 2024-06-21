from flask import Flask

# __name__ = "__main__"
app = Flask(__name__)

# criando uma rota
@app.route("/")

# oque será executado quando alguém acessar a rota
def hello_world():
  return "Hello, World!"

@app.route("/about")
def about():
  return "About page"

# executando a rota
if __name__ == "__main__": # isso é para garantir, que só quando a gente execute ele de forma manual, vamos subir o servidor dessa forma
  app.run(debug=True)

