import os

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

script_code = """
    <!-- Anti-Flash Script -->
    <script>
        window.addEventListener("beforeunload", function() {
            document.body.style.display = "none";
        });
    </script>
</head>"""

for file_path in files_to_edit:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<!-- Anti-Flash Script -->' not in content:
        content = content.replace("</head>", script_code)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added unload script.")
