from os import path

from youtube_dl import YoutubeDL

from VCsMusicBot.config import DURATION_LIMIT
from VCsMusicBot.helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio[ext=m4a]",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}

ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"❌  {DURATION_LIMIT} dakikadan uzun videolara izin verilmez, "
            f"sağlanan video {duration} dakikadır",
       )
    ydl.download([url])
    return path.join("downloads", f"{info['id']}.{info['ext']}")
