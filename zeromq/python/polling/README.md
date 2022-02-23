# ZeroMQ - POLLING (Pair/Pair) - Example

## Build

```shell
cpk build
```

## Run PAIR (server) node

```shell
cpk run -L server --name peer
```

## Run POLLING (client) node

```shell
cpk run -L client --name peer1 -- --link peer
```
