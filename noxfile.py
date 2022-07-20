"""Configuration of nox for testing & code validation."""

import tempfile

from nox_poetry import Session, session

PYTHON_VERSION = "3.9"


@session(python=PYTHON_VERSION)
def lint(session: Session) -> None:
    """Runs linting checks."""
    session.install(
        "flake8",
        "flake8-docstrings",
        "flake8-import-order",
        "flake8-black",
        "darglint",
        "flake8-annotations",
        "flake8-quotes",
        "flake8-requirements",
        "pep8-naming",
        "flake8-bugbear",
        "flake8-bandit",
    )
    session.run("flake8", "src/")
    session.run("flake8", "./all_the_names.py")


@session(python=PYTHON_VERSION)
def mypy(session: Session) -> None:
    """Runs static type checking analysis."""
    session.install("mypy", "types-requests", "types-pytz", "lxml")
    session.run("mypy", "--txt-report", "mypy_report.txt")


@session(python=PYTHON_VERSION)
def safety(session: Session) -> None:
    """Use safety to check for vulnerability in project dependencies."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")
