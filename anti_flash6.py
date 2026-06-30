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

old_script = """    <!-- Anti-Flash Script -->
    <script>
        window.addEventListener("beforeunload", function() {
            document.body.style.display = "none";
        });
    </script>
</head>"""

new_script = """    <!-- Smooth Page Transition Script -->
    <style>
        body { opacity: 0; transition: opacity 0.4s ease-in-out; }
    </style>
    <script>
        let fadedIn = false;
        function fadeIn() {
            if (!fadedIn) {
                document.body.style.opacity = "1";
                fadedIn = true;
            }
        }
        
        // Wait for images to load, but don't wait longer than 800ms to avoid infinite black screen
        window.addEventListener("load", fadeIn);
        document.addEventListener("DOMContentLoaded", function() {
            setTimeout(fadeIn, 800);
        });

        // Intercept link clicks to fade out BEFORE navigating
        document.addEventListener("click", function(e) {
            let target = e.target.closest('a');
            if (!target) return;
            
            let href = target.getAttribute('href');
            if (!href) return;
            
            let isInternal = target.host === window.location.host;
            let isSamePage = target.pathname === window.location.pathname || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:');
            let isBlank = target.target === "_blank";
            
            if (isInternal && !isSamePage && !isBlank) {
                e.preventDefault(); // Stop instant navigation
                document.body.style.opacity = "0"; // Trigger fade out
                setTimeout(function() {
                    window.location.href = target.href; // Navigate after fade completes
                }, 350);
            }
        });
        
        // Handle back/forward cache restore
        window.addEventListener("pageshow", function(e) {
            if (e.persisted) {
                fadeIn();
            }
        });
    </script>
</head>"""

for file_path in files_to_edit:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_script in content:
        content = content.replace(old_script, new_script)
    elif '<!-- Smooth Page Transition Script -->' not in content:
        content = content.replace("</head>", new_script)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added smooth page transition script.")
