from core.config import Config
from core.dependency_resolver import DependencyResolver
from core.path_router import PathRouter
from input.input_controller import InputController
from pipeline.media_pipeline import MediaPipeline
from ui.cli_builder import CLIBuilder


def main():
    # Instantiate CLI and Rich Console
    cli = CLIBuilder()

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
    os_relative_path = path_router.resolve_output_path()

    config.settings["path"] = os_relative_path

    cli.cli_banner()

    # Instantiate InputController
    input_controller = InputController(cli, config.settings)

    media_pipeline = MediaPipeline(
        input_controller.url, input_controller.media_info, config.settings, cli
    )

    media_pipeline.start_downloader()


if __name__ == "__main__":
    main()
