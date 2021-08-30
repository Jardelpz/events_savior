from flask import Flask
from src.utils.urls import make_resources
from src.utils.settings import ELASTIC_APM
from src.utils.apm import apm

app = Flask(__name__)
app.debug = True
app.url_map.strict_slashes = False
app.config['ELASTIC_APM'] = ELASTIC_APM
app.config['DEBUG'] = True

apm.init_app(app)
make_resources(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
