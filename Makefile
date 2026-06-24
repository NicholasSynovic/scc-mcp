.PHONY: build clean

build:
	uv build

clean:
	rm -rf dist
