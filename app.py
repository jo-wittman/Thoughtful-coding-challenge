from flask import Flask, render_template_string, request
from package_sorter import sort

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Package Sorter</title>
<h2>Package Sorter</h2>
<form method="post">
  Width (cm): <input type="number" name="width" required><br>
  Height (cm): <input type="number" name="height" required><br>
  Length (cm): <input type="number" name="length" required><br>
  Mass (kg): <input type="number" name="mass" required><br>
  <input type="submit" value="Sort">
</form>
{% if result %}
  <h3>Result: {{ result }}</h3>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        width = int(request.form["width"])
        height = int(request.form["height"])
        length = int(request.form["length"])
        mass = int(request.form["mass"])
        result = sort(width, height, length, mass)
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81) 