$sas1="2021031955:2:41c70c1d622be260cf1c874a59e44f2eb0577b7ff72b9cd214cb33afe3d3cabc"
$sas2="2027031858:4:6180a7377e7d7791562d16c0177a0427811d4d14b1b07863ff1270bb7601abb8"

Write-Output "# Test 1"

python3 client.py "pugna.snes.dcc.ufmg.br" "51001" "gtr" "2" $sas1 $sas2

Write-Output "# ------------------------------------------"

Write-Output "# Test 2"

python3 client.py "pugna.snes.dcc.ufmg.br" "51001" "gtr" "1" $sas1

Write-Output "# ------------------------------------------"
