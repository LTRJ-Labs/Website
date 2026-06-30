import re

file_path = r"c:\Users\levip\Downloads\Website\services\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# For each <div class="service-card-body">, if there's no service-card-img-placeholder before it, inject it.
# We will just do a direct string replace if it's not already there.

placeholder = """
                        <div class="service-card-img-placeholder">
                            [Photo]
                        </div>
"""

new_content = content.replace('                        <div class="service-card-body">', placeholder + '                        <div class="service-card-body">')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Added photo sections to services.")
