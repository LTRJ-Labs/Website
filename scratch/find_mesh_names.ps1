$json = Get-Content 'c:\Users\ryan2\Documents\GitHub\Website\img\RemoteTankMonitoring.gltf' -Raw | ConvertFrom-Json

Write-Host "Meshes in GLTF:"
for ($i = 0; $i -lt $json.meshes.Count; $i++) {
    $mesh = $json.meshes[$i]
    if ($mesh.name -like "*Casing*" -or $mesh.name -like "*Enclosure*" -or $mesh.name -like "*Top*" -or $mesh.name -like "*Bottom*" -or $mesh.name -like "*Frame*") {
        Write-Host "Mesh[$i]: Name: $($mesh.name) | Primitives: $($mesh.primitives.Count)"
    }
}
