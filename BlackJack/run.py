#! /usr/bin/env python
from flask import Flask
from jeu import app

if __name__ == "__main__":
    app.run(debug=True)