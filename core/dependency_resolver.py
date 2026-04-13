import shutil


class DependencyResolver:
    def _check_existence(self, tool):
        """Return the path if the tool exists, if not returns false"""
        path = shutil.which(tool)
        return path if bool(path) else False


dr = DependencyResolver()
dr._check_existence("ffmpeg")
