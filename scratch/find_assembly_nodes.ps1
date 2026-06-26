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

Write-Host "Nodes referencing meshes 360 to end:"
for ($i = 0; $i -lt $json.nodes.Count; $i++) {
    $node = $json.nodes[$i]
    if ($node.mesh -ne $null -and $node.mesh -ge 360) {
        $parentName = "NONE"
        if ($parents.ContainsKey($i)) {
            $parentIdx = $parents[$i]
            $parentName = $json.nodes[$parentIdx].name
        }
        Write-Host "Node[$i]: Name: $($node.name) | Mesh Index: $($node.mesh) (Mesh Name: $($json.meshes[$node.mesh].name)) | Parent: $parentName"
    }
}
