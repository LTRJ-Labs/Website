$json = Get-Content 'c:\Users\ryan2\Documents\GitHub\Website\img\RemoteTankMonitoring.gltf' -Raw | ConvertFrom-Json

Write-Host "Nodes matching 'Casing' or 'Enclosure' or 'Holder' or 'Mount' or 'Sensor' or 'PCB':"
for ($i = 0; $i -lt $json.nodes.Count; $i++) {
    $node = $json.nodes[$i]
    if ($node.name -like "*Casing*" -or $node.name -like "*Enclosure*" -or $node.name -like "*Holder*" -or $node.name -like "*Mount*" -or $node.name -like "*Sensor*" -or $node.name -like "*PCB*") {
        Write-Host "Node[$i]: Name: $($node.name) | Mesh Index: $($node.mesh) | Children Count: $($node.children.Count)"
        if ($node.children -ne $null -and $node.children.Count -gt 0) {
            Write-Host "  Children: $($node.children -join ', ')"
        }
    }
}
