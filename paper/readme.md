# Paper for TextDescriptives

`paper.md` contains the paper submitted to JOSS

`paper_quarter.qmd` contains the same content as `paper.md` but with a different yaml preamble that allows it to be converted to a nice arxiv-style pdf. To render to arxiv preprint do the following:

```
# install the quarto-arxiv template (https://github.com/mikemahoney218/quarto-arxiv)
quarto install extension mikemahoney218/quarto-arxiv

# render to pdf
quarto render paper_quarto.qmd
```
