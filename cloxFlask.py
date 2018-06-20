import sys
sys.path.insert(0, './scripts')

from flask import Flask
import startClox as sc

clox = Flask(__name__)

@clox.route('/')
def runClox():
    return sc.startClox()


if __name__ == "__main__":
    clox.run(host='0.0.0.0')

