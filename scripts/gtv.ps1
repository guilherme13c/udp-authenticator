$sas1 = "2021031955:2:41c70c1d622be260cf1c874a59e44f2eb0577b7ff72b9cd214cb33afe3d3cabc"
$sas2 = "2027031858:4:6180a7377e7d7791562d16c0177a0427811d4d14b1b07863ff1270bb7601abb8"
$gtoken1 = "2664d41e2666907fdd097800f5fcd5c0a929594270d07f28b10948af1675c9e3"
$gtoken2 = "7382d0430e9333337b35a8c722332ecdb0e7890b7e869a18884925d2a784d714"

Write-Output "# Test 1"

python3 client.py "150.164.213.243" "51001" "gtv" "2" ($sas1 + "+" + $sas2 + "+" + $gtoken1)

Write-Output "# ------------------------------------------"

Write-Output "# Test 2"

python3 client.py "150.164.213.243" "51001" "gtv" "1" ($sas1 + "+" + $gtoken2)

Write-Output "# ------------------------------------------"
