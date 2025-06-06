# import os
# from app import app, db

# with app.app_context():
#     db.create_all()   # ✅ This ensures tables are created on startup

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host="0.0.0.0", port=port)


import os
from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()   # Ensure tables are created at startup

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
