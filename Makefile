setup:
	brew install gcc openssl readline sqlite3 xz zlib
	echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/johnsmith/.zshrc
	brew install pyenv
	brew install pyenv-virtualenv
	echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.zshrc
	pyenv install 3.8.13 --skip-existing
	pyenv global 3.8.13

venv:
	pyenv install 3.8.13 --skip-existing
	-pyenv uninstall -f odds_venv
	-pyenv virtualenv 3.8.13 odds_venv
	-pyenv local odds_venv

deps:
	python -m pip install --upgrade pip
	pip install --upgrade pip-tools
	pip install -r requirements.txt

chrome:
	sudo mv com.google.Keystone.plist /Library/Managed\ Preferences/com.google.Keystone.plist


full-build: setup venv deps