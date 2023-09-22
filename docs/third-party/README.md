# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/korspollinering/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([07bd1b73 ...](https://git.sr.ht/~sthagen/korspollinering/blob/default/etc/sbom/cdx.json.sha256 "sha256:07bd1b73b09a28bcd250c13f442bdeb41e0d565137f5fd02e862b89c046d7ca4")).
<!--[[[end]]] (checksum: a0e6b3a94e8c75326e1d92080510c681)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                           | Version                                              | License     | Author                         | Description (from packaging data)                                    |
|:---------------------------------------------------------------|:-----------------------------------------------------|:------------|:-------------------------------|:---------------------------------------------------------------------|
| [GitPython](https://github.com/gitpython-developers/GitPython) | [3.1.37](https://pypi.org/project/GitPython/3.1.37/) | BSD License | Sebastian Thiel, Michael Trier | GitPython is a Python library used to interact with Git repositories |
| [PyYAML](https://pyyaml.org/)                                  | [6.0.1](https://pypi.org/project/PyYAML/6.0.1/)      | MIT License | Kirill Simonov                 | YAML parser and emitter for Python                                   |
| [typer](https://github.com/tiangolo/typer)                     | [0.9.0](https://pypi.org/project/typer/0.9.0/)       | MIT License | Sebastián Ramírez              | Typer, build great CLIs. Easy to code. Based on Python type hints.   |
<!--[[[end]]] (checksum: fa2e6dd25d8ed7e478c6b7aea631800d)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                   | Version                                          | License     | Author          | Description (from packaging data)                                   |
|:-------------------------------------------------------|:-------------------------------------------------|:------------|:----------------|:--------------------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)          | [8.1.6](https://pypi.org/project/click/8.1.6/)   | BSD License | UNKNOWN         | Composable command line interface toolkit                           |
| [gitdb](https://github.com/gitpython-developers/gitdb) | [4.0.10](https://pypi.org/project/gitdb/4.0.10/) | BSD License | Sebastian Thiel | Git Object Database                                                 |
| [smmap](https://github.com/gitpython-developers/smmap) | [5.0.0](https://pypi.org/project/smmap/5.0.0/)   | BSD License | Sebastian Thiel | A pure Python implementation of a sliding window memory map manager |
<!--[[[end]]] (checksum: 65d3b6ee224f9864d18a33a0a38f4c6f)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
GitPython==3.1.37
└── gitdb [required: >=4.0.1,<5, installed: 4.0.10]
    └── smmap [required: >=3.0.1,<6, installed: 5.0.0]
PyYAML==6.0.1
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.6]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: cd77edf31dc2fd3b60941261104aa4a7)-->
