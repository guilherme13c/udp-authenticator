#!/bin/bash

sas1=2021031955:2:41c70c1d622be260cf1c874a59e44f2eb0577b7ff72b9cd214cb33afe3d3cabc
sas2=2027031858:4:6180a7377e7d7791562d16c0177a0427811d4d14b1b07863ff1270bb7601abb8
gtoken=2664d41e2666907fdd097800f5fcd5c0a929594270d07f28b10948af1675c9e3

python3 client.py "slardar.snes.2advanced.dev" "51001" "gtv" "2" "$sas1+$sas2+$gtoken"
