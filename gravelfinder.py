from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('embedded_map.html')

def main():
    pass

if __name__ == '__main__':
    main()
