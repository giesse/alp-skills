import os


DEFAULT_TIMEOUT_SECONDS = 30


def local_config_path() -> str | None:
    return os.environ.get("APP_CONFIG_PATH")
