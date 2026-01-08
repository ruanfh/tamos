
import pytest
from fastapi.testclient import TestClient
from main import app
import tempfile
import sys
import types

@pytest.fixture(scope="module")
def client():
    # Patch ARCHIVE_DIR in all relevant modules to use a temp dir
    with tempfile.TemporaryDirectory() as tmpdir:
        # Patch in storage.writer
        import storage.writer
        storage.writer.ARCHIVE_DIR = tmpdir
        # Patch in storage.reader
        import storage.reader
        storage.reader.ARCHIVE_DIR = tmpdir
        # Patch in routes.archive
        import routes.archive
        routes.archive.ARCHIVE_DIR = tmpdir
        with TestClient(app) as c:
            yield c
