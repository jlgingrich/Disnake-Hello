# Disnake-Docker

This container image provides a simple way to develop Discord bots using the [Disnake](https://docs.disnake.dev/en/stable/index.html) Python library.

In addition to `disnake` and its requirements, this image also contains the community libraries `disnake-ext-plugins` and `disnake-ext-components`.

## Use

The easiest way to use this image is to create a `docker-compose.yaml` like the one below:

```yaml
name: my-disnake-container

volumes:
  data:
  logs:

services:
  core:
    container_name: core
    build:
      dockerfile_inline: |
        FROM jlgingrich/disnake
        COPY ./exts ./exts
    env_file:
      - .env
    volumes:
      - data:/app/data
      - logs:/app/logs
```

The `dockerfile_inline` copies a local folder of [Disnake Extensions](https://docs.disnake.dev/en/stable/ext/commands/extensions.html) into the container, which are automatically loaded on container start.

The `.env` file contains the `DISCORD_TOKEN` used by the bot to connect to Discord and can contain other environment variables used to modify the image. See [example.env](./example.env) for the other suggested environment variables. If the `.env` file is misconfigured, the container will receive a `ConfigurationError` and indicate which environment variable needs adjustment.

## Example

See [Disnake-Hello](https://github.com/jlgingrich/Disnake-Hello) for a repo to clone for easy bot development.


## Structure
```
app
├── common.py
├── bot.py
├── main.py
├── exts
│   ├── examples.py
│   └── ...
├── data
│   └── ...
└── logs
    └── ...
```

### `common.py`
This module defines variables that are used by `main.py` and provide a standard import for cogs. This module should not be directly edited, but can be imported from any cog in `/app/cogs` or a custom `bot.py` and provides 

### `bot.py`
This module defines the 'bot' instance used by the container. For most cogs, this file doesn't need to be changed. However, it can be overridden with a different file to have `main.py` use a different subclass of `disnake.Client`. See [bot.py](./bot.py) for more details.

### `main.py`
This module is executed by the container to load the cogs and run the bot. This module should not be directly edited, and represents the primary automation component provided by this image.

### `/app/exts`
This directory is where extensions should be copied to. At container start, the bot will attempt to load any extensions in this folder.

### `/app/data`
This is a volume where persistant data can be stored by the bot. This is not used by this base image but can be used by custom bot implementations or extensions.

### `/app/logs`
This is a volume where persistant logs can be stored by the bot. The default logging configuration provided by the base image puts a timed rotating log here named `disnake-core.log`.

## Building

The [Makefile](./Makefile) in this repository can build the latest image, create a Python venv in the current folder for development, and clean local Docker images.