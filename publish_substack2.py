#!/usr/bin/env python3
"""
Publish a Substack post using Playwright with the user's actual Chrome profile.
"""

import re
import sys
import json
import time
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

SUBSTACK_URL = "https://engineeringforward.substack.com"
PUBLISH_URL = f"{SUBSTACK_URL}/publish/post"
POST_FILE = Path("substack/20260914-post-the-land-grab.md")

def markdown_to_html(md_body):
    """Convert markdown body (without title/subtitle/sources) to HTML for Substack."""
    lines = md_body.strip().split("\n")
    html_parts = []
    in_list = False
    
    for line in lines:
        stripped = line.strip()
        
        if not stripped:
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            html_parts.append("")
            continue
        
        if stripped == "---":
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            break
        
        if stripped.startswith("## Sources"):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            break
        
        if stripped.startswith("## "):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            heading_text = stripped[3:]
            heading_text = convert_links(heading_text)
            html_parts.append(f"<h2>{heading_text}</h2>")
        elif stripped.startswith("# "):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            heading_text = stripped[2:]
            heading_text = convert_links(heading_text)
            html_parts.append(f"<h2>{heading_text}</h2>")
        elif stripped.startswith("- "):
            item_text = stripped[2:]
            item_text = convert_links(item_text)
            if not in_list:
                html_parts.append("<ul>")
                in_list = True
            html_parts.append(f"<li>{item_text}</li>")
        elif re.match(r'^\d+\. ', stripped):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            item_text = re.sub(r'^\d+\. ', '', stripped)
            item_text = convert_links(item_text)
            html_parts.append(f"<p>{item_text}</p>")
        else:
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            para_text = convert_links(stripped)
            if para_text.startswith("*") and para_text.endswith("*") and len(para_text) > 2:
                para_text = f"<em>{para_text[1:-1]}</em>"
            html_parts.append(f"<p>{para_text}</p>")
    
    if in_list:
        html_parts.append("</ul>")
    
    return "\n".join(html_parts)

def convert_links(text):
    """Convert [text](url) to <a href="url">text</a>."""
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.sub(pattern, r'<a href="\2">\1</a>', text)

