import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

from scholarly import MaxTriesExceededException, scholarly


def fetch_author(scholar_id: str) -> dict:
    for attempt in range(1, 4):
        try:
            author = scholarly.search_author_id(scholar_id)
            return scholarly.fill(
                author,
                sections=["basics", "indices", "counts", "publications"],
            )
        except MaxTriesExceededException:
            if attempt == 3:
                raise
            time.sleep(30 * attempt)

    raise RuntimeError("Google Scholar fetch exhausted without returning a result")


def main() -> None:
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID")
    if not scholar_id:
        raise RuntimeError("GOOGLE_SCHOLAR_ID is required")

    author = fetch_author(scholar_id)
    author["updated"] = datetime.now(timezone.utc).isoformat()
    author["publications"] = {
        publication["author_pub_id"]: publication
        for publication in author["publications"]
    }

    results_dir = Path(__file__).parent / "results"
    results_dir.mkdir(exist_ok=True)
    with (results_dir / "gs_data.json").open("w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shields_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author["citedby"]),
        "cacheSeconds": 3600,
    }
    with (results_dir / "gs_data_shieldsio.json").open(
        "w", encoding="utf-8"
    ) as outfile:
        json.dump(shields_data, outfile, ensure_ascii=False)

    print(
        f"Updated citation data for {author['name']}: "
        f"{author['citedby']} citations"
    )


if __name__ == "__main__":
    main()
