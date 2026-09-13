# frozen_string_literal: true

Jekyll::Hooks.register :site, :post_read do |site|
  projects = site.collections["projects"]
  next unless projects

  projects.docs.each do |project|
    legacy_url = "/projects/#{project.basename_without_ext}.html"
    project.data["redirect_from"] = (Array(project.data["redirect_from"]) + [legacy_url]).uniq
  end
end
