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

$meshNodes = @()
for ($i = 0; $i -lt $json.nodes.Count; $i++) {
    $node = $json.nodes[$i]
    if ($node.mesh -ne $null) {
        $parentName = "NONE"
        if ($parents.ContainsKey($i)) {
            $parentIdx = $parents[$i]
            $parentName = $json.nodes[$parentIdx].name
        }
        $meshNodes += [PSCustomObject]@{
            Index = $i
            Name = $node.name
            Parent = $parentName
            Mesh = $node.mesh
        }
    }
}

Write-Host "Total Mesh Nodes: $($meshNodes.Count)"
$meshNodes | Group-Object Parent | ForEach-Object {
    Write-Host "`nParent: $($_.Name) (Count: $($_.Count))"
    foreach ($item in $_.Group) {
        Write-Host "  - Node[$($item.Index)]: $($item.Name) (Mesh: $($item.Mesh))"
    }
}
