import platform


def machine_info() -> dict:
    os_name = platform.system()
    os_release = platform.release()
    os_architecture = platform.machine()
    language_version = ".".join(platform.python_version_tuple())

    info = {
        "name": os_name,
        "release": os_release,
        "architecture": os_architecture,
        "version": language_version,
    }

    return info


if __name__ == "__main__":
    machine_info()
