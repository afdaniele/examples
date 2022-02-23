# ZeroMQ - PAIR/PAIR - Example

## Build

```shell
cpk build
```

## Run PAIR (server) node

```shell
cpk run -L server --name peer
```

## Run PAIR (client) node

```shell
cpk run -L client --name peer1 -- --link peer
```
