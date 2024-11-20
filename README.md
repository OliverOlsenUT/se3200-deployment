#GUIDE FOR WORKING APPLICATION
#SITE SHOULD BE ACCESSIBLE AT oo.coureur.life NO OTHER CHANGES NEED TO BE MADE
**Apply Docker Files**
```
Ensure docker is installed.
Dockerfiles are located in their correct directories. No need to change or update them.
Use docker-compose up -d in order to build these files. This should be used for local testing.
Any changes made to Dockerfile and images were updated with the following commands:

docker tag example YOUR-USER-NAME/example
docker push YOUR-USER-NAME/example
```
**Apply the YAML Files**
   Ensure your Kubernetes is running and configured. Then apply the YAML files:
```
kubectl apply -f frontend.yaml
kubectl apply -f backend.yaml
kubectl apply -f ingress.yaml
Ingress is already set and the site should be accessible at https://oo.coureur.life/
Docker images are also configuired and can be accessed at austin963/frontend and austin963/backend on dockerhub
```

# Recommended Switch Games
An application to display, edit, add, and delete recommended switch games from the database. Documentation based on https://github.com/csse3200/markdown-example.

## Resource

**Game**

Attributes:

* name (string)
* review (string)
* genres (string)
* cost (double)
* esrb_rating (string)

## Schema

```sql
CREATE TABLE games (
id INTEGER PRIMARY KEY,
name TEXT,
review TEXT,
genres TEXT,
cost DOUBLE,
esrb_rating TEXT);
```

## REST Endpoints

Name                           | Method | Path
-------------------------------|--------|------------------
Retrieve game collection | GET    | /games
Retrieve game member     | GET    | /games/*\<id\>*
Create game member       | POST   | /games
Update game member       | PUT    | /games/*\<id\>*
Delete game member       | DELETE | /games/*\<id\>*
