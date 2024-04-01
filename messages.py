import socket
import struct


def decode_error_msg(response):
    values = struct.unpack('!HH', response)
    return values[1]


def itr(s: socket.socket, argv: list[str]):
    id_ = str(argv[4]).strip()
    nonce = int(argv[5])

    package = struct.pack(
        "!H 12s I",
        1,
        bytes(id_, encoding="ASCII"),
        nonce,
    )

    s.send(package)

    response = s.recv(82)

    if len(response) == 4:
        print(ERROR_CODES[decode_error_msg(response)])
        exit()

    values = struct.unpack(
        "!H 12s I 64s",
        response,
    )

    code, id_recv, nonce_recv, token_recv = values
    code = int(code)
    if code != 2:
        print(f"Unexpected message code. Got {code}, expected 2.")
        exit()

    id_recv = str(id_recv.decode("ASCII")).strip()
    token_recv = str(token_recv.decode("ASCII")).strip()

    if nonce != nonce_recv:
        print(f"Incorrect nonce received: {nonce_recv}")
        exit()

    print(f"{id_recv}:{nonce_recv}:{token_recv}")


def itv(s: socket.socket, argv: list[str]):
    sas = argv[4].split(":")
    if len(sas) != 3:
        print("Invalid sas")
        return

    id_, nonce, token = str(sas[0]).strip(), int(sas[1]), str(sas[2]).strip()

    package = struct.pack(
        "!H 12s I 64s",
        3,
        bytes(id_, encoding="ASCII"),
        nonce,
        bytes(token, encoding="ASCII")
    )

    s.send(package)

    response = s.recv(83)

    if len(response) == 4:
        print(ERROR_CODES[decode_error_msg(response)])
        exit()

    values = struct.unpack(
        "!H 12s I 64s B",
        response,
    )

    code, _, nonce_recv, token_recv, status_recv = values
    code = int(code)
    nonce_recv = int(nonce_recv)

    if code != 4:
        print(f"Unexpected message code. Got {code}, expected 4.")
        exit()

    token_recv = str(token_recv.decode("ASCII")).strip()
    status_recv = str(status_recv)

    if token != token_recv:
        print(f"Incorrect token received: {token_recv}")
        exit()

    if nonce != nonce_recv:
        print(f"Incorrect nonce received: {nonce_recv}")
        exit()

    print(status_recv)


def gtr(s: socket.socket, argv: list[str]):
    n = int(argv[4])

    sas_list = []
    for i in range(n):
        try:
            v = argv[5 + i].split(":")
            sas_list.append([str(v[0]).strip(), int(v[1]), str(v[2]).strip()])
        except:
            print(f"Invalid sas: {argv[5 + i]}")
            exit()

    sas_pack_list = []
    for (id_, nonce, token) in sas_list:
        sas_pack_list.append(
            struct.pack(
                "!12s I 64s ",
                bytes(id_, encoding="ASCII"),
                int(nonce),
                bytes(token, encoding="ASCII"),
            ),
        )
    sas_pack_list = b''.join(sas_pack_list)

    package = struct.pack(
        "!H H ",
        5,
        n,
    ) + sas_pack_list

    s.send(package)

    response = s.recv(4 + n * 80 + 64)

    if len(response) == 4:
        print(ERROR_CODES[decode_error_msg(response)])
        exit()

    values = struct.unpack(
        f"!H H {n * 80}s 64s",
        response,
    )

    code, n_recv, sas_list_recv, gtoken = int(values[0]), int(values[1]), values[2], str(values[3].decode("ASCII")).strip()

    if code != 6:
        print(f"Unexpected message code. Got {code}, expected 6.")
        exit()

    if n_recv != n:
        print(f"Unexpected sas count. Got {n_recv}, expected {n}.")
        exit()

    gas_list = []
    sas_list_recv_values = struct.unpack(
        "!" + n * "12s I 64s",
        sas_list_recv,
    )
    for i in range(n_recv):
        id_, nonce, token = sas_list_recv_values[3*i:3*i+3]

        id_ = str(id_.decode("ASCII")).strip()
        nonce = int(nonce)
        token = str(token.decode("ASCII")).strip()

        gas_list.append(f"{id_}:{nonce}:{token}")

    gas_list.append(gtoken)

    gas = "+".join(gas_list)

    print(gas)


def gtv(s: socket.socket, argv: list[str]):
    n = int(argv[4])
    gas = str(argv[5]).strip()

    sas_list = gas.split("+")
    gtoken = str(sas_list[-1]).strip()
    sas_list.pop(-1)

    sas_list_unpacked = []
    for i in range(n):
        try:
            v = sas_list[i].split(":")
            sas_list_unpacked.append([str(v[0]).strip(), int(v[1]), str(v[2]).strip()])
        except:
            print(f"Invalid sas: {sas_list[i]}")
            exit()

    sas_pack_list = []
    for (id_, nonce, token) in sas_list_unpacked:
        sas_pack_list.append(
            struct.pack(
                "!12s I 64s ",
                bytes(id_, encoding="ASCII"),
                int(nonce),
                bytes(token, encoding="ASCII"),
            )
        )
    sas_pack_list = b''.join(sas_pack_list)

    package = struct.pack(
        "!H H ",
        7,
        n,
    )
    package = package + sas_pack_list
    package = package + struct.pack(
        "64s ",
        bytes(gtoken, encoding="ASCII"),
    )

    s.send(package)

    response = s.recv(4 + 80 * n + 64 + 1)

    if len(response) == 4:
        print(ERROR_CODES[decode_error_msg(response)])
        exit()

    values = struct.unpack(
        f"!H H {n * 80}s 64s B",
        response,
    )

    code, n_recv, _, token_recv, status_recv = values

    if code != 8:
        print(f"Unexpected message code. Got {code}, expected 8.")
        exit()

    token_recv = str(token_recv.decode("ASCII")).strip()
    status_recv = str(status_recv)

    if n_recv != n:
        print(f"Unexpected sas count. Got {n_recv}, expected {n}.")
        exit()

    if gtoken != token_recv:
        print(f"Incorrect token received: {token_recv}")
        exit()

    print(status_recv)


ERROR_CODES = {
    1: "INVALID_MESSAGE_CODE",
    2: "INCORRECT_MESSAGE_LENGTH",
    3: "INVALID_PARAMETER",
    4: "INVALID_SINGLE_TOKEN",
    5: "ASCII_DECODE_ERROR",
}

COMMANDS = {
    "itr": itr,
    "itv": itv,
    "gtr": gtr,
    "gtv": gtv,
}
