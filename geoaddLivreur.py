#!/usr/bin/python3

#Import redis-py client package
import redis

#Connection information
redis_host = "localhost"
redis_port = 6379
redis_password = ""

def add_Delivery_Boy() :
    try:
        r = redis.Redis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        r.geoadd('StoreAppLivraison',4.861934,45.766797,'Livreur:6')
        print('Livreur ajouté!')
        print('Distance du Livreur 6 par rapport au Metro Gratte-Ciel :')
        print(r.geodist('StoreAppLivraison','Lieu:Metro Gratte-Ciel','Livreur:6'))
    except Exception as e:
        print(e)
if __name__ == '__main__':
    add_Delivery_Boy()
