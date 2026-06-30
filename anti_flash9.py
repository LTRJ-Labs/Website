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

old_block = """        // Wait for images to load, but don't wait longer than 800ms to avoid infinite black screen
        window.addEventListener("load", fadeIn);
        document.addEventListener("DOMContentLoaded", function() {
            setTimeout(fadeIn, 800);
        });"""

new_block = """        // Fade in immediately as soon as the DOM starts rendering to keep it feeling ultra-fast
        document.addEventListener("DOMContentLoaded", fadeIn);
        setTimeout(fadeIn, 50); // Instant fallback"""

for file_path in files_to_edit:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_block in content:
        content = content.replace(old_block, new_block)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated fade-in logic to be immediate.")
