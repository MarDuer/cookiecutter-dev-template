{% if cookiecutter.project_type == "c_tricore" -%}
/**
 * @file startup_tc375.c
 * @brief Startup code for TriCore TC375
 */

/*******************************************************************************
 * Includes
 ******************************************************************************/
#include <stdint.h>

/*******************************************************************************
 * External Functions
 ******************************************************************************/
extern int main(void);
extern void __init(void);

/*******************************************************************************
 * Stack Configuration
 ******************************************************************************/
#define STACK_SIZE 0x2000

__attribute__((section(".stack")))
static uint8_t stack[STACK_SIZE];

/*******************************************************************************
 * Reset Handler
 ******************************************************************************/
void Reset_Handler(void) __attribute__((noreturn));

void Reset_Handler(void)
{
    /* Initialize data and bss sections */
    __init();
    
    /* Call main */
    main();
    
    /* Should never return */
    while(1);
}

/*******************************************************************************
 * Default Handler
 ******************************************************************************/
void Default_Handler(void)
{
    while(1);
}

/*******************************************************************************
 * Weak Aliases
 ******************************************************************************/
void NMI_Handler(void) __attribute__((weak, alias("Default_Handler")));
void HardFault_Handler(void) __attribute__((weak, alias("Default_Handler")));
{%- endif %}
