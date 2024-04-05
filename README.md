# UDP Authenticator

**Author**: Guilherme Soeiro de Carvalho Caporali

**Registration Number**: 2021031955

---

**THIS PROGRAM WAS WRITTEN FOR EDUCATIONAL PURPOSES AND SHOULD NOT BE USED IN REAL-WORLD APPLICATIONS**

---

## Proof of success

The following lines contain the command used and the output received:

```powershell
scripts/itr                                
2021031955:2:41c70c1d622be260cf1c874a59e44f2eb0577b7ff72b9cd214cb33afe3d3cabc
2027031858:4:6180a7377e7d7791562d16c0177a0427811d4d14b1b07863ff1270bb7601abb8
```
```powershell
scripts/gtr
# Test 1
2021031955:2:41c70c1d622be260cf1c874a59e44f2eb0577b7ff72b9cd214cb33afe3d3cabc+2027031858:
4:6180a7377e7d7791562d16c0177a0427811d4d14b1b07863ff1270bb7601abb8+2664d41e2666907fdd0978
00f5fcd5c0a929594270d07f28b10948af1675c9e3
# ------------------------------------------
# Test 2                                  
2021031955:2:41c70c1d622be260cf1c874a59e44f2eb0577b7ff72b9cd214cb33afe3d3cabc+7382d0430e9
333337b35a8c722332ecdb0e7890b7e869a18884925d2a784d714
# ------------------------------------------
```
```powershell
scripts/gtr
2021031955:2:41c70c1d622be260cf1c874a59e44f2eb0577b7ff72b9cd214cb33afe3d3cabc+2027031858:
4:6180a7377e7d7791562d16c0177a0427811d4d14b1b07863ff1270bb7601abb8+2664d41e2666907fdd0978
00f5fcd5c0a929594270d07f28b10948af1675c9e3
```
```powershell
scripts/gtv
# Test 1
0
# ------------------------------------------
# Test 2
0
# ------------------------------------------
```

Obs.: The scripts used to test can be found on the folder `scripts/`.

---

## How to use

To use this program you must have python installed, then run the following command:

```shell
python3 client.py <host> <port> <cmd>
```

where `host` is the server address (ipv4 or ipv6), port is the `port`
in which the target server is running, `cmd` is one of the following:

1. `itr <id> <nonce>`

    This command should send an individual token request to the server. 
    The SAS received from the server must be printed as the program's output.

2. `itv <SAS>`

    This command should send an individual token validation message to 
    the server for the SAS given on the command line. The validation result
    must be printed as the program's output.

3. `gtr <N> <SAS-1> <SAS-2> ... <SAS-N>`

    This command should send a group token request to the server. The
    parameter N gives the number of SAS that will be sent to the server. The
    GAS received from the server should be printed as the program's output.

4. `gtv <GAS>`

    This command should send a group token validation message to the server.
    The validation result should be printed as the program's output.

where a **GAS** has the following structure:

```
<id>:<nonce>:<token>
```

and a **SAS**:

```
<SAS1>+<SAS2>+<SAS3>+<token>
```

---


