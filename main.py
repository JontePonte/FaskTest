from website import create_app

app = create_app()
DEBUG_MODE = True

if __name__ == '__main__':
    if DEBUG_MODE:
        app.run(debug=True)
    else:
        app.run(debug=False)
