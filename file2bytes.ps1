function file2bytes{

$file = Read-Host 'Target File Path'
$out = Read-Host 'Output Path'
$bytes = Get-Content $file -Encoding Byte
Set-Content -Path $out -Value $bytes
}

function bytes2file{

$file = Read-Host 'File Path'
$out = Read-Host 'Output Path'
$bytes = Get-Content -Path $file
[IO.File]::WriteAllBytes($out, $bytes)
}



