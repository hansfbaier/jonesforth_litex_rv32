#!/bin/bash
litex_sim --csr-csv csr.csv --ram-init jonesforth.bin --trace --trace-fst --trace-start 679e9 --cpu-variant imac
