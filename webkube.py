#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

inpp = cgi.FieldStorage()
y = inpp.getvalue("x").lower()

# List all the pods
if ('list' in y or 'show' in y or 'get' in y) and ('pod' in y or 'pods' in y):    
    cmd = "sudo kubectl get pods --kubeconfig admin.conf"
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))



# Launch a Pod
elif ('run' in y or 'create' in y or 'launch' in y) and ('pod' in y or 'pods' in y):
    str = y.split()
    if 'pod' in str:
        i = str.index(('pod')) + 1
    elif 'pods' in str:
        i = str.index('pods') + 1
    cmd = "sudo kubectl run {0} --image=vimal13/apache-webserver-php --kubeconfig admin.conf".format(str[i])
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))


# List all resourses
elif ('list' in y or 'show' in y or 'get' in y) and ('every' in y or 'all' in y) and ('resources' in y or 'resource' in y):    
    cmd = "sudo kubectl get all --kubeconfig admin.conf"
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# Launch Deployment
elif ('deployment' in y or 'deploy' in y) and ('create' in y or 'launch' in y):
    str = y.split()
    if 'deployment' in str:
        i = str.index(('deployment')) + 1
    elif 'deploy' in str:
        i = str.index('deploy') + 1
    cmd = "sudo kubectl create deployment {0} --image=vimal13/apache-webserver-php --kubeconfig admin.conf".format(str[i])
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# Expose deployment
elif ('deployment' in y or 'deploy' in y) and ('expose' in y or 'service' in y or 'services' in y) and ('port' in y):
    str = y.split()
    if 'deployment' in str:
        i = str.index(('deployment')) + 1
    elif 'deploy' in str:
        i = str.index('deploy') + 1
    port = str.index('port') + 1
    cmd = "sudo kubectl expose deployment {0} --port={1} --type=NodePort --kubeconfig admin.conf".format(str[i], str[port])
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# Scale deployment
elif ('deployment' in y or 'deploy' in y) and ('scale' in y or 'replica' in y or 'replicas' in y):
    str = y.split()
    if 'deployment' in str:
        i = str.index('deployment') + 1
    elif 'deploy' in str:
        i = str.index('deploy') + 1
    j = str.index('to') + 1
    cmd = "sudo kubectl scale deployment {0} --replicas={1} --kubeconfig admin.conf".format(str[i], str[j])
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# Delete deployment
elif ('deployment' in y or 'deploy' in y) and ('delete' in y or 'remove' in y):
    str = y.split()
    if 'deployment' in str:
        i = str.index(('deployment')) + 1
    elif 'deploy' in str:
        i = str.index('deploy') + 1
    cmd = "sudo kubectl delete deploy {} --kubeconfig admin.conf".format(str[i])
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# Get all deployment
elif ('list' in y or 'show' in y or 'get' in y) and ('every' in y or 'all' in y) and ('deploy' in y or 'deployment' in y):    
    cmd = "sudo kubectl get deployment --kubeconfig admin.conf"
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# List Services
elif ('list' in y or 'show' in y or 'get' in y) and ('svc' in y or 'services' in y or 'service' in y):    
    cmd = "sudo kubectl get svc --kubeconfig admin.conf"
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# Delete Service
elif ('deployment' in y or 'deploy' in y) and ('expose' in y or 'service' in y or 'services' in y) and ('delete' in y or 'remove' in y):
    str = y.split()
    if 'deployment' in str:
        i = str.index(('deployment')) + 1
    elif 'deploy' in str:
        i = str.index('deploy') + 1
    cmd = "sudo kubectl delete svc {} --kubeconfig admin.conf".format(str[i])
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# delete all resourses
elif ('delete' in y or 'terminate' in y) and ('every' in y or 'all' in y) and ('resources' in y or 'resource' in y):    
    cmd = "sudo kubectl delete all --all --kubeconfig admin.conf"
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

else:
    print("Invalid Request")
