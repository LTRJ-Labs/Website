import os
import re

portfolio_pages = [
    r"c:\Users\levip\Downloads\Website\portfolio\nucleof446re\index.html",
    r"c:\Users\levip\Downloads\Website\portfolio\pinkpigeon\index.html",
    r"c:\Users\levip\Downloads\Website\portfolio\watertank\index.html",
]

for file_path in portfolio_pages:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We want to replace this block:
    #                     <!-- Back Arrow positioned absolute to stay out of the text-center flow -->
    #                     <div style="position: absolute; left: 15px; top: 0; z-index: 10;">
    #                         <a href="../../portfolio/" class="portfolio-back-arrow" style="margin-bottom: 0;">
    #                             <i class="fa fa-long-arrow-left"></i>
    #                             <span class="portfolio-back-text">Back to Portfolio</span>
    #                         </a>
    #                     </div>
    #                     <!-- Centered Titles -->
    #                     <div class="text-center">
    #                         <h2 class="section-heading" style="text-transform: none; margin-top: 5px;">TITLE</h2>
    #                         <h3 class="section-subheading text-muted" style="margin-bottom: 30px;">SUBTITLE</h3>
    #                     </div>
    
    pattern = re.compile(
        r'<!-- Back Arrow positioned absolute to stay out of the text-center flow -->\s*<div style="position: absolute; left: 15px; top: 0; z-index: 10;">\s*<a href="../../portfolio/" class="portfolio-back-arrow" style="margin-bottom: 0;">\s*<i class="fa fa-long-arrow-left"></i>\s*<span class="portfolio-back-text">Back to Portfolio</span>\s*</a>\s*</div>\s*<!-- Centered Titles -->\s*<div class="text-center">\s*<h2 class="section-heading" style="text-transform: none; margin-top: 5px;">(.*?)</h2>\s*<h3 class="section-subheading text-muted" style="margin-bottom: 30px;">(.*?)</h3>\s*</div>',
        re.DOTALL
    )
    
    def replacer(match):
        title = match.group(1)
        subtitle = match.group(2)
        return f"""<!-- Centered Titles with inline back arrow -->
                    <div class="text-center">
                        <div style="display: inline-block; position: relative;">
                            <!-- Back Arrow positioned absolute relative to the text block -->
                            <div style="position: absolute; right: 100%; top: 50%; transform: translateY(-50%); padding-right: 20px; z-index: 10; white-space: nowrap;">
                                <a href="../../portfolio/" class="portfolio-back-arrow" style="margin-bottom: 0;">
                                    <i class="fa fa-long-arrow-left"></i>
                                    <span class="portfolio-back-text">Back to Portfolio</span>
                                </a>
                            </div>
                            <h2 class="section-heading" style="text-transform: none; margin-top: 5px; text-align: left; margin-bottom: 0;">{title}</h2>
                        </div>
                        <h3 class="section-subheading text-muted" style="margin-top: 10px; margin-bottom: 30px;">{subtitle}</h3>
                    </div>"""
    
    new_content = pattern.sub(replacer, content)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

print("Tweaked back arrow to be close to the text.")
