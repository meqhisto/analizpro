from flask import Flask

# Flask uygulamasını başlat
app = Flask(__name__)

# Uygulama için gizli anahtar (Secret Key) - Oturum yönetimi vb. için önemlidir.
# Gerçek uygulamalarda bu değeri güvenli bir yerden (örneğin ortam değişkeni) alın.
app.config['SECRET_KEY'] = 'cok-gizli-bir-anahtar-buraya-gelecek'

# Örnek bir route (anasayfa)
@app.route('/')
def index():
    return "Gayrimenkul Analiz Programına Hoş Geldiniz!"

# Uygulamanın doğrudan çalıştırılması durumunda development server'ı başlat
if __name__ == '__main__':
    # Debug modu geliştirme sırasında hataları görmek için kullanışlıdır.
    # Üretim ortamında False olarak ayarlanmalıdır.
    app.run(debug=True)
