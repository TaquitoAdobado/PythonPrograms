''' En este archivo importamos todas las clases que se usaran en el proyecto.
De esta forma podemos acceder a las clases desde app.py de manera mas sencilla.
ejemplo: 
    from models import User, Product
en vez de:
    from models.user import User
    from models.product import Product
'''

from .user import User