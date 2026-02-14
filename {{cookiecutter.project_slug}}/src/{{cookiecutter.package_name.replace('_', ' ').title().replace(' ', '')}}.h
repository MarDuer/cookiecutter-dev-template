{% if cookiecutter.project_type == "c_tricore" -%}
/**
 * @file {{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}.h
 * @brief External interface for {{ cookiecutter.project_name }}
 * 
 * This module implements a cyclic handler pattern for TriCore TC375.
 */

#ifndef {{ cookiecutter.package_name.upper() }}_H
#define {{ cookiecutter.package_name.upper() }}_H

#ifdef __cplusplus
extern "C" {
#endif

/*******************************************************************************
 * Includes
 ******************************************************************************/
#include <stdint.h>
#include <stdbool.h>

/*******************************************************************************
 * Public Function Prototypes
 ******************************************************************************/

/**
 * @brief Initialize the module
 * 
 * This function performs one-time initialization of the module.
 * Must be called before any other module functions.
 */
void {{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}_Init(void);

/**
 * @brief Re-initialize the module
 * 
 * This function re-initializes the module to its default state.
 * Can be called at runtime to reset the module.
 */
void {{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}_ReInit(void);

/**
 * @brief Cyclic handler function
 * 
 * This function should be called cyclically from the main loop.
 * Performs the main processing of the module.
 */
void {{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}_Hdl(void);

#ifdef __cplusplus
}
#endif

#endif /* {{ cookiecutter.package_name.upper() }}_H */
{%- endif %}
