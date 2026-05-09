import sys, re
from pathlib import Path
from playwright.sync_api import sync_playwright

def replace_section(text, start_tag, end_tag, new_content):
    pattern = re.compile(
        f"{re.escape(start_tag)}(.*?){re.escape(end_tag)}",
        re.DOTALL
    )
    replacement = f"{start_tag}\n{new_content.strip()}\n{end_tag}"
    return re.sub(pattern, replacement, text)

def main(username):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f'https://learn.microsoft.com/en-us/users/{username}')
        page.wait_for_selector('.card-header-image', timeout=60000)
        
        metadata = [
            {
                "src": img.get_attribute("src"),
                "alt": title.inner_text().strip()
            }
            for img, title in zip(page.query_selector_all('.card-header-image img'), page.query_selector_all('.card-content-title h3'))
        ]
        
        README_PATH = Path("README.md")
        readme = README_PATH.read_text(encoding="utf-8")

        START_TAG = "<!-- START_MICROSOFT_LEARN_BADGES -->"
        END_TAG = "<!-- END_MICROSOFT_LEARN_BADGES -->"

        TABLE_WIDTH = 4 * 200  # 800px — matches 4 cells × 200px each

        chunks = [metadata[i:i+4] for i in range(0, len(metadata), 4)]
        content = ""

        for chunk in chunks:
            content += f"<table border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"{TABLE_WIDTH}\"><tr>"
            for i in chunk:
                content += (
                    f"<td align=\"center\" width=\"200\">"
                    f"<a href=\"https://learn.microsoft.com/en-us/users/{username}\">"
                    f"<img src=\"https://learn.microsoft.com{i['src']}\" height=\"100\"/>"
                    f"</a><br/><sub><b>{i['alt']}</b></sub></td>"
                )
            content += "</tr></table>"

        updated = replace_section(readme, START_TAG, END_TAG, content)

        README_PATH.write_text(updated, encoding="utf-8")
        browser.close()

if __name__=='__main__':
    if len(sys.argv) != 2:
        print("Usage: python fetch-badges.py <mslearn-username>")
        sys.exit(1)

    username = sys.argv[1]
    main(username)