Q: find out why ```django-admin dumpdata --format yaml``` raise an exception
A: django serializer import yaml, which is not a dependency of django, ```pip install pyyaml``` fix this problem