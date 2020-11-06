import redis

r = redis.Redis(host='127.0.0.1',port = 6379,db=0)


task = '%s_%s_%s_%s' % ('sendMail','123@tedu.com','456@tedu.com','hell word')



r.lpush('pyl1',task)


