REG32 = {
    0xB8: "eax",
    0xB9: "ecx",
    0xBA: "edx",
    0xBB: "ebx",
    0xBC: "esp",
    0xBD: "ebp",
    0xBE: "esi",
    0xBF: "edi",
}


def decode(data):
    output = []
    i = 0

    while i < len(data):
        byte = data[i]

        if byte in REG32:
            if i + 4 >= len(data):
                raise ValueError(f"Short mov command: offset={i}")

            value = (
                data[i+1] |
                data[i+2] << 8 |
                data[i+3] << 16 |
                data[i+4] << 24
            )

            output.append(
                f"mov {REG32[byte]}, {value}"
            )

            i += 5

        elif byte == 0xC3:
            output.append("ret")
            i += 1

        elif byte == 0x90:
            output.append("nop")
            i += 1

        else:
            output.append(f"db 0x{byte:02X}")
            i += 1

    return "\n".join(output)