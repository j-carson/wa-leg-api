import nox

TESTED_PYTHONS = ["3.8", "3.9", "3.10", "3.11"]
nox.options.pythons = TESTED_PYTHONS
nox.options.error_on_external_run = True


@nox.session(python=TESTED_PYTHONS)
def test(session):
    session.install("-e", ".[dev]")
    session.run("pre-commit", "run", "--all-files")
    session.run("pytest", "tests")
