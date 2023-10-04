# DecentHolograms Wiki

This repository is the home of the [DecentHolograms Wiki][wiki].

It is build using [MkDocs][mkdocs] and the [Material for MkDocs theme][material].

## Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── publish_site.yml
├── docs/
│   ├── api/
│   │   └── ...
│   ├── assets/
│   │   ├── images/
│   │   │   └── ...
│   │   ├── js/
│   │   │   └── github-release.js
│   │   ├── stylesheets/
│   │   │   └── theme.css
│   │   └── site.webmanifest
│   └── ...
├── theme/
│   ├── partials/
│   │   └── ...
│   └── ...
├── LICENSE
├── README.md
├── mkdocs.yml
└── requirements.txt
```

- `docs` is the main directory containing the markdown files that get rendered into static HTML pages by MkDocs for the [wiki].
- `theme` contains overrides for the [Material for MkDocs theme][material] to customize some of its main behaviour (i.e. generating a page title and subtitle).
- `mkdocs.yml` contains the configuration used by MkDocs. This includes the theme, plugins and extensions used.
- `requirements.txt` contains the necessary dependencies that need to be installed during page publication. Note that MkDocs and PyMDown Extensions are included within Material for MkDocs when installing.

## Contribute

Feel free to contribute to this repository. All kinds of contributions no matter how big or small are welcomed.  
Just make sure to follow the below steps to have everything prepared to work on and test stuff.

### Prerequisite

- Python 3.11 or newer
- Pip (For dependency installing)
- Git (For repo cloning)

### Steps

- Fork this repository using the "Fork" button at the top
- On your PC, choose a folder where to clone your repository in, open Git bash and clone your fork
- `cd` into your fork
- Run `pip install -r requirements.txt` to install the necessary dependencies
- Use `mkdocs serve` to start a live-preview of the docs to look at.
- Start working

Once you're done with your changes, commit and push them to your fork and make a PR to the upstream (This) repository.  
If everything looks good will your changes be merged and the wiki updated.

[wiki]: https://wiki.decentholograms.eu
[mkdocs]: https://www.mkdocs.org
[material]: https://squidfunk.github.io/mkdocs-material
