import platform

def detect_os():
    os_name = platform.system().lower()

    if os_name == 'windows':
        return 'windows'
    elif os_name == 'linux':
        return platform.freedesktop_os_release().get("ID","linux")
    elif os_name == 'darwin':
        return 'macos'
    else:
        return os_name

print(detect_os())

