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

delete_build:
	echo "Deleting image..."
	docker rmi $(IMAGE_NAME)

build:
	@$(MAKE) -s delete_build || true
	echo "Building image..."
	docker build -t $(IMAGE_NAME) .
	@image_size=$$(docker images --format "{{.Size}}" $(IMAGE_NAME):latest); \
	echo "Image size: $$image_size"; \
	image_size_num=$$(echo $$image_size | sed 's/MB//;s/GB/*1024/;s/ //g' | bc); \
	image_size_limit=200; \
	if [ $$image_size_num -gt $$image_size_limit ]; then \
		echo "${red}WARNING: Image size exceeds $$image_size_limit MB!${clear}"; \
	fi
