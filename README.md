# Molecular maps based on broadly learned knowledge-based representations

Molecular representation of small molecules via descriptor-based molecular maps (images). The fingerprint-based molecular maps are available at eos59rr. These images can be used as inputs for an image-based deep learning model such as a convolutional neural network. The authors have demonstrated high performance of MolMap out-of-the-box with a broad range of tasks from MoleculeNet.

This model was incorporated on 2022-08-25.


## Information
### Identifiers
- **Ersilia Identifier:** `eos6m4j`
- **Slug:** `bidd-molmap-desc`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Descriptor`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1369`
- **Output Consistency:** `Fixed`
- **Interpretation:** Image representation of a molecule. Each pixel represents a molecular feature

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feature_0000 | float |  | Feature 0 of the MolMap descriptor |
| feature_0001 | float |  | Feature 1 of the MolMap descriptor |
| feature_0002 | float |  | Feature 2 of the MolMap descriptor |
| feature_0003 | float |  | Feature 3 of the MolMap descriptor |
| feature_0004 | float |  | Feature 4 of the MolMap descriptor |
| feature_0005 | float |  | Feature 5 of the MolMap descriptor |
| feature_0006 | float |  | Feature 6 of the MolMap descriptor |
| feature_0007 | float |  | Feature 7 of the MolMap descriptor |
| feature_0008 | float |  | Feature 8 of the MolMap descriptor |
| feature_0009 | float |  | Feature 9 of the MolMap descriptor |

_10 of 1369 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos6m4j](https://hub.docker.com/r/ersiliaos/eos6m4j)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6m4j.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6m4j.zip)

### Resource Consumption
- **Model Size (Mb):** `430`
- **Environment Size (Mb):** `1083`
- **Image Size (Mb):** `1576.29`

**Computational Performance (seconds):**
- 10 inputs: `79.26`
- 100 inputs: `100.3`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/shenwanxiang/bidd-molmap](https://github.com/shenwanxiang/bidd-molmap)
- **Publication**: [https://www.nature.com/articles/s42256-021-00301-6](https://www.nature.com/articles/s42256-021-00301-6)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos6m4j
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos6m4j
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
