#!/bin/bash

if [$1 = "dev"]; then
	docker run --bind=0.0.0.0:8000 --reload --timeout 120 APP:app
else
	docker run
fi
#CMD ["gunicorn", "--bind=0.0.0.0:80", "-w", "3", "-k", "aiohttp.worker.GunicornWebWorker", "APP:aioapp"]
