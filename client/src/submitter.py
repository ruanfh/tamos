import json
import urllib.request


def submit_gem(server_url: str, gem: dict) -> int:
    """
    Submit a gem to the TAMOS server.
    Returns the assigned gem ID.
    """

    url = server_url.rstrip("/") + "/submit"
    data = json.dumps(gem).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode("utf-8")
            result = json.loads(body)
            return result["id"]

    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Server returned error {e.code}: {e.read().decode()}")

    except urllib.error.URLError as e:
        raise RuntimeError(f"Failed to reach server: {e.reason}")