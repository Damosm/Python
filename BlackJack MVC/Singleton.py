class  InheritableSingleton (object):
    # Dictionnaire Python référencant les instances déjà créés
    instances = {}
    def __new__(cls, *args, **kargs): 
        if InheritableSingleton.instances.get(cls) is None:
            InheritableSingleton.instances[cls] = object.__new__(cls, *args, **kargs)
        return InheritableSingleton.instances[cls]
    
    