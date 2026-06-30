Add-Type -AssemblyName System.Drawing
$files = @("Levi2026-06-30.jpg", "Ryan2026-06-30.jpg", "Jaxon2026-06-30.jpg", "Tyler2026-06-30.jpg")
foreach ($f in $files) {
    $path = "c:\Users\levip\Downloads\Website\img\team\$f"
    $img = [System.Drawing.Image]::FromFile($path)
    $w = 1200
    $h = [math]::Round($img.Height * ($w / $img.Width))
    $bmp = New-Object System.Drawing.Bitmap($w, $h)
    $graph = [System.Drawing.Graphics]::FromImage($bmp)
    $graph.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $graph.DrawImage($img, 0, 0, $w, $h)
    
    # Save with high JPEG quality
    $encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
    $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
    $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]95)
    
    $outPath = "c:\Users\levip\Downloads\Website\img\team\opt_$f"
    $bmp.Save($outPath, $encoder, $encoderParams)
    $graph.Dispose()
    $bmp.Dispose()
    $img.Dispose()
}
