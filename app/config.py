class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL= 'https://api.themoviedb.org/3/movie/550?api_key=1a525dff9a6e960c06b72a3224a2a02d'



class ProdConfig(Config):
    '''
    Pruduction  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    DEBUG = True
