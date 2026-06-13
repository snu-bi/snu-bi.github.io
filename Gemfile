source "https://rubygems.org"

# jekyll
gem "jekyll", "~> 4.3"
gem "webrick", "~> 1.7"

# html-proofer: CI only (requires libcurl, not available locally on Windows)
group :ci do
  gem "html-proofer", "~> 5.0"
end

# plugins
group :jekyll_plugins do
  gem "jekyll-spaceship"
  gem "jekyll-sitemap"
  gem "jekyll-redirect-from"
  gem "jekyll-feed"
  gem "jekyll-last-modified-at"
end
