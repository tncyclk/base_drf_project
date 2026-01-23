# base_drf_project
base drf project


# Django REST API Projesi

Bu proje, **Django REST Framework** tabanlı bir backend uygulamasıdır. 
---

## Gereksinimler

- **Python 3.10 veya üzeri**
- (Önerilir) **virtualenv**

---

## Kurulum

### 1. Projeyi klonlayın

```bash
git clone <repo-url>
cd <proje-dizini>
```

### 2. Sanal ortam oluşturun ve aktif edin

```
python3 -m venv venv
source venv/bin/activate
````

### 3. Bağımlılıkları yükleyin

```
python3 -m pip install -r requirements.txt
```

### 4. Veritabanı İşlemleri

- Migration işlemlerini çalıştırın:
```
python3 manage.py migrate
````

### 5. Yönetici kullanıcı oluşturma

```
python3 manage.py createsuperuser
```
### 6. Uygulamayı Çalıştırma
```
python3 manage.py runserver
```