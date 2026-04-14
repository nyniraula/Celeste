from dataclasses import dataclass


@dataclass
class RankedData:
    vcodec_rank: int
    ext_rank: int
    height: int
    ref: dict


class FormatHandler:
    VCODEC_ORDER = ("av01", "vp9", "avc1")
    EXT_ORDER = ("mp4", "webm")

    def __init__(self, formats):
        self.formats = formats
        self._ranked_data = []

    def rank(self):
        self._ranked_data.clear()

        for fmt in self.formats:
            self._score_formats(fmt)

    def _score_formats(self, fmt):
        vcodec = fmt.get("vcodec")
        ext = fmt.get("ext")
        height = fmt.get("height")

        if not (vcodec or height):
            return None

        for VCODEC in FormatHandler.VCODEC_ORDER:
            if vcodec.startswith(VCODEC) and ext in FormatHandler.EXT_ORDER:
                score = RankedData(
                    vcodec_rank=(FormatHandler.VCODEC_ORDER.index(VCODEC)),
                    ext_rank=(FormatHandler.EXT_ORDER.index(ext)),
                    height=height,
                    ref=fmt,
                )

                self._ranked_data.append(score)
