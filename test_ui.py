import subprocess
import time
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module", autouse=True)
def start_local_server():
    # 1. Fire up a hidden background web server on your machine/container
    server = subprocess.Popen(["python", "-m", "http.server", "8080"])
    time.sleep(1) # Give the server 1 second to wake up
    yield
    server.terminate() # Shut down the server when the test finishes

def test_successful_login():
    with sync_playwright() as p:
        # 2. Open a hidden automated Chromium browser window
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # 3. Navigate to our mock website
        page.goto("http://localhost:8080/index.html")
        
        # 4. Mimic user actions (Type and click)
        page.fill("#username", "admin")
        page.fill("#password", "supersecret")
        page.click("#loginBtn")
        
        # 5. The Assertion (Verify if the welcome message appeared)
        success_message = page.locator("#message")
        assert success_message.text_content() == "Welcome Admin!"
        
        browser.close()
