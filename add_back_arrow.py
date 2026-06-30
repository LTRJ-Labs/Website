import os

css_block = """
/* ==========================================
   Portfolio Back Arrow (Left side animation)
   ========================================== */
.portfolio-back-arrow {
    display: inline-flex;
    align-items: center;
    color: #FF6600;
    text-decoration: none;
    padding: 8px 12px;
    border-radius: 4px;
    transition: background 0.3s ease;
    margin-bottom: 20px; 
}
.portfolio-back-arrow:hover {
    background: rgba(255, 102, 0, 0.1);
    color: #FF6600;
    text-decoration: none;
}
.portfolio-back-arrow i {
    font-size: 28px;
    transition: transform 0.3s ease;
}
.portfolio-back-text {
    font-family: Montserrat, sans-serif;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    white-space: nowrap;
    overflow: hidden;
    max-width: 0;
    opacity: 0;
    transform: translateX(-15px);
    transition: max-width 0.4s ease, opacity 0.3s ease, transform 0.4s ease, margin-left 0.3s ease;
}
.portfolio-back-arrow:hover .portfolio-back-text {
    max-width: 150px;
    opacity: 1;
    transform: translateX(0);
    margin-left: 12px;
}
.portfolio-back-arrow:hover i {
    transform: translateX(-3px);
}
"""

html_block = """        <div class="container">
            <div style="display: flex; justify-content: flex-start; margin-bottom: 20px; margin-top: -30px;">
                <a href="../../portfolio/" class="portfolio-back-arrow">
                    <i class="fa fa-long-arrow-left"></i>
                    <span class="portfolio-back-text">Back to Portfolio</span>
                </a>
            </div>"""

# 1. Append CSS to agency.css
with open(r"c:\Users\levip\Downloads\Website\css\agency.css", "a") as f:
    f.write(css_block)

# 2. Add HTML to the 3 portfolio pages
portfolio_pages = [
    r"c:\Users\levip\Downloads\Website\portfolio\nucleof446re\index.html",
    r"c:\Users\levip\Downloads\Website\portfolio\pinkpigeon\index.html",
    r"c:\Users\levip\Downloads\Website\portfolio\watertank\index.html",
]

for file_path in portfolio_pages:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We want to replace `<div class="container">` that comes right after `<section id="project-details" ...>`
    # Find section id="project-details"
    if 'id="project-details"' in content:
        # We will split at <div class="container"> and insert our block, but only the first instance after section
        parts = content.split('<section id="project-details"')
        if len(parts) > 1:
            subparts = parts[1].split('<div class="container">', 1)
            if len(subparts) > 1:
                new_content = parts[0] + '<section id="project-details"' + subparts[0] + html_block + subparts[1]
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)

print("Added back arrows.")
