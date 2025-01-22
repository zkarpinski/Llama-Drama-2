init:
    poetry install

lab:
    poetry run jupyter lab

test:
    . $(pwd)/test.env && poetry run pytest tests/
