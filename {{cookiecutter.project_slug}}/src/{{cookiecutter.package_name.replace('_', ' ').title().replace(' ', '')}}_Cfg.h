{% if cookiecutter.project_type == "c_tricore" -%}
/**
 * @file {{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}_Cfg.h
 * @brief Internal configuration for {{ cookiecutter.project_name }}
 * 
 * This file contains internal functions and configuration.
 * Not part of the public API.
 */

#ifndef {{ cookiecutter.package_name.upper() }}_CFG_H
#define {{ cookiecutter.package_name.upper() }}_CFG_H

#ifdef __cplusplus
extern "C" {
#endif

/*******************************************************************************
 * Includes
 ******************************************************************************/
#include <stdint.h>
#include <stdbool.h>

/*******************************************************************************
 * Configuration
 ******************************************************************************/

/* GPIO Configuration */
#define GPIO_PORT       P00
#define GPIO_PIN        0U

/*******************************************************************************
 * Internal Function Prototypes
 ******************************************************************************/

/**
 * @brief Initialize GPIO
 */
void GPIO_Init(void);

/**
 * @brief Toggle GPIO pin
 */
void GPIO_Toggle(void);

#ifdef __cplusplus
}
#endif

#endif /* {{ cookiecutter.package_name.upper() }}_CFG_H */
{%- endif %}
