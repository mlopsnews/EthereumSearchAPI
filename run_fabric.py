from fabric import Connection 
import os
import glob
x = glob.glob("./web/templates/*.html")
c = Connection("34.125.213.99", port=22, user="fady", connect_kwargs={'look_for_keys': False,'key_filename':'priv'})
for i in x:
    out =i.split("/")[-1]
    c.put(f"{i}",f"/home/fady/soild/web/templates/{out}")
res = c.run("sudo service uwsgi restart")
res = c.run("sudo service nginx restart")
res = c.run("sudo gcloud auth activate-service-account deployer --key-file=./key.json")
res = c.run("sudo gcloud app deploy --log-http --verbosity=debug --impersonate-service-account=fiverr")
print("Done")

