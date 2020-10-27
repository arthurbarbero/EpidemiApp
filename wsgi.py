import sys 

from src.main import app, init_database


if __name__ == "__main__":

    if 'init_db' in sys.argv:
        init_database(app)

    app.run(debug=False)