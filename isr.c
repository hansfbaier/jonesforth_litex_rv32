// This file is Copyright (c) 2020 Florent Kermarrec <florent@enjoy-digital.fr>
// License: BSD

#include <generated/csr.h>
#include <generated/soc.h>
#include <irq.h>
#include <uart.h>

void isr(void);

#ifdef CONFIG_CPU_HAS_INTERRUPT

uint32_t irq_count;

#pragma message " *** CPU has interrupts! *** "

void enable_uart_interrupts()
{
	irq_setmask(0);
	irq_setie(1);
}

void isr(void)
{
	uint32_t mcause;
	asm volatile ("csrr %0, mcause" : "=r" (mcause));

	irq_count++;
	ctrl_scratch_write(irq_pending());
	leds_out_write(irq_getmask());
	__attribute__((unused)) unsigned int irqs;
	irqs = irq_pending() & irq_getmask();


#ifndef UART_POLLING
	#pragma message " *** no polling! *** "
	if(irqs & (1 << UART_INTERRUPT))
		uart_isr();
#endif
}

#else
#pragma message " *** CPU has no interrupts! *** "

void isr(void){};

#endif
