# app.py
from flask import Flask, render_template, request
from foods import foods

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recommended = []
    if request.method == "POST":
        category = request.form.get("category")
        ingredient = request.form.get("ingredient", "").strip()

        # 음식 필터링: 카테고리 일치 + 재료 포함 여부
        for food in foods:
            if (category == "전체" or food["category"] == category) and \
               (ingredient == "" or ingredient in food["ingredients"]):
                recommended.append(food)

    return render_template("index.html", foods=recommended)

if __name__ == "__main__":
    app.run(debug=True)
