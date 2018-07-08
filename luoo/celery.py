from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery(
    "luoo",
    broker="redis://:1qa%40ws%23ed4rf@127.0.0.1:6379/0",
    backend="redis://:1qa%40ws%23ed4rf@127.0.0.1:6379/1",
    include=["luoo.tasks"],
)

# Optional configuration, see the application user guide.
app.conf.update(result_expires=3600)

if __name__ == "__main__":
    app.start()
