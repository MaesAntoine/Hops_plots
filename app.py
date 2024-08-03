from flask import Flask
import ghhops_server as hs
import importlib
import pkgutil

app = Flask(__name__)
hops = hs.Hops(app)

def import_components(package_name):
    components = []
    package = importlib.import_module(package_name)
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f'{package_name}.{module_name}')
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type) and hasattr(attr, 'register'):
                components.append(attr)
    return components

def register_components():
    for package in ['components.data', 'components.plots']:
        for component in import_components(package):
            component.register(hops)

if __name__ == "__main__":
    register_components()
    app.run(debug=False)