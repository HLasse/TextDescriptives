install:
	@echo "--- 🚀 Installing project ---"
	uv sync --extra docs --extra tests --extra style
	uv pip install pip
	uv pip install -r tests/requirements.txt

lint:
	@echo "--- 🧹 Running linters ---"
	uv run ruff format . 						            # running ruff formatting
	uv run ruff check **/*.py --fix						# running ruff linting

lint-check:
	@echo "--- 🧹 Check is project is linted ---"
	uv run ruff format . --check						    # running ruff formatting
	uv run ruff check **/*.py 						        # running ruff linting

test:
	@echo "--- 🧪 Running tests ---"
	make install
	pytest tests/ -n auto

build-docs:
	@echo "--- 📚 Building docs ---"
	@echo "Builds the docs and puts them in the 'site' folder"
	sphinx-build -M html docs/ docs/_build

view-docs:
	@echo "--- 👀 Viewing docs ---"
	@echo You might need to rebuild the docs first"
	open docs/_build/html/index.html