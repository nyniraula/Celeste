import shutil


class DependencyResolver:
    def __init__(self):
        self.ffmpeg = self.has_ffmpeg()
        self.js_runtimes = self.has_js_runtimes()

    def _check_existence(self, tool):
        """Returns the path if the tool exists, if not returns false"""
        return shutil.which(tool)

    def has_ffmpeg(self):
        return self._check_existence("ffmpeg")

    def has_js_runtimes(self):
        return {
            "deno": {"path": self._check_existence("deno")},
            "node": {"path": self._check_existence("node")},
        }
