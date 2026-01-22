# CI/CD Pipeline with GitHub Actions & Python

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![pytest](https://img.shields.io/badge/pytest-Testing-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org/)
[![Coverage](https://img.shields.io/badge/coverage-monitored-brightgreen)](https://coverage.readthedocs.io/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

## Descripción

Proyecto demostrativo de un **pipeline CI/CD completo** utilizando **GitHub Actions** y **Python**. Implementa las mejores prácticas de integración y despliegue continuo, incluyendo tests automatizados, cobertura de código, y validaciones de calidad.

## Características

- **Tests Automatizados**: Suite completa de tests unitarios con pytest
- **Cobertura de Código**: Análisis de cobertura con coverage.py
- **CI/CD Completo**: Pipeline automatizado con GitHub Actions
- **Quality Gates**: Validaciones de calidad antes de merge
- **Código Limpio**: Seguimiento de PEP 8 y buenas prácticas
- **Deploy Automático**: Despliegue automatizado en cada push a main

## Arquitectura del Pipeline

```
┌─────────────────────────────────────────────────────────┐
│              GitHub Repository                          │
│                                                          │
│  Push/PR to main                                        │
└────────────┬────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────┐
│           GitHub Actions Workflow                       │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  1. Setup Environment                            │  │
│  │     • Checkout code                              │  │
│  │     • Setup Python 3.x                           │  │
│  │     • Cache dependencies                         │  │
│  └──────────────────────────────────────────────────┘  │
│                       ▼                                  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  2. Install Dependencies                         │  │
│  │     • pip install -r requirements.txt            │  │
│  └──────────────────────────────────────────────────┘  │
│                       ▼                                  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  3. Run Tests                                    │  │
│  │     • pytest OperationsTest.py                   │  │
│  │     • Generate test reports                      │  │
│  └──────────────────────────────────────────────────┘  │
│                       ▼                                  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  4. Code Coverage                                │  │
│  │     • coverage run -m pytest                     │  │
│  │     • coverage report                            │  │
│  │     • Validate minimum coverage threshold        │  │
│  └──────────────────────────────────────────────────┘  │
│                       ▼                                  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  5. Code Quality                                 │  │
│  │     • Linting (flake8/pylint)                    │  │
│  │     • Security checks                            │  │
│  └──────────────────────────────────────────────────┘  │
│                       ▼                                  │
│  ┌──────────────────────────────────────────────────┐  │
│  │  6. Build & Deploy (if all pass)                │  │
│  │     • Build artifacts                            │  │
│  │     • Deploy to environment                      │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
└─────────────────────────────────────────────────────────┘
             │
             ▼
      Success / Failure
      (Notifications & Reports)
```

## Stack Tecnológico

### Core
- **Python 3.x** - Lenguaje de programación
- **pytest** - Framework de testing
- **coverage.py** - Análisis de cobertura de código

### CI/CD
- **GitHub Actions** - Automatización de workflows
- **GitHub Secrets** - Gestión segura de credenciales

### Quality Tools (opcional)
- **flake8** - Linting y estilo de código
- **pylint** - Análisis estático de código
- **bandit** - Análisis de seguridad
- **black** - Formateo automático de código

## Estructura del Proyecto

```
.
├── .github/
│   └── workflows/
│       ├── ci.yml                 # Pipeline de integración continua
│       └── cd.yml                 # Pipeline de despliegue continuo
│
├── Operations.py                  # Módulo con operaciones matemáticas
├── OperationsTest.py              # Tests unitarios
├── main.py                        # Punto de entrada de la aplicación
├── __init__.py                    # Inicializador del paquete
│
├── requirements.txt               # Dependencias del proyecto
├── .coverage                      # Datos de cobertura
├── .gitignore                     # Archivos ignorados por Git
└── LICENSE                        # Licencia Apache 2.0
```

## Pre-requisitos

### Para Desarrollo Local
- Python 3.8 o superior
- pip (gestor de paquetes)
- git

### Para CI/CD
- Cuenta de GitHub
- Repositorio con Actions habilitado

## 🔧 Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/SergioCMDev/CI-CD-to-execute-Pipeline-with-GithubActions.git
cd CI-CD-to-execute-Pipeline-with-GithubActions
```

### 2. Crear Entorno Virtual (Recomendado)
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate

# En Windows:
venv\Scripts\activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la Aplicación
```bash
python main.py
```

## Testing

### Ejecutar Tests
```bash
# Ejecutar todos los tests
pytest

# Ejecutar tests con verbose
pytest -v

# Ejecutar tests específicos
pytest OperationsTest.py

# Ejecutar con salida detallada
pytest -vv
```

### Cobertura de Código
```bash
# Ejecutar tests con cobertura
coverage run -m pytest

# Ver reporte en terminal
coverage report

# Generar reporte HTML
coverage html

# Abrir reporte en navegador
open htmlcov/index.html  # Mac
start htmlcov/index.html # Windows
xdg-open htmlcov/index.html # Linux
```

### Ejemplo de Salida
```bash
$ pytest -v
======================== test session starts ========================
platform linux -- Python 3.9.7, pytest-7.4.0
collected 5 items

OperationsTest.py::test_sum PASSED                           [ 20%]
OperationsTest.py::test_subtract PASSED                      [ 40%]
OperationsTest.py::test_multiply PASSED                      [ 60%]
OperationsTest.py::test_divide PASSED                        [ 80%]
OperationsTest.py::test_divide_by_zero PASSED               [100%]

======================== 5 passed in 0.03s ==========================
```

## Pipeline CI/CD

### GitHub Actions Workflow

El proyecto incluye workflows automatizados que se ejecutan en cada push o pull request:

#### Workflow de CI (Integración Continua)
```yaml
name: CI Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        cache: 'pip'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        pytest -v
    
    - name: Generate coverage report
      run: |
        coverage run -m pytest
        coverage report
        coverage xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
```

#### Workflow de CD (Despliegue Continuo)
```yaml
name: CD Pipeline

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    needs: test  # Solo se ejecuta si los tests pasan
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to production
      run: |
        echo "Deploying to production..."
        # Aquí irían los comandos de despliegue
```

### Status Badges

Puedes añadir badges al README para mostrar el estado del pipeline:

```markdown
![CI Status](https://github.com/SergioCMDev/CI-CD-to-execute-Pipeline-with-GithubActions/workflows/CI%20Pipeline/badge.svg)
![Coverage](https://codecov.io/gh/SergioCMDev/CI-CD-to-execute-Pipeline-with-GithubActions/branch/main/graph/badge.svg)
```

## Code Quality

### Linting con flake8
```bash
# Instalar flake8
pip install flake8

# Ejecutar linting
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# Con configuración personalizada
flake8 . --count --max-line-length=100 --statistics
```

### Formateo con black
```bash
# Instalar black
pip install black

# Verificar formato
black --check .

# Aplicar formato
black .
```

### Análisis de Seguridad con bandit
```bash
# Instalar bandit
pip install bandit

# Ejecutar análisis
bandit -r . -ll
```

## Secrets y Variables de Entorno

### Configurar GitHub Secrets

1. Ve a tu repositorio en GitHub
2. Settings → Secrets and variables → Actions
3. Click en "New repository secret"
4. Añade los secrets necesarios:
   - `DEPLOY_TOKEN`
   - `API_KEY`
   - Otros según necesites

### Usar Secrets en Workflows
```yaml
- name: Deploy
  env:
    DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
  run: |
    ./deploy.sh
```

## 📈 Mejores Prácticas Implementadas

### Testing
- Tests unitarios para todas las funciones
- Tests de casos edge (división por cero, etc.)
- Cobertura de código > 80%
- Tests aislados e independientes

### CI/CD
- Ejecución automática en cada push
- Tests antes de merge
- Deploy solo si tests pasan
- Notificaciones de estado

### Code Quality
- Seguimiento de PEP 8
- Documentación de funciones
- Manejo de errores
- Código limpio y mantenible

##  Casos de Uso

Este proyecto es ideal para:

-  **Aprendizaje**: Entender CI/CD desde cero
-  **Referencia**: Template para nuevos proyectos
-  **Experimentación**: Probar diferentes herramientas CI/CD
-  **Portfolio**: Demostrar conocimientos DevOps
-  **Base**: Punto de partida para proyectos reales

## Workflow Típico

### Para Desarrolladores

```bash
# 1. Crear rama feature
git checkout -b feature/nueva-funcionalidad

# 2. Desarrollar y testear localmente
python main.py
pytest

# 3. Commit y push
git add .
git commit -m "feat: añadir nueva funcionalidad"
git push origin feature/nueva-funcionalidad

# 4. Crear Pull Request
# GitHub Actions ejecutará automáticamente:
# - Tests
# - Cobertura
# - Linting

# 5. Merge a main (si todos los checks pasan)
# Se ejecutará automáticamente el CD pipeline
```

## Métricas y Reportes

### Coverage Report
El pipeline genera reportes de cobertura que puedes ver en:
- Terminal durante la ejecución
- Archivo `.coverage`
- Reportes HTML en `htmlcov/`
- Codecov (si está configurado)

### Test Reports
Los resultados de los tests incluyen:
- Número de tests ejecutados
- Tests pasados/fallados
- Tiempo de ejecución
- Detalles de fallos

## Troubleshooting

### Tests Fallan Localmente pero Pasan en CI
```bash
# Verificar versión de Python
python --version

# Reinstalar dependencias
pip install -r requirements.txt --force-reinstall

# Limpiar caché
pytest --cache-clear
```

### Pipeline Falla en GitHub Actions
```bash
# Verificar logs en:
# Repository → Actions → Failed workflow → Job → Step

# Verificar secrets configurados
# Settings → Secrets and variables → Actions
```

### Problemas de Cobertura
```bash
# Ejecutar con verbose
coverage run -m pytest -v

# Ver archivos no cubiertos
coverage report --show-missing
```

## Próximas Mejoras

- [ ] Añadir integración con SonarQube
- [ ] Implementar tests de integración
- [ ] Añadir performance tests
- [ ] Configurar pre-commit hooks
- [ ] Añadir Docker support
- [ ] Implementar deployment a diferentes entornos
- [ ] Añadir badges de calidad del código
- [ ] Configurar dependabot para actualizaciones

## Recursos Adicionales

### Documentación
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [pytest Documentation](https://docs.pytest.org/)
- [coverage.py](https://coverage.readthedocs.io/)
- [Python Testing Best Practices](https://docs.python-guide.org/writing/tests/)

### Tutoriales Recomendados
- [GitHub Actions Tutorial](https://lab.github.com/githubtraining/github-actions:-hello-world)
- [Pytest Tutorial](https://realpython.com/pytest-python-testing/)
- [CI/CD Best Practices](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)

## Contribuciones

¡Las contribuciones son bienvenidas! Para contribuir:

1. Fork el proyecto
2. Crea una rama feature (`git checkout -b feature/mejora`)
3. Asegúrate de que los tests pasan (`pytest`)
4. Verifica la cobertura (`coverage run -m pytest`)
5. Commit tus cambios (`git commit -m 'feat: añadir mejora'`)
6. Push a la rama (`git push origin feature/mejora`)
7. Abre un Pull Request

### Guía de Estilo
- Seguir PEP 8
- Añadir docstrings a funciones nuevas
- Escribir tests para nuevo código
- Mantener cobertura > 80%

## Licencia

Este proyecto está bajo la Licencia Apache 2.0. Ver archivo [LICENSE](LICENSE) para más detalles.

## Autor

**Sergio Cristauro Manzano**

- GitHub: [@SergioCMDev](https://github.com/SergioCMDev)
- LinkedIn: [Sergio Cristauro](https://www.linkedin.com/in/sergio-cristauro/)
- Email: sergiocmdev@gmail.com

##  Proyectos Relacionados

Este proyecto forma parte de mi portfolio DevOps:

- [Infra-AWS-EKS-Python](https://github.com/SergioCMDev/Infra-AWS-EKS-Python) - Infraestructura EKS con Terraform
- [PythonWebForIAC](https://github.com/SergioCMDev/PythonWebForIAC) - Aplicación Python para IaC
- [Wordpress-AWS-Terraform](https://github.com/SergioCMDev/Wordpress-and-phpMyAdmin-with-Terraform-and-AWS) - WordPress en AWS con IaC

##  Agradecimientos

- GitHub Actions team por la plataforma
- pytest community
- Python Software Foundation
- Open source community

---

 **Si este proyecto te ha sido útil, considera darle una estrella**

📚 **¿Aprendiendo CI/CD?** Este proyecto es un excelente punto de partida

💬 **¿Preguntas?** Abre un issue o contáctame directamente
