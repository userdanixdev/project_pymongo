from flask import Flask
import sys
from pathlib import Path

# adiciona a raiz do projeto no sys.path para permitir `import src...`
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from src.database.connection import db
from src.routes.carros import carros_pb
from src.routes.posts import posts_pb

app = Flask(__name__)
app.register_blueprint(carros_pb)  # Necessário registrar os blueprints
app.register_blueprint(posts_pb)   # Necessário registrar os blueprints

@app.route("/")
def home():
    return {"mensagem":"API MongoDB com Flask funcionando",
    "rotas": [
                "/posts",
                "/posts/<id>",
                "/carros",
                "/carros/<id>"
            ]}

if __name__ == "__main__":
    app.run(debug=True)
