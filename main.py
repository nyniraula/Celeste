from core.config import Config
from core.dependency_resolver import DependencyResolver
from core.path_router import PathRouter


def main():
    # Instantiates Dep Resolver and checks for ffmpeg
    dependency_resolver = DependencyResolver()

    # Halts the program execution if no ffmpeg found
    if not dependency_resolver.ffmpeg:
        print("No FFMPEG detected on system. Halting Execution!")
        return

    # Instantiates the config class and add paths to node or deno
    config = Config("config.json")
    config.settings["js_runtimes"] = dependency_resolver.js_runtimes

    # Instantiates Path router and resolves download dir
    path_router = PathRouter(config.settings)
    path_router.resolve_output_path()


if __name__ == "__main__":
    main()
