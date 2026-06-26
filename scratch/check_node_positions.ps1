$json = Get-Content 'c:\Users\ryan2\Documents\GitHub\Website\img\RemoteTankMonitoring.gltf' -Raw | ConvertFrom-Json

Write-Host "Direct children of RemoteTankMonitoring (Node 0) with their transforms:"
foreach ($idx in $json.nodes[0].children) {
    $node = $json.nodes[$idx]
    if ($node.mesh -ne $null -or ($node.children -ne $null -and $node.children.Count -gt 0)) {
        $pos = if ($node.translation -ne $null) { $node.translation -join ", " } else { "0, 0, 0" }
        $rot = if ($node.rotation -ne $null) { $node.rotation -join ", " } else { "0, 0, 0, 1" }
        $scale = if ($node.scale -ne $null) { $node.scale -join ", " } else { "1, 1, 1" }
        Write-Host "Node[$idx] Name: $($node.name) | Mesh: $($node.mesh) | Pos: ($pos) | Rot: ($rot) | Scale: ($scale)"
    }
}
