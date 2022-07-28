# nnmi-autoactionscript

## Send message to slack

### usage

- set OS environment

```
export WEBHOOK_URL=https://hooks.slack.com/services/foobar
```

- command options

```
slack.py --nodename ${NodeName} --incidentmessage ${IncidientMessage}
```

- output sample

```
$ python3 slack.py --nodename hostname --incidentmessage Node_Down

hostname: Node_Down
```

