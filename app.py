
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Fictional demo data only.
# These are display labels, not usable payment credentials.
PAYMENT_METHODS = [
    {
        "id": "pm_demo_1",
        "brand": "Visa",
        "last4": "4242",
        "label": "Everyday card",
        "recommended": True,
    },
    {
        "id": "pm_demo_2",
        "brand": "Mastercard",
        "last4": "8210",
        "label": "Backup card",
        "recommended": False,
    },
    {
        "id": "pm_demo_3",
        "brand": "Visa",
        "last4": "1005",
        "label": "Online shopping",
        "recommended": False,
    },
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        payment_methods=PAYMENT_METHODS,
    )


@app.route("/api/checkout", methods=["POST"])
def checkout():
    data = request.get_json(silent=True) or {}
    selected_id = data.get("payment_method_id")

    # Only accept IDs belonging to our fictional demo list.
    selected = next(
        (method for method in PAYMENT_METHODS
         if method["id"] == selected_id),
        None,
    )

    if selected is None:
        return jsonify({
            "success": False,
            "message": "Please select a valid demo payment method.",
        }), 400

    # This simulates checkout; it does not charge a card.
    return jsonify({
        "success": True,
        "message": (
            f"Demo checkout successful using "
            f"{selected['brand']} ending in {selected['last4']}. "
            "No payment was processed."
        ),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)