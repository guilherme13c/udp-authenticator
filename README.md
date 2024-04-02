# UDP Authenticator

**Author**: Guilherme Soeiro de Carvalho Caporali

**Registration Number**: 2021031955

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


