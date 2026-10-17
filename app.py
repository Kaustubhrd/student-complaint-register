import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

commit = os.getenv("RENDER_GIT_COMMIT", "local")[:7]

complaints = []


@app.route("/")
def home():
    return render_template("index.html", complaints=complaints, commit=commit)


@app.route("/add", methods=["POST"])
def add_complaint():
    name = request.form.get("name", "").strip()
    complaint = request.form.get("complaint", "").strip()
    category = request.form.get("category", "").strip()

    if not name or not complaint or not category:
        return render_template(
            "error.html",
            message="All fields are required"
        ), 400

    complaints.append({
        "name": name,
        "complaint": complaint,
        "category": category,
        "status": "Pending"
    })

    return redirect("/")


@app.route("/api/complaints")
def api_complaints():
    return complaints


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
