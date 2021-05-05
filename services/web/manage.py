from flask.cli import FlaskGroup
from project import app

cli = FlaskGroup(app)

if __name___ == "__main__":
    cli()
