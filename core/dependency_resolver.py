import shutil


class DependencyResolver:
    def __init__(self):
        self.ffmpeg = self.has_ffmpeg()
        self.js_runtime = self.has_js_runtime()

    def _check_existence(self, tool):
        """Returns the path if the tool exists, if not returns false"""
        return shutil.which(tool)

    def has_ffmpeg(self):
        return self._check_existence("ffmpeg")

    def has_js_runtime(self):
        """returns the first truthy value, if both are Falsy -> returns the last one which is None"""
        return self._check_existence("deno") or self._check_existence("node")
