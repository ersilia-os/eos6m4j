# BIDD MolMap
## Model identifiers
- Slug: bidd-molmap
- Ersilia ID: eos6m4j
- Tags: Image, Descriptor

# Model description
Molecular maps based on broadly learned knowledge-based representations. Note that, for now, this model returns data in flat format, and reshape needs to be done. For descriptors, please apply (37,37) reshaping, and for fingerprints, (37,36).
- Input: Compound
- Output: Image (i.e. matrix/tensor of floats) 
- Model type: Descriptor
- Training set: 8M
- Mode of training: It is pretrained.

# Source code
Cite the source publication.
- Code: https://github.com/shenwanxiang/bidd-molmap
- Checkpoints: N/A

# License
GPLv3

# History 
- Model was downloaded on the 25th of August, 2022.
- Dependencies were set to work on Python 3.6.
- Model was incorporated on the 25th of August, 2022.

# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
