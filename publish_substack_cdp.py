#!/usr/bin/env python3
"""
Publish a Substack post using Playwright connecting to the running Chrome instance
via Chrome DevTools Protocol (CDP) on port 9222.
"""

import re
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

SUBSTACK_URL = "https://engineeringforward.substack.com"
PUBLISH_URL = f"{SUBSTACK_URL}/publish/post"
POST_FILE = Path("substack/20260914-post-the-land-grab.md")

def markdown_to_html(md_body):
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
            heading_text = convert_links(stripped[3:])
            html_parts.append(f"<h2>{heading_text}</h2>")
        elif stripped.startswith("# "):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            heading_text = convert_links(stripped[2:])
            html_parts.append(f"<h2>{heading_text}</h2>")
        elif stripped.startswith("- "):
            item_text = convert_links(stripped[2:])
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
    
    with sync_playwright() as p:
        # Connect to the running Chrome instance via CDP
        print("Connecting to Chrome on port 9222...")
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9333")
        
        # Get existing context (the default one from the running Chrome)
        context = browser.contexts[0] if browser.contexts else browser.new_context()
        
        # Create a new page (tab) in the existing Chrome
        page = context.new_page()
        
        print(f"Navigating to {PUBLISH_URL}...")
        page.goto(PUBLISH_URL, wait_until="networkidle", timeout=30000)
        time.sleep(3)
        
        current_url = page.url
        print(f"Current URL: {current_url}")
        
        if "sign-in" in current_url or "login" in current_url:
            print("NOT LOGGED IN - Login page detected")
            page.screenshot(path="/tmp/substack-login3.png")
            print("Screenshot saved to /tmp/substack-login3.png")
            print("Page title:", page.title())
            page.close()
            browser.close()
            sys.exit(1)
        
        print("Logged in! Page title:", page.title())
        page.screenshot(path="/tmp/substack-publish3.png")
        
        # Fill title
        try:
            title_el = page.query_selector('textarea.pencraft.page-title')
            if title_el:
                print("Found title field")
                title_el.click()
                title_el.fill("")
                page.evaluate('(el, val) => { el.value = val; el.dispatchEvent(new Event("input", {bubbles: true})); el.dispatchEvent(new Event("change", {bubbles: true})); }', title_el, title)
                print("Title filled")
            else:
                print("Title field not found with primary selector")
                textareas = page.query_selector_all('textarea')
                print(f"Found {len(textareas)} textareas")
                for ta in textareas:
                    cls = ta.get_attribute('class') or ''
                    print(f"  class: {cls}")
                if textareas:
                    textareas[0].click()
                    textareas[0].fill(title)
                    print("Title filled via first textarea")
        except Exception as e:
            print(f"Error filling title: {e}")
        
        time.sleep(1)
        
        # Fill subtitle
        try:
            subtitle_el = page.query_selector('textarea.pencraft.subtitle')
            if subtitle_el:
                print("Found subtitle field")
                subtitle_el.click()
                subtitle_el.fill("")
                page.evaluate('(el, val) => { el.value = val; el.dispatchEvent(new Event("input", {bubbles: true})); el.dispatchEvent(new Event("change", {bubbles: true})); }', subtitle_el, subtitle)
                print("Subtitle filled")
            else:
                print("Subtitle field not found")
                textareas = page.query_selector_all('textarea')
                if len(textareas) > 1:
                    textareas[1].click()
                    textareas[1].fill(subtitle)
                    print("Subtitle filled via second textarea")
        except Exception as e:
            print(f"Error filling subtitle: {e}")
        
        time.sleep(1)
        
        # Fill body
        try:
            editor = page.query_selector('.tiptap.ProseMirror')
            if editor:
                print("Found editor")
                editor.click()
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
                print("Editor not found with primary selector")
                editors = page.query_selector_all('.ProseMirror')
                print(f"Found {len(editors)} ProseMirror elements")
                if editors:
                    editors[0].click()
                    editors[0].focus()
                    time.sleep(0.5)
                    page.evaluate("""
                        (htmlContent) => {
                            document.execCommand('selectAll', false, null);
                            document.execCommand('insertHTML', false, htmlContent);
                        }
                    """, body_html)
                    print("Body inserted via alternative")
        except Exception as e:
            print(f"Error filling body: {e}")
        
        time.sleep(3)
        page.screenshot(path="/tmp/substack-filled3.png")
        print("Screenshot after filling saved")
        
        # Wait for saved status
        try:
            page.wait_for_selector("text=Enregistré", timeout=15000)
            print("Article saved (Enregistré)")
        except PlaywrightTimeout:
            print("Saved status not found - checking for alternative text")
            try:
                page.wait_for_selector("text=Saved", timeout=5000)
                print("Article saved (Saved)")
            except PlaywrightTimeout:
                print("No saved status found - continuing anyway")
        
        # Click Continuer
        try:
            continue_btn = page.query_selector('button:has-text("Continuer")')
            if not continue_btn:
                continue_btn = page.query_selector('button:has-text("Continue")')
            if continue_btn:
                print("Clicking Continuer...")
                continue_btn.click()
                time.sleep(5)
                print(f"After continue, URL: {page.url}")
                page.screenshot(path="/tmp/substack-continue3.png")
            else:
                print("Continuer button not found - listing buttons:")
                buttons = page.query_selector_all('button')
                for btn in buttons:
                    t = btn.text_content() or ""
                    if t.strip():
                        print(f"  Button: '{t.strip()}'")
        except Exception as e:
            print(f"Error clicking Continuer: {e}")
        
        # Wait for publishing screen
        try:
            page.wait_for_selector("text=Envoyer à tous maintenant", timeout=15000)
            print("Found 'Envoyer à tous maintenant'")
        except PlaywrightTimeout:
            print("Did not find 'Envoyer à tous maintenant' - checking for English text")
            try:
                page.wait_for_selector("text=Send to everyone", timeout=5000)
                print("Found 'Send to everyone'")
            except PlaywrightTimeout:
                print("No publish button found - listing page state")
                page.screenshot(path="/tmp/substack-publish-screen3.png")
                buttons = page.query_selector_all('button')
                for btn in buttons:
                    t = btn.text_content() or ""
                    if t.strip():
                        print(f"  Button: '{t.strip()}'")
        
        # Click publish button
        try:
            publish_btn = page.query_selector('button:has-text("Envoyer à tous maintenant")')
            if not publish_btn:
                publish_btn = page.query_selector('button:has-text("Send to everyone")')
            if publish_btn:
                print("Clicking publish button...")
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
                    try:
                        page.wait_for_selector("text=Publish without buttons", timeout=5000)
                        no_btns = page.query_selector('button:has-text("Publish without buttons")')
                        if no_btns:
                            no_btns.click()
                            time.sleep(5)
                    except PlaywrightTimeout:
                        print("No dialog found")
                
                time.sleep(3)
                page.screenshot(path="/tmp/substack-published3.png")
                print(f"After publish, URL: {page.url}")
                
                if "/publish/posts/detail/" in page.url or "Publié" in page.content() or "Published" in page.content():
                    print("SUCCESS: Post published!")
                    print(f"URL: {page.url}")
                    
                    # Extract the post slug from the URL
                    if "/p/" in page.url:
                        post_url = page.url
                    else:
                        # Try to find the post URL
                        post_url = f"{SUBSTACK_URL}/p/the-land-grab"
                        print(f"Expected post URL: {post_url}")
                else:
                    print("Publish status unclear - checking page")
                    print("URL:", page.url)
                    # Check for error messages
                    body_text = page.text_content('body') or ""
                    if len(body_text) > 100:
                        print(f"Page text snippet: {body_text[:500]}")
            else:
                print("Publish button not found")
        except Exception as e:
            print(f"Error publishing: {e}")
        
        # Verify the post is live
        time.sleep(2)
        verify_url = f"{SUBSTACK_URL}/p/the-land-grab"
        print(f"\nVerifying post at {verify_url}...")
        page.goto(verify_url, wait_until="networkidle", timeout=30000)
        time.sleep(3)
        page_title = page.title()
        print(f"Verification page title: {page_title}")
        page.screenshot(path="/tmp/substack-verify.png")
        
        if "land grab" in page_title.lower() or "land-grab" in page_title.lower():
            print("VERIFIED: Post is live!")
            print(f"Public URL: {verify_url}")
        else:
            print("Post not found at expected URL - may need time to propagate")
            print(f"Page title: {page_title}")
        
        page.close()
        browser.close()

if __name__ == "__main__":
    main()