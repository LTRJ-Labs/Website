$json = Get-Content 'c:\Users\ryan2\Documents\GitHub\Website\img\RemoteTankMonitoring.gltf' -Raw | ConvertFrom-Json

$node = $json.nodes[367]
Write-Host "Enclosure+TankMount (Node 367) children:"
foreach ($idx in $node.children) {
    $c = $json.nodes[$idx]
    Write-Host "  Child[$idx]: Name: $($c.name) | Children Count: $($c.children.Count) | Mesh Index: $($c.mesh)"
    if ($c.children -ne $null -and $c.children.Count -gt 0) {
        foreach ($ccIdx in $c.children) {
            $cc = $json.nodes[$ccIdx]
            Write-Host "    Grandchild[$ccIdx]: Name: $($cc.name) | Mesh Index: $($cc.mesh)"
        }
    }
}
