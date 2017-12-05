## Neural mechanisms underlying sensitivity to reverse-phi motion in the fly

Leonhardt, Meier, Serbe, Eichner & Borst (2017)

MPI for Neurobiology, Martinsried

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/borstlab/reversephi_paper/master)

### Abstract

Optical illusions provide powerful tools for mapping the algorithms and circuits that underlie visual processing, revealing structure through atypical function. Of particular note in the study of motion detection has been the reverse-phi illusion. When contrast reversals accompany discrete movement, detected direction tends to invert. This occurs across a wide range of organisms, spanning humans and invertebrates. Here, we map an algorithmic account of the phenomenon onto neural circuitry in the fruit fly *Drosophila melanogaster*. Through targeted silencing experiments in tethered walking flies as well as electrophysiology and calcium imaging, we demonstrate that ON- or OFF-selective local motion detector cells T4 and T5 are sensitive to certain interactions between ON and OFF. A biologically plausible detector model accounts for subtle features of this particular form of illusory motion reversal, like the re-inversion of turning responses occurring at extreme stimulus velocities. In light of comparable circuit architecture in the mammalian retina, we suggest that similar mechanisms may apply even to human psychophysics.

---

### Binder support

Each figure of this manuscript is based on a single Jupyter notebook. You can interactively explore these notebooks on mybinder.org; simply click the badge above. Note that due to issues with using Git-LFS, HDF5 data (i.e., behavioral/calcium/electrophysiology data) are not available at the moment. We might add a way to load data remotely (e.g., via S3) at some later point.

### Versioning

We've tagged the "release" version of our code as `v1.0`. This represents the exact code used to generate all figures for the published manuscript. If you want to reproduce our plots exactly, check out this tag. We might occasionally add commits to the `master` when improving documentation etc.

### Building the manuscript

This repository includes full raw data as well as the complete code used to analyze data, run simulations, and build the figures. If you're keen, it's easy to build the full MS on the command line. There's a number of requirements:

* Working installation of the Anaconda Python distribution (`conda`)
* ImageMagick (`convert` with support for PDF & TIFF)
* Standard UNIX tooling (specifically, `make` and `zip`)

First, after checking out the repository, install and activate a pre-configured `conda` environment from the supplied `my_environment.yml`:

```bash
$ git clone https://github.com/borstlab/reversephi_paper.git
$ cd reversephi_paper
$ conda env create -f my_environment.yml
$ source activate reversephi_plosone
```

Next, build the MS and figures:

```
$ make all
```

This should give you the PDF as well as a TIFF file for each figure in the `output` directory. Everything's built from scratch, including potentially time-consuming simulations. It's possible that depending on your computer, you need to change the `jupyter` timeout to larger values by adjusting the `--ExecutePreprocessor.timeout` settings in the Makefile. Note that we have only tested this on macOS 10.13.

### Data

We make all data (behavior, calcium imaging, and electrophysiology) available at the lowest feasible level. For instance, with *Drosophila* treadmill experiments, this gives you access to every experimental trial of every fly for any given genotype and experiment. The data are stored in `pandas` data frames serialized to HDF5, including lots of critical metadata.

To load a data file, make sure you have `pandas` installed and do the following:

```python
import pandas as pd
data = pd.read_hdf("behav_phi.data")
```

The structure of our data is largely self-explanatory, but see the notebooks in `figures` and analysis tooling in `lib` for details of how we processed everything.
