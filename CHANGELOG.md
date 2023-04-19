# Changelog

<!--next-version-placeholder-->

## v2.4.5 (2023-04-19)
### Fix
* Dep dist. test ([`a3b54a6`](https://github.com/HLasse/TextDescriptives/commit/a3b54a6b3e3d57acc140b0f9afd72406a88104f8))
* Coherence model now handles empty strings as intended ([`abfa507`](https://github.com/HLasse/TextDescriptives/commit/abfa5071ba075f25ff8c170f5cee4f84ef648ea5))
* Dep distance test ([`2bed2c1`](https://github.com/HLasse/TextDescriptives/commit/2bed2c194b98062aad66d6ca0985fb92af6be977))

### Documentation
* Added demo to docs ([`6121eeb`](https://github.com/HLasse/TextDescriptives/commit/6121eebc0a125e68979591f6c585d19fae70746b))

## v2.4.4 (2023-03-28)
### Fix
* Add .zenodo.json ([`3cc463c`](https://github.com/HLasse/TextDescriptives/commit/3cc463c5bcc236bb5c49fc51eaba0b419d84ffcc))

### Documentation
* Add test requirements to faq ([`1550de7`](https://github.com/HLasse/TextDescriptives/commit/1550de7c4815779f53cc8ba260ddedcdbf8f0358))

## v2.4.3 (2023-03-01)
### Fix
* Add descriptive_stats pipe no matter the verbosity ([`3fd3240`](https://github.com/HLasse/TextDescriptives/commit/3fd3240bb5f706da6b882af8129945781021bb80))
* Change default verbosity of readability component ([`ddfd269`](https://github.com/HLasse/TextDescriptives/commit/ddfd269ae2c0d784b7e06bab0af74cbce293a288))
* Change verbosity of `lexeme_prob_table` ([`b64631f`](https://github.com/HLasse/TextDescriptives/commit/b64631fee040f08ec50b65ecd0c3a13ffe3d0dde))
* Automatically download supplied spacy model if not on disk ([`f54a9b6`](https://github.com/HLasse/TextDescriptives/commit/f54a9b61a018c0a77d72be986a2bc22f27a84c44))

### Documentation
* Change quick start model to lg ([`653fb49`](https://github.com/HLasse/TextDescriptives/commit/653fb49f887941cf6b4afb7566952f836ae0359b))
* Update readme to use lg model for proper coherence calculation ([`cdd85b7`](https://github.com/HLasse/TextDescriptives/commit/cdd85b7b9de08a94ad43aab14d42293acaf3b910))

## v2.4.2 (2023-03-01)
### Fix
* Handle case where extension is set, but pipeline is not ([`2ba2dd2`](https://github.com/HLasse/TextDescriptives/commit/2ba2dd210f612974f5279ad8302ee254d5c611b3))
* `extract_metrics` failing if `metrics=None` ([`6bfe6b0`](https://github.com/HLasse/TextDescriptives/commit/6bfe6b0ed74a7e490587878ea06ac2b9f3a9900a))

## v2.4.1 (2023-02-08)
### Fix
* Change auto-approve event  ([`729836f`](https://github.com/HLasse/TextDescriptives/commit/729836feb76a12507a6a0f703b434ec071124f5f))

## v2.4.0 (2023-01-31)
### Feature
* Add out of vocabulary ratio to quality component ([`a1177e5`](https://github.com/HLasse/TextDescriptives/commit/a1177e597de75f31507895540d2e6243dccafe27))

### Documentation
* Update quality docs with oov_ratio ([`74c22b1`](https://github.com/HLasse/TextDescriptives/commit/74c22b143fae43227feea28f74f19eff439a3240))

## v2.3.0 (2023-01-23)
### Feature
* Added information theoretic features ([`076c638`](https://github.com/HLasse/TextDescriptives/commit/076c638d3fa8109a2de924d686959c456f548c96))

### Fix
* Fix error caused by running all tests at once ([`5e46202`](https://github.com/HLasse/TextDescriptives/commit/5e46202f9bc939c07c55405487fb81f6d713546a))

### Documentation
* Added information metrics to docs ([`15bb255`](https://github.com/HLasse/TextDescriptives/commit/15bb255828ac7c15dc834b5976e7047126533541))
* Added update timer and fail on timeout ([`0d39b2e`](https://github.com/HLasse/TextDescriptives/commit/0d39b2ef3cabeb93c93d925e3af53b9e5ee9365f))
* Fixed tutorial to not download model ([`42589f6`](https://github.com/HLasse/TextDescriptives/commit/42589f6f453ea9e1d5be7e9cbe868e9baade32a4))

## v2.2.0 (2023-01-16)
### Feature
* Added QualityOutput ([`c0fb63c`](https://github.com/HLasse/TextDescriptives/commit/c0fb63c671ed1e4ccbe75afa4fb3301104a1ad0e))
* Updated way that that quality thresholds is set ([`f799186`](https://github.com/HLasse/TextDescriptives/commit/f7991864ba62a4dc0a36f42f2a13ad3079909a02))

### Documentation
* Removed multiprocessing from pipes ([`c224580`](https://github.com/HLasse/TextDescriptives/commit/c22458097d7ca97679da748e63be6ad1523c9a41))
* Changed print of quality ([`deb148b`](https://github.com/HLasse/TextDescriptives/commit/deb148bcbe9014c5285fe5a062320f7541b1c1d5))
* Fixed multiprocessing in tutorial ([`4ddebdf`](https://github.com/HLasse/TextDescriptives/commit/4ddebdf3be5124b92cb4bafe5b69fe1632143aa6))
* Updated docs with changes to the API ([`580bea1`](https://github.com/HLasse/TextDescriptives/commit/580bea199e91cb95e1876a0e4b7ea0ca5439129d))
* Updated tutorial ([`57d0054`](https://github.com/HLasse/TextDescriptives/commit/57d00543c1ce0525fee6570b8bb843bc62295bf7))
* Added quality tutorial to docs ([`2017fb3`](https://github.com/HLasse/TextDescriptives/commit/2017fb351c9b2157bb59525322f509e8367792a6))
* Added tutorial ([`fa2d65c`](https://github.com/HLasse/TextDescriptives/commit/fa2d65c1114cd6ae03d4638a44e7fe0c525aa80f))
* Added new tutorial for quality filtering ([`3697e59`](https://github.com/HLasse/TextDescriptives/commit/3697e596cc397c6b22be04f9841f2d55b4721903))
* Fix typo in coherence.rst ([`be83cf3`](https://github.com/HLasse/TextDescriptives/commit/be83cf354039179ef4d7d25ce4d99e237fc644be))
* Minor mismention ([`f5155c2`](https://github.com/HLasse/TextDescriptives/commit/f5155c28b5ccced6a334feb1b25f7ae3d4d91854))

## v2.1.0 (2023-01-06)
### Feature
* Wrapper function ([`fb33e19`](https://github.com/HLasse/TextDescriptives/commit/fb33e19e09b2551a049dccf42722d67f5c17199a))

### Fix
* Remove previously assigned extensions before extracting new metrics ([`1a7ca00`](https://github.com/HLasse/TextDescriptives/commit/1a7ca00559f1db0060cfcb0d0a120a1948d697c7))
* Remove doc extension instead of pipe component. TODO double check all assigns are correct ([`bc32d47`](https://github.com/HLasse/TextDescriptives/commit/bc32d479da59bfb438bb860795ca56e02fc60196))

### Documentation
* Add arxiv badge to readme ([`7b57aea`](https://github.com/HLasse/TextDescriptives/commit/7b57aeac655d56b21eac96e6a17c9a6c9c16831a))
* Update readme after review and add citation in docs ([`728a0d4`](https://github.com/HLasse/TextDescriptives/commit/728a0d40ab48d5626d733e800fd2208dab97d3f8))
* Add arxiv citation ([`bfab60b`](https://github.com/HLasse/TextDescriptives/commit/bfab60b89e57b101fd4efbb72fefe9a8ca4e7b6d))
* Add `extract_metrics` to docs and readme ([`163bee5`](https://github.com/HLasse/TextDescriptives/commit/163bee57ff5e26718594069564ff0ac8a0e63c47))
* Download spacy model in tutorial ([`96634cb`](https://github.com/HLasse/TextDescriptives/commit/96634cb62008ac18132513e4babbaa04350b1bc0))
* Reset changelog ([`12007b7`](https://github.com/HLasse/TextDescriptives/commit/12007b7d6f72223edd699cfc310ab035830c4ce6))

