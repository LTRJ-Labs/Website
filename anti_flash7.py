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

for file_path in files_to_edit:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace 0.4s with 0.05s (50ms)
    content = content.replace("transition: opacity 0.4s ease-in-out;", "transition: opacity 0.05s ease-in-out;")
    
    # Replace the setTimeout delay 350 with 50
    content = content.replace("}, 350);", "}, 50);")
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated fade time to 50ms.")
