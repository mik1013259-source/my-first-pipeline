import subprocess
import time
import pytest

@pytest.fixture(scope="module", autouse=True)

def start_local_server():
    server = subprocess.Popen(["python", "-m", "http.server", "8080"])
    time.sleep(1) 
    yield
    server.kill()  # Use kill() instead of terminate() to prevent CI hangs


def test_successful_login(page):  #  Inject the 'page' fixture here
    page.goto("http://localhost:8080/index.html")

    page.fill("#username", "admin")
    page.fill("#password", "no-secret")
    page.click("#loginBtn")

    success_message = page.locator("#message")
    assert success_message.text_content() == "Welcome Admin!"
        
    browser.close()
