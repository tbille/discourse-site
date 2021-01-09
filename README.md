# Discourse static site generator

Generate static sites from [discourse](https://www.discourse.org/) topics. This project is a proof of concept.

## How it works

- Use a discourse topics to generate the content for your static site
- The site gets generated with [Jekyll](https://jekyllrb.com/)
- Easy to deploy with [GitHub Pages](https://pages.github.com/)
- Manage your pages configuration via a yaml file

## Light configuration

The `.site.yaml` configuration file will generate a site from discourse topics.

```yaml
pages:
  - name: Homepage
    siteUrl: /
    discourseTopic: "https://discourse.charmhub.io/t/access-the-kubeflow-dashboard/3883"
  - name: page2
    siteUrl: /page2
    discourseTopic: "https://discourse.charmhub.io/t/update-charms/4040"

website:
  baseUrl: /discourse-site
  name: Test
  url: "http://example.com"
```

## Generate site

Make sure you have Jekyll install. Then:

```
gem install bundler jekyll
pip install -r requirements
python generate.py
cd dist
bundle exec jekyll serve
```

The site should be available on: http://127.0.0.1:4000/discourse-site/

# Next steps

- [ ] Cleaner code for the generate script
- [ ] Make the generate script a CLI
- [ ] Github action that checks if a topic was upated to deploy again
- [ ] Custom Jekyll templating
- [ ] Add navigation
- [ ] Add CNAME for custom domains
- [ ] Document how to use the project
- [ ] Get more explanatories discourse topics
- [ ] Replace links in the discourse topics with site links if link is part of the `.site.yaml`