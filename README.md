# JAMS Ontology
The JAMS ontology module of the [Polifonia ontology network](https://github.com/polifonia-project/ontology-network) provides a comprehensive schema to describe JAMS files and their annotations.

## Competency questions addressed by this ontology module

TBD

## Imported ontologies
### Imported from the Polifonia Ontology Network

- [Core Module](https://github.com/polifonia-project/core-ontology/)
- [Musical Composition Module](https://github.com/polifonia-project/musical-composition-ontology/)
- [Musical Features Module](https://github.com/polifonia-project/musical-features-ontology/)
- [Musical Performance](https://github.com/polifonia-project/musical-performance-ontology/)
- [Roman Chord](https://github.com/polifonia-project/roman-chord-ontology/)

### External Imports
- [Chord Ontology](http://motools.sourceforge.net/chord_draft_1/chord.html)

## Ontology Description

This ontology makes it possible to describe structured annotations from a JAMS file, as described in:

```
Eric J. Humphrey, Justin Salamon, Oriol Nieto, Jon Forsyth, Rachel M. Bittner, and Juan P. Bello, 
"JAMS: A JSON Annotated Music Specification for Reproducible MIR Research", 
Proceedings of the 15th International Conference on Music Information Retrieval, 2014.
``` 

JAMS is a JSON-based music annotation format whioch aims to provide a simple, structured, and sustainable approach to representing rich information in a human-readable, language agnostic format.
JAMS is not only a formal scheme, but also a set of software tools that has been implemented to interact with this scheme. The annotation and software specifications can be found in the [official documentation](https://jams.readthedocs.io/en/stable/).

However, the objective of this ontology module is not only to recreate the structure of a JAMS file in an RDF serialisation. Instead, the aim of this module of the Polifonia Ontology Network is to enrich the JAMS model with new information that is semantically consistent. 

### JAMS Annotation
![jams-observations](https://user-images.githubusercontent.com/44606182/173377824-0776045e-a02f-4e6d-add2-9aa23d2f5cf0.png)

### JAMS Observation
![jams-annotation](https://user-images.githubusercontent.com/44606182/173377852-6a07e415-ae5d-4af9-aef6-5e52f15b4645.png)


## Bibliography

1. Eric J. Humphrey, Justin Salamon, Oriol Nieto, Jon Forsyth, Rachel M. Bittner, and Juan P. Bello, 
"JAMS: A JSON Annotated Music Specification for Reproducible MIR Research", 
Proceedings of the 15th International Conference on Music Information Retrieval, 2014.
2. Harte, Christopher & Sandler, Mark & Abdallah, Samer & Gómez, Emilia. (2005). Symbolic Representation of Musical Chords: A Proposed Syntax for Text Annotations.. 66-71. 
3. Raimond, Yves & Abdallah, Samer & Sandler, Mark & Giasson, Frederick. (2007). The Music Ontology. Proceedings of the 8th International Conference on Music Information Retrieval, ISMIR 2007. 

## License

TBD
