from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class RankedData:
    vcodec_rank: int
    ext_rank: int
    height: int
    ref: dict


class FormatHandler:
    VCODEC_ORDER = ("av01", "vp9", "avc1")
    EXT_ORDER = ("mp4", "webm")
    MIN_BASE_HEIGHT = 720

    def __init__(self, formats):
        self.formats = formats
        self._ranked_data = []

    def rank(self):
        self._ranked_data.clear()

        for fmt in self.formats:
            scored = self._score_formats(fmt)

            if scored:
                self._ranked_data.append(scored)

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

                return score

        return None

    def resolve_ranked(self):
        if not self._ranked_data:
            return []

        sorted_data = sorted(
            self._ranked_data, key=lambda d: (-d.height, d.vcodec_rank, d.ext_rank)
        )

        seen_heights = set()
        deduped_data = []

        for data in sorted_data:
            if data.height not in seen_heights:
                seen_heights.add(data.height)
                deduped_data.append(data)

        applied_min_height_data = [
            d for d in deduped_data if d.height >= FormatHandler.MIN_BASE_HEIGHT
        ]

        finalized_data = (
            applied_min_height_data
            if len(applied_min_height_data) > 1
            else deduped_data
        )

        return [f.ref for f in finalized_data]
