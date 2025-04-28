import bcrypt

DATABASE_URL = "mssql+pyodbc://kullaniciadi:sifre@sunucuadi/veritabaniadi?driver=ODBC+Driver+17+for+SQL+Server"
USERNAME = "altan"
PASSWORD = "Yxrkt2bb7q8."
SUNUCU_ADI = "46.221.49.106"
VERITABANI_ADI = "invecoarsa"

# Parolayı hash'le
hashed_password = bcrypt.hashpw(PASSWORD.encode('utf-8'), bcrypt.gensalt())

# Yapılandırma bilgilerini sakla
DATABASE_CONFIG = {
    'DATABASE_URL': DATABASE_URL,
    'USERNAME': USERNAME,
    'PASSWORD': hashed_password.decode('utf-8')
}
