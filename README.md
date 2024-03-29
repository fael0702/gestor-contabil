## Como executar

### Copiar o arquivo .env.sample para o .env

```
cp .env.sample .env
```

### Criar e executar containers

#### Realizar o build na primeira vez

```
docker-compose -f docker-compose-dev.yml up --build
```

#### subir o container

```
docker-compose -f docker-compose-dev.yml up -d
```

### Migrations

#### Checar historico do alembic

```
docker exec -it gestor-contabil-api alembic history
```

#### Criar uma migration

```
docker exec -it gestor-contabil-api alembic revision --autogenerate -m "My migration"
```

#### Merging duas ou mais Migrations de diferentes Branches

```
docker exec -it gestor-contabil-api alembic merge heads -m "Merge heads"
```

#### Executar Migrations

```
docker exec -it gestor-contabil-api alembic upgrade head
```
