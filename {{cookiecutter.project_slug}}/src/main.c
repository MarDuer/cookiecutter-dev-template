{% if cookiecutter.project_type == "c_tricore" -%}
/**
 * @file main.c
 * @brief Main application for {{ cookiecutter.project_name }}
 */

/*******************************************************************************
 * Includes
 ******************************************************************************/
#include "{{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}.h"

/*******************************************************************************
 * Main Function
 ******************************************************************************/

int main(void)
{
    /* Initialize module */
    {{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}_Init();
    
    /* Main loop */
    while(1)
    {
        /* Call cyclic handler */
        {{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}_Hdl();
    }
    
    return 0;
}
{%- endif %}
