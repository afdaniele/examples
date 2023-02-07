# ZeroMQ - PUB/SUB - Example

## Build

```shell
cpk build
```

## Run PUB node

```shell
cpk run -L pub --name pub
```

## Run SUB node

```shell
cpk run -L sub --name sub -- --link pub
```
