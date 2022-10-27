dist:
	./venv/Scripts/activate && pyinstaller main.spec

clean:
	rm -r build dist