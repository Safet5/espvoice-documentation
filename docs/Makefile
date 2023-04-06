# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXAUTOBUILD = sphinx-autobuild
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

ALLSPHINXLIVEOPTS   = $(ALLSPHINXOPTS) -q \
   -p 0 \
   -H 0.0.0.0 \
   -B \
   --delay 1 \
   --ignore "*.swp" \
   --ignore "*.pdf" \
   --ignore "*.log" \
   --ignore "*.out" \
   --ignore "*.toc" \
   --ignore "*.aux" \
   --ignore "*.idx" \
   --ignore "*.ind" \
   --ignore "*.ilg" \
   --ignore "*.tex" \
   --watch source
   
# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)



.PHONY: livehtml
livehtml:
	$(SPHINXAUTOBUILD) -b html $(SPHINXOPTS) $(O)

	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)."

.PHONY: spelling
spelling:
	$(SPHINXBUILD) -b spelling "$(SOURCEDIR)" "$(BUILDDIR)/spelling" $(SPHINXOPTS) $(O)
	@echo "Checked spelling, results are in $(BUILDDIR)/spelling/output.txt."

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
