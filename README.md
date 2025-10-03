# Gravelfinder Notes

## Packaging Docker Image

```
docker build . -t gravelfinder:<tag>
```

Run locally in docker

```
docker run --env GOOGLE_API_KEY=<GOOGLE_API_KEY> -p 8080:5000 -p 9090:9090 gravelfinder:<tag>
```

## Pushing to a registry

```
docker tag gravelfinder:<tag> myregistry.example.come/gravelfinder:<tag>
```