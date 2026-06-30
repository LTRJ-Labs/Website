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

meta_tags = """    <meta name="color-scheme" content="dark">
    <meta name="theme-color" content="#222222">"""

# Add a script to smoothly fade out on page transition to prevent any hard flashes
fade_script = """
    <script>
        // Prevent white flash by keeping the body hidden until parsed, and fading out on navigate
        document.addEventListener("DOMContentLoaded", function() {
            document.body.style.opacity = "1";
            document.body.style.transition = "opacity 0.2s ease-in";
        });
        window.addEventListener("beforeunload", function() {
            document.body.style.opacity = "0";
        });
    </script>
"""

# And we will initialize body opacity to 0 in the inline style, if possible. Actually, no, if js is disabled it stays 0.
# Just adding the meta tags is usually enough. Let's just do the meta tags first.

for file_path in files_to_edit:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<meta name="color-scheme"' not in content:
        content = content.replace("<head>", f"<head>\n{meta_tags}")
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added color-scheme meta tags.")
