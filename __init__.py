from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    name = request.args.get('name')
    message = request.args.get('message')
    return (f'Hello {name}! {message}!')

def main():
    app.run()
if __name__ == "__main__":
    main
    