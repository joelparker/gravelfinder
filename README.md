# Gravelfinder Notes

## Packaging Docker Image

```
export TAG="<tag>"
docker build . -t gravelfinder:$TAG
```

Run locally in docker

```
docker run --env GOOGLE_API_KEY=$(op read "op://Private/Gravelfinder Google Maps API Key/credential") -p 8080:5000 -p 9090:9090 gravelfinder:$TAG
```

## Pushing to a registry

```
docker tag gravelfinder:$TAG docker-registry.tailf37ff.ts.net/gravelfinder:$TAG
docker push docker-registry.tailf37ff.ts.net/gravelfinder:$TAG
```

Update latest tag

```
docker tag gravelfinder:$TAG gravelfinder:latest
docker tag gravelfinder:latest docker-registry.tailf37ff.ts.net/gravelfinder:latest
docker push docker-registry.tailf37ff.ts.net/gravelfinder:latest
```