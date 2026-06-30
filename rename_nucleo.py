import re

portfolio_index = r"c:\Users\levip\Downloads\Website\portfolio\index.html"
nucleo_page = r"c:\Users\levip\Downloads\Website\portfolio\nucleof446re\index.html"

# 1. Process portfolio/index.html
with open(portfolio_index, "r", encoding="utf-8") as f:
    p_content = f.read()

p_content = p_content.replace('Camosun College Nucleo F446RE LCD Board', 'Camosun College ECET-260 Board')
p_content = p_content.replace('STM32 Nucleo Project', 'ECET-260 Project')
p_content = p_content.replace('STM32 Nucleo F446RE', 'ECET-260 Board')
# Just in case there's any stray Nucleo text in the thumbnail section
p_content = p_content.replace('Nucleo F446RE', 'ECET-260')

with open(portfolio_index, "w", encoding="utf-8") as f:
    f.write(p_content)

# 2. Process portfolio/nucleof446re/index.html
with open(nucleo_page, "r", encoding="utf-8") as f:
    n_content = f.read()

# Replace strings
n_content = n_content.replace('STM32 Nucleo F446RE LCD Board', 'ECET-260 Board')
n_content = n_content.replace('STM32 Nucleo Board Image', 'ECET-260 Board Image')
n_content = n_content.replace('STM32 Nucleo F446RE', 'ECET-260 Board')
n_content = n_content.replace('STM32 Nucleo development board', 'ECET-260 development board')
n_content = n_content.replace('NUCLEO LEFT', 'ECET-260 LEFT')
n_content = n_content.replace('NUCLEO RIGHT', 'ECET-260 RIGHT')
n_content = n_content.replace('NUCLEO LCD SHIELD V1.1', 'ECET-260 SHIELD V1.1')
n_content = n_content.replace('STM32, Nucleo, F446RE', 'STM32, ECET-260')

# Also replace the main title if it was purely "Nucleo F446RE" or similar
n_content = n_content.replace('<h2 class="section-heading" style="text-transform: none; margin-top: 5px; text-align: left; margin-bottom: 0;">Nucleo F446RE</h2>', '<h2 class="section-heading" style="text-transform: none; margin-top: 5px; text-align: left; margin-bottom: 0;">ECET-260 Board</h2>')

# Just run a general regex for any remaining "Nucleo F446RE" -> "ECET-260 Board"
n_content = re.sub(r'\bNucleo F446RE\b', 'ECET-260 Board', n_content)
n_content = re.sub(r'\bNucleo\b', 'ECET-260 Board', n_content)

# Remove the theme-info-box block
n_content = re.sub(r'<div class="theme-info-box".*?</div>', '', n_content, flags=re.DOTALL)

# Remove the testimonial-card block
n_content = re.sub(r'<div class="testimonial-card">.*?</div>\s*</div>\s*</div>\s*</div>', '</div>\n</div>\n</div>\n</div>', n_content, flags=re.DOTALL)
# The above regex might be fragile with the closing divs. Let's just remove the testimonial card directly:
n_content = re.sub(r'<!-- Client Testimonial -->\s*<div class="testimonial-card">.*?</div>', '', n_content, flags=re.DOTALL)

# Let's fix the regex for testimonial card removal to be safer if it doesn't have the comment
n_content = re.sub(r'<div class="testimonial-card">.*?</div>\s*<div class="testimonial-author">.*?</div>\s*<div class="testimonial-company">.*?</div>\s*</div>', '', n_content, flags=re.DOTALL)

with open(nucleo_page, "w", encoding="utf-8") as f:
    f.write(n_content)

print("Renamed Nucleo to ECET-260 and removed status/quote blocks.")
