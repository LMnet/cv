# Caveat regarding python virtual environments:
# when you need to create a recipe that requires a virtual environment
# you should write it with `#!/usr/bin/env bash`.

ROOT := justfile_directory()
VENV := ROOT / ".venv"
BIN := VENV / "bin"

# Prepare repository for local development: setup virtual environment and install dependencies
bootstrap:
  #!/usr/bin/env bash
  python3.11 -m venv {{VENV}}
  source {{BIN}}/activate
  pip install --requirement requirements.txt --constraint constraints.txt

# Clean everything, including virtual environment
clean:
  rm -rf {{VENV}}

# Run this when you add a new dependency in `requirements.txt` file.
new_dependency:
  #!/usr/bin/env bash
  source {{BIN}}/activate
  pip install --requirement requirements.txt --constraint constraints.txt
  pip freeze > constraints.txt

# Regenerate `constraints.txt` file. Useful when dependencies were changed or deleted.
freeze:
  #!/usr/bin/env bash
  source {{BIN}}/activate
  pip install --requirement requirements.txt
  pip freeze > constraints.txt

# Update dependencies.
update:
  #!/usr/bin/env bash
  source {{BIN}}/activate
  pip install --requirement requirements.txt --constraint constraints.txt

# Build everything.
build:
  #!/usr/bin/env bash
  source {{BIN}}/activate
  python {{ROOT}}/src/build.py
