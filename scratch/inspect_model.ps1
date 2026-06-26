$json = Get-Content 'c:\Users\ryan2\Documents\GitHub\Website\img\RemoteTankMonitoring.gltf' -Raw | ConvertFrom-Json

Write-Host "SCENES:"
foreach ($scene in $json.scenes) {
    Write-Host "  Scene Name: $($scene.name) | Nodes: $($scene.nodes -join ', ')"
}

Write-Host "`nTOP LEVEL NODES IN SCENE 0:"
foreach ($nodeIdx in $json.scenes[0].nodes) {
    $node = $json.nodes[$nodeIdx]
    Write-Host "  Node [$nodeIdx]: $($node.name) | Children Count: $($node.children.Count) | Mesh Index: $($node.mesh)"
    if ($node.children -ne $null) {
        foreach ($cIdx in $node.children) {
            $cNode = $json.nodes[$cIdx]
            Write-Host "    Child [$cIdx]: $($cNode.name) | Children Count: $($cNode.children.Count) | Mesh Index: $($cNode.mesh)"
            if ($cNode.children -ne $null -and $cNode.name -eq "Enclosure+TankMount") {
                foreach ($ccIdx in $cNode.children) {
                    $ccNode = $json.nodes[$ccIdx]
                    Write-Host "      Grandchild [$ccIdx]: $($ccNode.name) | Children Count: $($ccNode.children.Count) | Mesh Index: $($ccNode.mesh)"
                }
            }
        }
    }
}
