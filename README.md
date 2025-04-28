# Gayrimenkul Analiz Programı

Bu proje, kullanıcıların sahip olduğu veya ilgilendiği gayrimenkuller (arsa, tarla, ev, villa vb.) hakkında veri girerek detaylı analiz raporları almasını sağlayan Python Flask tabanlı bir web uygulamasıdır. Veritabanı olarak Microsoft SQL Server (MSSQL) kullanmaktadır.

## Teknolojiler

*   **Backend:** Python, Flask
*   **Veritabanı:** Microsoft SQL Server (MSSQL)
*   **Frontend:** HTML, CSS, JavaScript (veya seçilecek bir framework)

## Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1.  **Depoyu Klonlayın:**
    ```bash
    git clone <repository-url>
    cd <proje-dizini>
    ```

2.  **Sanal Ortam Oluşturun ve Aktive Edin:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Gerekli Paketleri Yükleyin:**
    *Proje geliştikçe bir `requirements.txt` dosyası oluşturulacaktır.*
    ```bash
    pip install Flask pyodbc # Örnek paketler, güncellenecek
    # pip install -r requirements.txt # requirements.txt oluşturulduğunda
    ```

4.  **Veritabanı Bağlantısını Yapılandırın:**
    *   Uygulamanın MSSQL veritabanına bağlanabilmesi için gerekli bağlantı bilgilerini (sunucu adı, veritabanı adı, kullanıcı adı, şifre vb.) yapılandırmanız gerekecektir. Bu genellikle bir `.env` dosyası veya bir `config.py` dosyası aracılığıyla yapılır (Bu kısım proje ilerledikçe detaylandırılacaktır).
    *   MSSQL sunucunuzda proje için bir veritabanı oluşturduğunuzdan emin olun.

5.  **Veritabanı Şemasını Oluşturun:**
    *   (Eğer bir ORM veya migration aracı kullanılıyorsa) Veritabanı tablolarını oluşturmak için gerekli komutları çalıştırın. Örneğin: `flask db upgrade` (Flask-Migrate kullanılıyorsa).

6.  **Uygulamayı Çalıştırın:**
    ```bash
    flask run
    ```
    Uygulama varsayılan olarak `http://127.0.0.1:5000/` adresinde çalışacaktır.

## Kullanım

Uygulama çalıştırıldıktan sonra web tarayıcınız üzerinden erişebilir, gayrimenkul verilerinizi girerek analiz raporları talep edebilirsiniz. (Detaylar eklenecek)

## Katkıda Bulunma

Katkıda bulunma yönergeleri daha sonra eklenecektir.