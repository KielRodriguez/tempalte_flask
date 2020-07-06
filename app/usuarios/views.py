from . import usuarios

@usuarios.route('/')
def index():
    return "This is an example app"