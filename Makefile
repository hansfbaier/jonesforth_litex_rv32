#BUILD_DIR?=

include $(BUILD_DIR)/software/include/generated/variables.mak
include $(SOC_DIRECTORY)/software/common.mak

OBJECTS   = isr.o jonesforth.o

all: jonesforth.bin

# pull in dependency info for *existing* .o files
-include $(OBJECTS:.o=.d)

%.bin: %.elf
	$(OBJCOPY) -O binary $< $@
	chmod -x $@

jonesforth.elf: $(OBJECTS)
	$(LD) $(LDFLAGS) \
		-Map=jonesforth.map \
		-T linker.ld \
		-N -o $@ \
		$(BUILD_DIR)/software/libbase/crt0.o \
		$(OBJECTS) \
		-L$(BUILD_DIR)/software/libbase \
		-L$(BUILD_DIR)/software/libcompiler_rt \
		-lbase-nofloat -lcompiler_rt
	chmod -x $@
	size $@

jonesforth.o: jonesforth.S

%.o: %.c
	$(compile)

%.o: %.S
	$(assemble) 

clean:
	$(RM) $(OBJECTS) $(OBJECTS:.o=.d) jonesforh.elf jonesforth.bin .*~ *~

.PHONY: all clean load
