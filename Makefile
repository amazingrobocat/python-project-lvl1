install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

<<<<<<< HEAD
package-venv-install:
	python3 -m pip install --force-reinstall dist/*.whl

=======
>>>>>>> d1030c156dec2811e580d205d0c11730cf21438e
lint:
	poetry run flake8 brain_games