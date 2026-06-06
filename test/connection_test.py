from data.connection_db import get_connection

def test_get_connection():
    with get_connection("test_batch_control.db") as cursor:
        assert cursor is not None

def test_get_connection_lotes():
    with get_connection("test_batch_control.db") as cursor:
        lotes = cursor.execute("SELECT * FROM lotes").fetchall()
        assert len(lotes) > 0