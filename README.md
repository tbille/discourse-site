# Build a website from discourse

Jekyll website generator from discourse.

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
python generate.py
cd dist
bundle exec jekyll serve
```

The site should be available on: http://127.0.0.1:4000/discourse-site/