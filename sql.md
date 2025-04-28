-- Veritabanı oluşturma
CREATE DATABASE GayrimenkulAnaliz;

-- Kullanıcı oluşturma (güçlü bir parola ile değiştirin)
CREATE LOGIN KullaniciAdi WITH PASSWORD = 'GucluParola';
CREATE USER KullaniciAdi FOR LOGIN KullaniciAdi;

-- Kullanıcıya veritabanı üzerinde yetki verme
ALTER ROLE db_owner ADD MEMBER KullaniciAdi;