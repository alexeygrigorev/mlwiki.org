# Variables
JEKYLL = bundle exec jekyll
GITHUB_REPO = https://github.com/YOUR_USERNAME/my-wiki.git

# Default target
.DEFAULT_GOAL := help

## 🎯 Help: Show available commands
help:
	@echo "Available commands:"
	@echo "  make install     Install Jekyll and dependencies"
	@echo "  make build       Generate the static site"
	@echo "  make serve       Serve the site locally"
	@echo "  make clean       Remove old builds"
	@echo "  make deploy      Push site to GitHub Pages"

## 🔧 Install: Install Jekyll and dependencies
install:
	@echo "Installing Jekyll and dependencies..."
	gem install bundler
	bundle install

## 🔨 Build: Generate the static site
build:
	@echo "Building the Jekyll site..."
	$(JEKYLL) build

## 🚀 Serve: Run Jekyll locally
serve:
	@echo "Serving Jekyll on http://localhost:4000..."
	$(JEKYLL) serve --trace

## 🗑 Clean: Remove old site builds
clean:
	@echo "Cleaning up old builds..."
	rm -rf _site

## 🚀 Deploy: Push to GitHub Pages
deploy: build
	@echo "Deploying to GitHub Pages..."
	git add .
	git commit -m "Deploy updated wiki"
	git push origin main
