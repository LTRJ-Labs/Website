import os
import re

files_to_edit = [
    r"c:\Users\levip\Downloads\Website\contact\index.html",
    r"c:\Users\levip\Downloads\Website\index.html",
    r"c:\Users\levip\Downloads\Website\portfolio\index.html",
    r"c:\Users\levip\Downloads\Website\portfolio\nucleof446re\index.html",
    r"c:\Users\levip\Downloads\Website\portfolio\pinkpigeon\index.html",
    r"c:\Users\levip\Downloads\Website\portfolio\watertank\index.html",
    r"c:\Users\levip\Downloads\Website\privacy\index.html",
    r"c:\Users\levip\Downloads\Website\services\index.html",
    r"c:\Users\levip\Downloads\Website\team\index.html",
]

anti_flash_style = "<style>html, body { background-color: #222 !important; color: #fff !important; }</style>"

for file_path in files_to_edit:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the old one at the bottom if it exists
    content = content.replace("    <style>html, body { background-color: #222; color: #fff; }</style>\n", "")
    content = content.replace("<style>html, body { background-color: #222; color: #fff; }</style>", "")
    
    # Check if already added
    if anti_flash_style not in content:
        # Add right after <head>
        content = content.replace("<head>", f"<head>\n    {anti_flash_style}", 1)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Moved anti-flash styles to the very top of <head>.")
