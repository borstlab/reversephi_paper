PDF = output/ms.pdf output/Fig1.tif output/Fig2.tif output/Fig3.tif output/Fig4.tif output/Fig5.tif output/Fig6.tif output/Fig7.tif output/Fig8.tif output/Fig9.tif output/Fig10.tif output/Fig11.tif output/Fig12.tif
TEMPDIR := $(shell mktemp -d)
OPTS = --latex-engine=xelatex --variable mainfont="Arial" --variable fontsize=12pt --variable papersize=a4 -H manuscript/options.sty --smart --bibliography manuscript/mylib.bib --csl manuscript/plos-one.csl
OPTS_DOCX = --reference-docx=manuscript/reference.docx --smart --bibliography manuscript/mylib.bib --csl manuscript/plos-one.csl
.PHONY: all clean

all: output/full_ms.zip

output/full_ms.zip: $(PDF)
	zip -j output/full_ms.zip $(PDF)

output/ms.pdf: manuscript/manuscript.md manuscript/mylib.bib manuscript/options.sty manuscript/plos-one.csl
	pandoc -f markdown -s manuscript/manuscript.md -o output/ms.pdf $(OPTS)

output/Fig1.tif: figures/static/figure1.pdf
	convert -flatten -alpha remove -density 600 -depth 8 -compress lzw figures/static/figure1.pdf output/Fig1.tif

output/Fig2.tif: figures/figure_2_motionenergymodel.ipynb
	jupyter nbconvert --ExecutePreprocessor.kernel_name="python2" --execute --to notebook --output $(TEMPDIR) figures/figure_2_motionenergymodel.ipynb
	convert -alpha remove -compress lzw output/Fig2.tif output/Fig2.tif

output/Fig3.tif: figures/figure_3_behavior_lambda.ipynb
	jupyter nbconvert --ExecutePreprocessor.kernel_name="python2" --execute --to notebook --output $(TEMPDIR) figures/figure_3_behavior_lambda.ipynb
	convert -alpha remove -compress lzw output/Fig3.tif output/Fig3.tif

output/Fig4.tif: figures/figure_4_behavior_block.ipynb
	jupyter nbconvert --ExecutePreprocessor.kernel_name="python2" --execute --to notebook --output $(TEMPDIR) figures/figure_4_behavior_block.ipynb
	convert -alpha remove -compress lzw output/Fig4.tif output/Fig4.tif

output/Fig5.tif: figures/figure_5_ephys.ipynb
	jupyter nbconvert --ExecutePreprocessor.kernel_name="python2" --execute --to notebook --output $(TEMPDIR) figures/figure_5_ephys.ipynb
	convert -alpha remove -compress lzw output/Fig5.tif output/Fig5.tif

output/Fig6.tif: figures/static/figure6.pdf
	convert -flatten -alpha remove -density 600 -depth 8 -compress lzw figures/static/figure6.pdf output/Fig6.tif

output/Fig7.tif: figures/figure_7_modelcomp.ipynb
	jupyter nbconvert --ExecutePreprocessor.kernel_name="python2" --ExecutePreprocessor.timeout=1024 --execute --to notebook --output $(TEMPDIR) figures/figure_7_modelcomp.ipynb
	convert -alpha remove -compress lzw output/Fig7.tif output/Fig7.tif

output/Fig8.tif: figures/figure_8_tuningmodel.ipynb
	jupyter nbconvert --ExecutePreprocessor.kernel_name="python2" --execute --to notebook --output $(TEMPDIR) figures/figure_8_tuningmodel.ipynb
	convert -alpha remove -compress lzw output/Fig8.tif output/Fig8.tif

output/Fig9.tif: figures/figure_9_flicker_decoupled.ipynb
	jupyter nbconvert --ExecutePreprocessor.kernel_name="python2" --execute --to notebook --output $(TEMPDIR) figures/figure_9_flicker_decoupled.ipynb
	convert -alpha remove -compress lzw output/Fig9.tif output/Fig9.tif

output/Fig10.tif: figures/figure_10_detailedmodel.ipynb
	jupyter nbconvert --ExecutePreprocessor.kernel_name="python2" --ExecutePreprocessor.timeout=1024 --execute --to notebook --output $(TEMPDIR) figures/figure_10_detailedmodel.ipynb
	convert -alpha remove -compress lzw output/Fig10.tif output/Fig10.tif

output/Fig11.tif: figures/figure_11_calcium.ipynb
	jupyter nbconvert --ExecutePreprocessor.kernel_name="python2" --execute --to notebook --output $(TEMPDIR) figures/figure_11_calcium.ipynb
	convert -alpha remove -compress lzw output/Fig11.tif output/Fig11.tif

output/Fig12.tif: figures/figure_12_behavior_pathway_blocks.ipynb
	jupyter nbconvert --ExecutePreprocessor.kernel_name="python2" --execute --to notebook --output $(TEMPDIR) figures/figure_12_behavior_pathway_blocks.ipynb
	convert -alpha remove -compress lzw output/Fig12.tif output/Fig12.tif

clean:
	rm -f output/*.pdf output/*.docx output/*.eps output/*.tif output/*.zip
