from playwright.sync_api import sync_playwright
import sys


def run_automation():
    # Menggunakan context manager agar resource bersih setelah selesai
    with sync_playwright() as p:
        # Launch browser: headless=False agar jendela muncul
        # slow_mo=500 agar gerakan automation sedikit melambat (biar enak dilihat)
        browser = p.chromium.launch(headless=False, slow_mo=500)

        # Membuat context browser baru
        context = browser.new_context()

        # Buka halaman baru
        page = context.new_page()

        try:
            print("--- Memulai Navigasi ---")
            page.goto("https://playwright.dev")

            # Verifikasi apakah kita di halaman yang benar
            title = page.title()
            print(f"Berhasil membuka: {title}")

            # Melakukan screenshot sederhana sebagai bukti
            page.screenshot(path="screenshot_playwright.png")
            print("Screenshot berhasil disimpan sebagai 'screenshot_playwright.png'")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

        finally:
            print("Menutup browser dalam 10 detik...")
            page.wait_for_timeout(10000)
            browser.close()


if __name__ == "__main__":
    run_automation()