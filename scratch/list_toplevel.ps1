$json = Get-Content 'c:\Users\ryan2\Documents\GitHub\Website\img\RemoteTankMonitoring.gltf' -Raw | ConvertFrom-Json

$parents = @{}
for ($i = 0; $i -lt $json.nodes.Count; $i++) {
    $node = $json.nodes[$i]
    if ($node.children -ne $null) {
        foreach ($childIdx in $node.children) {
            $parents[$childIdx] = $i
        }
    }
}

Write-Host "Top-Level Nodes (No Parent):"
for ($i = 0; $i -lt $json.nodes.Count; $i++) {
    if (!$parents.ContainsKey($i)) {
        $node = $json.nodes[$i]
        Write-Host "Node[$i]: Name: $($node.name) | Children: $($node.children.Count) | Mesh: $($node.mesh)"
    }
}
