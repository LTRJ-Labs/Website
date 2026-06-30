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
    
    # We want to replace the block starting from <div class="container"> down to the section-subheading
    # Current structure is roughly:
    # <div class="container">
    #     <div style="display: flex; justify-content: flex-start; margin-bottom: 20px; margin-top: -30px;">
    #         <a href="../../portfolio/" class="portfolio-back-arrow">
    #             <i class="fa fa-long-arrow-left"></i>
    #             <span class="portfolio-back-text">Back to Portfolio</span>
    #         </a>
    #     </div>
    #     <div class="row">
    #         <div class="col-lg-12 text-center">
    #             <h2 class="section-heading" style="text-transform: none;">TITLE</h2>
    #             <h3 class="section-subheading text-muted" style="margin-bottom: 30px;"><strong>SUBTITLE</strong></h3>
    
    pattern = re.compile(
        r'<div class="container">\s*<div style="display: flex; justify-content: flex-start; margin-bottom: 20px; margin-top: -30px;">\s*<a href="../../portfolio/" class="portfolio-back-arrow">\s*<i class="fa fa-long-arrow-left"></i>\s*<span class="portfolio-back-text">Back to Portfolio</span>\s*</a>\s*</div>\s*<div class="row">\s*<div class="col-lg-12 text-center">\s*<h2 class="section-heading" style="text-transform: none;">(.*?)</h2>\s*<h3 class="section-subheading text-muted" style="margin-bottom: 30px;">(.*?)</h3>',
        re.DOTALL
    )
    
    def replacer(match):
        title = match.group(1)
        subtitle = match.group(2)
        return f"""<div class="container">
            <div class="row">
                <div class="col-lg-12" style="position: relative;">
                    <!-- Back Arrow positioned absolute to stay out of the text-center flow -->
                    <div style="position: absolute; left: 15px; top: 0; z-index: 10;">
                        <a href="../../portfolio/" class="portfolio-back-arrow" style="margin-bottom: 0;">
                            <i class="fa fa-long-arrow-left"></i>
                            <span class="portfolio-back-text">Back to Portfolio</span>
                        </a>
                    </div>
                    <!-- Centered Titles -->
                    <div class="text-center">
                        <h2 class="section-heading" style="text-transform: none; margin-top: 5px;">{title}</h2>
                        <h3 class="section-subheading text-muted" style="margin-bottom: 30px;">{subtitle}</h3>
                    </div>"""
    
    new_content = pattern.sub(replacer, content)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

print("Moved back arrow to be inline with title.")
