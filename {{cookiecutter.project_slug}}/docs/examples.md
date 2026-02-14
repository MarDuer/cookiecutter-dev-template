# Examples

{% if cookiecutter.project_type == "python_cli" -%}
## Basic Usage

### Example 1: Initialize and Run

```python
from {{ cookiecutter.package_name }}.config import Config
from {{ cookiecutter.package_name }}.core import Core

# Load configuration
config = Config()

# Create core instance
core = Core(config._config)

# Process data
result = core.process("hello world")
print(result)  # Output: HELLO WORLD
```

### Example 2: Custom Configuration

```python
from {{ cookiecutter.package_name }}.config import Config

config = Config()
config.load_yaml("environments/dev.yaml")
print(config.get("environment"))  # Output: development
```

{%- elif cookiecutter.project_type == "c_tricore" -%}
## Basic Usage

### Example 1: Module Initialization

```c
#include "ModuleName.h"

int main(void) {
    // Initialize module
    ModuleName_Init();

    // Main loop
    while(1) {
        ModuleName_Hdl();
    }

    return 0;
}
```

{%- endif %}

## More Examples

Check the `examples/` directory in the repository for more detailed examples.
