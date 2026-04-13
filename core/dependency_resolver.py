import shutil


class DependencyResolver:
    def _check_existence(self, tool: str) -> str | bool:
        """Returns the path if the tool exists, if not returns false"""
        path: str = shutil.which(tool)
        return path if bool(path) else False

    def has_ffmpeg(self) -> str | bool:
        return self._check_existence("ffmpeg")

    def has_js_runtime(self) -> str | None:
        deno_path: str | bool = self._check_existence("deno")
        node_path: str | bool = self._check_existence("node")

        if deno_path:
            return deno_path
        elif node_path:
            return node_path
        else:
            return None
