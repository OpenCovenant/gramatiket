## gramatiket - Grammatical Error Correction Dataset For Albanian

This repository contains a dataset aimed to train AI models for the task of Grammatical Error Correction.

### Getting Started

The file [gramatiket.json](gramatiket.json) contains a list of sentences with an instrumented grammatical error as
dictated by the tag and a corrected version of the source sentence. The list of the created tags can be found
in [token_level_transformations.json](token_level_transformations.json). Certain checks are performed on the pipeline
once changes are made to the dataset.

### Constraints of the Dataset

- The sentences should not have any other issues themselves.
- The tag REPLACE_ELEMENT means that the source token should be replaced **with** ELEMENT.
- Do **NOT** add tags that don’t need context to be solved.
- The value in the "tag" column **MUST** be unique, otherwise we can’t know exactly which transformation we are
  referring to.
- The tag will apply the exact operation as depicted in the tag, i.e. if the tag is REPLACE_tre then we cannot apply
  it to the sentence "Tri nga ato u kthyen." In this scenario a new tag will have to be created, REPLACE_Tre.

### Contributors

The entries found in this dataset have been added in a number of various ways. We'd like to express our gratitude in the
following alphabetical list.

- AndiBraimllari (Andi Braimllari)
- KostaTB (Kostian Qirjazi)
