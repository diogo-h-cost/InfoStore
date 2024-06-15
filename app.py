from flask import Flask, render_template, request, redirect, url_for, flash
from configs.config import db
from entitie.entities import Produtos

# ------------ App ------------

app = Flask(__name__)

# ------------ Import Class Config ------------

app.config.from_object('configs.config.Config')

# ------------ Inicializar banco ------------

db.init_app(app)

# ------------ Execulta c/ App | Cria tabelas ------------

with app.app_context():
    db.create_all()

# ------------ Rotas ------------

@app.route("/", methods=["GET", "POST"])
def principal():
    titulo = "InfoStore - Loja de Informatica"
    return render_template("index.html", title=titulo)

# ------------ Read All ------------

@app.route("/home")
def home():
    titulo = "InfoStore - Estoque"
    return render_template("home.html", title=titulo, produtos=Produtos.query.all())

# ------------ Create ------------

@app.route("/create", methods=["GET", "POST"])
def create():
    titulo = "InfoStore - Adicionar Item"

    prod = request.form.get("produto")
    desc = request.form.get("descricao")
    uni = request.form.get("unidade")

    if request.method == "POST":
        if not prod or not desc or not uni:
            flash("Preencha todos os campos do formulário","error")
        else:
            product = Produtos(prod, desc, uni)
            db.session.add(product)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("create.html", title=titulo)

# ------------ Update ------------

@app.route("/<int:id>/update", methods=["GET", "POST"])
def update(id):
    titulo = "InfoStore - Editar Item"

    product = Produtos.query.filter_by(id=id).first()
    if request.method == "POST":
        prod = request.form["produto"]
        desc = request.form["descricao"]
        uni = request.form["unidade"]

        Produtos.query.filter_by(id=id).update({"prod":prod, "desc":desc, "uni":uni})
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update.html", title=titulo, product=product)

# ------------ Delete ------------

@app.route("/<int:id>/delete", methods=["POST"])
def delete(id):
    product = Produtos.query.filter_by(id=id).first()
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("home"))

# ------------ Conf ------------

if __name__ == "__main__":
    app.run(debug=True)