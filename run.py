import os
from app.api.v2 import create_app
from app.api.v2.db.db_connection import init_database
config = os.getenv("CONFIG_STAGE") or "default"
app = create_app(config)
init_database()
if __name__ == "__main__":
    app.run(debug=True)
