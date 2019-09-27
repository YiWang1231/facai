from app import create_app
from config import Config
from app.model import UserPositons

app = create_app(Config)


@app.shell_context_processor
def make_shell_context():
    return {'position': UserPositons}