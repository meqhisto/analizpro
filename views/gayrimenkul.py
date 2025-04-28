from flask import Blueprint, render_template, request, redirect, url_for
from models.models import Gayrimenkul, db

gayrimenkul_bp = Blueprint('gayrimenkul', __name__, url_prefix='/gayrimenkul')

@gayrimenkul_bp.route('/')
def index():
    return render_template('gayrimenkul/index.html')

@gayrimenkul_bp.route('/ekle', methods=['GET', 'POST'])
def ekle():
    if request.method == 'POST':
        tip = request.form.get('tip')
        adres = request.form.get('adres')
        fiyat = request.form.get('fiyat', type=float)

        gayrimenkul = Gayrimenkul(tip=tip, adres=adres, fiyat=fiyat)
        db.session.add(gayrimenkul)
        db.session.commit()

        return redirect(url_for('gayrimenkul.index'))

    return render_template('gayrimenkul/ekle.html')