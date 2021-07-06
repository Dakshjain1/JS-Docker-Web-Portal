# Instructions to setup & use our JS-Docker-Web-Portal

First setup an Apache web server & install Docker.  
I have setup in RHEL 8.  

```
# yum install httpd -y
# yum install docker-ce -y
# setenforce 0 // or create an SELINUX rule for apache group to access docker
- create an entry in sudoers file
# vim /etc/sudoers
...
apache	ALL=(ALL:ALL) NOPASSWD: ALL
...
# systemctl start httpd 
# systemctl enable httpd 
# systemctl start docker 
# systemctl enable docker 
```
Then put the html folder from this repo into /var/www/html
```
cp -rf ./html/*  var/www/html/
```
Put the cgi-bin folder into /var/www/cgi-bin
```
cp -rf ./cgi-bin/*  var/www/cgi-bin/
```
Apache service should be running on port 80 by default (you can change it as well)
Then easily use the site - 
```
http://IP:80/JSDockerWebsite/index.html
```
Then you can use the portal to - 
* launch docker containers
* remove docker containers
* stop docker containers
* list all docker containers with status (running or stopped)
* list all available images in the server

We provide a cute Docker scale which keeps you updated about the number of docker containers running in the server.  
Rest you can explore in the images below - 
![docker_website](https://miro.medium.com/max/2000/1*3VvUa9guUgJFQgavEGSEcQ.png)
