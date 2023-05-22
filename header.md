---
component-id: https://w3id.org/polifonia/ontology/source/
type: Ontology
name: Source ontology
description: Source represents various sources of music-related information
image: diagrams/source-module.png
work-package:
- WP2
pilot:
- MEETUPS
- MUSICBO
project: polifonia-project
resource: ontology/jams.owl
release-date: 13/04/2023
release-number: v1.0
release-link: https://github.com/polifonia-project/jams-ontology
doi: 10.5281/zenodo.7919970
changelog: https://github.com/polifonia-project/jams-ontology
licence: 
- CC BY 4.0, https://creativecommons.org/licenses/by/4.0/
copyright: "Copyright (c) 2023 Source Ontology Contributors"
contributors: # replace these with the GitHub URL of each contributor
- Jacopo de Berardinis <https://github.com/jonnybluesman>
- Andrea Poltronieri <https://github.com/andreamust>
related-components:
- informed-by:
  - https://github.com/polifonia-project/polifoniacq-dataset
- reuses:  # any reused/imported ontology
  - https://github.com/polifonia-project/core-ontology/
  - https://github.com/polifonia-project/core/
  - https://github.com/polifonia-project/core/
- story:  # any related story this ontology addresses
- persona:  # any persona this ontology addresses
- documentation:  # link any resource providing documentation for this ontology
  - https://github.com/polifonia-project/source-ontology
---

# JAMS Ontology

The JAMS ontology mimics the structure of a JAMS (JSON Annotated Music Specification for Reproducible MIR Research) document. It semantically describes and connects all the elements of the JAMS specification (Annotatio, Observation, etc.), including the music metadata and the annotation contents using the Music Meta and Music Representation modules, respectively.
JAMS is a JSON-based music annotation format whioch aims to provide a simple, structured, and sustainable approach to representing rich information in a human-readable, language agnostic format. JAMS is not only a formal scheme, but also a set of software tools that has been implemented to interact with this scheme. The annotation and software specifications can be found in the official documentation.

[Link to the website](https://github.com/polifonia-project/jams-ontology)
