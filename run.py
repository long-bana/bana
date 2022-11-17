from app import bana


@bana.route("/")
def hello_world():
    return "hello world!"


if __name__ == '__main__':
    bana.run("0.0.0.0", threaded=True, port=7777)
