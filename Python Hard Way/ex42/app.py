from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flash'

@app.route("/hello", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        greet = request.form.get('greet', '').strip()

        if not name or not greet:
            flash("Both fields are required.")
            return render_template("hello_form_laid_out.html", name=name, greet=greet)

        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)

    return render_template("hello_form_laid_out.html", name='', greet='')

if __name__ == "__main__":
    app.run(debug=True)
