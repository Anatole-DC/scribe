<h1 align="center">SCRIBE</h1>

Welcome to the scribe project !

Scribe is an automation tools that generates markdown documentation architectures (with clean summaries), based on markdowns files foundt in subdirectories.

___

**Version :** 1.0.0

**Technos :** Python 3, Markdown

**Author :** Anatole de Chauveron

**Licence :** All rights reserved

___

## Getting started with scribe

### Installation

**Get the project :**

Start by cloning this project on your local machine.

```bash
git clone https://github.com/Anatole-DC/scribe.git
```

**Add the script to your path :**

_This step is optionnal but can improve the comfort using scribe._

Add the scribe shell executable to your aliases to run scribe from anywhere on your local machine.

### Running scribe

To use scribe, start by creating a project containing an architecture as such :

```bash
exemple/
├── docs
└── README.md
```

Then you can run the following command, adjusting the path to your directory.

```bash
scribe .                    # If you are in the exemple directory

scribe /path/to/exemple/    # Otherwise
```

## Contact

_For any questions about this project, please reach the author at **adechauveron@gmail.com**._