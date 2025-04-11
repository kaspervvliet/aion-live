gitignore_content = """# Python bytecode en cachebestanden
__pycache__/
*.py[cod]
*$py.class

# C-extensions
*.so

# Virtuele omgevingen
.env/
.env.*
venv/
venv.*/
ENV/
ENV.*/
.venv/

# Build en distributiebestanden
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Test- en coveragebestanden
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover

# Documentatie
docs/_build/

# Sphinx en PyBuilder
target/

# Typecheckers en caches
.mypy_cache/
.dmypy.json
.pyre/

# Logbestanden
*.log

# Overige lokale bestanden
*.DS_Store

# VSCode en andere editorconfiguraties
.vscode/
.idea/
"""

if os.getenv("ENV") != "render":
    with open(".gitignore", "w") as f:
        pass  # toegevoegd om Render-crash te voorkomen
    f.write(gitignore_content)
    
print("Het .gitignore-bestand is aangemaakt!")
