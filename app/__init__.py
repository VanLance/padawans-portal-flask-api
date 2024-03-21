from flask import Flask

app = Flask(__name__)

from resources.post import bp as post_bp
app.register_blueprint(post_bp)
from resources.user import bp as user_bp
app.register_blueprint(user_bp)

from resources.post import routes
from resources.user import routes
