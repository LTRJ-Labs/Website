$json = Get-Content 'c:\Users\ryan2\Documents\GitHub\Website\img\RemoteTankMonitoring.gltf' -Raw | ConvertFrom-Json

Write-Host "Meshes index 350 to end:"
for ($i = 350; $i -lt $json.meshes.Count; $i++) {
    $mesh = $json.meshes[$i]
    Write-Host "Mesh[$i]: Name: $($mesh.name) | Primitives: $($mesh.primitives.Count)"
}
