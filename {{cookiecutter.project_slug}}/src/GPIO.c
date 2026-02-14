{% if cookiecutter.project_type == "c_tricore" -%}
/**
 * @file GPIO.c
 * @brief Simple GPIO driver for TriCore TC375
 */

/*******************************************************************************
 * Includes
 ******************************************************************************/
#include "{{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}_Cfg.h"

/*******************************************************************************
 * Private Variables
 ******************************************************************************/
static bool gpioState = false;

/*******************************************************************************
 * Public Functions
 ******************************************************************************/

void GPIO_Init(void)
{
    /* Initialize GPIO pin as output */
    /* Example: Configure P00.0 as output */
    /* Add actual TriCore GPIO initialization here */
    gpioState = false;
}

void GPIO_Toggle(void)
{
    /* Toggle GPIO state */
    gpioState = !gpioState;
    
    /* Write to GPIO pin */
    /* Add actual TriCore GPIO write here */
}
{%- endif %}
