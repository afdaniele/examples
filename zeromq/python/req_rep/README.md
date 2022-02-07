# ZeroMQ - REQ/REP - Example

## Build

```shell
cpk build
```

## Run REP node

```shell
cpk run -L rep --name rep
```

## Run REQ node

```shell
cpk run -L req --name req -- --link rep
```
