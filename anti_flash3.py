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
    
    # Check and add style to <html>
    if '<html lang="en">' in content:
        content = content.replace('<html lang="en">', '<html lang="en" style="background-color: #222;">')
        
    # Check and add style to <body>
    # We will use regex to find <body ...> and add the style if not already there
    body_match = re.search(r'<body([^>]*)>', content)
    if body_match:
        body_attrs = body_match.group(1)
        if 'style="background-color: #222;"' not in body_attrs:
            # Add it
            new_body = f'<body{body_attrs} style="background-color: #222;">'
            content = content.replace(body_match.group(0), new_body, 1)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added inline styles to html and body tags.")
