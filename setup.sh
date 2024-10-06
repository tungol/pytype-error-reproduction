mkdir -p stubs
if ! [ -e .venv312 ]; then
	python3.12 -m venv .venv312
fi
source .venv312/bin/activate
pip install pytype==2024.9.13
