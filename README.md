## Neural mechanisms underlying sensitivity to reverse-phi motion in the fly

Leonhardt, Meier, Serbe, Eichner & Borst (2017)

MPI for Neurobiology, Martinsried

### Abstract

Optical illusions provide powerful tools for mapping the algorithms and circuits that underlie visual processing, revealing structure through atypical function. Of particular note in the study of motion detection has been the reverse-phi illusion. When contrast reversals accompany discrete movement, detected direction tends to invert. This occurs across a wide range of organisms, spanning humans and invertebrates. Here, we map an algorithmic account of the phenomenon onto neural circuitry in the fruit fly *Drosophila melanogaster*. Through targeted silencing experiments in tethered walking flies as well as electrophysiology and calcium imaging, we demonstrate that ON- or OFF-selective local motion detector cells T4 and T5 are sensitive to certain interactions between ON and OFF. A biologically plausible detector model accounts for subtle features of this particular form of illusory motion reversal, like the re-inversion of turning responses occurring at extreme stimulus velocities. In light of comparable circuit architecture in the mammalian retina, we suggest that similar mechanisms may apply even to human psychophysics.

### Building the manuscript

This repository includes full raw data as well as the complete code used to analyze data, run simulations, and build the figures. If you're keen, it's easy to build the full MS on the command line. There's a number of requirements:

* Working installation of the Anaconda Python distribution (`conda`)
* ImageMagick (`convert` with support for PDF & TIFF)
* Standard UNIX tooling (specifically, `make` and `zip`)

First, after checking out the repository, install and activate a pre-configured `conda` environment from the supplied `environment.yml`:

```bash
$ git clone https://github.com/borstlab/reversephi_paper.git
$ cd reversephi_paper
$ conda env create -f environment.yml
$ source activate reversephi_plosone
```

Next, build the MS and figures:

```
$ make all
```

This should give you the PDF as well as a TIFF file for each figure in the `output` directory. Everything's built from scratch, including potentially time-consuming simulations. It's possible that depending on your computer, you need to change the `jupyter` timeout to larger values by adjusting the `--ExecutePreprocessor.timeout` settings in the Makefile. Note that we have only tested this on macOS 10.13.