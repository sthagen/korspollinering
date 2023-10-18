# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/korspollinering/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([7527d09a ...](https://git.sr.ht/~sthagen/korspollinering/blob/default/etc/sbom/cdx.json.sha256 "sha256:7527d09a0cc2afe44ade9191a14371505d5bbc6c619c03bbcf013deb893f1cce")).
<!--[[[end]]] (checksum: 2bea5fe5dca728f131e35db678adacab)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                           | Version                                              | License     | Author                         | Description (from packaging data)                                    |
|:---------------------------------------------------------------|:-----------------------------------------------------|:------------|:-------------------------------|:---------------------------------------------------------------------|
| [GitPython](https://github.com/gitpython-developers/GitPython) | [3.1.40](https://pypi.org/project/GitPython/3.1.40/) | BSD License | Sebastian Thiel, Michael Trier | GitPython is a Python library used to interact with Git repositories |
| [PyYAML](https://pyyaml.org/)                                  | [6.0.1](https://pypi.org/project/PyYAML/6.0.1/)      | MIT License | Kirill Simonov                 | YAML parser and emitter for Python                                   |
| [typer](https://github.com/tiangolo/typer)                     | [0.9.0](https://pypi.org/project/typer/0.9.0/)       | MIT License | Sebastián Ramírez              | Typer, build great CLIs. Easy to code. Based on Python type hints.   |
<!--[[[end]]] (checksum: 0b63eaf8fb366756baafa7c63f7b918b)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                   | Version                                          | License     | Author                                | Description (from packaging data)                                   |
|:-------------------------------------------------------|:-------------------------------------------------|:------------|:--------------------------------------|:--------------------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)          | [8.1.6](https://pypi.org/project/click/8.1.6/)   | BSD License | Pallets <contact@palletsprojects.com> | Composable command line interface toolkit                           |
| [gitdb](https://github.com/gitpython-developers/gitdb) | [4.0.10](https://pypi.org/project/gitdb/4.0.10/) | BSD License | Sebastian Thiel                       | Git Object Database                                                 |
| [smmap](https://github.com/gitpython-developers/smmap) | [5.0.0](https://pypi.org/project/smmap/5.0.0/)   | BSD License | Sebastian Thiel                       | A pure Python implementation of a sliding window memory map manager |
<!--[[[end]]] (checksum: de5e1606c939c4d8a05a3495133e6923)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
GitPython==3.1.40
└── gitdb [required: >=4.0.1,<5, installed: 4.0.10]
    └── smmap [required: >=3.0.1,<6, installed: 5.0.0]
PyYAML==6.0.1
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.6]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: e82632d3627efc678ca59a41c19f791e)-->
