# 🚀 Playwright Python Automation Framework

Automation framework untuk Web UI testing menggunakan **Playwright + Python + Pytest**
Dirancang dengan **best practice (Page Object Model)** agar mudah di-maintain dan scalable.

---

# 📂 Project Structure

```
playwright-python-framework/
│
├── config/            # Konfigurasi environment
│   ├── config.py
│   └── settings.yaml
│
├── pages/             # Page Object Model (POM)
│   ├── base_page.py
│   └── home_page.py
│
├── tests/             # Test cases
│   ├── conftest.py
│   └── test_home.py
│
├── utils/             # Helper & utilities
│   └── logger.py
│
├── data/              # Test data (JSON, CSV, dll)
├── reports/           # Output report
├── screenshots/       # Screenshot hasil test
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# 🧠 Konsep Utama

Framework ini menggunakan:

### ✅ Page Object Model (POM)

* Semua interaksi UI disimpan di folder `pages/`
* Test hanya fokus ke scenario, bukan locator
* Memudahkan maintenance jika UI berubah

### ✅ Pytest Fixture

* Setup browser otomatis
* Cleanup otomatis setelah test selesai
* Menghindari duplicate code

### ✅ Centralized Config

* Semua konfigurasi ada di `config/settings.yaml`
* Mudah ganti environment tanpa ubah test

---

# ⚙️ Prerequisites

Pastikan sudah install:

* Python 3.9 atau lebih baru
* pip

Cek versi Python:

```bash
python --version
```

---

# 📦 Installation

### 1. Clone repository

```bash
git clone <your-repo-url>
cd playwright-python-framework
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Playwright browser

```bash
playwright install
```

---

# ▶️ Cara Menjalankan Test

Jalankan semua test:

```bash
pytest
```

Jalankan test spesifik:

```bash
pytest tests/test_home.py
```

---

# 🧪 Contoh Test Case

```python
from pages.home_page import HomePage
from config.config import config

def test_open_homepage(page):
    home = HomePage(page)

    home.navigate(config.base_url)

    assert home.verify_page_loaded()
```

---

# ⚙️ Konfigurasi

File: `config/settings.yaml`

```yaml
base_url: "https://playwright.dev"
headless: false
slow_mo: 500
timeout: 10000
```

### Penjelasan:

| Key      | Fungsi                                  |
| -------- | --------------------------------------- |
| base_url | URL utama aplikasi                      |
| headless | true = tanpa UI, false = tampil browser |
| slow_mo  | Delay tiap action (ms)                  |
| timeout  | Timeout default (ms)                    |

---

# 📸 Screenshot

Screenshot otomatis akan tersimpan di folder:

```
screenshots/
```

Contoh penggunaan manual:

```python
page.screenshot(path="screenshots/debug.png")
```

---

# 🧱 Cara Menambahkan Test Baru

### 1. Tambahkan Page Object

Contoh:

```
pages/login_page.py
```

### 2. Tambahkan Test Case

```
tests/test_login.py
```

### 3. Gunakan di Test

```python
login = LoginPage(page)
login.login("user", "password")
```

---

# 🧰 Best Practice

### ✅ DO

* Gunakan Page Object untuk semua interaksi UI
* Simpan config di YAML
* Buat test kecil dan spesifik
* Gunakan assertion yang jelas

### ❌ DON'T

* Jangan taruh locator di test
* Jangan hardcode URL di test
* Jangan gunakan `time.sleep()`
* Hindari duplicate code

---

# 🐞 Debugging Tips

### Jalankan dengan browser (visual)

```yaml
headless: false
```

### Tambahkan delay

```yaml
slow_mo: 1000
```

### Screenshot saat debugging

```python
page.screenshot(path="debug.png")
```

---

# 🚀 Improvement (Next Step)

Framework ini bisa dikembangkan menjadi:

* ✅ Allure Report (report HTML interaktif)
* ✅ Parallel Execution (`pytest-xdist`)
* ✅ CI/CD Integration (Jenkins / GitLab CI)
* ✅ Multi Environment (dev, staging, production)
* ✅ API + UI Testing dalam satu framework
* ✅ Video recording test
* ✅ Retry mechanism untuk flaky test

---

# 🤝 Contributing

1. Buat branch baru:

```bash
git checkout -b feature/nama-feature
```

2. Commit perubahan:

```bash
git commit -m "Add: fitur baru"
```

3. Push ke repo:

```bash
git push origin feature/nama-feature
```

4. Buat Pull Request

---

# 📌 Notes

Framework ini dibuat dengan tujuan:

* Mudah dipahami untuk pemula
* Mudah dikembangkan untuk skala besar
* Clean dan maintainable

---

🔥 Happy Testing & Build Like a Pro!
