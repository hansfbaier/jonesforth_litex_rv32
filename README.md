# Jonesforth RISC-V

RISC-V 32 implementation of Jones forth.

The code is based on Richard WM Jones's excellent literate x86 assembly
implementation of Forth, more on which here:
http://rwmj.wordpress.com/2010/08/07/jonesforth-git-repository/

The x86 version source code is copied from a mirror repo: https://github.com/nornagon/jonesforth

The RISC-V version is rewritten by [JJy](https://justjjy.com), mostly modification is in the `jonesforth.S` file.
The RISC-V 32 version has been ported by [Hans Baier](https://www.hans-baier.de)

> This RISC-V version jonesforth is using RV32 instructions, so the WORD size and alignment is 4 bytes.

## Run

Run Qemu VM:

1. Start qemu RISC-V VM: `make qemu` - will outputs lots out logs, wait until complete the boot.
2. Push files to qemu VM: `make push-remote` - the files are under `/jonesforth`.
3. Connect to RISC-V VM: `make ssh`.

> The docker image is very large, you can build it locally if you can't download it from server https://github.com/jjyr/docker-riscv-qemu-fedora

Compile & Run:

1. Compile `make`.
2. Start REPL: `make run`.
3. Run all tests: `make test`

> We haven't passed all tests yet: [issue #1](https://github.com/jjyr/jonesforth_riscv/issues/1)

## RISC-V references

* [RISCV Specification](https://riscv.org/technical/specifications/)
* [RISC-V Assembly Programmer's Manual](https://github.com/riscv/riscv-asm-manual/blob/master/riscv-asm.md)
* [RISC-V Quick Reference](https://www.cl.cam.ac.uk/teaching/1617/ECAD+Arch/files/docs/RISCVGreenCardv8-20151013.pdf)