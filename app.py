from flask import Flask, render_template, request, redirect

app = Flask(__name__)
employees = []

@app.route("/")
def home():
    return render_template("index.html", employees=employees)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    emp_id = request.form["emp_id"]
    employees.append({"name": name, "id": emp_id})
    return redirect("/")

@app.route("/health")
def health():
    return {"status": "UP"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)