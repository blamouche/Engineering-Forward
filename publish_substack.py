#!/usr/bin/env python3
"""
Publish a Substack post using Playwright (headless browser automation).
This script:
1. Navigates to the Substack publish/post page
2. Fills in title, subtitle, and body
3. Clicks through the publish flow
4. Reports the published URL
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
        
        # Check for sources separator
        if stripped == "---":
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            break
        
        # Check for sources section
        if stripped.startswith("## Sources"):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            break
        
        # Headers
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
        elif stripped.startswith("1. ") or re.match(r'^\d+\. ', stripped):
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
            # Handle italic paragraphs (subtitle-like)
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
    # Read the markdown file
    content = POST_FILE.read_text()
    lines = content.split("\n")
    
    # Extract title (first line starting with #)
    title = ""
    subtitle = ""
    body_start = 0
    
    for i, line in enumerate(lines):
        if line.startswith("# ") and not title:
            title = line[2:].strip()
            body_start = i + 1
        elif line.startswith("*") and line.endswith("*") and not subtitle and title:
            subtitle = line.strip()
            # Remove surrounding * *
            if subtitle.startswith("*") and subtitle.endswith("*"):
                subtitle = subtitle[1:-1].strip()
            body_start = i + 1
            break
    
    # Extract body (everything until --- or ## Sources)
    body_lines = []
    in_body = False
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
        auth_state = Path.home() / ".cache" / "substack-auth.json"
        
        # Use system Google Chrome since Playwright's bundled Chromium doesn't support macOS 12
        launch_opts = {
            "headless": True,
            "executable_path": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        }
        
        if auth_state.exists():
            context = browser = p.chromium.launch_persistent_context(
                user_data_dir=str(Path.home() / ".cache" / "substack-browser-data"),
                storage_state=str(auth_state),
                viewport={"width": 1440, "height": 900},
                **launch_opts
            )
            print("Loaded saved auth state (persistent context)")
        else:
            browser = p.chromium.launch(**launch_opts)
            context = browser.new_context(
                viewport={"width": 1440, "height": 900},
            )
        
        page = context.new_page()
        
        # Navigate to the publish page
        print(f"Navigating to {PUBLISH_URL}...")
        page.goto(PUBLISH_URL, wait_until="networkidle", timeout=30000)
        time.sleep(3)
        
        # Check if we're on a login page
        current_url = page.url
        print(f"Current URL: {current_url}")
        
        if "login" in current_url or "signin" in current_url or "account" in current_url:
            print("NOT LOGGED IN - Login page detected")
            # Take screenshot for debugging
            page.screenshot(path="/tmp/substack-login.png")
            print("Screenshot saved to /tmp/substack-login.png")
            print("Page title:", page.title())
            print("Cannot publish - not logged in to Substack")
            browser.close()
            sys.exit(1)
        
        # Take screenshot to see what we have
        page.screenshot(path="/tmp/substack-publish.png")
        print("Screenshot saved to /tmp/substack-publish.png")
        print("Page title:", page.title())
        
        # Try to find and fill the title field
        try:
            title_el = page.query_selector('textarea.pencraft.page-title')
            if title_el:
                print("Found title field")
                title_el.fill("")
                title_el.fill(title)
                title_el.dispatch_event("input")
                title_el.dispatch_event("change")
            else:
                print("Title field not found with selector 'textarea.pencraft.page-title'")
                # Try alternative selectors
                title_el = page.query_selector('[data-testid="title"]')
                if title_el:
                    print("Found title with data-testid")
                    title_el.fill(title)
                else:
                    print("Trying to find any textarea...")
                    textareas = page.query_selector_all('textarea')
                    print(f"Found {len(textareas)} textareas")
                    for i, ta in enumerate(textareas):
                        print(f"  textarea {i}: class={ta.get_attribute('class')}")
                    if textareas:
                        textareas[0].fill(title)
        except Exception as e:
            print(f"Error filling title: {e}")
        
        time.sleep(1)
        
        # Try to fill subtitle
        try:
            subtitle_el = page.query_selector('textarea.pencraft.subtitle')
            if subtitle_el:
                print("Found subtitle field")
                subtitle_el.fill("")
                subtitle_el.fill(subtitle)
                subtitle_el.dispatch_event("input")
                subtitle_el.dispatch_event("change")
            else:
                print("Subtitle field not found")
                # Try alternative
                subtitle_el = page.query_selector('[data-testid="subtitle"]')
                if subtitle_el:
                    subtitle_el.fill(subtitle)
        except Exception as e:
            print(f"Error filling subtitle: {e}")
        
        time.sleep(1)
        
        # Try to fill the body editor
        try:
            editor = page.query_selector('.tiptap.ProseMirror')
            if editor:
                print("Found editor")
                editor.focus()
                time.sleep(0.5)
                
                # Select all and insert HTML
                page.evaluate("""
                    (htmlContent) => {
                        document.execCommand('selectAll', false, null);
                        document.execCommand('insertHTML', false, htmlContent);
                    }
                """, body_html)
                print("Body inserted")
            else:
                print("Editor not found with selector '.tiptap.ProseMirror'")
                editors = page.query_selector_all('.ProseMirror')
                print(f"Found {len(editors)} ProseMirror elements")
                if editors:
                    editors[0].focus()
                    page.evaluate("""
                        (htmlContent) => {
                            document.execCommand('selectAll', false, null);
                            document.execCommand('insertHTML', false, htmlContent);
                        }
                    """, body_html)
                    print("Body inserted via alternative selector")
        except Exception as e:
            print(f"Error filling body: {e}")
        
        time.sleep(2)
        page.screenshot(path="/tmp/substack-filled.png")
        print("Screenshot after filling saved")
        
        # Wait for "Enregistré" (Saved) status
        try:
            page.wait_for_selector("text=Enregistré", timeout=15000)
            print("Article saved (Enregistré)")
        except PlaywrightTimeout:
            print("Did not find 'Enregistré' status - continuing anyway")
        
        # Click "Continuer" (Continue) button
        try:
            continue_btn = page.query_selector('button:has-text("Continuer")')
            if continue_btn:
                print("Clicking Continuer...")
                continue_btn.click()
                time.sleep(5)
                page.screenshot(path="/tmp/substack-continue.png")
                print("After continue, URL:", page.url)
            else:
                print("Continuer button not found")
                # Try to find any publish/continue button
                buttons = page.query_selector_all('button')
                for btn in buttons:
                    text = btn.text_content() or ""
                    print(f"  Button: {text.strip()}")
        except Exception as e:
            print(f"Error clicking Continuer: {e}")
        
        # Wait for publishing screen
        try:
            page.wait_for_selector("text=Envoyer à tous maintenant", timeout=15000)
            print("Found publish button 'Envoyer à tous maintenant'")
        except PlaywrightTimeout:
            print("Did not find 'Envoyer à tous maintenant' - checking page state")
            page.screenshot(path="/tmp/substack-publish-screen.png")
            print("URL:", page.url)
            print("Page content snippet:", page.content()[:2000])
        
        # Click "Envoyer à tous maintenant" (Send to everyone now)
        try:
            publish_btn = page.query_selector('button:has-text("Envoyer à tous maintenant")')
            if publish_btn:
                print("Clicking publish button...")
                publish_btn.click()
                time.sleep(3)
                
                # Handle dialog if it appears
                try:
                    page.wait_for_selector("text=Publier sans boutons", timeout=5000)
                    no_buttons_btn = page.query_selector('button:has-text("Publier sans boutons")')
                    if no_buttons_btn:
                        print("Clicking 'Publier sans boutons'...")
                        no_buttons_btn.click()
                        time.sleep(5)
                except PlaywrightTimeout:
                    print("No 'Publier sans boutons' dialog")
                
                time.sleep(3)
                page.screenshot(path="/tmp/substack-published.png")
                print("After publish, URL:", page.url)
                
                # Check if published
                if "/publish/posts/detail/" in page.url or "Publié" in page.content():
                    print("SUCCESS: Post published!")
                    print(f"URL: {page.url}")
                else:
                    print("Publish status unclear")
                    print("URL:", page.url)
            else:
                print("Publish button not found")
        except Exception as e:
            print(f"Error publishing: {e}")
        
        # Save auth state for future runs
        auth_state.parent.mkdir(parents=True, exist_ok=True)
        context.storage_state(path=str(auth_state))
        print(f"Auth state saved to {auth_state}")
        
        browser.close()

if __name__ == "__main__":
    main()