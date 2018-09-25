# Standard library imports
import os

# Local application imports
from app.api.v1 import create_app
config = os.getenv("CONFIG_STAGE") or "default"
app=create_app(config)

if __name__ == '__main__':
    app.run(debug=True)
