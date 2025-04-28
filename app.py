from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config
from views.admin import admin_bp
from views.gayrimenkul import gayrimenkul_bp
from models.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONFIG['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(admin_bp)
app.register_blueprint(gayrimenkul_bp)

@app.route("/")
def anasayfa():
    return render_template('anasayfa.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
