# pytocpu

[![PIP Downloads](https://static.pepy.tech/personalized-badge/pytocpu?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=Downloads)]([https://pypi.org/project/pytocpu])

**pytocpu** is a Python library for generating machine code programmatically.

> **Current status:** Alpha (0.1.0)

## Features

* Generate x86 machine code
* Save output as binary (`.bin`) files
* Get machine code as bytes
* Get machine code as hexadecimal text
* Lightweight and easy to use

## Installation

```bash
pip install pytocpu
```

## Example

```python
from pytocpu import X86

asm = X86()

asm.mov("eax", 123)
asm.nop()
asm.ret()

print(asm.hex())
asm.save("program.bin")
```

Output:

```
B8 7B 00 00 00 90 C3
```

## Supported Instructions

* `mov`
* `nop`
* `ret`

More instructions will be added in future releases.

## Roadmap

### Version 0.2.0

* x64 support

### Future

* ARM64 support
* RISC-V support
* More x86 instructions
* Labels and jumps
* Executable generation utilities

## License

MIT License.
