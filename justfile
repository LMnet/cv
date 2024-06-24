# Caveat regarding python virtual environments:
# when you need to create a recipe that requires a virtual environment
# you should write it with `#!/usr/bin/env bash`.

ROOT := justfile_directory()
VENV := ROOT / ".venv"
BIN := VENV / "bin"
TARGET := ROOT / "target"

# Prepare repository for local development: setup virtual environment and install dependencies
bootstrap:
  #!/usr/bin/env bash
  python3.11 -m venv {{VENV}}
  source {{BIN}}/activate
  pip install -r requirements.txt

# Clean everything, including virtual environment
clean:
  rm -rf {{VENV}}
  rm -rf {{TARGET}}


# Run supplied command through `pip` from virtual environment
pip *command:
  #!/usr/bin/env bash
  source {{BIN}}/activate
  pip {{command}}

# Run this when you add a new dependency in `requirements.txt` file.
new_dependency:
  #!/usr/bin/env bash
  source {{BIN}}/activate
  pip install -r requirements.txt
  pip freeze > constraints.txt
