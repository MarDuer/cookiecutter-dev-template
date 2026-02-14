{% if cookiecutter.project_type == "c_tricore" -%}
/**
 * @file traps.c
 * @brief Trap handlers for TriCore TC375
 */

/*******************************************************************************
 * Includes
 ******************************************************************************/
#include <stdint.h>

/*******************************************************************************
 * Trap Handlers
 ******************************************************************************/

void Trap_0_Handler(void) __attribute__((interrupt));
void Trap_1_Handler(void) __attribute__((interrupt));
void Trap_2_Handler(void) __attribute__((interrupt));
void Trap_3_Handler(void) __attribute__((interrupt));
void Trap_4_Handler(void) __attribute__((interrupt));
void Trap_5_Handler(void) __attribute__((interrupt));
void Trap_6_Handler(void) __attribute__((interrupt));
void Trap_7_Handler(void) __attribute__((interrupt));

/*******************************************************************************
 * Default Trap Handler
 ******************************************************************************/
static void Default_Trap_Handler(void)
{
    /* Trap occurred - enter infinite loop */
    while(1);
}

/*******************************************************************************
 * Trap Handler Implementations
 ******************************************************************************/

void Trap_0_Handler(void)
{
    /* MMU Trap */
    Default_Trap_Handler();
}

void Trap_1_Handler(void)
{
    /* Internal Protection Trap */
    Default_Trap_Handler();
}

void Trap_2_Handler(void)
{
    /* Instruction Error Trap */
    Default_Trap_Handler();
}

void Trap_3_Handler(void)
{
    /* Context Management Trap */
    Default_Trap_Handler();
}

void Trap_4_Handler(void)
{
    /* System Bus and Peripheral Error Trap */
    Default_Trap_Handler();
}

void Trap_5_Handler(void)
{
    /* Assertion Trap */
    Default_Trap_Handler();
}

void Trap_6_Handler(void)
{
    /* System Call Trap */
    Default_Trap_Handler();
}

void Trap_7_Handler(void)
{
    /* Non-Maskable Interrupt Trap */
    Default_Trap_Handler();
}
{%- endif %}
