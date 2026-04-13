import shutil


class DependencyResolver:
    def _check_existence(self, tool):
        """Returns the path if the tool exists, if not returns false"""
        path = shutil.which(tool)
        return path if bool(path) else False

    def has_ffmpeg(self):
        return self._check_existence("ffmpeg")

    def has_js_runtime(self):
        deno_path = self._check_existence("deno")
        node_path = self._check_existence("node")

        if deno_path:
            return deno_path
        elif node_path:
            return node_path
        else:
            return None
