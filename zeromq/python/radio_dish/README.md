# ZeroMQ - RADIO/DISH - Example

## Build

```shell
cpk build
```

## Run DISH node

```shell
cpk run -L dish --name dish
```

## Run RADIO node

```shell
cpk run -L radio --name radio -- --link dish
```
