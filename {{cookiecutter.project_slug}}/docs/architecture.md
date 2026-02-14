# Architecture

## Overview

{% if cookiecutter.project_type == "python_cli" -%}
{{ cookiecutter.project_name }} follows a modular CLI architecture:

```mermaid
graph TD
    A[CLI Entry Point] --> B[Command Parser]
    B --> C[Init Command]
    B --> D[Run Command]
    B --> E[Config Command]
    C --> F[Core Logic]
    D --> F
    E --> G[Configuration]
    F --> G
```

## Components

### CLI Layer
- Argument parsing with argparse
- Command routing
- Error handling

### Core Layer
- Business logic
- Data processing

### Configuration Layer
- Environment variable loading (.env, .env-private)
- Config file support (YAML, JSON, TOML)
- Priority-based configuration

{%- elif cookiecutter.project_type == "python_library" -%}
{{ cookiecutter.project_name }} follows a layered library architecture:

```mermaid
graph TD
    A[Public API] --> B[Core Logic]
    B --> C[Configuration]
    B --> D[Utilities]
```

{%- elif cookiecutter.project_type == "c_tricore" -%}
{{ cookiecutter.project_name }} follows a cyclic handler pattern for embedded systems:

```mermaid
graph TD
    A[Main Loop] --> B[ModuleName_Hdl]
    B --> C[Process Data]
    C --> D[Update Outputs]
    D --> A
    E[Startup] --> F[ModuleName_Init]
    F --> G[ModuleName_ReInit]
    G --> A
```

## Components

### Cyclic Handler
- `ModuleName_Init`: One-time initialization
- `ModuleName_ReInit`: Re-initialization
- `ModuleName_Hdl`: Cyclic handler called every cycle

### Hardware Abstraction
- GPIO interface
- Memory-mapped I/O

{%- endif %}

## Design Decisions

See [Architecture Decision Records](decisions/) for detailed design decisions.
