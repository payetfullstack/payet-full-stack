# Path to local venv
VENV=venv/bin/activate
# Name of the built image
IMAGE_NAME=adria-full-stack-image
# Colors
clear=\033[0m
red=\033[31m

run_backend:
	echo "Running FastAPI with Uvicorn..."
	. $(VENV) && uvicorn app.main:app --reload --log-level debug

test_unit:
	echo "Running unit tests..."
	. $(VENV) && pytest app/tests/unit/

install:
	echo "Installing dependencies..."
	. $(VENV) && pip install -r requirements.txt

update_requirements_txt:
	echo "Checking if pipreqs is installed..."
	bash -c "source $(VENV) && (pip show pipreqs > /dev/null 2>&1 || pip install pipreqs)"
	echo "Running pipreqs to update requirements.txt..."
	bash -c "source $(VENV) && pipreqs . --force"

docker_delete_build:
	echo "Deleting image..."
	docker rmi $(IMAGE_NAME)

docker_build:
	@$(MAKE) -s delete_build || true
	echo "Building image..."
	docker build -t $(IMAGE_NAME) .
	@image_size=$$(docker images --format "{{.Size}}" $(IMAGE_NAME):latest); \
	echo "Image size: $$image_size"; \
	image_size_num=$$(echo $$image_size | sed -E 's/([0-9.]+)MB/\1/; s/([0-9.]+)GB/(\1*1024)/' | bc -l); \
	image_size_limit=200.0; \
	exceeds_limit=$$(echo "$$image_size_num > $$image_size_limit" | bc -l); \
	if [ "$$exceeds_limit" = "1" ]; then \
		echo "${red}WARNING: Image size exceeds $$image_size_limit MB!${clear}"; \
	fi

docker_run: docker_build
	. ./.env && \
	export `sed -e 's/=.*$$//' -e '/^#/d' .env` && \
	docker run --rm --network=host \
	--env-file .env \
	--name backend $(IMAGE_NAME):latest
