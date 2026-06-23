$json = Get-Content 'c:\Users\ryan2\Documents\GitHub\Website\img\RemoteTankMonitoring.gltf' -Raw | ConvertFrom-Json

# Let's inspect the positions of the meshes to find their absolute center in parent space
Write-Host "Direct child node positions of RemoteTankMonitoring (Node 0):"
foreach ($idx in $json.nodes[0].children) {
    $node = $json.nodes[$idx]
    if ($node.mesh -ne $null) {
        $mesh = $json.meshes[$node.mesh]
        # Let's find min and max from accessors used by this mesh
        $accessorMinMax = ""
        foreach ($prim in $mesh.primitives) {
            $posAccIdx = $prim.attributes.POSITION
            $acc = $json.accessors[$posAccIdx]
            $accessorMinMax = "Min: ($($acc.min -join ', ')) | Max: ($($acc.max -join ', '))"
            break
        }
        $translation = if ($node.translation -ne $null) { $node.translation -join ", " } else { "0, 0, 0" }
        Write-Host "Node Name: $($node.name) | Mesh: $($mesh.name) | Node Pos: ($translation) | Geom Bounds: $accessorMinMax"
    }
}
