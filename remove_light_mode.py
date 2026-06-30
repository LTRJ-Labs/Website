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

for file_path in files_to_edit:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the theme switch script
    content = re.sub(r'<script>\(function\(\)\{const t=localStorage\.getItem\("theme"\)\|\|"dark";document\.body\.classList\.add\(t\+"-mode"\);\}\)\(\);</script>', '', content)
    
    # Remove the theme switch list item in nav
    content = re.sub(r'<li>\s*<div class="theme-switch-wrapper">[\s\S]*?</div>\s*</li>', '', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Removed HTML toggle scripts.")
