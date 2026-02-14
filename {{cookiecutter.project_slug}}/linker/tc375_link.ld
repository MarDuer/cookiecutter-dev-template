{% if cookiecutter.project_type == "c_tricore" -%}
/**
 * Linker script for TriCore TC375
 * 
 * Memory Map:
 * - PFLASH: Program Flash (4MB)
 * - DFLASH: Data Flash (384KB)
 * - PSRAM: Program Scratch RAM (64KB)
 * - DSRAM: Data Scratch RAM (240KB)
 */

MEMORY
{
    PFLASH (rx)  : ORIGIN = 0x80000000, LENGTH = 4M
    DFLASH (r)   : ORIGIN = 0xAF000000, LENGTH = 384K
    PSRAM (rwx)  : ORIGIN = 0x70000000, LENGTH = 64K
    DSRAM (rw)   : ORIGIN = 0x70010000, LENGTH = 240K
}

SECTIONS
{
    /* Code section in program flash */
    .text :
    {
        KEEP(*(.reset))
        *(.text)
        *(.text*)
        *(.rodata)
        *(.rodata*)
    } > PFLASH

    /* Initialized data in RAM, loaded from flash */
    .data :
    {
        __data_start = .;
        *(.data)
        *(.data*)
        __data_end = .;
    } > DSRAM AT> PFLASH

    /* Uninitialized data in RAM */
    .bss :
    {
        __bss_start = .;
        *(.bss)
        *(.bss*)
        *(COMMON)
        __bss_end = .;
    } > DSRAM

    /* Stack section */
    .stack :
    {
        __stack_start = .;
        . = . + 0x2000;
        __stack_end = .;
    } > DSRAM

    /* Heap section */
    .heap :
    {
        __heap_start = .;
        . = . + 0x4000;
        __heap_end = .;
    } > DSRAM
}

/* Entry point */
ENTRY(Reset_Handler)
{%- endif %}
