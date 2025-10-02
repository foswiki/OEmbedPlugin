SPECS=\
  header.spec \
  providers.spec \
  footer.spec

CONVERT=$(FOSWIKI_ROOT)/tools/convert_providers

all: Config.spec

clean:
	@echo "cleaning up"
	@rm -f Config.spec providers.spec

git:
	git clone https://github.com/iamcal/oembed.git git

ifneq (,$(wildcard git))
providers.spec: git/providers/*yml
	@echo "creating providers.spec"
	@$(CONVERT) ./extra.spec $^ > $@
endif

Config.spec: $(SPECS) 
	@echo "creating Config.spec"
	@cat $(SPECS) > $@