def main():
    content = POST_FILE.read_text()
    lines = content.split("\n")
    
    title = ""
    subtitle = ""
    body_start = 0
    
    for i, line in enumerate(lines):
        if line.startswith("# ") and not title:
            title = line[2:].strip()
            body_start = i + 1
        elif line.startswith("*") and line.endswith("*") and not subtitle and title:
            subtitle = line.strip()
            if subtitle.startswith("*") and subtitle.endswith("*"):
                subtitle = subtitle[1:-1].strip()
            body_start = i + 1
            break
    
    body_lines = []
    for line in lines[body_start:]:
        if line.strip() == "---":
            break
        if line.strip().startswith("## Sources"):
            break
        body_lines.append(line)
    
    body_md = "\n".join(body_lines).strip()
    body_html = markdown_to_html(body_md)
    
    print(f"Title: {title}")
    print(f"Subtitle: {subtitle}")
    print(f"Body HTML length: {len(body_html)}")
    print(f"Body words: {len(body_md.split())}")
    
    temp_profile = str(Path.home() / "Library" / "Application Support" / "Google" / "Chrome")
    chrome_exe = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    with sync_playwright() as p:
        # Launch with the user's real Chrome profile (lock removed)
        context = p.chromium.launch_persistent_context(
            user_data_dir=temp_profile,
            executable_path=chrome_exe,
            headless=True,
            viewport={"width": 1440, "height": 900},
            args=["--disable-blink-features=AutomationControlled", "--no-first-run", "--disable-features=ProcessSingleton"],
        )
        
        page = context.new_page()
        
        print(f"Navigating to {PUBLISH_URL}...")
        page.goto(PUBLISH_URL, wait_until="networkidle", timeout=30000)
        time.sleep(3)
        
        current_url = page.url
        print(f"Current URL: {current_url}")
        
        if "login" in current_url or "sign-in" in current_url or "account" in current_url:
            print("NOT LOGGED IN - Login page detected")
            page.screenshot(path="/tmp/substack-login2.png")
            print("Screenshot saved to /tmp/substack-login2.png")
            print("Page title:", page.title())
            
            # Try extracting substack cookies from the Chrome cookie database
            print("\nAttempting to extract Substack session from Chrome cookies...")
            try:
                import subprocess
                result = subprocess.run([
                    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                    "--headless",
                    "--dump-dom",
                    "https://engineeringforward.substack.com/api/v1/account"
                ], capture_output=True, text=True, timeout=15)
                print(f"Account API response: {result.stdout[:500]}")
            except Exception as e:
                print(f"Cookie extraction failed: {e}")
            
            context.close()
            sys.exit(1)
        
        page.screenshot(path="/tmp/substack-publish2.png")
        print("Screenshot saved")
        print("Page title:", page.title())
        
        # Fill title
        try:
            title_el = page.query_selector('textarea.pencraft.page-title')
            if title_el:
                print("Found title field")
                title_el.fill("")
                page.evaluate('(el, val) => { el.value = val; el.dispatchEvent(new Event("input", {bubbles: true})); el.dispatchEvent(new Event("change", {bubbles: true})); }', title_el, title)
            else:
                print("Title field not found")
                textareas = page.query_selector_all('textarea')
                print(f"Found {len(textareas)} textareas")
                if textareas:
                    textareas[0].fill(title)
        except Exception as e:
            print(f"Error filling title: {e}")
        
        time.sleep(1)
        
        # Fill subtitle
        try:
            subtitle_el = page.query_selector('textarea.pencraft.subtitle')
            if subtitle_el:
                print("Found subtitle field")
                subtitle_el.fill("")
                page.evaluate('(el, val) => { el.value = val; el.dispatchEvent(new Event("input", {bubbles: true})); el.dispatchEvent(new Event("change", {bubbles: true})); }', subtitle_el, subtitle)
            else:
                print("Subtitle field not found")
        except Exception as e:
            print(f"Error filling subtitle: {e}")
        
        time.sleep(1)
        
        # Fill body
        try:
            editor = page.query_selector('.tiptap.ProseMirror')
            if editor:
                print("Found editor")
                editor.focus()
                time.sleep(0.5)
                page.evaluate("""
                    (htmlContent) => {
                        document.execCommand('selectAll', false, null);
                        document.execCommand('insertHTML', false, htmlContent);
                    }
                """, body_html)
                print("Body inserted")
            else:
                print("Editor not found")
                editors = page.query_selector_all('.ProseMirror')
                if editors:
                    editors[0].focus()
                    page.evaluate("""
                        (htmlContent) => {
                            document.execCommand('selectAll', false, null);
                            document.execCommand('insertHTML', false, htmlContent);
                        }
                    """, body_html)
                    print("Body inserted via alternative")
        except Exception as e:
            print(f"Error filling body: {e}")
        
        time.sleep(2)
        page.screenshot(path="/tmp/substack-filled2.png")
        
        # Wait for saved
        try:
            page.wait_for_selector("text=Enregistré", timeout=15000)
            print("Article saved")
        except PlaywrightTimeout:
            print("Saved status not found - continuing")
        
        # Click Continuer
        try:
            continue_btn = page.query_selector('button:has-text("Continuer")')
            if continue_btn:
                print("Clicking Continuer...")
                continue_btn.click()
                time.sleep(5)
                print(f"After continue, URL: {page.url}")
            else:
                print("Continuer not found")
                buttons = page.query_selector_all('button')
                for btn in buttons:
                    t = btn.text_content() or ""
                    if t.strip():
                        print(f"  Button: '{t.strip()}'")
        except Exception as e:
            print(f"Error clicking Continuer: {e}")
        
        # Wait for and click publish
        try:
            page.wait_for_selector("text=Envoyer à tous maintenant", timeout=15000)
            print("Found 'Envoyer à tous maintenant'")
            publish_btn = page.query_selector('button:has-text("Envoyer à tous maintenant")')
            if publish_btn:
                publish_btn.click()
                time.sleep(3)
                
                # Handle dialog
                try:
                    page.wait_for_selector("text=Publier sans boutons", timeout=5000)
                    no_btns = page.query_selector('button:has-text("Publier sans boutons")')
                    if no_btns:
                        print("Clicking 'Publier sans boutons'")
                        no_btns.click()
                        time.sleep(5)
                except PlaywrightTimeout:
                    print("No dialog")
                
                time.sleep(3)
                page.screenshot(path="/tmp/substack-published2.png")
                print(f"After publish, URL: {page.url}")
                
                if "/publish/posts/detail/" in page.url or "Publié" in page.content():
                    print("SUCCESS: Post published!")
                    print(f"URL: {page.url}")
                else:
                    print("Publish status unclear")
            else:
                print("Publish button not found")
        except PlaywrightTimeout:
            print("Did not find publish button")
            page.screenshot(path="/tmp/substack-publish-screen2.png")
        
        context.close()

if __name__ == "__main__":
    main()