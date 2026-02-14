{% if cookiecutter.project_type == "c_tricore" -%}
/**
 * @file {{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}.c
 * @brief Implementation of {{ cookiecutter.project_name }}
 */

/*******************************************************************************
 * Includes
 ******************************************************************************/
#include "{{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}.h"
#include "{{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}_Cfg.h"

/*******************************************************************************
 * Private Variables
 ******************************************************************************/
static bool isInitialized = false;
static uint32_t cycleCounter = 0U;

/*******************************************************************************
 * Private Function Prototypes
 ******************************************************************************/
static void ProcessData(void);
static void UpdateOutputs(void);

/*******************************************************************************
 * Public Functions
 ******************************************************************************/

void {{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}_Init(void)
{
    /* Initialize module */
    cycleCounter = 0U;
    isInitialized = true;
    
    /* Initialize GPIO (example) */
    GPIO_Init();
}

void {{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}_ReInit(void)
{
    /* Re-initialize to default state */
    cycleCounter = 0U;
}

void {{ cookiecutter.package_name.replace('_', ' ').title().replace(' ', '') }}_Hdl(void)
{
    if (isInitialized)
    {
        /* Increment cycle counter */
        cycleCounter++;
        
        /* Process data */
        ProcessData();
        
        /* Update outputs */
        UpdateOutputs();
    }
}

/*******************************************************************************
 * Private Functions
 ******************************************************************************/

static void ProcessData(void)
{
    /* Example: Process input data */
    /* Add your processing logic here */
}

static void UpdateOutputs(void)
{
    /* Example: Toggle GPIO every 1000 cycles */
    if ((cycleCounter % 1000U) == 0U)
    {
        GPIO_Toggle();
    }
}
{%- endif %}
