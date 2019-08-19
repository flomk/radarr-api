

class SystemStatus(object):
    def __init__(self, *args, **kwargs):
        # super(CLASS_NAME, self).__init__(*args, **kwargs)
        self._version = kwargs.get("version", "")
        self._build_time = kwargs.get("buildTime", "")
        self._is_debug = kwargs.get("isDebug", "")
        self._is_production = kwargs.get("isProduction", "")
        self._is_admin = kwargs.get("isAdmin", "")
        self._is_user_interactive = kwargs.get("isUserInteractive", "")
        self._startup_path = kwargs.get("startupPath", "")
        self._app_data = kwargs.get("appData", "")
        self._os_version = kwargs.get("osVersion", "")
        self._is_mono_runtime = kwargs.get("isMonoRuntime", "")
        self._is_mono = kwargs.get("isMono", "")
        self._is_linux = kwargs.get("isLinux", "")
        self._is_osx = kwargs.get("isOsx", "")
        self._is_windows = kwargs.get("isWindows", "")
        self._branch = kwargs.get("branch", "")
        self._authentication = kwargs.get("authentication", "")
        self._sqlite_version = kwargs.get("sqliteVersion", "")
        self._url_base = kwargs.get("urlBase", "")
        self._runtime_version = kwargs.get("runtimeVersion", "")

    def __repr__(self):
        return "%s (%s)" % (self.__class__, self.__dict__)

    @property
    def version(self):
        return self._version

    @property
    def build_time(self):
        return self._build_time

    @property
    def is_debug(self):
        return self._is_debug

    @property
    def is_production(self):
        return self._is_production

    @property
    def is_admin(self):
        return self._is_admin

    @property
    def is_user_interactive(self):
        return self._is_user_interactive

    @property
    def startup_path(self):
        return self._startup_path

    @property
    def app_data(self):
        return self._app_data

    @property
    def os_version(self):
        return self._os_version

    @property
    def is_mono_runtime(self):
        return self._is_mono_runtime

    @property
    def is_mono(self):
        return self._is_mono

    @property
    def is_linux(self):
        return self._is_linux

    @property
    def is_osx(self):
        return self._is_osx

    @property
    def is_windows(self):
        return self._is_windows

    @property
    def branch(self):
        return self._branch

    @property
    def authentication(self):
        return self._authentication

    @property
    def sqlite_version(self):
        return self._sqlite_version

    @property
    def url_base(self):
        return self._url_base

    @property
    def runtime_version(self):
        return self._runtime_version
