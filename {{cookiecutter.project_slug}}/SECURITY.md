# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Currently supported versions:

| Version | Supported          |
| ------- | ------------------ |
| {{ cookiecutter.version }}   | :white_check_mark: |

## Reporting a Vulnerability

We take the security of {{ cookiecutter.project_name }} seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Please do NOT:

- Open a public GitHub issue
- Discuss the vulnerability in public forums or social media

### Please DO:

1. **Email us directly** at {{ cookiecutter.author_email }}
2. **Include the following information:**
   - Type of vulnerability
   - Full paths of source file(s) related to the vulnerability
   - Location of the affected source code (tag/branch/commit or direct URL)
   - Step-by-step instructions to reproduce the issue
   - Proof-of-concept or exploit code (if possible)
   - Impact of the vulnerability

### What to expect:

- **Acknowledgment:** We will acknowledge receipt of your vulnerability report within 48 hours
- **Updates:** We will send you regular updates about our progress
- **Timeline:** We aim to resolve critical vulnerabilities within 7 days
- **Credit:** We will credit you in the security advisory (unless you prefer to remain anonymous)

## Security Update Process

1. The security report is received and assigned to a primary handler
2. The problem is confirmed and affected versions are determined
3. Code is audited to find any similar problems
4. Fixes are prepared for all supported versions
5. Fixes are released and security advisory is published

## Security Best Practices

When using {{ cookiecutter.project_name }}:

{% if cookiecutter.project_type in ["python_cli", "python_library"] -%}
- Keep dependencies up to date (use `just install` regularly)
- Review security advisories from Dependabot
- Use `.env-private` for sensitive credentials (never commit this file)
- Enable GitHub's security features (Dependabot, CodeQL)
{%- elif cookiecutter.project_type == "c_tricore" -%}
- Follow MISRA-C:2012 guidelines
- Run static analysis regularly (`just misra`)
- Review security advisories for toolchain updates
{%- endif %}

## Disclosure Policy

When we receive a security bug report, we will:

1. Confirm the problem and determine affected versions
2. Audit code to find similar problems
3. Prepare fixes for all supported versions
4. Release new versions as soon as possible

## Comments on this Policy

If you have suggestions on how this process could be improved, please submit a pull request.
