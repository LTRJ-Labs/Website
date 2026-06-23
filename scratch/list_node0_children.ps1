$json = Get-Content 'c:\Users\ryan2\Documents\GitHub\Website\img\RemoteTankMonitoring.gltf' -Raw | ConvertFrom-Json

$node0 = $json.nodes[0]
Write-Host "Children of RemoteTankMonitoring (Node 0):"
$childrenWithMesh = @()
$childrenWithChildren = @()
$flatChildren = @()

foreach ($idx in $node0.children) {
    $child = $json.nodes[$idx]
    if ($child.mesh -ne $null) {
        $childrenWithMesh += "  - [$idx] Name: $($child.name) (Mesh: $($child.mesh))"
    }
    if ($child.children -ne $null -and $child.children.Count -gt 0) {
        $childrenWithChildren += "  - [$idx] Name: $($child.name) (Children: $($child.children.Count))"
    }
    if ($child.mesh -eq $null -and ($child.children -eq $null -or $child.children.Count -eq 0)) {
        $flatChildren += "  - [$idx] Name: $($child.name)"
    }
}

Write-Host "`nChildren with Mesh: $($childrenWithMesh.Count)"
foreach ($item in $childrenWithMesh[0..15]) { Write-Host $item }
if ($childrenWithMesh.Count -gt 16) { Write-Host "  ... and $($childrenWithMesh.Count - 16) more" }

Write-Host "`nChildren with Children: $($childrenWithChildren.Count)"
foreach ($item in $childrenWithChildren) { Write-Host $item }

Write-Host "`nFlat/Empty Children: $($flatChildren.Count)"
foreach ($item in $flatChildren[0..10]) { Write-Host $item }
if ($flatChildren.Count -gt 10) { Write-Host "  ... and $($flatChildren.Count - 10) more" }
