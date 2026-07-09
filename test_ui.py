#import subprocess
#import time
#import pytest

# @pytest.fixture(scope="module", autouse=True)

def test_successful_login(page):
    page.goto("http://localhost:8080/index.html")

    page.fill("#username", "admin")
    page.fill("#password", "no-secret")
    page.click("#loginBtn")

    success_message = page.locator("#message")
    assert success_message.text_content() == "Welcome Admin!"

    # browser.close()
