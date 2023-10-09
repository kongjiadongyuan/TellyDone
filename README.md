# TellyDone

A simple tool that notifies you when something happens via `apprise`.

This tool is still in a very early stage of development and is used for my own work.

## Install

```bash
pip install git+https://github.com/kongjiadongyuan/TellyDone.git
```

## Config File

Configuration files are read according to the following priorities

- ~/.telly_done
- /etc/telly_done

```yaml
apprise_url:
    - schan://xxxxxxxx/
```

Apprise_url must conform to apprise's format


## Future Work

- [ ] Interactively create configuration files
- [ ] Notify when specific `process` ends