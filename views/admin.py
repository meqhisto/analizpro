from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Giriş işlemleri
        pass
    return render_template('admin/login.html')

@admin_bp.route('/config', methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        # Veritabanı yapılandırma işlemleri
        db_url = request.form.get('db_url')
        db_user = request.form.get('db_user')
        db_password = request.form.get('db_password')

        # Parolayı hash'le
        hashed_password = generate_password_hash(db_password)

        # Yapılandırma bilgilerini kaydet
        pass
    return render_template('admin/config.html')