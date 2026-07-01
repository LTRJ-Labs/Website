import re

with open('portfolio/mothnode/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

debug_injector = """        const numParts = explodeParts.length;
        // --- DEBUG START ---
        let debugNames = [];
        if (bottomCasingPart) debugNames.push(bottomCasingPart.name);
        explodeParts.forEach(child => debugNames.push(child.name));
        let debugDiv = document.createElement('div');
        debugDiv.style.position = 'fixed';
        debugDiv.style.top = '10px';
        debugDiv.style.left = '10px';
        debugDiv.style.background = 'rgba(0,0,0,0.8)';
        debugDiv.style.color = 'lime';
        debugDiv.style.zIndex = '9999';
        debugDiv.style.padding = '10px';
        debugDiv.style.maxHeight = '90vh';
        debugDiv.style.overflow = 'auto';
        debugDiv.innerHTML = '<strong>Debug Part Names:</strong><br>' + debugNames.join('<br>');
        document.body.appendChild(debugDiv);
        // --- DEBUG END ---"""

content = content.replace("const numParts = explodeParts.length;", debug_injector)

with open('portfolio/mothnode/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
