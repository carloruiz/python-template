import os

config = {
    'PRODUCTION'        : True,
    'FLASK_APP'         : '',
    'FLASK_ENV'         : 'production',
    'SECRET_ENV'        : os.environ['SECRET_KEY'],
    
    'DEV_ORIGIN'        : 'http://localhost:3000',
    'PRODUCTION_ORIGIN' : '',
    
    'DB_NAME'           : '',
    'DB_USER'           : '',
    'DB_HOST'           : '',
    'DB_URI_LOCAL'      : 'postgresql://carloruiz@localhost:5432/[DB_NAME]'
}

config['ORIGIN'] = config['PRODUCTION_ORIGIN'] if config['PRODUCTION'] else config['DEV_ORIGIN'] 
#config['ORIGIN'] = config['DEV_ORIGIN']
config['DB_URI_PRODUCTION'] = 'postgresql://{}:{}@{}:5432/{}'.format(
                                    config["DB_USER"], os.environ['DB_PASSWORD'], 
                                    config["DB_HOST"], config["DB_NAME"])
config['DB_URI'] = config['DB_URI_PRODUCTION'] if config['PRODUCTION'] else config['DB_URI_LOCAL']

print(config)
