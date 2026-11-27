from playwright.sync_api import sync_playwright

REPORT_URL = "https://app.fabric.microsoft.com/groups/40def66e-beaa-4e53-b24e-6a528446483b/reports/9de03948-8ea1-47bf-9cd9-183e97ab3df1/d98e344d3040d548c9c4?experience=fabric-developer"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(REPORT_URL)
    page.wait_for_timeout(15000)

    text = page.inner_text("body")
    if "Something's wrong" in text:
        print("Gate 5: FAIL - report shows an error")
    else:
        print("Gate 5: PASS - report opened, no error message")

    page.screenshot(path="report_check.png")
    browser.close()