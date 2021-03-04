print('input the OS ..ubuntu or centos')
name = input()
print('input the application')
application = input()
if name == 'ubuntu':
   name_of_base = 'FROM ubuntu:18.04'
   distribution = 'debian'
elif name == 'centos':
     name_of_base = 'FROM centos:7'
     distribution = 'red hat'
print(name_of_base)
print(distribution)

if application == 'apache' and distribution == 'debian' :
   application_string = 'RUN apt-get update && \\ \n apt-get install -y apache2 apache2-utils && \\ \n apt-get clean && \\ \n rm -rf /var/lib/apt/lists/* \n EXPOSE 80 \n ENTRYPOINT ["apache2ctl"] \n CMD ["-DFOREGROUND"]'
elif application == 'apache' and distribution == 'red hat' :
     application_string = 'RUN yum update -y && yum install httpd httpd-tools -y \n\n  EXPOSE 80 \n\n CMD     ["/usr/sbin/httpd","-D","FOREGROUND"]'

def create_docker_file(name_of_base,application_string):
    dockerfile = open('Dockerfile','a')
    dockerfile.write(name_of_base + '\n' + application_string)
    dockerfile.close

create_docker_file(name_of_base,application_string)
#dockerfile = open('Dockerfile','a')
#dockerfile.write(name_of_base + '\n' + application_string)
#dockerfile.write('FROM ubuntu:18.04\n\n RUN apt-get update && \\ \n apt-get install -y apache2 apache2-utils && \\ \n apt-get clean && \\ \n rm -rf /varRUN apt-get update && \\ \n apt-get install -y apache2 apache2-utils && \\ \n apt-get clean && \\ \n rm -rf /var/lib/apt/lists/* \n EXPOSE 80 \n ENTRYPOINT ["apache2ctl"] \n CMD ["-DFOREGROUND"]/lib/apt/lists/* \n EXPOSE 80 \n ENTRYPOINT ["apache2ctl"] \n CMD ["-DFOREGROUND"]')

#dockerfile.write('FROM centos:7\n RUN yum update -y && yum install httpd httpd-tools -y \n\n  EXPOSE 80 \n\n CMD     ["/usr/sbin/httpd","-D","FOREGROUND"]')
#dockerfile.close
