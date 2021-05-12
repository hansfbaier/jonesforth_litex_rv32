# Jonesforth RISC-V

RISC-V 32 implementation of Jones forth.

The code is based on Richard WM Jones's excellent literate x86 assembly
implementation of Forth, more on which here:
http://rwmj.wordpress.com/2010/08/07/jonesforth-git-repository/

The x86 version source code is copied from a mirror repo: https://github.com/nornagon/jonesforth

The RISC-V version is rewritten by [JJy](https://justjjy.com), mostly modification is in the `jonesforth.S` file.
The RISC-V 32 on LiteX version has been ported by [Hans Baier](https://www.hans-baier.de)

> This RISC-V version jonesforth is using RV32 instructions, so the WORD size and alignment is 4 bytes.

## Run
1. Set the BUILD_DIR environment variable to wherever the LiteX build directory of your SoC is, for example:
```
export BUILD_DIR=build/qmtech_xc7a35t
```

2. Build the binary
```
make clean; make
```

3. Upload the binary
```
litex_term --kernel jonesforth.bin  --serial-boot --speed 115200 /dev/ttyUSBX
```
after Liftoff, cancel litex_term by pressing Ctrl+C twice

Don´t forget to use the right serial device filename.

4. Upload the bootstrap Forth code, and interact:

```
picocom -b 115200 /dev/ttyUSBX --imap lfcrlf,crcrlf --omap delbs,crlf --send-cmd "ascii-xfr -s -c 1 -n"
```
Then press Ctrl+A S
and enter: jonesforth.f

Also here, don't forget to replace ttyUSBX with the device name of your serial adapter.

5. Ready to use!

## Project Status
It currently runs on simulator and FPGA.
It still has bugs, especially the input routine is quite whacky.
Nevertheless, as this is an educational implementation it would take much more work
to mold it into something one actually would want to use.
This is impractical, because there already exist good embedded Forth implementations
for RV32, like mecrisp-quintus. So porting that one definitely would be preferrable.
Because of this the project development is considered complete.
Occasional pull requests are welcome.

## RISC-V references

* [RISCV Specification](https://riscv.org/technical/specifications/)
* [RISC-V Assembly Programmer's Manual](https://github.com/riscv/riscv-asm-manual/blob/master/riscv-asm.md)
* [RISC-V Quick Reference](https://www.cl.cam.ac.uk/teaching/1617/ECAD+Arch/files/docs/RISCVGreenCardv8-20151013.pdf)