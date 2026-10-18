from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    message = (data.get("message") or "").strip()

    if not name or not email or not message:
        return jsonify({"ok": False, "message": "Please fill in all fields."}), 400

    # Demo behavior: no email is sent or stored yet.
    return jsonify({
        "ok": True,
        "message": f"Thanks, {name}! The demo form works. Connect an email service to receive messages."
    })

if __name__ == "__main__":
    app.run(debug=True)
