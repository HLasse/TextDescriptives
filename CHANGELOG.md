# CHANGELOG



## v2.7.1 (2023-10-31)

### Ci

* ci: codespell ignore changelog ([`ce35d57`](https://github.com/HLasse/TextDescriptives/commit/ce35d57af99652dbdd8edce731c7c33b488dc76c))

### Fix

* fix: ensure always consistent column output of pos_proportions ([`c12ba20`](https://github.com/HLasse/TextDescriptives/commit/c12ba20c2b2993e28f0715d072797012a04381da))

### Unknown

* Merge pull request #290 from HLasse/fix-consistent-pos-prop-output

Fix-consistent-pos-prop-output ([`66e5525`](https://github.com/HLasse/TextDescriptives/commit/66e552549eea311ea9d32d1a2b398a7ff7050d43))

* lint ([`ed49b23`](https://github.com/HLasse/TextDescriptives/commit/ed49b230a23b820924ce975997d1ba0806bac160))

* tests: add test for correct number of pos tags ([`3aab19b`](https://github.com/HLasse/TextDescriptives/commit/3aab19b4c3accb55ef6a653ad12f6a6a3cc678cd))

* Merge pull request #289 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`09e6993`](https://github.com/HLasse/TextDescriptives/commit/09e6993a3b22cef534a0f2924003b384b057aa41))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/astral-sh/ruff-pre-commit: v0.1.1 → v0.1.3](https://github.com/astral-sh/ruff-pre-commit/compare/v0.1.1...v0.1.3) ([`b6de966`](https://github.com/HLasse/TextDescriptives/commit/b6de96644fc0b1b95d9ad381fcc6f7a983060cb6))

* Merge pull request #287 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`42c2442`](https://github.com/HLasse/TextDescriptives/commit/42c2442ad41cb2201d26b13a8f4a6f2921be52c5))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/psf/black: 23.9.1 → 23.10.1](https://github.com/psf/black/compare/23.9.1...23.10.1)
- [github.com/astral-sh/ruff-pre-commit: v0.0.292 → v0.1.1](https://github.com/astral-sh/ruff-pre-commit/compare/v0.0.292...v0.1.1)
- [github.com/pre-commit/mirrors-mypy: v1.6.0 → v1.6.1](https://github.com/pre-commit/mirrors-mypy/compare/v1.6.0...v1.6.1) ([`70e9c24`](https://github.com/HLasse/TextDescriptives/commit/70e9c24de5ad51701f70ecc2f4cba4210a43f6d8))

* Merge pull request #286 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`42ed7a6`](https://github.com/HLasse/TextDescriptives/commit/42ed7a640ef8ff9d65d38bbef7c685632428b0c9))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/pre-commit/mirrors-mypy: v1.5.1 → v1.6.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.5.1...v1.6.0) ([`65c3bcc`](https://github.com/HLasse/TextDescriptives/commit/65c3bcc0bc8c58bf6e7908b6024d53bdefec706b))

* Merge pull request #285 from HLasse/fix-codespell-changelog

ci: codespell ignore changelog ([`c103ff6`](https://github.com/HLasse/TextDescriptives/commit/c103ff66b1d1534c7e183e7fdee62fe6b5be3da0))


## v2.7.0 (2023-10-12)

### Build

* build: pin autodoc_pydantic version ([`5e6c3e2`](https://github.com/HLasse/TextDescriptives/commit/5e6c3e283de0c69b1f14654875042553c1c70929))

### Ci

* ci: fix documentation ci ([`7a2133c`](https://github.com/HLasse/TextDescriptives/commit/7a2133cc740a71bddce77922b51bf60eda1c6e5e))

* ci: fix documentation ci ([`99707b5`](https://github.com/HLasse/TextDescriptives/commit/99707b5a2d8a5d835c64099a5baa201fc3059e10))

### Documentation

* docs: add admonitions to information theory and readability docs ([`36abc80`](https://github.com/HLasse/TextDescriptives/commit/36abc80d125d8d6fd2e01f1ba7003b40c0e368d4))

* docs: fix readability docs formatting ([`6d6130a`](https://github.com/HLasse/TextDescriptives/commit/6d6130a6f5a42e0141bba6baa21276f8ff870ab8))

* docs: fix minor typo in docs ([`a833ebd`](https://github.com/HLasse/TextDescriptives/commit/a833ebdd87dc45c8e491caa311cc66ca200c1835))

* docs: add note on lexeme prop table to informatino theory ([`13d2b1e`](https://github.com/HLasse/TextDescriptives/commit/13d2b1e1b8edc44e2e663ecaca88ecef045f314a))

* docs: update readability docs ([`11981c0`](https://github.com/HLasse/TextDescriptives/commit/11981c045694a53d1f1bef78e98257578dbf8fbb))

* docs: Fixed codespell errors ([`8f7a0e3`](https://github.com/HLasse/TextDescriptives/commit/8f7a0e3995fcffab817062ca665591abe75798be))

### Feature

* feat: return nan for readability metrics requiring syllables if they can&#39;t be calculated ([`654ec6c`](https://github.com/HLasse/TextDescriptives/commit/654ec6c991c07289d1daf9192cd38577657c3b05))

* feat: return nan in descriptive stats  syllables if cant be calculated ([`bd08eb1`](https://github.com/HLasse/TextDescriptives/commit/bd08eb1d5f07a3a44598dca350825e93dfcc6959))

* feat: raise warning and set np.nan if language not supported for information theory ([`9ac2156`](https://github.com/HLasse/TextDescriptives/commit/9ac2156c14526659191d732469b836972315f2d5))

### Fix

* fix: add verbose flag to descriptive statistics ([`83980f3`](https://github.com/HLasse/TextDescriptives/commit/83980f3cfa219908a7c84fdede55f6c61ff7d375))

### Unknown

* Merge pull request #282 from HLasse/raise-warnings

Raise warning and output nan for languages without lexeme prop table and hyphenation module ([`1189cbf`](https://github.com/HLasse/TextDescriptives/commit/1189cbf371f059a22bdb76bc3c7478d6fd12ebec))

* misc ([`4984d50`](https://github.com/HLasse/TextDescriptives/commit/4984d501f1c49b3b7c320ae3fb4461024016765e))

* tests: test lexeme prop table and readability with languages without ([`e3b0371`](https://github.com/HLasse/TextDescriptives/commit/e3b03715729765bfa9466aa01bb35ba3aeb0e140))

* Merge pull request #281 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`d8122b6`](https://github.com/HLasse/TextDescriptives/commit/d8122b65d0a0eee4b5c28d2d03af838383da0c91))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/asottile/pyupgrade: v3.14.0 → v3.15.0](https://github.com/asottile/pyupgrade/compare/v3.14.0...v3.15.0) ([`7413f87`](https://github.com/HLasse/TextDescriptives/commit/7413f8703c02a92842183db6573a12772d69623e))

* Merge pull request #280 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`d98fe0a`](https://github.com/HLasse/TextDescriptives/commit/d98fe0a9ab9c6338b696493997e70682693420d1))

* [pre-commit.ci] auto fixes from pre-commit.com hooks

for more information, see https://pre-commit.ci ([`7da78b1`](https://github.com/HLasse/TextDescriptives/commit/7da78b1f73b567f0158bb8f057162af83ed992e9))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/codespell-project/codespell: v2.2.5 → v2.2.6](https://github.com/codespell-project/codespell/compare/v2.2.5...v2.2.6)
- [github.com/asottile/pyupgrade: v3.13.0 → v3.14.0](https://github.com/asottile/pyupgrade/compare/v3.13.0...v3.14.0)
- [github.com/astral-sh/ruff-pre-commit: v0.0.291 → v0.0.292](https://github.com/astral-sh/ruff-pre-commit/compare/v0.0.291...v0.0.292) ([`37e0454`](https://github.com/HLasse/TextDescriptives/commit/37e04542d674cd797521a26bc22f8b94f99d6446))

* Merge pull request #278 from HLasse/dependabot/pip/black-23.9.1

:arrow_up: Bump black from 23.7.0 to 23.9.1 ([`6470458`](https://github.com/HLasse/TextDescriptives/commit/64704589508f0e5b6e367ef5e6681c67e97b0f76))

* :arrow_up: Bump black from 23.7.0 to 23.9.1

Bumps [black](https://github.com/psf/black) from 23.7.0 to 23.9.1.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/23.7.0...23.9.1)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`671af21`](https://github.com/HLasse/TextDescriptives/commit/671af21f29fe40a6dd1c8a81c86916904001203f))

* Merge pull request #279 from HLasse/dependabot/pip/pre-commit-3.4.0

:arrow_up: Bump pre-commit from 3.3.3 to 3.4.0 ([`e6f9781`](https://github.com/HLasse/TextDescriptives/commit/e6f9781511174101eb09e96f2ac293065e99bbd1))

* :arrow_up: Bump pre-commit from 3.3.3 to 3.4.0

Bumps [pre-commit](https://github.com/pre-commit/pre-commit) from 3.3.3 to 3.4.0.
- [Release notes](https://github.com/pre-commit/pre-commit/releases)
- [Changelog](https://github.com/pre-commit/pre-commit/blob/main/CHANGELOG.md)
- [Commits](https://github.com/pre-commit/pre-commit/compare/v3.3.3...v3.4.0)

---
updated-dependencies:
- dependency-name: pre-commit
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`309761c`](https://github.com/HLasse/TextDescriptives/commit/309761c94b62a7a07fb74dc395af8d7d93768a3e))

* Merge pull request #276 from HLasse/dependabot/pip/ipython-lte-8.16.0

:arrow_up: Update ipython requirement from &lt;=8.14.0 to &lt;=8.16.0 ([`8572877`](https://github.com/HLasse/TextDescriptives/commit/8572877c767a028284bd1d3b83dbd7bf26dd61a1))

* Merge pull request #277 from HLasse/dependabot/pip/ruff-0.0.291

:arrow_up: Bump ruff from 0.0.286 to 0.0.291 ([`9ab23ae`](https://github.com/HLasse/TextDescriptives/commit/9ab23ae69527523cc4b7aba6f1fe7a3c7734c611))

* :arrow_up: Bump ruff from 0.0.286 to 0.0.291

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.0.286 to 0.0.291.
- [Release notes](https://github.com/astral-sh/ruff/releases)
- [Changelog](https://github.com/astral-sh/ruff/blob/main/BREAKING_CHANGES.md)
- [Commits](https://github.com/astral-sh/ruff/compare/v0.0.286...v0.0.291)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`cd8abf0`](https://github.com/HLasse/TextDescriptives/commit/cd8abf0b104573833d3250dc9e95695a49ca57ac))

* :arrow_up: Update ipython requirement from &lt;=8.14.0 to &lt;=8.16.0

Updates the requirements on [ipython](https://github.com/ipython/ipython) to permit the latest version.
- [Release notes](https://github.com/ipython/ipython/releases)
- [Commits](https://github.com/ipython/ipython/compare/rel-0.8.4...8.16.0)

---
updated-dependencies:
- dependency-name: ipython
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`3aaf88b`](https://github.com/HLasse/TextDescriptives/commit/3aaf88b92862892fe02926d60f9ccf1e45376ef9))

* Merge pull request #275 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`76f5675`](https://github.com/HLasse/TextDescriptives/commit/76f56755a40945ca6d0ca3502298d57942480f2c))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/asottile/pyupgrade: v3.11.0 → v3.13.0](https://github.com/asottile/pyupgrade/compare/v3.11.0...v3.13.0)
- [github.com/astral-sh/ruff-pre-commit: v0.0.290 → v0.0.291](https://github.com/astral-sh/ruff-pre-commit/compare/v0.0.290...v0.0.291) ([`8e8cc82`](https://github.com/HLasse/TextDescriptives/commit/8e8cc8286acaac5bb937c84c8a0aba448370cd47))

* Merge pull request #274 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`43d32e0`](https://github.com/HLasse/TextDescriptives/commit/43d32e05d068d12e7e845b66b148e1865487c3f9))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/asottile/pyupgrade: v3.10.1 → v3.11.0](https://github.com/asottile/pyupgrade/compare/v3.10.1...v3.11.0)
- [github.com/astral-sh/ruff-pre-commit: v0.0.288 → v0.0.290](https://github.com/astral-sh/ruff-pre-commit/compare/v0.0.288...v0.0.290) ([`cdadb4e`](https://github.com/HLasse/TextDescriptives/commit/cdadb4e80ab6c4fefaa2ebd88156d2accca7e889))

* Merge pull request #273 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`f4e97b9`](https://github.com/HLasse/TextDescriptives/commit/f4e97b92081e0ea262648a0a5b1365ea5b279172))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/psf/black: 23.7.0 → 23.9.1](https://github.com/psf/black/compare/23.7.0...23.9.1)
- [github.com/astral-sh/ruff-pre-commit: v0.0.287 → v0.0.288](https://github.com/astral-sh/ruff-pre-commit/compare/v0.0.287...v0.0.288) ([`d600a6b`](https://github.com/HLasse/TextDescriptives/commit/d600a6b2121a85d9394b905b6d5427fc5162e656))

* Merge pull request #272 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`c49c460`](https://github.com/HLasse/TextDescriptives/commit/c49c460d288d81e531b3f421e8e555f55071462b))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/asottile/add-trailing-comma: v3.0.1 → v3.1.0](https://github.com/asottile/add-trailing-comma/compare/v3.0.1...v3.1.0)
- [github.com/astral-sh/ruff-pre-commit: v0.0.286 → v0.0.287](https://github.com/astral-sh/ruff-pre-commit/compare/v0.0.286...v0.0.287) ([`d18f63d`](https://github.com/HLasse/TextDescriptives/commit/d18f63d278cf81dc4207a39a7dfcf1e23d09b6b9))

* Merge pull request #271 from HLasse/dependabot/pip/mypy-1.5.1

:arrow_up: Bump mypy from 1.4.1 to 1.5.1 ([`02230da`](https://github.com/HLasse/TextDescriptives/commit/02230daa4db47b780b7b3bd32bc5633324d6b14b))

* :arrow_up: Bump mypy from 1.4.1 to 1.5.1

Bumps [mypy](https://github.com/python/mypy) from 1.4.1 to 1.5.1.
- [Commits](https://github.com/python/mypy/compare/v1.4.1...v1.5.1)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b0e28bd`](https://github.com/HLasse/TextDescriptives/commit/b0e28bdc7393d81402eb85711f21c7ee3edac384))

* Merge pull request #270 from HLasse/dependabot/pip/ruff-0.0.286

:arrow_up: Bump ruff from 0.0.281 to 0.0.286 ([`8b1daa8`](https://github.com/HLasse/TextDescriptives/commit/8b1daa84b6391e070434a84333731b87e1649b8f))

* :arrow_up: Bump ruff from 0.0.281 to 0.0.286

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.0.281 to 0.0.286.
- [Release notes](https://github.com/astral-sh/ruff/releases)
- [Changelog](https://github.com/astral-sh/ruff/blob/main/BREAKING_CHANGES.md)
- [Commits](https://github.com/astral-sh/ruff/compare/v0.0.281...v0.0.286)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`372a79c`](https://github.com/HLasse/TextDescriptives/commit/372a79c57bbf94503490fd2a92011cc0b16894ec))

* Merge pull request #269 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`8db3c9e`](https://github.com/HLasse/TextDescriptives/commit/8db3c9e82dabee688a69232b6c8a28d94708990b))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/astral-sh/ruff-pre-commit: v0.0.285 → v0.0.286](https://github.com/astral-sh/ruff-pre-commit/compare/v0.0.285...v0.0.286) ([`533afbf`](https://github.com/HLasse/TextDescriptives/commit/533afbf2c4c828a7265ccf2ae8d6a3a29077aff5))

* Merge pull request #268 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`d73d25f`](https://github.com/HLasse/TextDescriptives/commit/d73d25fe181975a66584e9d4255e42fa556ffdc9))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/astral-sh/ruff-pre-commit: v0.0.284 → v0.0.285](https://github.com/astral-sh/ruff-pre-commit/compare/v0.0.284...v0.0.285)
- [github.com/pre-commit/mirrors-mypy: v1.5.0 → v1.5.1](https://github.com/pre-commit/mirrors-mypy/compare/v1.5.0...v1.5.1) ([`ba46eab`](https://github.com/HLasse/TextDescriptives/commit/ba46eab51a15bd42d1f93d115591858edc1a63e2))

* Merge pull request #267 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`b1712f6`](https://github.com/HLasse/TextDescriptives/commit/b1712f678694fd75817a3baa3c6dbe2fe8db2fa9))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/astral-sh/ruff-pre-commit: v0.0.282 → v0.0.284](https://github.com/astral-sh/ruff-pre-commit/compare/v0.0.282...v0.0.284)
- [github.com/pre-commit/mirrors-mypy: v1.4.1 → v1.5.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.4.1...v1.5.0) ([`c579264`](https://github.com/HLasse/TextDescriptives/commit/c57926402ae4d3cbd94da74c2527c166558d8b88))

* Merge pull request #264 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`9594a26`](https://github.com/HLasse/TextDescriptives/commit/9594a268c725614aa87a05c7b32073211d6f9eef))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/astral-sh/ruff-pre-commit: v0.0.281 → v0.0.282](https://github.com/astral-sh/ruff-pre-commit/compare/v0.0.281...v0.0.282) ([`59c9320`](https://github.com/HLasse/TextDescriptives/commit/59c9320437a52bfbdfb182f4e2cbade2f69bfb83))

* Merge pull request #263 from HLasse/dependabot/pip/ruff-0.0.281

:arrow_up: Bump ruff from 0.0.275 to 0.0.281 ([`b4072cc`](https://github.com/HLasse/TextDescriptives/commit/b4072cc4fb59c6ad7c3801a3e57f5130a1f37023))

* :arrow_up: Bump ruff from 0.0.275 to 0.0.281

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.0.275 to 0.0.281.
- [Release notes](https://github.com/astral-sh/ruff/releases)
- [Changelog](https://github.com/astral-sh/ruff/blob/main/BREAKING_CHANGES.md)
- [Commits](https://github.com/astral-sh/ruff/compare/v0.0.275...v0.0.281)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`676adb0`](https://github.com/HLasse/TextDescriptives/commit/676adb0be63fa82f56756010f167a204fbbc6b83))

* Merge pull request #262 from HLasse/dependabot/pip/black-23.7.0

:arrow_up: Bump black from 23.3.0 to 23.7.0 ([`14afb8c`](https://github.com/HLasse/TextDescriptives/commit/14afb8cfeede74ad5d09fa3295cf5d68cbacd6b1))

* :arrow_up: Bump black from 23.3.0 to 23.7.0

Bumps [black](https://github.com/psf/black) from 23.3.0 to 23.7.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/23.3.0...23.7.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f9f2e6c`](https://github.com/HLasse/TextDescriptives/commit/f9f2e6cc61e25ad27bbcf73f644664d55705d6da))

* Merge pull request #261 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`6d619cb`](https://github.com/HLasse/TextDescriptives/commit/6d619cbf2ad04c108a4596a5cb9e7fe9b9345202))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/asottile/pyupgrade: v3.9.0 → v3.10.1](https://github.com/asottile/pyupgrade/compare/v3.9.0...v3.10.1)
- [github.com/asottile/add-trailing-comma: v3.0.0 → v3.0.1](https://github.com/asottile/add-trailing-comma/compare/v3.0.0...v3.0.1)
- [github.com/astral-sh/ruff-pre-commit: v0.0.280 → v0.0.281](https://github.com/astral-sh/ruff-pre-commit/compare/v0.0.280...v0.0.281) ([`8a51afb`](https://github.com/HLasse/TextDescriptives/commit/8a51afb4f03deb9be5cacbb2812b72ae866058e5))

* Merge pull request #260 from HLasse/fix-codespell

docs: Fixed codespell errors ([`2dd08f5`](https://github.com/HLasse/TextDescriptives/commit/2dd08f584a1ab3e9e517b6fc1a90a25ab77b232e))


## v2.6.2 (2023-07-31)

### Ci

* ci: update semver release version ([`86d6bd8`](https://github.com/HLasse/TextDescriptives/commit/86d6bd8646bb9a5d22952e878a025749bc7f051c))

* ci: maybe fix semver ([`2e0ab85`](https://github.com/HLasse/TextDescriptives/commit/2e0ab853f8ccd8e22808d49d575dcd7a443318f9))

* ci: update sem ver project version ([`21dd787`](https://github.com/HLasse/TextDescriptives/commit/21dd787e3b87ea97ab760fbf39beb34ea4a45440))

* ci: update semantic versioning ([`0d3e14d`](https://github.com/HLasse/TextDescriptives/commit/0d3e14d2b381d4a2accbf35c8c41393cc87cfe32))

### Fix

* fix: force version bump ([`d233737`](https://github.com/HLasse/TextDescriptives/commit/d233737e8d6e1403b4d8b550cfd8bb5db3c69a3b))

### Unknown

* Merge pull request #259 from HLasse/KennethEnevoldsen-patch-1

Removed upper bound on robust libraries ([`87c1980`](https://github.com/HLasse/TextDescriptives/commit/87c1980afcbb78e36870fbe20f99ab485c1a0f70))

* Removed upper bound on robust libraries

Notably addressing #258 ([`606bc78`](https://github.com/HLasse/TextDescriptives/commit/606bc787b839e1a4223b82fbc3f331d4bbff95a4))

* Merge pull request #257 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`9ec4f2d`](https://github.com/HLasse/TextDescriptives/commit/9ec4f2d7567099a0f5551190b6df02fcae5bb67c))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/astral-sh/ruff-pre-commit: v0.0.278 → v0.0.280](https://github.com/astral-sh/ruff-pre-commit/compare/v0.0.278...v0.0.280) ([`f5c49f0`](https://github.com/HLasse/TextDescriptives/commit/f5c49f02a7e85b4da2ed790e15b5d58f41869dda))

* Merge pull request #256 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`6d083ff`](https://github.com/HLasse/TextDescriptives/commit/6d083ff5c4e3b7a70ccc82fec4825635b5978604))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/astral-sh/ruff-pre-commit: v0.0.277 → v0.0.278](https://github.com/astral-sh/ruff-pre-commit/compare/v0.0.277...v0.0.278) ([`0015900`](https://github.com/HLasse/TextDescriptives/commit/00159003f15e60bb7f0d2165340907992eeadbe8))

* Update release.yml ([`f88d6b3`](https://github.com/HLasse/TextDescriptives/commit/f88d6b301a3016d46dffd135f4ebec8eb5cfd131))

* Merge pull request #252 from HLasse/dependabot/pip/pre-commit-3.3.3

:arrow_up: Bump pre-commit from 3.3.2 to 3.3.3 ([`78c21b8`](https://github.com/HLasse/TextDescriptives/commit/78c21b81bcbddc1c9794bc1c7413484d6011fda8))

* Merge pull request #251 from HLasse/dependabot/pip/mypy-1.4.1

:arrow_up: Bump mypy from 1.3.0 to 1.4.1 ([`8c01f28`](https://github.com/HLasse/TextDescriptives/commit/8c01f28189083d76e494a6ed6280b77f4d18c03d))

* :arrow_up: Bump mypy from 1.3.0 to 1.4.1

Bumps [mypy](https://github.com/python/mypy) from 1.3.0 to 1.4.1.
- [Commits](https://github.com/python/mypy/compare/v1.3.0...v1.4.1)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b0671e5`](https://github.com/HLasse/TextDescriptives/commit/b0671e528beff2ae2e22d0be6010a969e0dcdd8a))

* :arrow_up: Bump pre-commit from 3.3.2 to 3.3.3

Bumps [pre-commit](https://github.com/pre-commit/pre-commit) from 3.3.2 to 3.3.3.
- [Release notes](https://github.com/pre-commit/pre-commit/releases)
- [Changelog](https://github.com/pre-commit/pre-commit/blob/main/CHANGELOG.md)
- [Commits](https://github.com/pre-commit/pre-commit/compare/v3.3.2...v3.3.3)

---
updated-dependencies:
- dependency-name: pre-commit
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b87af7a`](https://github.com/HLasse/TextDescriptives/commit/b87af7aefebf1de9d5d43b65fadc8d640aed9e25))

* Merge pull request #250 from HLasse/dependabot/pip/ruff-0.0.275

:arrow_up: Bump ruff from 0.0.270 to 0.0.275 ([`9efdf96`](https://github.com/HLasse/TextDescriptives/commit/9efdf9626a77ad5841814aa420a26f07162f11b8))

* Merge pull request #255 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`034e8f0`](https://github.com/HLasse/TextDescriptives/commit/034e8f06ffd23cfddc57057d51fb57fb0c79e8a5))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/asottile/pyupgrade: v3.8.0 → v3.9.0](https://github.com/asottile/pyupgrade/compare/v3.8.0...v3.9.0)
- [github.com/psf/black: 23.3.0 → 23.7.0](https://github.com/psf/black/compare/23.3.0...23.7.0)
- [github.com/astral-sh/ruff-pre-commit: v0.0.276 → v0.0.277](https://github.com/astral-sh/ruff-pre-commit/compare/v0.0.276...v0.0.277) ([`4428231`](https://github.com/HLasse/TextDescriptives/commit/44282316442c1973af86b600a12e535bc07bf1cd))

* Merge pull request #253 from HLasse/dependabot/pip/ipython-lte-8.14.0

:arrow_up: Update ipython requirement from &lt;=8.12 to &lt;=8.14.0 ([`61afb31`](https://github.com/HLasse/TextDescriptives/commit/61afb31f42d81bda7b36b717e9d5869c97280d76))

* Merge pull request #254 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`a32fadf`](https://github.com/HLasse/TextDescriptives/commit/a32fadf63f6e34c66f81b994e3481e715852c77e))

* [pre-commit.ci] auto fixes from pre-commit.com hooks

for more information, see https://pre-commit.ci ([`218f9e1`](https://github.com/HLasse/TextDescriptives/commit/218f9e1c645323923253b520484886b96bcec303))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/asottile/pyupgrade: v3.7.0 → v3.8.0](https://github.com/asottile/pyupgrade/compare/v3.7.0...v3.8.0)
- [github.com/asottile/add-trailing-comma: v2.5.1 → v3.0.0](https://github.com/asottile/add-trailing-comma/compare/v2.5.1...v3.0.0)
- https://github.com/charliermarsh/ruff-pre-commit → https://github.com/astral-sh/ruff-pre-commit
- [github.com/astral-sh/ruff-pre-commit: v0.0.275 → v0.0.276](https://github.com/astral-sh/ruff-pre-commit/compare/v0.0.275...v0.0.276) ([`98576dd`](https://github.com/HLasse/TextDescriptives/commit/98576dde9eb7cba9bdfc8aa83c35302a8b1c77e5))

* Merge pull request #249 from HLasse/dependabot/pip/numpy-gte-1.20.0-and-lt-1.26.0

:arrow_up: Update numpy requirement from &lt;1.25.0,&gt;=1.20.0 to &gt;=1.20.0,&lt;1.26.0 ([`791afac`](https://github.com/HLasse/TextDescriptives/commit/791afac42a9995e951f3a7fbbc119a02a305480c))

* :arrow_up: Update ipython requirement from &lt;=8.12 to &lt;=8.14.0

Updates the requirements on [ipython](https://github.com/ipython/ipython) to permit the latest version.
- [Release notes](https://github.com/ipython/ipython/releases)
- [Commits](https://github.com/ipython/ipython/compare/rel-0.8.4...8.14.0)

---
updated-dependencies:
- dependency-name: ipython
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`aa7e639`](https://github.com/HLasse/TextDescriptives/commit/aa7e6394b8abb6c6f8e62a31d25ab1c2f783be90))

* :arrow_up: Bump ruff from 0.0.270 to 0.0.275

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.0.270 to 0.0.275.
- [Release notes](https://github.com/astral-sh/ruff/releases)
- [Changelog](https://github.com/astral-sh/ruff/blob/main/BREAKING_CHANGES.md)
- [Commits](https://github.com/astral-sh/ruff/compare/v0.0.270...v0.0.275)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7ab940f`](https://github.com/HLasse/TextDescriptives/commit/7ab940f75b541fee90fb9525c1c7b5609ea82dc1))

* :arrow_up: Update numpy requirement

Updates the requirements on [numpy](https://github.com/numpy/numpy) to permit the latest version.
- [Release notes](https://github.com/numpy/numpy/releases)
- [Changelog](https://github.com/numpy/numpy/blob/main/doc/RELEASE_WALKTHROUGH.rst)
- [Commits](https://github.com/numpy/numpy/compare/v1.20.0...v1.25.0)

---
updated-dependencies:
- dependency-name: numpy
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`dc33dd9`](https://github.com/HLasse/TextDescriptives/commit/dc33dd9587e08cac13342cd154a0ae3803ef26f5))

* Merge pull request #248 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`faf0f95`](https://github.com/HLasse/TextDescriptives/commit/faf0f95d5e9441d66bce9d9cab82cb3854c95bd0))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/charliermarsh/ruff-pre-commit: v0.0.272 → v0.0.275](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.272...v0.0.275)
- [github.com/pre-commit/mirrors-mypy: v1.3.0 → v1.4.1](https://github.com/pre-commit/mirrors-mypy/compare/v1.3.0...v1.4.1) ([`1d28d39`](https://github.com/HLasse/TextDescriptives/commit/1d28d3939efb57200a5c973e07a729aedea4e852))

* Merge pull request #247 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`4c23036`](https://github.com/HLasse/TextDescriptives/commit/4c2303604f90a477b400635830b62986d3278dce))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/codespell-project/codespell: v2.2.4 → v2.2.5](https://github.com/codespell-project/codespell/compare/v2.2.4...v2.2.5)
- [github.com/asottile/pyupgrade: v3.6.0 → v3.7.0](https://github.com/asottile/pyupgrade/compare/v3.6.0...v3.7.0) ([`c152e61`](https://github.com/HLasse/TextDescriptives/commit/c152e616e85b8ca5a20b23b9e498567bdcd203ee))

* Merge pull request #246 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`3661abd`](https://github.com/HLasse/TextDescriptives/commit/3661abde5c1de936576c3131cb6ba7c8852d79e2))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/asottile/pyupgrade: v3.4.0 → v3.6.0](https://github.com/asottile/pyupgrade/compare/v3.4.0...v3.6.0)
- [github.com/asottile/add-trailing-comma: v2.4.0 → v2.5.1](https://github.com/asottile/add-trailing-comma/compare/v2.4.0...v2.5.1)
- [github.com/charliermarsh/ruff-pre-commit: v0.0.270 → v0.0.272](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.270...v0.0.272) ([`c291f88`](https://github.com/HLasse/TextDescriptives/commit/c291f88ca39e8ed05822dcffc985e6e8fc90c05c))

* Merge pull request #243 from HLasse/dependabot/pip/pre-commit-3.3.2

:arrow_up: Bump pre-commit from 3.2.2 to 3.3.2 ([`c14826c`](https://github.com/HLasse/TextDescriptives/commit/c14826c2b23c9be451c940aac43aef5be074c9d3))

* :arrow_up: Bump pre-commit from 3.2.2 to 3.3.2

Bumps [pre-commit](https://github.com/pre-commit/pre-commit) from 3.2.2 to 3.3.2.
- [Release notes](https://github.com/pre-commit/pre-commit/releases)
- [Changelog](https://github.com/pre-commit/pre-commit/blob/main/CHANGELOG.md)
- [Commits](https://github.com/pre-commit/pre-commit/compare/v3.2.2...v3.3.2)

---
updated-dependencies:
- dependency-name: pre-commit
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ee23864`](https://github.com/HLasse/TextDescriptives/commit/ee23864f4c300d85bdb50fd5e95c514326f252f7))

* Merge pull request #242 from HLasse/dependabot/pip/ruff-0.0.270

:arrow_up: Bump ruff from 0.0.263 to 0.0.270 ([`eadc7af`](https://github.com/HLasse/TextDescriptives/commit/eadc7afb4da4fee26b7c6fc5d63964f0498ef17e))

* :arrow_up: Bump ruff from 0.0.263 to 0.0.270

Bumps [ruff](https://github.com/charliermarsh/ruff) from 0.0.263 to 0.0.270.
- [Release notes](https://github.com/charliermarsh/ruff/releases)
- [Changelog](https://github.com/charliermarsh/ruff/blob/main/BREAKING_CHANGES.md)
- [Commits](https://github.com/charliermarsh/ruff/compare/v0.0.263...v0.0.270)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`536c559`](https://github.com/HLasse/TextDescriptives/commit/536c559cc5231c9a7982255d7c41841e1c03d604))

* Merge pull request #241 from HLasse/dependabot/pip/mypy-1.3.0

:arrow_up: Bump mypy from 1.1.1 to 1.3.0 ([`d6b9074`](https://github.com/HLasse/TextDescriptives/commit/d6b90745eafd5e16705e7e674e3ea3393da28dd1))

* Merge pull request #245 from HLasse/dependabot/pip/pandas-gte-1.0.0-and-lt-2.1.0

:arrow_up: Update pandas requirement from &lt;1.6.0,&gt;=1.0.0 to &gt;=1.0.0,&lt;2.1.0 ([`fe2c590`](https://github.com/HLasse/TextDescriptives/commit/fe2c59009a83cdc39535327c875dd2441131785b))

* :arrow_up: Update pandas requirement

Updates the requirements on [pandas](https://github.com/pandas-dev/pandas) to permit the latest version.
- [Release notes](https://github.com/pandas-dev/pandas/releases)
- [Commits](https://github.com/pandas-dev/pandas/compare/v1.0.0...v2.0.2)

---
updated-dependencies:
- dependency-name: pandas
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f5e68a5`](https://github.com/HLasse/TextDescriptives/commit/f5e68a5d6304a51462013f0a25b57c03b431cc0c))

* :arrow_up: Bump mypy from 1.1.1 to 1.3.0

Bumps [mypy](https://github.com/python/mypy) from 1.1.1 to 1.3.0.
- [Commits](https://github.com/python/mypy/compare/v1.1.1...v1.3.0)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a0ada59`](https://github.com/HLasse/TextDescriptives/commit/a0ada59b3ce00e8f4b71df38e5cb7959c06604db))

* Merge pull request #240 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`98add8b`](https://github.com/HLasse/TextDescriptives/commit/98add8bb60fdf100b3bc065d3f685b83e2cdd903))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/charliermarsh/ruff-pre-commit: v0.0.269 → v0.0.270](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.269...v0.0.270) ([`1fb4e9c`](https://github.com/HLasse/TextDescriptives/commit/1fb4e9c8fcec34696eeb1ce88799d698a45792b2))

* Merge pull request #239 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`b2069c7`](https://github.com/HLasse/TextDescriptives/commit/b2069c76ecc57006fca56df95ab7203ad0b1cccc))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/charliermarsh/ruff-pre-commit: v0.0.267 → v0.0.269](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.267...v0.0.269) ([`9c10dfc`](https://github.com/HLasse/TextDescriptives/commit/9c10dfc1ac7ea92450c43541881d53f946f75b77))

* Merge pull request #238 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`f837615`](https://github.com/HLasse/TextDescriptives/commit/f837615902c8c2b8201cfb44fdae2610b821a1a3))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/charliermarsh/ruff-pre-commit: v0.0.265 → v0.0.267](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.265...v0.0.267)
- [github.com/pre-commit/mirrors-mypy: v1.2.0 → v1.3.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.2.0...v1.3.0) ([`a599885`](https://github.com/HLasse/TextDescriptives/commit/a599885f61e1b4d59795dd77a10dcf1591d1e8ec))

* Merge pull request #236 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`6c254a5`](https://github.com/HLasse/TextDescriptives/commit/6c254a5a39418db35ce0e13d29eec9179563d6fb))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/asottile/pyupgrade: v3.3.2 → v3.4.0](https://github.com/asottile/pyupgrade/compare/v3.3.2...v3.4.0)
- [github.com/charliermarsh/ruff-pre-commit: v0.0.263 → v0.0.265](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.263...v0.0.265) ([`6c2e56b`](https://github.com/HLasse/TextDescriptives/commit/6c2e56bd667562bb72c07899b5629bf52798d4ea))


## v2.6.1 (2023-05-03)

### Build

* build: cap ipython version in tutorials for 3.8 compatibility ([`9199946`](https://github.com/HLasse/TextDescriptives/commit/91999465dd3f613dd3bc86691d2710cdd1494d31))

### Documentation

* docs: removed error from notebook ([`708d9d7`](https://github.com/HLasse/TextDescriptives/commit/708d9d72ed9f90e9da2840261173c6d6609fff3e))

* docs: Added description of readability scores ([`16cda18`](https://github.com/HLasse/TextDescriptives/commit/16cda18ce2742fd403822387a14ac10d109d649f))

### Fix

* fix: Updated dev. dependencies to not include upper bounds ([`48bedec`](https://github.com/HLasse/TextDescriptives/commit/48bedecfb9565b23c1cb11f52b0fd414d2554d01))

### Unknown

* Merge pull request #233 from HLasse/updated-deps

docs: Updated documentation to include description of readability scores ([`5c9f689`](https://github.com/HLasse/TextDescriptives/commit/5c9f6899d4ec126583ac0d9b53bf96a0c55225ed))

* Apply suggestions from code review

docs: minor edits to readability docs ([`43df11f`](https://github.com/HLasse/TextDescriptives/commit/43df11f86b1b923aeb12fc714c704f4e94e40a67))

* Merge pull request #231 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`0683ad4`](https://github.com/HLasse/TextDescriptives/commit/0683ad4d57db6f7676c5152e90e1ec53c7af2535))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/charliermarsh/ruff-pre-commit: v0.0.262 → v0.0.263](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.262...v0.0.263) ([`eee436e`](https://github.com/HLasse/TextDescriptives/commit/eee436e15b78b8dc78c49cf3c279d02b3933f878))

* Merge pull request #230 from HLasse/dependabot/pip/sphinx-gte-5.3.0-and-lt-7.1.0

:arrow_up: Update sphinx requirement from &lt;6.2.0,&gt;=5.3.0 to &gt;=5.3.0,&lt;7.1.0 ([`be030a7`](https://github.com/HLasse/TextDescriptives/commit/be030a77df80bd9357137300436619e943d34deb))

* :arrow_up: Update sphinx requirement

Updates the requirements on [sphinx](https://github.com/sphinx-doc/sphinx) to permit the latest version.
- [Release notes](https://github.com/sphinx-doc/sphinx/releases)
- [Changelog](https://github.com/sphinx-doc/sphinx/blob/master/CHANGES)
- [Commits](https://github.com/sphinx-doc/sphinx/compare/v5.3.0...v7.0.0)

---
updated-dependencies:
- dependency-name: sphinx
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8f9d027`](https://github.com/HLasse/TextDescriptives/commit/8f9d02720be76bd189cb38a9bb60b1ee2f021a7a))

* Merge pull request #225 from HLasse/HLasse-patch-1 ([`106513a`](https://github.com/HLasse/TextDescriptives/commit/106513a48ca364939b701d8e2dbd63a83b770a9f))

* readme: remove arxiv badge, clean up intro ([`7e62691`](https://github.com/HLasse/TextDescriptives/commit/7e62691766d3e60eb13fdfb098dc85de6740e125))


## v2.6.0 (2023-04-28)

### Build

* build: remove python3.7 support ([`5e68fc2`](https://github.com/HLasse/TextDescriptives/commit/5e68fc2428d6be4e8f5fe2e6886b77ed306337f0))

* build: as sklearn as possible extra dependency ([`86ff127`](https://github.com/HLasse/TextDescriptives/commit/86ff127c9e6f91f32a36f715d7a27d9ceda361c0))

* build: py3.7 compatibility ([`a0ad679`](https://github.com/HLasse/TextDescriptives/commit/a0ad6798c9a90e28fbb8661c8586cd51fbd7162e))

### Chore

* chore: pre-commit ([`cad0b34`](https://github.com/HLasse/TextDescriptives/commit/cad0b342bde99820a90f7332ba0b785ba75261de))

* chore: pre-commit ([`44aa0f0`](https://github.com/HLasse/TextDescriptives/commit/44aa0f000f3a9825cd808e3ce306c594a4404689))

### Documentation

* docs: add sklearn to requirements in docs ([`33194c9`](https://github.com/HLasse/TextDescriptives/commit/33194c937803acdd2abb4198b97ead3981958fd1))

* docs: minor docstring changes ([`375d3e0`](https://github.com/HLasse/TextDescriptives/commit/375d3e03a8792b54f5dfd6080e27ca34925628c3))

* docs: add sklearn tutorial ([`4220072`](https://github.com/HLasse/TextDescriptives/commit/42200725c2c89c738a07fffdc1b8f7b6d111fc6c))

### Feature

* feat: add sklearn transformer ([`be733c6`](https://github.com/HLasse/TextDescriptives/commit/be733c6161993deb6e284475224d6363c99a8962))

### Refactor

* refactor: move sklearn integration to separate module ([`12bb8c4`](https://github.com/HLasse/TextDescriptives/commit/12bb8c4202a444740b31c6627b05dc641cd853dc))

### Unknown

* Merge pull request #224 from HLasse/sklearn_tutorial

feat: sklearn integration ([`4cc31ce`](https://github.com/HLasse/TextDescriptives/commit/4cc31ce5ce1c838411e3027d1a295c559ccfaea3))

* Merge branch &#39;sklearn_tutorial&#39; of https://github.com/HLasse/TextDescriptives into sklearn_tutorial ([`415e027`](https://github.com/HLasse/TextDescriptives/commit/415e027683239a165bae20ac7c8c70fae7fa16b1))


## v2.5.1 (2023-04-26)

### Fix

* fix: don&#39;t subtract 1 from counts if `add_all_tags` is False ([`02b61a6`](https://github.com/HLasse/TextDescriptives/commit/02b61a6358764af5901891e002bc4e3771c777c6))


## v2.5.0 (2023-04-26)

### Chore

* chore: minor refactor ([`bfeaa58`](https://github.com/HLasse/TextDescriptives/commit/bfeaa58796ebd3ddac1ebed5a83772dfce822197))

* chore: pre-commit ([`c703203`](https://github.com/HLasse/TextDescriptives/commit/c703203e9f70dd6458fa2e3d4a8571c2fc81fc06))

* chore: pre-commit ([`e80799b`](https://github.com/HLasse/TextDescriptives/commit/e80799b3059451a48e5ac92ac7ada44e7f820aa6))

### Feature

* feat: add proportions of all pos tags ([`664c0e8`](https://github.com/HLasse/TextDescriptives/commit/664c0e886a4ff075ea15ec08c9acf1e76a785477))

### Fix

* fix: Listed metrics deviate between extraction functions in docs
Fixes #219 ([`4632407`](https://github.com/HLasse/TextDescriptives/commit/4632407bb5c02cb1a602e287b8e77918390214ca))

* fix: handle empty strings in pos_proportions ([`762b7b2`](https://github.com/HLasse/TextDescriptives/commit/762b7b2f454eaeec214cf5c2421dab75a8ec95c4))

### Unknown

* Merge pull request #223 from HLasse/HLasse/Listed-metrics-deviate-between-extraction-functions-in-docs

HLasse/Listed-metrics-deviate-between-extraction-functions-in-docs ([`84ce853`](https://github.com/HLasse/TextDescriptives/commit/84ce853fbf498f89da4de3963010022ca45dc23b))

* citation: update citation with JOSS paper ([`d8676ba`](https://github.com/HLasse/TextDescriptives/commit/d8676ba9bb67d8b0b0c071dd2d25383c77cb736d))

* Merge pull request #220 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`207c5fb`](https://github.com/HLasse/TextDescriptives/commit/207c5fb11b86606a4403b7fc9ba067d35d1c6e4d))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/asottile/pyupgrade: v3.3.1 → v3.3.2](https://github.com/asottile/pyupgrade/compare/v3.3.1...v3.3.2)
- [github.com/charliermarsh/ruff-pre-commit: v0.0.261 → v0.0.262](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.261...v0.0.262) ([`156deda`](https://github.com/HLasse/TextDescriptives/commit/156dedae7286631acb69473b29485fd6af66eaa8))


## v2.4.6 (2023-04-24)

### Fix

* fix: bump version ([`b59cdd1`](https://github.com/HLasse/TextDescriptives/commit/b59cdd17379c7c8460accccbb569283a1f2c8717))

### Unknown

* paper: add information theory component and web app ([`b7ecced`](https://github.com/HLasse/TextDescriptives/commit/b7ecced83270315e132bfbcd1b2a92c008e26964))


## v2.4.5 (2023-04-19)

### Documentation

* docs: Added demo to docs ([`6121eeb`](https://github.com/HLasse/TextDescriptives/commit/6121eebc0a125e68979591f6c585d19fae70746b))

### Fix

* fix: dep dist. test ([`a3b54a6`](https://github.com/HLasse/TextDescriptives/commit/a3b54a6b3e3d57acc140b0f9afd72406a88104f8))

* fix: coherence model now handles empty strings as intended ([`abfa507`](https://github.com/HLasse/TextDescriptives/commit/abfa5071ba075f25ff8c170f5cee4f84ef648ea5))

* fix: dep distance test

unsure why this failed. Potentially due to a changed model? ([`2bed2c1`](https://github.com/HLasse/TextDescriptives/commit/2bed2c194b98062aad66d6ca0985fb92af6be977))

### Style

* style: format black ([`78e2915`](https://github.com/HLasse/TextDescriptives/commit/78e2915c4cf6c9e950ac7ab412312517be3a4329))

### Unknown

* Merge pull request #217 from HLasse/fix-213

fixed fail on empty string ([`72ca102`](https://github.com/HLasse/TextDescriptives/commit/72ca10211194ebd37819e7f141a48e1e2c823eae))

* Merge pull request #216 from HLasse/demo_to_readme

docs: Added demo to docs ([`a395e57`](https://github.com/HLasse/TextDescriptives/commit/a395e57da0da9bc4b93c8f481c71c503f975b80c))

* fixed fail on empty string ([`cb55e23`](https://github.com/HLasse/TextDescriptives/commit/cb55e2345165f834ff8238f6a5e9acb02cee6450))

* readme: add app as badge and to news ([`3f747f2`](https://github.com/HLasse/TextDescriptives/commit/3f747f20c9d5359007e6ee852646c44e6c317720))

* Merge pull request #214 from HLasse/pos_stats

Replaces all pos_stats with pos_proportions ([`326f2a7`](https://github.com/HLasse/TextDescriptives/commit/326f2a77b215c50360af34f30aee07f0329aa631))

* Replaces all pos_stats with pos_proportions ([`c682f1c`](https://github.com/HLasse/TextDescriptives/commit/c682f1c8ca4f827d7fc842f3a13d1c2d274bc8de))

* Merge pull request #211 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`a78c863`](https://github.com/HLasse/TextDescriptives/commit/a78c863452a18f44e749d7409cf2460f4cb7be67))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/charliermarsh/ruff-pre-commit: v0.0.260 → v0.0.261](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.260...v0.0.261)
- [github.com/pre-commit/mirrors-mypy: v1.1.1 → v1.2.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.1.1...v1.2.0) ([`fec46a4`](https://github.com/HLasse/TextDescriptives/commit/fec46a42072a68c8012deb26cdea74e3a6ba8069))

* Merge pull request #210 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`8f72dd0`](https://github.com/HLasse/TextDescriptives/commit/8f72dd071377e51e96290b25bdd3bcacc0336a4a))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/psf/black: 23.1.0 → 23.3.0](https://github.com/psf/black/compare/23.1.0...23.3.0)
- [github.com/charliermarsh/ruff-pre-commit: v0.0.257 → v0.0.260](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.257...v0.0.260) ([`2c93dc1`](https://github.com/HLasse/TextDescriptives/commit/2c93dc1e0965b0b88fcab149f06a8a18825ccc54))

* Merge pull request #206 from HLasse/dependabot/pip/ruff-0.0.260

:arrow_up: Bump ruff from 0.0.253 to 0.0.260 ([`8e9f083`](https://github.com/HLasse/TextDescriptives/commit/8e9f083a2c4477760d5d75e4a36b721f4cab06ce))

* :arrow_up: Bump ruff from 0.0.253 to 0.0.260

Bumps [ruff](https://github.com/charliermarsh/ruff) from 0.0.253 to 0.0.260.
- [Release notes](https://github.com/charliermarsh/ruff/releases)
- [Changelog](https://github.com/charliermarsh/ruff/blob/main/BREAKING_CHANGES.md)
- [Commits](https://github.com/charliermarsh/ruff/compare/v0.0.253...v0.0.260)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`3ceda3c`](https://github.com/HLasse/TextDescriptives/commit/3ceda3cac4bf79b8075b6b9ef7ebe8826a67fff7))

* Merge pull request #207 from HLasse/dependabot/pip/black-23.3.0

:arrow_up: Bump black from 22.8.0 to 23.3.0 ([`f371691`](https://github.com/HLasse/TextDescriptives/commit/f3716911490311257d40387f41368affd8a98e10))

* :arrow_up: Bump black from 22.8.0 to 23.3.0

Bumps [black](https://github.com/psf/black) from 22.8.0 to 23.3.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/22.8.0...23.3.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`580de9b`](https://github.com/HLasse/TextDescriptives/commit/580de9b50cf9f3b4fb44bb9f68580e9996f5f14e))

* Merge pull request #208 from HLasse/dependabot/pip/furo-2023.3.27

:arrow_up: Bump furo from 2022.12.7 to 2023.3.27 ([`9948f76`](https://github.com/HLasse/TextDescriptives/commit/9948f76fea23cab0e14741e3ead8cd08b087bba1))

* Merge pull request #205 from HLasse/dependabot/pip/mypy-1.1.1

:arrow_up: Bump mypy from 1.0.1 to 1.1.1 ([`82c890b`](https://github.com/HLasse/TextDescriptives/commit/82c890bff309dae2142f6d0dd094400f33f8eb9b))

* Merge pull request #209 from HLasse/dependabot/pip/pyphen-gte-0.11.0-and-lt-0.15.0

:arrow_up: Update pyphen requirement from &lt;0.12.0,&gt;=0.11.0 to &gt;=0.11.0,&lt;0.15.0 ([`14baf34`](https://github.com/HLasse/TextDescriptives/commit/14baf34a2f2ba511819b5d51f9cc5fdf1c239dbd))

* :arrow_up: Update pyphen requirement

Updates the requirements on [pyphen](https://github.com/Kozea/Pyphen) to permit the latest version.
- [Release notes](https://github.com/Kozea/Pyphen/releases)
- [Changelog](https://github.com/Kozea/Pyphen/blob/master/docs/changelog.rst)
- [Commits](https://github.com/Kozea/Pyphen/compare/0.11.0...0.14.0)

---
updated-dependencies:
- dependency-name: pyphen
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`4f3de06`](https://github.com/HLasse/TextDescriptives/commit/4f3de06744d609f1fa9155dbed828e42d7e33e62))

* :arrow_up: Bump furo from 2022.12.7 to 2023.3.27

Bumps [furo](https://github.com/pradyunsg/furo) from 2022.12.7 to 2023.3.27.
- [Release notes](https://github.com/pradyunsg/furo/releases)
- [Changelog](https://github.com/pradyunsg/furo/blob/main/docs/changelog.md)
- [Commits](https://github.com/pradyunsg/furo/compare/2022.12.07...2023.03.27)

---
updated-dependencies:
- dependency-name: furo
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0fe4607`](https://github.com/HLasse/TextDescriptives/commit/0fe4607c14573a6339e033f975b77c6c4693ee5a))

* :arrow_up: Bump mypy from 1.0.1 to 1.1.1

Bumps [mypy](https://github.com/python/mypy) from 1.0.1 to 1.1.1.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v1.0.1...v1.1.1)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8898530`](https://github.com/HLasse/TextDescriptives/commit/889853097a4fad0e25a1c3c0a2b5eddcc2febb99))


## v2.4.4 (2023-03-28)

### Documentation

* docs: add test requirements to faq ([`1550de7`](https://github.com/HLasse/TextDescriptives/commit/1550de7c4815779f53cc8ba260ddedcdbf8f0358))

### Fix

* fix: add .zenodo.json ([`3cc463c`](https://github.com/HLasse/TextDescriptives/commit/3cc463c5bcc236bb5c49fc51eaba0b419d84ffcc))

### Unknown

* Merge pull request #204 from HLasse/fix-paper-and-zenodo

Fix-paper-and-zenodo ([`0967fc0`](https://github.com/HLasse/TextDescriptives/commit/0967fc0033757d179dac212f6e3fbf5729937f87))

* paper: remove redundant title in paper ([`5613513`](https://github.com/HLasse/TextDescriptives/commit/56135138e5af50c442eec6ad75d736fe3393e569))

* Merge pull request #202 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`4e9cc80`](https://github.com/HLasse/TextDescriptives/commit/4e9cc80b13b2bdcdba92b9fb39d50464879668c7))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/charliermarsh/ruff-pre-commit: v0.0.255 → v0.0.257](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.255...v0.0.257) ([`e43a4f6`](https://github.com/HLasse/TextDescriptives/commit/e43a4f63b6e795b4d17a16fa9e1348236fa4ebe7))

* Merge pull request #200 from HLasse/update-spacy-models-test

Update-spacy-models-test ([`4958acd`](https://github.com/HLasse/TextDescriptives/commit/4958acdf55d5271327ade3a2d9564ab82288de1f))

* tests: update spacy model in tests ([`105b48b`](https://github.com/HLasse/TextDescriptives/commit/105b48b602559bcf6a5dcde49b50f4823c26b75f))

* Merge pull request #198 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`16de25e`](https://github.com/HLasse/TextDescriptives/commit/16de25e9a317fdb82abcfbe40e509f3d3e3d2b08))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/codespell-project/codespell: v2.2.2 → v2.2.4](https://github.com/codespell-project/codespell/compare/v2.2.2...v2.2.4)
- [github.com/charliermarsh/ruff-pre-commit: v0.0.254 → v0.0.255](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.254...v0.0.255)
- [github.com/pre-commit/mirrors-mypy: v1.0.1 → v1.1.1](https://github.com/pre-commit/mirrors-mypy/compare/v1.0.1...v1.1.1) ([`fc620bb`](https://github.com/HLasse/TextDescriptives/commit/fc620bbde9d42e86bd2c6741d797479504fb92ec))

* Merge pull request #197 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`da5a9bf`](https://github.com/HLasse/TextDescriptives/commit/da5a9bf43fcaf7bbc1e80b7c7dc3dce0bf0b8105))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/charliermarsh/ruff-pre-commit: v0.0.253 → v0.0.254](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.253...v0.0.254) ([`74dfb9f`](https://github.com/HLasse/TextDescriptives/commit/74dfb9f0cacb750ffd05052c98b1625a227ddd58))

* readme: add how to download spacy pipeline ([`e9138b0`](https://github.com/HLasse/TextDescriptives/commit/e9138b026b9d200ac4e3f3b1a4d8d1765f828599))

* Merge pull request #188 from HLasse/dependabot/pip/datasets-gte-2.8.0-and-lt-2.11.0

:arrow_up: Update datasets requirement from &lt;2.9.0,&gt;=2.8.0 to &gt;=2.8.0,&lt;2.11.0 ([`c353c71`](https://github.com/HLasse/TextDescriptives/commit/c353c711a65a785034b2094e93a7b1080e93dc98))

* :arrow_up: Update datasets requirement

Updates the requirements on [datasets](https://github.com/huggingface/datasets) to permit the latest version.
- [Release notes](https://github.com/huggingface/datasets/releases)
- [Commits](https://github.com/huggingface/datasets/compare/2.8.0...2.10.1)

---
updated-dependencies:
- dependency-name: datasets
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b4baed8`](https://github.com/HLasse/TextDescriptives/commit/b4baed8c9a5e9857f7745cd54830f33e740a4da5))

* Merge pull request #195 from sdruskat/patch-1

Fix CITATION.cff file name and invalid DOI value ([`9dad636`](https://github.com/HLasse/TextDescriptives/commit/9dad636ac2eabe660b99fe9ac8d43834f062b3e0))

* citation: add Ludvig to author list ([`ae96a16`](https://github.com/HLasse/TextDescriptives/commit/ae96a16e159d15baee3500ad3742ff80f9f42185))

* Merge pull request #191 from HLasse/dependabot/pip/sphinxext-opengraph-gte-0.7.3-and-lt-0.8.2

:arrow_up: Update sphinxext-opengraph requirement from &lt;0.8.1,&gt;=0.7.3 to &gt;=0.7.3,&lt;0.8.2 ([`257efac`](https://github.com/HLasse/TextDescriptives/commit/257efac559d5dd98b5eb5ee7bc82f01a1b74a14f))

* :arrow_up: Update sphinxext-opengraph requirement

Updates the requirements on [sphinxext-opengraph](https://github.com/wpilibsuite/sphinxext-opengraph) to permit the latest version.
- [Release notes](https://github.com/wpilibsuite/sphinxext-opengraph/releases)
- [Commits](https://github.com/wpilibsuite/sphinxext-opengraph/compare/v0.7.3...v0.8.1)

---
updated-dependencies:
- dependency-name: sphinxext-opengraph
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`e3b0392`](https://github.com/HLasse/TextDescriptives/commit/e3b039297753c1c77e90a24e4f987be4aa573467))

* Merge pull request #189 from HLasse/dependabot/pip/pre-commit-3.1.1

:arrow_up: Bump pre-commit from 3.0.4 to 3.1.1 ([`0893422`](https://github.com/HLasse/TextDescriptives/commit/0893422cff5e1d52ccaf3304b5a1a3965090e85b))

* :arrow_up: Bump pre-commit from 3.0.4 to 3.1.1

Bumps [pre-commit](https://github.com/pre-commit/pre-commit) from 3.0.4 to 3.1.1.
- [Release notes](https://github.com/pre-commit/pre-commit/releases)
- [Changelog](https://github.com/pre-commit/pre-commit/blob/main/CHANGELOG.md)
- [Commits](https://github.com/pre-commit/pre-commit/compare/v3.0.4...v3.1.1)

---
updated-dependencies:
- dependency-name: pre-commit
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`949f007`](https://github.com/HLasse/TextDescriptives/commit/949f00729feba626fec61a4059584be1b8fb1eb3))

* Merge pull request #190 from HLasse/dependabot/pip/ruff-0.0.253

:arrow_up: Bump ruff from 0.0.239 to 0.0.253 ([`fecf5db`](https://github.com/HLasse/TextDescriptives/commit/fecf5db89a7e2c947a76f665b1f5f0a3ff6675b3))

* Fix CITATION.cff file name and invalid DOI value

- Change the file name to adhere to the CFF format definition: https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md#general-structure-of-a-citationcff-file
- Fix the DOI value to be the DOI, not the resolver URL: https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md#definitionsdoi ([`187384a`](https://github.com/HLasse/TextDescriptives/commit/187384a223533f54337552f36ae8cddcb0001a53))

* :arrow_up: Bump ruff from 0.0.239 to 0.0.253

Bumps [ruff](https://github.com/charliermarsh/ruff) from 0.0.239 to 0.0.253.
- [Release notes](https://github.com/charliermarsh/ruff/releases)
- [Changelog](https://github.com/charliermarsh/ruff/blob/main/BREAKING_CHANGES.md)
- [Commits](https://github.com/charliermarsh/ruff/compare/v0.0.239...v0.0.253)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`199dba4`](https://github.com/HLasse/TextDescriptives/commit/199dba4791ea3e980f869f8ba3840233dd4cf22b))

* Merge pull request #192 from HLasse/dependabot/pip/mypy-1.0.1

:arrow_up: Bump mypy from 0.991 to 1.0.1 ([`5e7cc0c`](https://github.com/HLasse/TextDescriptives/commit/5e7cc0c5e310a70335d4804abe2f09c77a694dad))

* :arrow_up: Bump mypy from 0.991 to 1.0.1

Bumps [mypy](https://github.com/python/mypy) from 0.991 to 1.0.1.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.991...v1.0.1)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`3c9f628`](https://github.com/HLasse/TextDescriptives/commit/3c9f6288e1815cbd2a51148ca3ee31a41fd60fd9))


## v2.4.3 (2023-03-01)

### Chore

* chore: pre-commit ([`c33ddaa`](https://github.com/HLasse/TextDescriptives/commit/c33ddaa99280ae97836ec5a030b7e6f3dc3393bd))

* chore: ci ([`250435f`](https://github.com/HLasse/TextDescriptives/commit/250435fe0c6d88d63b06aab227c5af184b61ae23))

### Ci

* ci: add codespell to pre-commit ([`326cccd`](https://github.com/HLasse/TextDescriptives/commit/326cccd5fb4b85fbe7304c440d108355cd9cf3c9))

### Documentation

* docs: change quick start model to lg ([`653fb49`](https://github.com/HLasse/TextDescriptives/commit/653fb49f887941cf6b4afb7566952f836ae0359b))

* docs: update readme to use lg model for proper coherence calculation ([`cdd85b7`](https://github.com/HLasse/TextDescriptives/commit/cdd85b7b9de08a94ad43aab14d42293acaf3b910))

### Fix

* fix: add descriptive_stats pipe no matter the verbosity ([`3fd3240`](https://github.com/HLasse/TextDescriptives/commit/3fd3240bb5f706da6b882af8129945781021bb80))

* fix: change default verbosity of readability component ([`ddfd269`](https://github.com/HLasse/TextDescriptives/commit/ddfd269ae2c0d784b7e06bab0af74cbce293a288))

* fix: change verbosity of `lexeme_prob_table` ([`b64631f`](https://github.com/HLasse/TextDescriptives/commit/b64631fee040f08ec50b65ecd0c3a13ffe3d0dde))

* fix: automatically download supplied spacy model if not on disk ([`f54a9b6`](https://github.com/HLasse/TextDescriptives/commit/f54a9b61a018c0a77d72be986a2bc22f27a84c44))

### Unknown

* Merge pull request #194 from HLasse/download-spacy-model-if-not-on-disk

Download-spacy-model-if-not-on-disk ([`8870acd`](https://github.com/HLasse/TextDescriptives/commit/8870acd0e50618830dda290a0f068436ca1f6799))

* Merge branch &#39;main&#39; into download-spacy-model-if-not-on-disk ([`60f2adb`](https://github.com/HLasse/TextDescriptives/commit/60f2adb3e42a2512523a6e5ce2bcb5539d3d6341))

* Merge pull request #193 from HLasse/codespell-pre-commit

ci: add codespell to pre-commit ([`f69fac1`](https://github.com/HLasse/TextDescriptives/commit/f69fac15cc901ea47a7713fb2a1556d8a832bdf1))

* Merge branch &#39;main&#39; into codespell-pre-commit ([`feb8464`](https://github.com/HLasse/TextDescriptives/commit/feb84647880069b92fab3bdf57ff270083cf008c))

* Merge pull request #187 from HLasse/paper-add-ludvig

Paper-add-ludvig ([`f2d032c`](https://github.com/HLasse/TextDescriptives/commit/f2d032cf624b8ee7ae677c324884e8ae24c481bd))

* Merge branch &#39;main&#39; into paper-add-ludvig ([`0f42762`](https://github.com/HLasse/TextDescriptives/commit/0f427623677c13f45c658096721db9f298056d0b))


## v2.4.2 (2023-03-01)

### Chore

* chore: ci ([`7873f88`](https://github.com/HLasse/TextDescriptives/commit/7873f8856a95f478967097073d125d1206c05357))

* chore: pre-commit limbo ([`d2e8436`](https://github.com/HLasse/TextDescriptives/commit/d2e84360ad39114ddc2707b34d06e63c775fa608))

* chore: pre-commit ([`2e4d069`](https://github.com/HLasse/TextDescriptives/commit/2e4d0699c03245155d56d0bd09c3341f2ce542a1))

* chore: pre-commit ([`05209b6`](https://github.com/HLasse/TextDescriptives/commit/05209b6f1b3f937dde691550b8cfc39f2a45e01d))

### Ci

* ci: remove docformatter due to black incompatibility ([`5ad185d`](https://github.com/HLasse/TextDescriptives/commit/5ad185daef7fb9c9d62b31fce2943014e2fde1b2))

* ci: make docformatter and black compatible ([`4f37b6b`](https://github.com/HLasse/TextDescriptives/commit/4f37b6b14317e50cf32ff97ef544414d9c537122))

### Fix

* fix: Handle case where extension is set, but pipeline is not ([`2ba2dd2`](https://github.com/HLasse/TextDescriptives/commit/2ba2dd210f612974f5279ad8302ee254d5c611b3))

* fix: `extract_metrics` failing if `metrics=None` ([`6bfe6b0`](https://github.com/HLasse/TextDescriptives/commit/6bfe6b0ed74a7e490587878ea06ac2b9f3a9900a))

### Unknown

* Merge pull request #186 from HLasse/fix-extract-metrics-all-metrics

Fix-extract-metrics-all-metrics ([`e730af6`](https://github.com/HLasse/TextDescriptives/commit/e730af67b724c1398d65fd43943fc9c6eb193aca))

* paper: remove Ludvig from acknowledgements ([`56f5ff4`](https://github.com/HLasse/TextDescriptives/commit/56f5ff4ea857c9e2d7669e3eaa7fd67d34841d81))

* paper: add Ludvig as coauthor ([`c29849c`](https://github.com/HLasse/TextDescriptives/commit/c29849c9638fc046c13b493010508e8166a0b8c1))

* Merge branch &#39;main&#39; into fix-extract-metrics-all-metrics ([`7c48924`](https://github.com/HLasse/TextDescriptives/commit/7c48924e93c27f0067c5674a9bb9e6609ed9a021))

* Merge pull request #185 from HLasse/add-contributor-guidelines

Add contributor guidelines ([`f672f9b`](https://github.com/HLasse/TextDescriptives/commit/f672f9bbe30a2901569ea3c691e14ad667619ce8))

* tests: add test for `extract_metric` with `metrics=None` ([`680b52f`](https://github.com/HLasse/TextDescriptives/commit/680b52f7d910645cdbbf2e8f6523c08a7c68085c))

* Create CONTRIBUTING.md ([`a0d1640`](https://github.com/HLasse/TextDescriptives/commit/a0d1640fd9c2cec3a533a2dc093e853af6cec4d3))

* Create CODE_OF_CONDUCT.md ([`254f4e2`](https://github.com/HLasse/TextDescriptives/commit/254f4e290687f19e1a6af5cda38d9e0c8ddb00d7))

* Merge pull request #183 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`a288a54`](https://github.com/HLasse/TextDescriptives/commit/a288a54e4faf79c22c7f0c583d610792904f7442))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/charliermarsh/ruff-pre-commit: v0.0.249 → v0.0.253](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.249...v0.0.253) ([`f475611`](https://github.com/HLasse/TextDescriptives/commit/f475611f0f160c41b475377ed0ac7cd7ba379ef3))

* Merge pull request #182 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`9b235e6`](https://github.com/HLasse/TextDescriptives/commit/9b235e6ab446d117efea4801da93d283cfba3d66))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/charliermarsh/ruff-pre-commit: v0.0.246 → v0.0.249](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.246...v0.0.249)
- [github.com/pre-commit/mirrors-mypy: v1.0.0 → v1.0.1](https://github.com/pre-commit/mirrors-mypy/compare/v1.0.0...v1.0.1) ([`0ca1821`](https://github.com/HLasse/TextDescriptives/commit/0ca182132bd1ab1f0046705e1191b302d8149ca6))

* Merge pull request #181 from HLasse/paper--update-speaking-your-mind-reference

paper: update speaking your mind reference to preprint ([`58032e8`](https://github.com/HLasse/TextDescriptives/commit/58032e8c672c81653e590f7e5d474f5aa41e9d0d))

* paper: update speaking your mind reference to preprint ([`8c7d43d`](https://github.com/HLasse/TextDescriptives/commit/8c7d43d5e46c2fa41331ca08e59de574fdefcb8f))

* Merge pull request #180 from HLasse/paper--add-missing-doi

paper: add missing doi ([`c89c9b3`](https://github.com/HLasse/TextDescriptives/commit/c89c9b31034e0f776a0552bdb02b13c5d61c0f9c))

* paper: add missing doi ([`ec22526`](https://github.com/HLasse/TextDescriptives/commit/ec22526566de3dd314d71dc7c877940b721ddc5b))

* Merge pull request #170 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`5c4ae75`](https://github.com/HLasse/TextDescriptives/commit/5c4ae75caaa3dd4f05cec6eebd7afb8466282115))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/PyCQA/docformatter: v1.5.1 → v1.6.0.rc1](https://github.com/PyCQA/docformatter/compare/v1.5.1...v1.6.0.rc1)
- [github.com/psf/black: 22.12.0 → 23.1.0](https://github.com/psf/black/compare/22.12.0...23.1.0)
- [github.com/charliermarsh/ruff-pre-commit: v0.0.223 → v0.0.246](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.223...v0.0.246)
- [github.com/pre-commit/mirrors-mypy: v0.991 → v1.0.0](https://github.com/pre-commit/mirrors-mypy/compare/v0.991...v1.0.0) ([`f30a6c2`](https://github.com/HLasse/TextDescriptives/commit/f30a6c22d6365d99c9d31705d6c50c7576993796))

* Merge pull request #178 from HLasse/dependabot/pip/sphinxext-opengraph-gte-0.7.3-and-lt-0.8.1

:arrow_up: Update sphinxext-opengraph requirement from &lt;0.7.4,&gt;=0.7.3 to &gt;=0.7.3,&lt;0.8.1 ([`c0254b5`](https://github.com/HLasse/TextDescriptives/commit/c0254b55f5191722bd23ef7b6ecf301686aa5468))


## v2.4.1 (2023-02-08)

### Ci

* ci: Fix semantic release ([`ad4069b`](https://github.com/HLasse/TextDescriptives/commit/ad4069b27ed4793fbbcbe3a67379fb4fe83f4a2f))

* ci: remove pytest coverage badge ([`a9c98cc`](https://github.com/HLasse/TextDescriptives/commit/a9c98cc34104586c9fa60d8be01e51a0704175bc))

* ci: approve before merge dependabot ([`4d2461f`](https://github.com/HLasse/TextDescriptives/commit/4d2461f7f6235269ce559abc8be0392520a7391b))

### Fix

* fix: change auto-approve event 

Following https://github.com/hmarr/auto-approve-action ([`729836f`](https://github.com/HLasse/TextDescriptives/commit/729836feb76a12507a6a0f703b434ec071124f5f))

### Unknown

* Merge pull request #179 from HLasse/ci-fix-semantic-release

ci: Fix semantic release ([`fa138e9`](https://github.com/HLasse/TextDescriptives/commit/fa138e9356d8780969ca04301c5da93f2bb03d1d))

* :arrow_up: Update sphinxext-opengraph requirement

Updates the requirements on [sphinxext-opengraph](https://github.com/wpilibsuite/sphinxext-opengraph) to permit the latest version.
- [Release notes](https://github.com/wpilibsuite/sphinxext-opengraph/releases)
- [Commits](https://github.com/wpilibsuite/sphinxext-opengraph/compare/v0.7.3...V0.8.0)

---
updated-dependencies:
- dependency-name: sphinxext-opengraph
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0221c1c`](https://github.com/HLasse/TextDescriptives/commit/0221c1cb75e4b24a9fc34714b1136640903ac668))

* Merge pull request #171 from HLasse/dependabot/pip/sphinx-gte-5.3.0-and-lt-6.2.0

:arrow_up: Update sphinx requirement from &lt;5.4.0,&gt;=5.3.0 to &gt;=5.3.0,&lt;6.2.0 ([`4e7e7bf`](https://github.com/HLasse/TextDescriptives/commit/4e7e7bfaaf5a5f40ed74ae942e8a2729a159741f))

* Merge pull request #174 from HLasse/dependabot/pip/spacy-lookups--gte-3.1.0-and-lt-3.6.0

:arrow_up: Update spacy[lookups] requirement from &lt;3.5.0,&gt;=3.1.0 to &gt;=3.1.0,&lt;3.6.0 ([`447f2b3`](https://github.com/HLasse/TextDescriptives/commit/447f2b316d60de8492f6c921c40140847fb0c857))

* :arrow_up: Update sphinx requirement

Updates the requirements on [sphinx](https://github.com/sphinx-doc/sphinx) to permit the latest version.
- [Release notes](https://github.com/sphinx-doc/sphinx/releases)
- [Changelog](https://github.com/sphinx-doc/sphinx/blob/master/CHANGES)
- [Commits](https://github.com/sphinx-doc/sphinx/compare/v5.3.0...v6.1.3)

---
updated-dependencies:
- dependency-name: sphinx
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`27652cd`](https://github.com/HLasse/TextDescriptives/commit/27652cd7469aa9ef425818dacf6fd0f365850325))

* :arrow_up: Update spacy[lookups] requirement

Updates the requirements on [spacy[lookups]](https://github.com/explosion/spaCy) to permit the latest version.
- [Release notes](https://github.com/explosion/spaCy/releases)
- [Commits](https://github.com/explosion/spaCy/compare/v3.1.0...v3.5.0)

---
updated-dependencies:
- dependency-name: spacy[lookups]
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`da2aa29`](https://github.com/HLasse/TextDescriptives/commit/da2aa29115b692568c08d8884d032089955fac1d))

* Merge pull request #177 from HLasse/dependabot/pip/pre-commit-3.0.4

:arrow_up: Bump pre-commit from 2.20.0 to 3.0.4 ([`34ffd33`](https://github.com/HLasse/TextDescriptives/commit/34ffd33ac633f0b3adb8120d7b64cbcfed326d1a))

* :arrow_up: Bump pre-commit from 2.20.0 to 3.0.4

Bumps [pre-commit](https://github.com/pre-commit/pre-commit) from 2.20.0 to 3.0.4.
- [Release notes](https://github.com/pre-commit/pre-commit/releases)
- [Changelog](https://github.com/pre-commit/pre-commit/blob/main/CHANGELOG.md)
- [Commits](https://github.com/pre-commit/pre-commit/compare/v2.20.0...v3.0.4)

---
updated-dependencies:
- dependency-name: pre-commit
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8e29052`](https://github.com/HLasse/TextDescriptives/commit/8e290528e0c2a2847f0e40c53343798af4bca034))

* Merge pull request #173 from HLasse/dependabot/pip/ruff-0.0.239

:arrow_up: Bump ruff from 0.0.191 to 0.0.239 ([`dea2d14`](https://github.com/HLasse/TextDescriptives/commit/dea2d146263c3a8cf62e246d049563e235251f69))

* Merge branch &#39;main&#39; into dependabot/pip/ruff-0.0.239 ([`4c647a0`](https://github.com/HLasse/TextDescriptives/commit/4c647a018a3eba7f9c8f602681b92da699ef7acd))

* Update dependabot_automerge.yml ([`135a73e`](https://github.com/HLasse/TextDescriptives/commit/135a73eb951f21e473c0e7376175cd15d5d77868))

* :arrow_up: Bump ruff from 0.0.191 to 0.0.239

Bumps [ruff](https://github.com/charliermarsh/ruff) from 0.0.191 to 0.0.239.
- [Release notes](https://github.com/charliermarsh/ruff/releases)
- [Changelog](https://github.com/charliermarsh/ruff/blob/main/BREAKING_CHANGES.md)
- [Commits](https://github.com/charliermarsh/ruff/compare/v0.0.191...v0.0.239)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7d5de24`](https://github.com/HLasse/TextDescriptives/commit/7d5de2424b060c3ae77b2dcca412b624991acba2))


## v2.4.0 (2023-01-31)

### Documentation

* docs: update quality docs with oov_ratio ([`74c22b1`](https://github.com/HLasse/TextDescriptives/commit/74c22b143fae43227feea28f74f19eff439a3240))

### Unknown

* Merge pull request #164 from HLasse/HLasse/Add-proportion-of-word-in-vocabuary

feat: add out of vocabulary ratio to quality component ([`835053d`](https://github.com/HLasse/TextDescriptives/commit/835053d2019143c46668b04d53b88c0e30a43605))

* Merge branch &#39;main&#39; into HLasse/Add-proportion-of-word-in-vocabuary ([`531cbd4`](https://github.com/HLasse/TextDescriptives/commit/531cbd4f7c7c29067d234285953fc974fa2590b3))

* tests: parameterize oov ratio further ([`7338488`](https://github.com/HLasse/TextDescriptives/commit/7338488731bf6cd9ede0b33df8b0a86c49ccbc20))


## v2.3.0 (2023-01-23)

### Build

* build: Add lookups to requirements ([`bd97890`](https://github.com/HLasse/TextDescriptives/commit/bd97890c160fc514efea9bb962e3931b08b6372b))

* build: remove test coverage badge ([`07f363f`](https://github.com/HLasse/TextDescriptives/commit/07f363f82b7abaef3c61f4213692d948e343aa04))

### Chore

* chore: precommit ([`2628ec6`](https://github.com/HLasse/TextDescriptives/commit/2628ec6f7694198d1c5f0128dd4d95cf92d1a499))

* chore: update after review ([`2559c97`](https://github.com/HLasse/TextDescriptives/commit/2559c97a8c90bcdce4b2eacf029b8e095fe48ba1))

* chore: fix type ([`ea05cf3`](https://github.com/HLasse/TextDescriptives/commit/ea05cf3d9e511bd1e1404be568557a32f6d83062))

* chore: precommit ([`a87a5ea`](https://github.com/HLasse/TextDescriptives/commit/a87a5eacfa1895caa5de5c9c775b5012df1f1267))

* chore: fixes after review ([`c3dea6c`](https://github.com/HLasse/TextDescriptives/commit/c3dea6c213890a17967a164286b76758a5956fdf))

### Documentation

* docs: Added information metrics to docs ([`15bb255`](https://github.com/HLasse/TextDescriptives/commit/15bb255828ac7c15dc834b5976e7047126533541))

* docs: Added update timer and fail on timeout ([`0d39b2e`](https://github.com/HLasse/TextDescriptives/commit/0d39b2ef3cabeb93c93d925e3af53b9e5ee9365f))

* docs: fixed tutorial to not download model ([`42589f6`](https://github.com/HLasse/TextDescriptives/commit/42589f6f453ea9e1d5be7e9cbe868e9baade32a4))

### Feature

* feat: Added information theoretic features ([`076c638`](https://github.com/HLasse/TextDescriptives/commit/076c638d3fa8109a2de924d686959c456f548c96))

* feat: add out of vocabulary ratio to quality component ([`a1177e5`](https://github.com/HLasse/TextDescriptives/commit/a1177e597de75f31507895540d2e6243dccafe27))

### Fix

* fix: Fix error caused by running all tests at once ([`5e46202`](https://github.com/HLasse/TextDescriptives/commit/5e46202f9bc939c07c55405487fb81f6d713546a))

### Unknown

* Merge pull request #166 from HLasse/entrophy

feat: Added information theoretic features ([`463b7c7`](https://github.com/HLasse/TextDescriptives/commit/463b7c72f870f5ad90e144278a1833a66bbf2681))

* Merge branch &#39;entrophy&#39; of https://github.com/hlasse/TextDescriptives into entrophy ([`56885e5`](https://github.com/HLasse/TextDescriptives/commit/56885e52aa626270a81d32376c60a1059af8651c))

* tests: fix spacy model req for tests ([`9c06711`](https://github.com/HLasse/TextDescriptives/commit/9c0671178f8fbdd187e909a09916591edd0e200a))

* Apply suggestions from code review

Co-authored-by: Lasse Hansen &lt;lasseh0310@gmail.com&gt; ([`c709f9d`](https://github.com/HLasse/TextDescriptives/commit/c709f9d536a09deda27675831a6cf06b8042d88e))

* tests: add spacy medium to test requirements ([`8eb070e`](https://github.com/HLasse/TextDescriptives/commit/8eb070e3887a69eb20198af464ba0b52609be751))

* Merge pull request #161 from HLasse/docs-fix-rendering

docs: Added update timer and fail on timeout ([`48ccef8`](https://github.com/HLasse/TextDescriptives/commit/48ccef8377aeae39a595316f2c3431da5b5e519c))

* Merge branch &#39;main&#39; into docs-fix-rendering ([`8f50f61`](https://github.com/HLasse/TextDescriptives/commit/8f50f6132e98b84370cd35440550debbc7fc6add))

* Update requirements.txt ([`e88ed64`](https://github.com/HLasse/TextDescriptives/commit/e88ed641c82a56fa41c73df9b6f383843b0d159f))

* Merge pull request #160 from HLasse/docs-fix-rendering

doc: fix rendering of introductory tutorail ([`3831a61`](https://github.com/HLasse/TextDescriptives/commit/3831a618c701f4a150bc6b2081f8f5cb1dad3b79))

* Merge branch &#39;main&#39; of https://github.com/hlasse/TextDescriptives into tutorial_quality ([`f1075c6`](https://github.com/HLasse/TextDescriptives/commit/f1075c62477c27b8153f42474bcd4741cf167fd9))

* Merge pull request #159 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`a849727`](https://github.com/HLasse/TextDescriptives/commit/a849727d380d1b6fc82d64578eada89194e92c7f))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/charliermarsh/ruff-pre-commit: v0.0.216 → v0.0.223](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.216...v0.0.223) ([`332ba8f`](https://github.com/HLasse/TextDescriptives/commit/332ba8f49cdff3b2599491465f6800903cfe04f8))

* Merge pull request #156 from HLasse/ci-remove-test-coverage-badge

build: remove test coverage badge ([`62ea5b2`](https://github.com/HLasse/TextDescriptives/commit/62ea5b2803666b629e8b9d83791257d55e660c1e))

* readme: remove test coverage badge ([`341796d`](https://github.com/HLasse/TextDescriptives/commit/341796d7ca82d80659cfeb5e87a8608885a31d55))


## v2.2.0 (2023-01-16)

### Build

* build: update numpy requirement ([`28f524f`](https://github.com/HLasse/TextDescriptives/commit/28f524fba1613315049b2530418354470f12a248))

### Ci

* ci: add token to cov comment ([`37ffa93`](https://github.com/HLasse/TextDescriptives/commit/37ffa93d78247b63a7eadfb87a8424749f3056ad))

### Documentation

* docs: removed multiprocessing from pipes ([`c224580`](https://github.com/HLasse/TextDescriptives/commit/c22458097d7ca97679da748e63be6ad1523c9a41))

* docs: changed print of quality ([`deb148b`](https://github.com/HLasse/TextDescriptives/commit/deb148bcbe9014c5285fe5a062320f7541b1c1d5))

* docs: fixed multiprocessing in tutorial ([`4ddebdf`](https://github.com/HLasse/TextDescriptives/commit/4ddebdf3be5124b92cb4bafe5b69fe1632143aa6))

* docs: Updated docs with changes to the API ([`580bea1`](https://github.com/HLasse/TextDescriptives/commit/580bea199e91cb95e1876a0e4b7ea0ca5439129d))

* docs: updated tutorial ([`57d0054`](https://github.com/HLasse/TextDescriptives/commit/57d00543c1ce0525fee6570b8bb843bc62295bf7))

* docs: added quality tutorial to docs ([`2017fb3`](https://github.com/HLasse/TextDescriptives/commit/2017fb351c9b2157bb59525322f509e8367792a6))

* docs: added tutorial ([`fa2d65c`](https://github.com/HLasse/TextDescriptives/commit/fa2d65c1114cd6ae03d4638a44e7fe0c525aa80f))

* docs: Added new tutorial for quality filtering ([`3697e59`](https://github.com/HLasse/TextDescriptives/commit/3697e596cc397c6b22be04f9841f2d55b4721903))

* docs: fix typo in coherence.rst

seperate -&gt; separate ([`be83cf3`](https://github.com/HLasse/TextDescriptives/commit/be83cf354039179ef4d7d25ce4d99e237fc644be))

### Feature

* feat: Added QualityOutput ([`c0fb63c`](https://github.com/HLasse/TextDescriptives/commit/c0fb63c671ed1e4ccbe75afa4fb3301104a1ad0e))

* feat: Updated way that that quality thresholds is set ([`f799186`](https://github.com/HLasse/TextDescriptives/commit/f7991864ba62a4dc0a36f42f2a13ad3079909a02))

### Unknown

* Merge pull request #153 from HLasse/tutorial_quality

Added quality tutorial ([`21499a6`](https://github.com/HLasse/TextDescriptives/commit/21499a64899ebfde8d22d924aa2e69ea33b10457))

* tutorial: minor descriptions in tutorial ([`e89a80c`](https://github.com/HLasse/TextDescriptives/commit/e89a80cbfcb548778f99e0843bea0d6d1e8e7fa5))

* Update README.md ([`246365c`](https://github.com/HLasse/TextDescriptives/commit/246365c01112036a36e8cb6b0f39a270ebc175be))

* Merge branch &#39;tutorial_quality&#39; of https://github.com/hlasse/TextDescriptives into tutorial_quality ([`d8edb46`](https://github.com/HLasse/TextDescriptives/commit/d8edb46202210c489ea093c359e70af99873e6f8))

* Fixed number of cores when filtering ([`18392c5`](https://github.com/HLasse/TextDescriptives/commit/18392c589a1d81c2e97220267b72ceb507444e36))

* Merge pull request #154 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`798b1ee`](https://github.com/HLasse/TextDescriptives/commit/798b1eed558fc7e20d0162b6156c7f49e4eaaa72))

* tutorial: minor ([`c5e9eff`](https://github.com/HLasse/TextDescriptives/commit/c5e9eff8cbe82b31e21d37dab8c1be8c7f16abf2))

* Merge branch &#39;main&#39; of https://github.com/hlasse/TextDescriptives into tutorial_quality ([`c339782`](https://github.com/HLasse/TextDescriptives/commit/c33978271f7a299b807d807272c3dfbe6986dfcc))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/charliermarsh/ruff-pre-commit: v0.0.206 → v0.0.216](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.206...v0.0.216) ([`d939822`](https://github.com/HLasse/TextDescriptives/commit/d939822ddefe28331d11d6d423378f42be03c4ab))

* tutorial: minor updates to quality tutorial ([`9f5d22f`](https://github.com/HLasse/TextDescriptives/commit/9f5d22f459fc55b35ce61942b8511dbd9c222a37))

* Merge pull request #140 from HLasse/ci-dependabot-auto

CI Update automerge for dependabot and pre-commit-ci ([`ab86f7d`](https://github.com/HLasse/TextDescriptives/commit/ab86f7d484318f16a7879bcaec72cc504067f8f2))

* Update .github/workflows/dependabot_automerge.yml ([`3c92cbc`](https://github.com/HLasse/TextDescriptives/commit/3c92cbc4ac67b18fae64da9ac9a80560f9f2b869))

* Update .github/workflows/dependabot_automerge.yml ([`35e5caf`](https://github.com/HLasse/TextDescriptives/commit/35e5caf693656f2980ec9c5bec352356f871a836))

* Merge pull request #149 from eltociear/patch-1

docs: fix typo in coherence.rst ([`3a1742b`](https://github.com/HLasse/TextDescriptives/commit/3a1742b965ed4692dd31a658d8d05d01c1fe6070))

* Merge pull request #150 from HLasse/ci-cov-comment

ci: add token to cov comment ([`59eea75`](https://github.com/HLasse/TextDescriptives/commit/59eea756a946a6246dc156327cec66ec95dffc57))

* Merge branch &#39;main&#39; of https://github.com/hlasse/TextDescriptives into tutorial_quality ([`4215bc1`](https://github.com/HLasse/TextDescriptives/commit/4215bc1fdcb228374c5a8eef5737891766782519))

* Merge pull request #148 from HLasse/HLasse-patch-1

build: update numpy requirement ([`6a6bc03`](https://github.com/HLasse/TextDescriptives/commit/6a6bc03a9393ae31c26ff7d763ce50de0fda856f))

* Update README.md ([`2201416`](https://github.com/HLasse/TextDescriptives/commit/2201416cf07b3d5315fe6cca84919fe18b821b97))

* Merge pull request #139 from HLasse/ci-add-stale

Update CI ([`91d3002`](https://github.com/HLasse/TextDescriptives/commit/91d3002aa43b40a5f817a916acc015d43eb7b1a8))


## v2.1.0 (2023-01-06)

### Chore

* chore: pre-commit ([`29b4b2a`](https://github.com/HLasse/TextDescriptives/commit/29b4b2a1a3ee7e31491186abc6f98febec324f19))

* chore: update assigns for `all` component ([`c5fdbcf`](https://github.com/HLasse/TextDescriptives/commit/c5fdbcf28d834cfd4639ceb17fb3c458cb9912c3))

* chore: moving and renaming utils for extract_metrics ([`b3cdc26`](https://github.com/HLasse/TextDescriptives/commit/b3cdc26b04a9253ca9a74eec1b377e840ed37d30))

* chore: ssort ([`91acab4`](https://github.com/HLasse/TextDescriptives/commit/91acab47ef3e2a70720a9f7da21bdede8ad6bfa0))

### Ci

* ci: run converted notebooks with ipython to supper !pip install ([`a26bb83`](https://github.com/HLasse/TextDescriptives/commit/a26bb8339c2b54b3efb9e7bfcb1da4a3d8934e3f))

* ci: update automerge for dependabot ([`bc1de64`](https://github.com/HLasse/TextDescriptives/commit/bc1de649460733fe3036dd15953491bf214ecf10))

* ci: remove autoupdate on ci ([`55f2b35`](https://github.com/HLasse/TextDescriptives/commit/55f2b35fa76b32b9dab4474a15eb081350f214c5))

* ci: update stalebot ([`01c77a3`](https://github.com/HLasse/TextDescriptives/commit/01c77a33b19353f0bc5f51605ee1704d3502250b))

### Documentation

* docs: add arxiv badge to readme ([`7b57aea`](https://github.com/HLasse/TextDescriptives/commit/7b57aeac655d56b21eac96e6a17c9a6c9c16831a))

* docs: update readme after review and add citation in docs ([`728a0d4`](https://github.com/HLasse/TextDescriptives/commit/728a0d40ab48d5626d733e800fd2208dab97d3f8))

* docs: add arxiv citation ([`bfab60b`](https://github.com/HLasse/TextDescriptives/commit/bfab60b89e57b101fd4efbb72fefe9a8ca4e7b6d))

* docs: add `extract_metrics` to docs and readme ([`163bee5`](https://github.com/HLasse/TextDescriptives/commit/163bee57ff5e26718594069564ff0ac8a0e63c47))

* docs: minor mismention ([`f5155c2`](https://github.com/HLasse/TextDescriptives/commit/f5155c28b5ccced6a334feb1b25f7ae3d4d91854))

* docs: download spacy model in tutorial ([`96634cb`](https://github.com/HLasse/TextDescriptives/commit/96634cb62008ac18132513e4babbaa04350b1bc0))

* docs: reset changelog ([`12007b7`](https://github.com/HLasse/TextDescriptives/commit/12007b7d6f72223edd699cfc310ab035830c4ce6))

### Feature

* feat: wrapper function
Fixes #135 ([`fb33e19`](https://github.com/HLasse/TextDescriptives/commit/fb33e19e09b2551a049dccf42722d67f5c17199a))

### Fix

* fix: remove previously assigned extensions before extracting new metrics ([`1a7ca00`](https://github.com/HLasse/TextDescriptives/commit/1a7ca00559f1db0060cfcb0d0a120a1948d697c7))

* fix: remove doc extension instead of pipe component. TODO double check all assings are correct ([`bc32d47`](https://github.com/HLasse/TextDescriptives/commit/bc32d479da59bfb438bb860795ca56e02fc60196))

### Unknown

* Merge pull request #137 from HLasse/HLasse/Create-wrapper-function

Create wrapper function (`extract_metrics`) ([`158ceeb`](https://github.com/HLasse/TextDescriptives/commit/158ceeb06888c137b109fc95662c14f54e8d1da0))

* Merge pull request #142 from HLasse/KennethEnevoldsen-patch-1

Added arXiv reference ([`23ccda0`](https://github.com/HLasse/TextDescriptives/commit/23ccda0942fe2a6667f7b9106a75e928012d016d))

* Update README.md ([`6b69eb6`](https://github.com/HLasse/TextDescriptives/commit/6b69eb6ba4158a0097c69bb1ab1fadbe3332af7e))

* tutorial: update tutorial to also include `extract_metrics` ([`da46ca1`](https://github.com/HLasse/TextDescriptives/commit/da46ca18bbcb0e2416be0cfbae5e04214d96cc1a))

* Merge branch &#39;main&#39; of https://github.com/hlasse/TextDescriptives ([`45c7cf7`](https://github.com/HLasse/TextDescriptives/commit/45c7cf7222325f8027ecf28cf7ea288f3ebf304c))

* Merge branch &#39;HLasse/Create-wrapper-function&#39; of https://github.com/HLasse/TextDescriptives into HLasse/Create-wrapper-function ([`5cb931f`](https://github.com/HLasse/TextDescriptives/commit/5cb931fd109b4a00a1f902d6a04df5eae42bb3b8))

* paper: misc paper updates and fixes ([`267ea80`](https://github.com/HLasse/TextDescriptives/commit/267ea80760f844166934db0e3d68ed320cf3f8e4))

* Update paper.bib ([`f7a1cbd`](https://github.com/HLasse/TextDescriptives/commit/f7a1cbde73a6ad016e1418b1d115f742f2873bb4))

* Update paper.md ([`9c29621`](https://github.com/HLasse/TextDescriptives/commit/9c29621a669fac5462334c755659fed1ac121b95))

* [pre-commit.ci] auto fixes from pre-commit.com hooks

for more information, see https://pre-commit.ci ([`1648480`](https://github.com/HLasse/TextDescriptives/commit/16484809739a7da300280edcb032b058ed96d547))

* merged ([`16f9f3f`](https://github.com/HLasse/TextDescriptives/commit/16f9f3fd7274330625f7a00744a72913bcda6ddb))

* [pre-commit.ci] auto fixes from pre-commit.com hooks

for more information, see https://pre-commit.ci ([`441db6a`](https://github.com/HLasse/TextDescriptives/commit/441db6a7f82e5d0170e804ff07eece1793557e82))

* paper: minor paper styling ([`0a10b96`](https://github.com/HLasse/TextDescriptives/commit/0a10b96d7c474d186d8a06dec3ecaa8b58ec649d))

* paper: add paper html to docs ([`f17a0d1`](https://github.com/HLasse/TextDescriptives/commit/f17a0d1fcbe7b139ef82e67ab6c377da8a3d90ec))

* paper: remove tex ([`eba2488`](https://github.com/HLasse/TextDescriptives/commit/eba2488583bf9afac01809b2a6535a818ca470b8))

* Update .gitignore

Co-authored-by: Kenneth Enevoldsen &lt;kennethcenevoldsen@gmail.com&gt; ([`14e3a68`](https://github.com/HLasse/TextDescriptives/commit/14e3a686f8bb25f2a0e84c003638e999b4cc96f1))

* paper: add joss draft and preprint ([`80da69a`](https://github.com/HLasse/TextDescriptives/commit/80da69a4aaa1d5c3861287e6c5fce96afe4f1812))

* paper: move paper to root dir ([`c89a018`](https://github.com/HLasse/TextDescriptives/commit/c89a018a8b520e96ebedcffc67ad5f165cb7d9d9))

* Merge branch &#39;main&#39; of https://github.com/HLasse/TextDescriptives into main ([`f8f7e6d`](https://github.com/HLasse/TextDescriptives/commit/f8f7e6d85292e009d112a8a122616d76b2db8cf4))

* paper: add paper draft and workflow ([`90c53c2`](https://github.com/HLasse/TextDescriptives/commit/90c53c29b9e069d31716bc0a91b1eef2a80eecf4))


## v2.0.10 (2023-01-03)

### Fix

* fix: correct pypi api token ([`da723f1`](https://github.com/HLasse/TextDescriptives/commit/da723f1f7ccc69a056814ab807f6b0fe9a2a4f20))

### Unknown

* Merge branch &#39;main&#39; of https://github.com/HLasse/TextDescriptives into main ([`94542ba`](https://github.com/HLasse/TextDescriptives/commit/94542ba3b960a113e27effde3cdb718ee1c49fe4))


## v2.0.9 (2023-01-03)

### Fix

* fix: sem ver ([`365de7a`](https://github.com/HLasse/TextDescriptives/commit/365de7a0de40f72a084bab0da5dd1a976ce3858a))


## v2.0.8 (2023-01-03)

### Fix

* fix: ci for sem ver ([`6762803`](https://github.com/HLasse/TextDescriptives/commit/6762803fa1a4e61b6dcdc7b059d6cf03e54f8c1a))

### Unknown

* Merge branch &#39;main&#39; of https://github.com/HLasse/TextDescriptives into main ([`8374be3`](https://github.com/HLasse/TextDescriptives/commit/8374be3c5790ab2fdb1fe075c4139db8df2e7057))


## v2.0.7 (2023-01-03)

### Fix

* fix: semantic release(!?) ([`2d9a4d2`](https://github.com/HLasse/TextDescriptives/commit/2d9a4d2d58943f93886e182d54a35c343a9241bf))


## v2.0.6 (2023-01-03)

### Fix

* fix: semantic versioning automatic upload ([`54f9e95`](https://github.com/HLasse/TextDescriptives/commit/54f9e956330157d458d0851f8d040b01899503c7))

### Unknown

* Merge branch &#39;main&#39; of https://github.com/HLasse/TextDescriptives into main ([`c1bc4d2`](https://github.com/HLasse/TextDescriptives/commit/c1bc4d2a7ee2409d541c41bab73ba5d7157b9f9a))


## v2.0.5 (2023-01-03)

### Ci

* ci: add documentation concurrency ([`4b8ae69`](https://github.com/HLasse/TextDescriptives/commit/4b8ae69365d6d311b4127bbdd45ea71bc8eccffc))

### Fix

* fix: testing semantic release ([`fcd797b`](https://github.com/HLasse/TextDescriptives/commit/fcd797bd81a4e5fbc7d162d4d8530f6898ea4b1a))


## v2.0.4 (2023-01-03)

### Ci

* ci: add stale ci ([`a6fc4c7`](https://github.com/HLasse/TextDescriptives/commit/a6fc4c71e53fb47dbf5d9446a94a175a507eec21))

* ci: concurrency causes jobs on other python version to be cancelled ([`78bc8cb`](https://github.com/HLasse/TextDescriptives/commit/78bc8cbb11548321ac9370f9131751d1074ec930))

* ci: A believes fix for prerelease ([`273785c`](https://github.com/HLasse/TextDescriptives/commit/273785ca76801975dd2f19d27504d8dce7e5f330))

### Fix

* fix: testing semantic release ([`95bbadc`](https://github.com/HLasse/TextDescriptives/commit/95bbadc040d64bbf6c1d3579b9ad44f9fe0a2459))

### Unknown

* Merge pull request #134 from HLasse/ci-fix

ci: A believed fix for prerelease ([`5bbb90b`](https://github.com/HLasse/TextDescriptives/commit/5bbb90b84ea74c9b46f5939d7b67c1dac4915329))

* Update .github/workflows/stale.yml ([`7a85b8a`](https://github.com/HLasse/TextDescriptives/commit/7a85b8ac9e40e9d9ea95ea42495084e62792b81a))

* Update .github/workflows/stale.yml ([`625713d`](https://github.com/HLasse/TextDescriptives/commit/625713dda037bbc165ddf20b5ed401acbfcadcd3))

* Merge pull request #133 from HLasse/pre-commit-ci-update-config

[pre-commit.ci] pre-commit autoupdate ([`7cef51a`](https://github.com/HLasse/TextDescriptives/commit/7cef51a208f4331df7405d6f347518b429ae4602))

* [pre-commit.ci] pre-commit autoupdate

updates:
- [github.com/asottile/pyupgrade: v2.38.0 → v3.3.1](https://github.com/asottile/pyupgrade/compare/v2.38.0...v3.3.1)
- [github.com/asottile/add-trailing-comma: v2.3.0 → v2.4.0](https://github.com/asottile/add-trailing-comma/compare/v2.3.0...v2.4.0)
- [github.com/PyCQA/docformatter: v1.5.0 → v1.5.1](https://github.com/PyCQA/docformatter/compare/v1.5.0...v1.5.1)
- [github.com/psf/black: 22.8.0 → 22.12.0](https://github.com/psf/black/compare/22.8.0...22.12.0)
- [github.com/charliermarsh/ruff-pre-commit: v0.0.181 → v0.0.206](https://github.com/charliermarsh/ruff-pre-commit/compare/v0.0.181...v0.0.206) ([`a447f18`](https://github.com/HLasse/TextDescriptives/commit/a447f18b34f64c9fe001eac7afa71bbf82f6ecda))

* Update README.md ([`7aeca29`](https://github.com/HLasse/TextDescriptives/commit/7aeca29f3e6b464e2b42e5490b7ede8c65d3092d))


## v2.0.3 (2023-01-02)

### Chore

* chore: precommit ([`55654ef`](https://github.com/HLasse/TextDescriptives/commit/55654efa98ed10bb6f9f8338dff00c7649eeff20))

### Fix

* fix: semantic version test ([`733ae89`](https://github.com/HLasse/TextDescriptives/commit/733ae898969322b3a214e841de41885f235815dc))


## v2.0.2 (2023-01-02)

### Fix

* fix: add setup.py ([`7ab6aed`](https://github.com/HLasse/TextDescriptives/commit/7ab6aedae39943781d75025e9ae8e403ad9ece6a))


## v2.0.1 (2023-01-02)

### Ci

* ci: fix semantic release ([`032f556`](https://github.com/HLasse/TextDescriptives/commit/032f5568f1d3af52d4210e30007ea6cc3d322ce5))

* ci: split test and release workflows ([`ede8339`](https://github.com/HLasse/TextDescriptives/commit/ede8339e10dd999b14eac1c74f4c3a7ed8bda000))

### Fix

* fix: release checkout with token ([`f6cbb3a`](https://github.com/HLasse/TextDescriptives/commit/f6cbb3afd2c9624e38d59f62ec122bd98a8629df))

* fix: remove duplicate workflow ([`e7a568c`](https://github.com/HLasse/TextDescriptives/commit/e7a568c87a2f938ed222d3c83b641ec7d2006a44))

* fix: semantic versioning ([`a297d66`](https://github.com/HLasse/TextDescriptives/commit/a297d666626ed2997d69eec55b77e9d09b636a8c))

### Unknown

* Merge pull request #132 from HLasse/semantic_versioning

ci: ensure semantic release uses main branch ([`2651b05`](https://github.com/HLasse/TextDescriptives/commit/2651b05b78c07378b1124799d4e23b0c4108a004))

* v2.0.0 ([`d2bceb6`](https://github.com/HLasse/TextDescriptives/commit/d2bceb611371e14edb69c5c4b5ad5621aadfd2dd))

* readme: fix badge ([`15d083e`](https://github.com/HLasse/TextDescriptives/commit/15d083e7a18ee5f8b410a4d2b0f3b29ec739e0a9))

* readme: fix badge ([`6935012`](https://github.com/HLasse/TextDescriptives/commit/6935012606cec215664326423d4cfe47b9974b7a))

* Merge pull request #131 from HLasse/ci--split-release-and-test-to-two-workflows

ci: split test and release workflows ([`f7113e5`](https://github.com/HLasse/TextDescriptives/commit/f7113e555c1ea4d669cffa45f62b214c1bab90a1))

* readme: fix badge ([`259cf83`](https://github.com/HLasse/TextDescriptives/commit/259cf83c2f482700dc0f7c9f28143590ae7bcf06))

* Merge pull request #130 from HLasse/ci_updates

Build: Add missing dependency for tutorial ([`c48be9e`](https://github.com/HLasse/TextDescriptives/commit/c48be9e9fcc0d2a78892592d41d20cdd427df6aa))

* Build: Add missing dependency for tutorial ([`9b7b2fc`](https://github.com/HLasse/TextDescriptives/commit/9b7b2fc152d08bac36dda19815749b32e5214583))


## v2.0.0 (2023-01-02)

### Build

* build: updated spacy dependency ([`f218684`](https://github.com/HLasse/TextDescriptives/commit/f2186841a0309008d74270ff2f80aec2fd417bca))

* build: remove unused dependency ([`525bac0`](https://github.com/HLasse/TextDescriptives/commit/525bac01d21dc80f87c75cc41acfa92dc566ce60))

* build: transitioned to pyproject.toml ([`8aa1cce`](https://github.com/HLasse/TextDescriptives/commit/8aa1cce86676aef6aa38a874b7bf41287a72c0a8))

* build: update manifest ([`f6893bb`](https://github.com/HLasse/TextDescriptives/commit/f6893bb0e400a4e242181c7eda99c294b51cab1f))

* build: better building 🤷‍♂️ ([`2e9ac71`](https://github.com/HLasse/TextDescriptives/commit/2e9ac71cf5a7f3f0f72f7c3b1281201aa4acb2e7))

* build: remove package autofind for correct building ([`ea1345e`](https://github.com/HLasse/TextDescriptives/commit/ea1345eacf0003d8a1e96bc8265410e521818134))

* build: bumb spacy version ([`d2180d1`](https://github.com/HLasse/TextDescriptives/commit/d2180d15324cf05e33cac74065902ff6f364ba0b))

* build: update version number ([`bee7881`](https://github.com/HLasse/TextDescriptives/commit/bee788164c53910e1566ccdac362af5cc7c75328))

### Chore

* chore: moved spam.csv back into data ([`f42283d`](https://github.com/HLasse/TextDescriptives/commit/f42283d967c4de706149ea3148a5d5828ced98e7))

* chore: moved testfolder out of package ([`c026967`](https://github.com/HLasse/TextDescriptives/commit/c026967c5c4501e428eb4819b6a44032d24a73da))

* chore: black ([`33f7aed`](https://github.com/HLasse/TextDescriptives/commit/33f7aed0a6d43b1fcf2ab09f30c0baa117755cef))

### Ci

* ci: removed non neede token ([`2683ac1`](https://github.com/HLasse/TextDescriptives/commit/2683ac15f0ee22ad93edc418e9c6ddc3db08b1ce))

* ci: removed python setup from docs workflow ([`42e1fe9`](https://github.com/HLasse/TextDescriptives/commit/42e1fe91c0d941e407eaa3d02173d4123fcc4265))

* ci: fix cache path ([`a03c45d`](https://github.com/HLasse/TextDescriptives/commit/a03c45d9abfd1ec552b9c4ea6623741179ad4801))

* ci: Fix cache path ([`6af7a3e`](https://github.com/HLasse/TextDescriptives/commit/6af7a3eed29d56c317db3bfa244e518976ff15a3))

* ci: cahce using pyproject.toml ([`c9ed231`](https://github.com/HLasse/TextDescriptives/commit/c9ed2315adcb8e6e13d02cce8e5ad27eb7e0c449))

* ci: re-enable cache ([`aab4439`](https://github.com/HLasse/TextDescriptives/commit/aab44394bfd663ab32c24fbf49ecd73b7def1924))

* ci: invalidate cache ([`793bf3f`](https://github.com/HLasse/TextDescriptives/commit/793bf3fcc6347d21b24dedde0e39012211ec8c7a))

* ci: remove autofix from ruff ([`31903f3`](https://github.com/HLasse/TextDescriptives/commit/31903f3ce0891a941dc108735720b3f32ea56114))

* ci: required bash for running shell commands ([`b02a06c`](https://github.com/HLasse/TextDescriptives/commit/b02a06c7a47a35ba0c2a32099079e34ec208aa0b))

* ci: fixed version of ci ([`54e0ac0`](https://github.com/HLasse/TextDescriptives/commit/54e0ac040b648909170da32f9961faa8ddb90add))

* ci: added test of notebooks to test_and_relase ([`b9ed67d`](https://github.com/HLasse/TextDescriptives/commit/b9ed67d00512f082a319ff8d5f9ef9e51e9b5486))

* ci: added pre-commit-ci to automerge ([`eb471d5`](https://github.com/HLasse/TextDescriptives/commit/eb471d5da46cdfaec157ffddb2ad8f143931fec6))

* ci: remove outdated workflows ([`e1c9235`](https://github.com/HLasse/TextDescriptives/commit/e1c9235c3a94e6cc4241615846e410ab9782cad4))

* ci: Added semantic release ci ([`d271165`](https://github.com/HLasse/TextDescriptives/commit/d2711654b77210980454e928ba55cf22365faec3))

* ci: updated ci to import version from package ([`08ffebc`](https://github.com/HLasse/TextDescriptives/commit/08ffebc6cbecea26e37a0ee149b12fa2c8778708))

* ci: fixed error in version specification ([`260b26d`](https://github.com/HLasse/TextDescriptives/commit/260b26dbce22281fd7cf0f29e3fb21a171d07cda))

* ci: Added documentation build to PR ([`e4518ad`](https://github.com/HLasse/TextDescriptives/commit/e4518adbb180f69b05f9ac596c6dd4d728dbd53b))

* ci: moved docs requirements to main requirements.txt ([`51139c8`](https://github.com/HLasse/TextDescriptives/commit/51139c89589e2aba1c5728b7b83854b9f7e8df76))

* ci: Added mypy and refactored quality thresholds ([`69ea0fd`](https://github.com/HLasse/TextDescriptives/commit/69ea0fdd7bdd3e2353154a3a13bbdd07adbbb441))

* ci: update ci branches to main ([`6a27b78`](https://github.com/HLasse/TextDescriptives/commit/6a27b78e7d12590bcf0a0eb3b50537f31233d4d3))

* ci: dependabot automerge if tests pass ([`8906458`](https://github.com/HLasse/TextDescriptives/commit/8906458d4cdae1ad9ab9a1d88255fca22bd6ce31))

* ci: reduce OS test matrix ([`6620c55`](https://github.com/HLasse/TextDescriptives/commit/6620c55dec4dbd5605e7f691786673e51aa1a676))

* ci: update pytest coverage comment ([`78a4643`](https://github.com/HLasse/TextDescriptives/commit/78a4643f2e6949a554a0cb62681015fb37095fd6))

* ci: remove pytest-cov-comment ([`e135201`](https://github.com/HLasse/TextDescriptives/commit/e135201fd9318d0e55ca517f4eeab3ed8ce37a8e))

* ci: update pytest-coverage.comment version ([`dc1ddb3`](https://github.com/HLasse/TextDescriptives/commit/dc1ddb343b0f5baa66dccdd593f0971725a93820))

### Documentation

* docs: build documentation without return an error ([`2e91f9a`](https://github.com/HLasse/TextDescriptives/commit/2e91f9a415a8756ee30dc7fb28b41e3a598b44f3))

* docs: Minor polished to the documentation ([`3f48688`](https://github.com/HLasse/TextDescriptives/commit/3f48688876ff98e3ea0706bbc97d76d20f701c18))

* docs: polished docs ([`799d57a`](https://github.com/HLasse/TextDescriptives/commit/799d57a946d150b137931ff55dbe2240b274bdd7))

* docs: more informative error messages in coherence component. Fixes empty output for coherence with a blank pipeline #115 ([`086bfbe`](https://github.com/HLasse/TextDescriptives/commit/086bfbe6529973054f108ea3564445b45d29208d))

* docs: misc doc updates ([`f9aee35`](https://github.com/HLasse/TextDescriptives/commit/f9aee35d9c16f48c5f237eb84d65bc522268965a))

* docs: update readme ([`17b0133`](https://github.com/HLasse/TextDescriptives/commit/17b0133404327900d03872f407bfd7e402d90ec3))

* docs: minor fomatting ([`faa86f7`](https://github.com/HLasse/TextDescriptives/commit/faa86f7b10ef29fb4782fb61b6ae88defbbc176b))

* docs: add tutorial to docs ([`fbeab00`](https://github.com/HLasse/TextDescriptives/commit/fbeab0062f2b088e38ec3bbb85616ccb12acd69b))

* docs: Added faq for developers ([`795f49d`](https://github.com/HLasse/TextDescriptives/commit/795f49d5acc92547c0617d3e3476b6c7c2b0fb65))

* docs: update usingthepackage. Fixes Add quality to table of available-attributes #107 ([`2264162`](https://github.com/HLasse/TextDescriptives/commit/2264162d3c2fde9830f9041c06e275bf2c9be34f))

* docs: add example to coherence docs. Fixes #114 ([`b0802aa`](https://github.com/HLasse/TextDescriptives/commit/b0802aa9b1817dcc7337bbc66182991e7e4d35b5))

* docs: Added documentation to create functions ([`11619cf`](https://github.com/HLasse/TextDescriptives/commit/11619cf480787e03a8db3e4192a162a1f8e1324e))

* docs: updated docstring based on review ([`bb6503a`](https://github.com/HLasse/TextDescriptives/commit/bb6503a7850b7f7f724fc2fe6e312987a9e97214))

* docs: updated docs ([`45a5684`](https://github.com/HLasse/TextDescriptives/commit/45a5684c31782492428b582a134898c09dca94e5))

* docs: add how to use custom word embeddings ([`153764b`](https://github.com/HLasse/TextDescriptives/commit/153764bf16735b6b1ced0dd979bba4e9c1e73591))

* docs: minor ([`1523786`](https://github.com/HLasse/TextDescriptives/commit/15237861d84a6e2dd5c3cf29e567070e38202a80))

* docs: add docs for coherence ([`d3d152a`](https://github.com/HLasse/TextDescriptives/commit/d3d152aa620787a36a473d16eabd90abf4687bfb))

* docs: minor formatting ([`26804c6`](https://github.com/HLasse/TextDescriptives/commit/26804c611a212a81e57dc6c621e3efee196a47a4))

* docs: Create simple tutorial
Fixes #86 ([`75669e5`](https://github.com/HLasse/TextDescriptives/commit/75669e5e3822af0c0db5c0ce3c98ade4dd67864e))

* docs: add usage docs to components ([`c310a91`](https://github.com/HLasse/TextDescriptives/commit/c310a917ae32aa62ad56d148dcbe1fa7cde0a9c3))

* docs: add pos_proportions example ([`a8602fd`](https://github.com/HLasse/TextDescriptives/commit/a8602fd2d63c5ea2bfa9510568c2abb68db6a4b1))

* docs: docs for dependency distance formula
Fixes #77 ([`ec360fc`](https://github.com/HLasse/TextDescriptives/commit/ec360fc9ab7547721c638f87410f1bea800fea45))

* docs: update quality docs ([`b63d88c`](https://github.com/HLasse/TextDescriptives/commit/b63d88c6f200339bc78e3733e86362a778709fdc))

* docs: update docstrings and misc minor ([`5ef3afc`](https://github.com/HLasse/TextDescriptives/commit/5ef3afc9469d517ad7800e54f77185e988329cca))

* docs: misc docs ([`6202c52`](https://github.com/HLasse/TextDescriptives/commit/6202c522fc3495e6e0b9d011014f2a467d71c15b))

* docs: add quality checks to docs ([`b4953f5`](https://github.com/HLasse/TextDescriptives/commit/b4953f50452d7e15d192aa76ca5ee7172fc80b09))

### Feature

* feat: spacy 3.4 compatibility - dashes to slashes in factory names ([`95cc0fb`](https://github.com/HLasse/TextDescriptives/commit/95cc0fb58a4270ff24e306f7d78bba46a85912b1))

* feat: add word embedding coherence/similarity
Fixes #50 ([`143d648`](https://github.com/HLasse/TextDescriptives/commit/143d648997da91f15a1f9a1a8cbe66c21bd72e62))

* feat: add loader for tutorial dataset ([`7c08710`](https://github.com/HLasse/TextDescriptives/commit/7c08710d4b2e945076d58d459c520325e9177b50))

* feat: Separate component loaders
Fixes #85 ([`2fdee32`](https://github.com/HLasse/TextDescriptives/commit/2fdee325272375ebc0229907f051c9b609692a77))

* feat: add new icon ([`765a428`](https://github.com/HLasse/TextDescriptives/commit/765a42890eb24ef5bf1ec09af41a2ce356755207))

### Fix

* fix: changed warning to info message ([`c1a7978`](https://github.com/HLasse/TextDescriptives/commit/c1a797864a8fa7197e0f920f1628bf735df6c4b4))

* fix: Avoid raising warning for empty lists ([`5bfc7f9`](https://github.com/HLasse/TextDescriptives/commit/5bfc7f958d5a24dc6549c1d83ec9233306863162))

* fix: move text to first position ([`2d5c29c`](https://github.com/HLasse/TextDescriptives/commit/2d5c29c87934762941bf548f3c1c0d9627022b72))

* fix: fixed bug when testing vector shape ([`c3e3f4d`](https://github.com/HLasse/TextDescriptives/commit/c3e3f4d943f031b6c6e46c7c1b25a661ce53a6bc))

* fix: bug in `extract_dict` causing only the first metric to to extracted ([`94f3c68`](https://github.com/HLasse/TextDescriptives/commit/94f3c68468b0ec6f97985aa4bb3aee6c7cd995a5))

* fix: fix fetching package version in python 3.7 ([`325ad08`](https://github.com/HLasse/TextDescriptives/commit/325ad0872861b7b46f3ba513a8acf93bc8d5f264))

* fix: fix fetching package version in python 3.7 ([`66a5595`](https://github.com/HLasse/TextDescriptives/commit/66a559534da00c8e8601be25b3f64c329972aad7))

* fix: Added generalized load component to include new component

Added missing component: coherence ([`9823160`](https://github.com/HLasse/TextDescriptives/commit/9823160ba24b5c70fcc2f1fac805af36dd7f3309))

* fix: fixed bug where extract overwrote values with mulitple components ([`a7210ce`](https://github.com/HLasse/TextDescriptives/commit/a7210ceecbec7ce43bd4af1e358f6795213583c6))

* fix: test which occurs when running multiple tests together ([`ab3ed0e`](https://github.com/HLasse/TextDescriptives/commit/ab3ed0e4f077be1d2cc70a3ae77f1f87828f4c32))

* fix: minor spelling errors ([`290634b`](https://github.com/HLasse/TextDescriptives/commit/290634b466040776733971ef74396ac77be5a9e5))

* fix: fixed quality component ([`c6647fa`](https://github.com/HLasse/TextDescriptives/commit/c6647fa44f5984e75cfd523bd29aa1d3a0845aff))

* fix: fixed missing imports ([`ec01f0a`](https://github.com/HLasse/TextDescriptives/commit/ec01f0a677894cbe3786e554536329bc7e602459))

* fix: remove `span_to_doc_getter` ([`9c7c032`](https://github.com/HLasse/TextDescriptives/commit/9c7c0320180126a79be5f92d486aaa092adab215))

* fix: allow multiprocessing in descriptive stats component ([`f16443f`](https://github.com/HLasse/TextDescriptives/commit/f16443f62e7397fcd2bdd033d9ee955f7dac41a8))

* fix: handle texts with ngrams below the range ([`01084f3`](https://github.com/HLasse/TextDescriptives/commit/01084f33137c93e8bc22f9f028888e7aa90d0aed))

* fix: extract_df failing if metric=&#34;all&#34; and not all components set ([`9519c6c`](https://github.com/HLasse/TextDescriptives/commit/9519c6c4321c118f0f5dd669b7e2c4731f91f829))

* fix: typo that caused everything to fail ([`d796207`](https://github.com/HLasse/TextDescriptives/commit/d796207598db1a205ec006f60621667238242dde))

* fix: icon name ([`85d85cc`](https://github.com/HLasse/TextDescriptives/commit/85d85cc0d8dd233cda30090842cc9a5e75156b0f))

### Refactor

* refactor: to use src ([`b414d86`](https://github.com/HLasse/TextDescriptives/commit/b414d862e83168a70c508a5b9bafd48e21042231))

* refactor: refactored get ([`defb5fc`](https://github.com/HLasse/TextDescriptives/commit/defb5fcc31fae056661c8284fc3f301b2a541343))

### Test

* test: Fixed error in tests ([`01fc259`](https://github.com/HLasse/TextDescriptives/commit/01fc2593c1b3015334a72dcb2e665b91838174b6))

* test: updated introductory tutorials ([`c15ed7e`](https://github.com/HLasse/TextDescriptives/commit/c15ed7ee0bdadfcb9db39904dfd30a4ec8bf5978))

* test: multiprocessing in quality component ([`de9126b`](https://github.com/HLasse/TextDescriptives/commit/de9126b312d13aa858b00c71939ef692b9dc040c))

* test: icon works? ([`c61c587`](https://github.com/HLasse/TextDescriptives/commit/c61c5873bf47867db6dc9f0e1c4ea4e816258091))

### Unknown

* Merge pull request #129 from HLasse/dev

CI: Fix errors in CI ([`e539e7b`](https://github.com/HLasse/TextDescriptives/commit/e539e7b3dc760379f34ce3ab7d14aa71697c3a1f))

* Revert &#34;Revert &#34;test: Fixed error in tests&#34;&#34;

This reverts commit a0bb828a86752f43c9f453ca8e6c8c9878c15f73. ([`644ba24`](https://github.com/HLasse/TextDescriptives/commit/644ba246858b3001679b5b65d8132d992ee31acc))

* Revert &#34;test: Fixed error in tests&#34;

This reverts commit 01fc2593c1b3015334a72dcb2e665b91838174b6. ([`a0bb828`](https://github.com/HLasse/TextDescriptives/commit/a0bb828a86752f43c9f453ca8e6c8c9878c15f73))

* Merge pull request #118 from HLasse/dev

Version 2.0 ([`2d028f1`](https://github.com/HLasse/TextDescriptives/commit/2d028f109f1734d7a85443637f0b664665d64b1b))

* Merge branch &#39;dev&#39; of https://github.com/hlasse/TextDescriptives into dev ([`6a189b1`](https://github.com/HLasse/TextDescriptives/commit/6a189b1a84a3a97d90b9c0a0fc32015bdf05d214))

* [pre-commit.ci] auto fixes from pre-commit.com hooks

for more information, see https://pre-commit.ci ([`531866b`](https://github.com/HLasse/TextDescriptives/commit/531866b8b7b4e9b6e135500f97765d090e373091))

* Merge branch &#39;dev&#39; of https://github.com/hlasse/TextDescriptives into dev ([`22d0e34`](https://github.com/HLasse/TextDescriptives/commit/22d0e34dcce48c431a40f5726cf1be8bb26e9e76))

* Merge branch &#39;dev&#39; of https://github.com/HLasse/TextDescriptives into dev ([`c96b582`](https://github.com/HLasse/TextDescriptives/commit/c96b582f255c86530156052bed55f9a4928ad7d7))

* Update README.md ([`817990a`](https://github.com/HLasse/TextDescriptives/commit/817990ab80a8bfd0b6431eb2d031648e0612aad8))

* Update README.md ([`0204914`](https://github.com/HLasse/TextDescriptives/commit/0204914f9e119a96b9ad7253e49f8c2b0218025e))

* Update README
Fixes #119 ([`7452aba`](https://github.com/HLasse/TextDescriptives/commit/7452abad3f044e1baabe03d12b1f0606178d0f99))

* Merge pull request #128 from HLasse:HLasse/Update-README

HLasse/Update-README ([`7cba797`](https://github.com/HLasse/TextDescriptives/commit/7cba797ae9b88c900bd03964f6f38b3f35aaca40))

* tutorial: add open in colab badge ([`8af97c5`](https://github.com/HLasse/TextDescriptives/commit/8af97c58218faa7d25e852cfb9959254cc601811))

* tutorial: update installer ([`1903a18`](https://github.com/HLasse/TextDescriptives/commit/1903a18a80866190d6f7114ab3e4647beb6dafb7))

* Merge pull request #125 from HLasse:tutorial-to-colab

tutorial: add open in colab button ([`3ead0eb`](https://github.com/HLasse/TextDescriptives/commit/3ead0eb739676cca699c31329dde923cfc286bc9))

* tutorial: add open in colab button ([`c134da2`](https://github.com/HLasse/TextDescriptives/commit/c134da2022476e129ddfe6f2ef8481b4ede7a497))

* Merge pull request #123 from HLasse/HLasse/Change-documentation-landing-page

HLasse/Change-documentation-landing-page ([`ee7d0c8`](https://github.com/HLasse/TextDescriptives/commit/ee7d0c85114a27fc40319f08e32c1cf0be849b01))

* Merge branch &#39;dev&#39; into HLasse/Change-documentation-landing-page ([`826200d`](https://github.com/HLasse/TextDescriptives/commit/826200dfccfc41203f6ab5f714fedbd15cc064c8))

* Merge pull request #122 from HLasse/build-transition-to-pyproject-toml

Build-transition-to-pyproject-toml ([`289db69`](https://github.com/HLasse/TextDescriptives/commit/289db69ea842826204e7ba529f4eb4cd95a2b4e4))

* tests: Added missing import leading to failed tests when running tests individually ([`79972d2`](https://github.com/HLasse/TextDescriptives/commit/79972d2cd562f271435c9025e5b615b3829001b6))

* tests: Added test of blank pipes to coherence ([`8bde489`](https://github.com/HLasse/TextDescriptives/commit/8bde48961e39e961e3bcdc05f61964de47098843))

* Change documentation landing page
Fixes #120 ([`4644d26`](https://github.com/HLasse/TextDescriptives/commit/4644d26df5aeef08e004c5278232477c353d48c0))

* tests: Added missing imports to coherence tests ([`97ca004`](https://github.com/HLasse/TextDescriptives/commit/97ca0044dbe90e15219accffd4cd8333518aa896))

* tests: re-enable coherence tests ([`812b674`](https://github.com/HLasse/TextDescriptives/commit/812b67405a442e35a212c00fb0bc641b4b2e6ece))

* Merge pull request #117 from HLasse/docs-move-documentation-to-create-func

Docs-move-documentation-to-create-func ([`147e4fc`](https://github.com/HLasse/TextDescriptives/commit/147e4fc76a86e4b534891103f41a943a92a1e8b0))

* Merge branch &#39;dev&#39; into docs-move-documentation-to-create-func ([`53424d7`](https://github.com/HLasse/TextDescriptives/commit/53424d767a80f3eeef751b4c3503b00d6a3c22d6))

* Merge pull request #116 from HLasse/extract_df_and_tutorial_fix

Extract_df_and_tutorial_fix ([`09eb68d`](https://github.com/HLasse/TextDescriptives/commit/09eb68d9496f9a13d9fe900669414805e2ed73d2))

* [pre-commit.ci] auto fixes from pre-commit.com hooks

for more information, see https://pre-commit.ci ([`2bee774`](https://github.com/HLasse/TextDescriptives/commit/2bee77488d825979ff900ce101746e263d461c00))

* misc: test if coverage report updates ([`aecc581`](https://github.com/HLasse/TextDescriptives/commit/aecc581eb143a76579fc063c8fd78b767a8630b9))

* tutorial: include all output ([`39635a1`](https://github.com/HLasse/TextDescriptives/commit/39635a143b7368e8408ed7ea306d4bf7125cc952))

* tests: added a few tests for `extract_df` fixes tests: improve extract_df|dict tests #112 ([`782b1b9`](https://github.com/HLasse/TextDescriptives/commit/782b1b91e26145c80c1af7f4242747dcb08748d7))

* Merge pull request #111 from HLasse/ci-mypy

Ci mypy ([`66e6f3b`](https://github.com/HLasse/TextDescriptives/commit/66e6f3b58f1c9831fc40a697a7385b00cdd13433))

* tests: Added missing requirements for test of notebooks ([`bb661ee`](https://github.com/HLasse/TextDescriptives/commit/bb661eee68f198a4cddc8a0e62a188c76c9ca839))

* Merge branch &#39;ci-mypy&#39; of https://github.com/hlasse/TextDescriptives into ci-mypy ([`2c84d20`](https://github.com/HLasse/TextDescriptives/commit/2c84d20846966a60ea65bf8c0ec55005157f0448))

* Update textdescriptives/components/quality.py

Co-authored-by: Lasse Hansen &lt;lasseh0310@gmail.com&gt; ([`475724a`](https://github.com/HLasse/TextDescriptives/commit/475724a7488cb736e046f66369e30b62b2cd61a9))

* Apply suggestions from code review

Co-authored-by: Lasse Hansen &lt;lasseh0310@gmail.com&gt; ([`7083618`](https://github.com/HLasse/TextDescriptives/commit/708361868cc9f390b91422b2cc3657361e622041))

* Merge pull request #110 from HLasse/ci-semantic-release

CI: Added semantic release ([`4adfbf9`](https://github.com/HLasse/TextDescriptives/commit/4adfbf9d44617d93e5825e5c66c380c115cac49c))

* Merge branch &#39;ci-mypy&#39; into ci-semantic-release ([`5a5893e`](https://github.com/HLasse/TextDescriptives/commit/5a5893e7483d4acb3f6e5d3a6423e4962c0894af))

* Merge branch &#39;ci-semantic-release&#39; of https://github.com/hlasse/TextDescriptives into ci-semantic-release ([`f3368fb`](https://github.com/HLasse/TextDescriptives/commit/f3368fb3db8d3b97df0bf5d5f50d67ce89f914c3))

* Ci: add pre-commit (#97)

* ci: added pre-commit

* style: apply ruff

* tests: remove unused test

* [pre-commit.ci] auto fixes from pre-commit.com hooks

for more information, see https://pre-commit.ci

* style: black

Co-authored-by: pre-commit-ci[bot] &lt;66853113+pre-commit-ci[bot]@users.noreply.github.com&gt; ([`192559e`](https://github.com/HLasse/TextDescriptives/commit/192559e9a20e2d90d918194729c572983b8eeb84))

* Update documentation.yml ([`09ae0e6`](https://github.com/HLasse/TextDescriptives/commit/09ae0e6dea2eed55f59dc060c17993d579ffb564))

* Merge pull request #96 from HLasse/HLasse/Make-`quality`-work-with-`n_process`-&gt;-1

HLasse/Make-`quality`-work-with-`n_process`-&gt;-1 ([`a50de7a`](https://github.com/HLasse/TextDescriptives/commit/a50de7aa6406f52ce9a545812c57583ab60eb327))

* tests: misc ([`c12d80a`](https://github.com/HLasse/TextDescriptives/commit/c12d80a0d43ce9875a895e7724a74a8580dea0df))

* Merge pull request #92 from HLasse/HLasse/Add-word-embedding-coherence/similary

feat: add word embedding coherence/similarity ([`f397750`](https://github.com/HLasse/TextDescriptives/commit/f3977501a5c595eb70a6d5137f2781bd14423c4e))

* Merge pull request #95 from HLasse:spacy-3.4-compatibility

feat: spacy 3.4 compatibility - dashes to slashes in factory names ([`39c0825`](https://github.com/HLasse/TextDescriptives/commit/39c082592db760039f0effe279ed4d6ff6a0cf1e))

* misc: improvement from review ([`b75c219`](https://github.com/HLasse/TextDescriptives/commit/b75c2197d5563f8514398804678a7f903fadda19))

* Merge pull request #91 from HLasse/fix-multiprocessing

fix: allow multiprocessing in descriptive stats component ([`6cad4cb`](https://github.com/HLasse/TextDescriptives/commit/6cad4cb11a77fe2978380c623e3a1b8ac565df4a))

* Merge pull request #90 from HLasse/HLasse/Create-simple-tutorial

Simple tutorial and misc docs ([`dc4a1f9`](https://github.com/HLasse/TextDescriptives/commit/dc4a1f9af22cc6b6afe1595ce1cbc610c197c737))

* tests: test extract_df with single component ([`f3c494f`](https://github.com/HLasse/TextDescriptives/commit/f3c494f5813eade793f14527e3da7675f7483ab2))

* Merge branch &#39;dev&#39; into HLasse/Create-simple-tutorial ([`e391e69`](https://github.com/HLasse/TextDescriptives/commit/e391e69cf7b03a0ecccb1892ad3f88f3eb97e27a))

* Merge pull request #88 from HLasse/HLasse/Separate-component-loaders

feat: Separate component loaders ([`faa7bb8`](https://github.com/HLasse/TextDescriptives/commit/faa7bb88f1526dd94d3dad04494991fbe33ef883))

* Merge pull request #89 from HLasse:HLasse/Formulae-for-dependency-distance-calculation-on-Doc-level

docs: docs for dependency distance formula ([`2b87c85`](https://github.com/HLasse/TextDescriptives/commit/2b87c8531e59356185b2cc5c82790f6e46cc0d17))

* Merge pull request #84 from HLasse/HLasse/Add-_syllables-to-Span

Update docstrings ([`7a91a53`](https://github.com/HLasse/TextDescriptives/commit/7a91a53c8b48d085946079d8727dbb45295c6fcc))

* Update README.md ([`9451671`](https://github.com/HLasse/TextDescriptives/commit/94516712f977aff01effa1cfbb81968596caa435))

* Merge pull request #75 from rbroc/fix-pos

Fix pos_stats extraction ([`b189234`](https://github.com/HLasse/TextDescriptives/commit/b1892347c98950d98d3017b051140dc389977610))

* Merge pull request #78 from HLasse/automerge-dependabot

ci: dependabot automerge if tests pass ([`78a2eb0`](https://github.com/HLasse/TextDescriptives/commit/78a2eb03460c8c1cecbb6ea4582be749473e1f6a))

* update patch version ([`4479223`](https://github.com/HLasse/TextDescriptives/commit/4479223c6d17894801bfcb8e0a48f02dd347db7c))

* Merge pull request #76 from HLasse/dependabot/github_actions/MishaKav/pytest-coverage-comment-1.1.39

:arrow_up: Bump MishaKav/pytest-coverage-comment from 1.1.37 to 1.1.39 ([`b484729`](https://github.com/HLasse/TextDescriptives/commit/b4847293dc143330b48f9cd338947b497be99698))

* :arrow_up: Bump MishaKav/pytest-coverage-comment from 1.1.37 to 1.1.39

Bumps [MishaKav/pytest-coverage-comment](https://github.com/MishaKav/pytest-coverage-comment) from 1.1.37 to 1.1.39.
- [Release notes](https://github.com/MishaKav/pytest-coverage-comment/releases)
- [Changelog](https://github.com/MishaKav/pytest-coverage-comment/blob/main/CHANGELOG.md)
- [Commits](https://github.com/MishaKav/pytest-coverage-comment/compare/v1.1.37...v1.1.39)

---
updated-dependencies:
- dependency-name: MishaKav/pytest-coverage-comment
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`fc42a30`](https://github.com/HLasse/TextDescriptives/commit/fc42a3060f1d7c56e09270fd1c7e85ade71f8790))

* fix and simplify logic for component extraction ([`9a676bb`](https://github.com/HLasse/TextDescriptives/commit/9a676bb60b8e0fbf264556cf68834c67b39c5812))

* map pos_stats to pos_proportions in __unpack_extension method ([`bd8bd1e`](https://github.com/HLasse/TextDescriptives/commit/bd8bd1e8a5d600d35b186363ff1dac42a4ec76f2))

* Merge pull request #72 from HLasse/dependabot/github_actions/schneegans/dynamic-badges-action-1.6.0

:arrow_up: Bump schneegans/dynamic-badges-action from 1.3.0 to 1.6.0 ([`7e4aee5`](https://github.com/HLasse/TextDescriptives/commit/7e4aee599ae522bb3dd1021a12db323e6fa7d34c))

* Merge pull request #73 from HLasse/dependabot/pip/pytest-gte-7.1.3-and-lt-7.3.0

:arrow_up: Update pytest requirement from &lt;7.2.0,&gt;=7.1.3 to &gt;=7.1.3,&lt;7.3.0 ([`3c07f0b`](https://github.com/HLasse/TextDescriptives/commit/3c07f0ba47e2fb87c2f2de460c9641d43dd92021))

* :arrow_up: Update pytest requirement

Updates the requirements on [pytest](https://github.com/pytest-dev/pytest) to permit the latest version.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.1.3...7.2.0)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`06540ae`](https://github.com/HLasse/TextDescriptives/commit/06540ae9ce747e1ad27002eed6d18a50664bf65e))

* :arrow_up: Bump schneegans/dynamic-badges-action from 1.3.0 to 1.6.0

Bumps [schneegans/dynamic-badges-action](https://github.com/schneegans/dynamic-badges-action) from 1.3.0 to 1.6.0.
- [Release notes](https://github.com/schneegans/dynamic-badges-action/releases)
- [Changelog](https://github.com/Schneegans/dynamic-badges-action/blob/master/changelog.md)
- [Commits](https://github.com/schneegans/dynamic-badges-action/compare/v1.3.0...v1.6.0)

---
updated-dependencies:
- dependency-name: schneegans/dynamic-badges-action
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`4f5c158`](https://github.com/HLasse/TextDescriptives/commit/4f5c1588bbec2462ee0084dafd87a8fb653ce77b))

* Merge pull request #69 from HLasse/dependabot/pip/pandas-gte-1.0.0-and-lt-1.6.0

:arrow_up: Update pandas requirement from &lt;1.5.0,&gt;=1.0.0 to &gt;=1.0.0,&lt;1.6.0 ([`fc1f704`](https://github.com/HLasse/TextDescriptives/commit/fc1f704246d7fc4ec9c8022f0026c35297c8ee9b))

* merge main ([`0ff2218`](https://github.com/HLasse/TextDescriptives/commit/0ff221843bb830b040dc34be43eeb2f63a7da2c4))

* Update pytest-cov-comment.yml ([`ae7a1be`](https://github.com/HLasse/TextDescriptives/commit/ae7a1bea3d24920ca2c1be41f5e34a3a2030b931))

* Update README.md ([`a546b49`](https://github.com/HLasse/TextDescriptives/commit/a546b499a3b07ed5e87e7bb74e7589e5dd836911))

* Merge pull request #70 from HLasse/update-pytest-coverage-comment

ci: update pytest-coverage.comment version ([`f7badd1`](https://github.com/HLasse/TextDescriptives/commit/f7badd19705eb334b4eeb50081236f3acf36bf09))

* :arrow_up: Update pandas requirement

Updates the requirements on [pandas](https://github.com/pandas-dev/pandas) to permit the latest version.
- [Release notes](https://github.com/pandas-dev/pandas/releases)
- [Changelog](https://github.com/pandas-dev/pandas/blob/main/RELEASE.md)
- [Commits](https://github.com/pandas-dev/pandas/compare/v1.0.0...v1.5.0)

---
updated-dependencies:
- dependency-name: pandas
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`86ca4c6`](https://github.com/HLasse/TextDescriptives/commit/86ca4c6998d3f7f2f042d314b3e1946b274025dd))

* readme: fix path to icon ([`0a76a25`](https://github.com/HLasse/TextDescriptives/commit/0a76a250865df7d22fd23f1a6032c181ee967ada))

* Merge pull request #68 from HLasse/icon

add icon ([`e53e229`](https://github.com/HLasse/TextDescriptives/commit/e53e229d7f3656e30216b95424ce4ad8901a0403))

* add icon ([`57d59e8`](https://github.com/HLasse/TextDescriptives/commit/57d59e8d2c78f41f3de2cc9cc68e76fee3b5228a))

* delete icon ([`196b80b`](https://github.com/HLasse/TextDescriptives/commit/196b80bafd1b19fdad6e7a180f5e086c6828e60a))

* one more try ([`34398ed`](https://github.com/HLasse/TextDescriptives/commit/34398edd7cbeb6ae127a8f39658eec92fb7f21a0))

* different icon ([`077c188`](https://github.com/HLasse/TextDescriptives/commit/077c1887c1233a53eab3b0102192d3be261ebe57))


## v1.10.0 (2022-09-26)

### Build

* build: update requirements for python 3.10 ([`6704c4a`](https://github.com/HLasse/TextDescriptives/commit/6704c4aee8ec84184850ec3c5d32670f917ad49d))

### Ci

* ci: Added python 3.10 ([`9d709b7`](https://github.com/HLasse/TextDescriptives/commit/9d709b7c0a36dd6024bab880e2f641860745458c))

### Documentation

* docs: build docs ([`0d5e960`](https://github.com/HLasse/TextDescriptives/commit/0d5e9600ba950271236cd0c927d970d1eca67168))

* docs: minor readme updates ([`88cbc40`](https://github.com/HLasse/TextDescriptives/commit/88cbc40d81454fddb7dbf7c414897e2796c10f1b))

* docs: add reference to DFM ([`1578599`](https://github.com/HLasse/TextDescriptives/commit/15785993eee366bc2e8951f53fccbe02cbd4bf9c))

* docs: minor update to news ([`03b9d84`](https://github.com/HLasse/TextDescriptives/commit/03b9d84b7ea77ee57370fae7a0b46a7f57a6f757))

* docs: added documentation for quality ([`976c050`](https://github.com/HLasse/TextDescriptives/commit/976c050e8a4db19a5e60bbb0e5fa2db3e656537e))

* docs: minor additions to docs ([`a1cdd3b`](https://github.com/HLasse/TextDescriptives/commit/a1cdd3b166dfacec5524b1bd65de284e4a544bdb))

### Feature

* feat: add quality metrics to `Extractor` ([`92a70e8`](https://github.com/HLasse/TextDescriptives/commit/92a70e87f0a366b74a3a978139b89cc3fea65c60))

* feat: added quality estimation ([`347ac8d`](https://github.com/HLasse/TextDescriptives/commit/347ac8dc3e5fdc60ebe56c10c07bd6621d92b478))

### Fix

* fix: Fixed erros in test due by forcing the extension to be set. ([`b47d602`](https://github.com/HLasse/TextDescriptives/commit/b47d60273e6fa6d8c29b15a7860aabd3b9da2537))

### Refactor

* refactor: changed default of force to True ([`2aadd11`](https://github.com/HLasse/TextDescriptives/commit/2aadd118882e35f390d49dddb0e99a4501e49ebb))

* refactor: removed all but one set of defaults. ([`6231433`](https://github.com/HLasse/TextDescriptives/commit/6231433b011e4047cf86590d62270928300e6a4f))

### Style

* style: Added style to requirement.txt ([`9e2940d`](https://github.com/HLasse/TextDescriptives/commit/9e2940d7ceed68a45e641ab27f487e5c4a65ebd9))

### Test

* test: Added tests to quality filter ([`b70f850`](https://github.com/HLasse/TextDescriptives/commit/b70f85088f25437971a9c6bef6fe082675ed90f5))

### Unknown

* readme: fix table ([`836c4ca`](https://github.com/HLasse/TextDescriptives/commit/836c4ca5b9b82d752050b6da989a26e114085a13))

* Merge pull request #67 from HLasse/update-docs

docs: fix failing documentation ([`854b6f3`](https://github.com/HLasse/TextDescriptives/commit/854b6f36030515b567efd28f4d12b591b488ccca))

* Merge pull request #66 from HLasse/fix-ci

Update pytest-cov-comment.yml ([`25b05b7`](https://github.com/HLasse/TextDescriptives/commit/25b05b7be54ca1d600a86940e8c8732e81150766))

* Merge pull request #63 from HLasse/feature-add-quality

Feature: Add quality descriptives ([`b317cf0`](https://github.com/HLasse/TextDescriptives/commit/b317cf0199c08aa64cd719f74ae53467b8fb629c))

* Update pytest-cov-comment.yml

Fixes #65 ([`5629824`](https://github.com/HLasse/TextDescriptives/commit/5629824fdbd3759e56c2cc1e79cfb1bc07c3b5d0))

* Merge pull request #62 from HLasse/build-updated-for-3.10

build: update requirements for python 3.10 ([`4b9179f`](https://github.com/HLasse/TextDescriptives/commit/4b9179fb44a7ac9466116bbde88838168a1517c6))

* Update dependabot.yml ([`c5409fa`](https://github.com/HLasse/TextDescriptives/commit/c5409fa47c7c16c61a48ea280abe223e530406f4))


## v1.0.7 (2022-05-04)

### Chore

* chore: make black happy.. ([`4025065`](https://github.com/HLasse/TextDescriptives/commit/40250653cbf3c46f9daf45d103aa1723bef463cd))

### Fix

* fix: gistID ([`2a49cfb`](https://github.com/HLasse/TextDescriptives/commit/2a49cfb297edb0475fff26de6ca86d1f49172f13))

* fix: updated dep dists tests ([`73f4e48`](https://github.com/HLasse/TextDescriptives/commit/73f4e486abebb3364c120d971a9927be64f8aa76))

* fix: robust pos tests ([`1781a7e`](https://github.com/HLasse/TextDescriptives/commit/1781a7ed3eec27853334feef6715fb6655c955e7))

* fix: update spacy core sm to most recent ([`26e3921`](https://github.com/HLasse/TextDescriptives/commit/26e3921544e88688ab6c75670c4bde43d4f1b8b1))

### Unknown

* Merge pull request #48 from HLasse/update-version

update package version ([`04bb72c`](https://github.com/HLasse/TextDescriptives/commit/04bb72c929639b71474a95c9291803eabce0c4bb))

* update package version ([`3a121d8`](https://github.com/HLasse/TextDescriptives/commit/3a121d8c7f0ce7986fcdb9e4a10afeec6cebd639))

* Merge pull request #45 from HLasse/fix-pytest-cov

update pytest-coverage-comment ([`ec7cad2`](https://github.com/HLasse/TextDescriptives/commit/ec7cad2ef0ea824953f3c4eca9f8202a439fb510))

* Merge pull request #47 from HLasse/master

check tests ([`885236a`](https://github.com/HLasse/TextDescriptives/commit/885236a56cdac034bcf29a061a8587462997c8be))

* Merge pull request #46 from HLasse/update-spacy-model-download

update: more robust spacy model download ([`6f92725`](https://github.com/HLasse/TextDescriptives/commit/6f9272558ef1110fe189a55631b9b32706738e43))

* update: more robust spacy model download ([`31de553`](https://github.com/HLasse/TextDescriptives/commit/31de553c77340afa4a3edda78f8adf028e0f4267))

* update pytest-coverage-comment ([`da6d095`](https://github.com/HLasse/TextDescriptives/commit/da6d0958019a6076cfe33b99562d43d956619431))

* Merge pull request #41 from HLasse/dependabot/github_actions/schneegans/dynamic-badges-action-1.3.0

:arrow_up: Bump schneegans/dynamic-badges-action from 1.2.0 to 1.3.0 ([`c84219f`](https://github.com/HLasse/TextDescriptives/commit/c84219fb5cef498d42f88a3e6dc4031b1ca3a6d3))

* Merge pull request #39 from HLasse/dependabot/github_actions/actions/setup-python-3

:arrow_up: Bump actions/setup-python from 2 to 3 ([`033fe5b`](https://github.com/HLasse/TextDescriptives/commit/033fe5b29486f5d5bbfe2b45951681ff7e00aa22))

* Merge pull request #35 from HLasse/dependabot/pip/ftfy-gte-6.0.3-and-lt-6.2.0

:arrow_up: Update ftfy requirement from &lt;6.1.0,&gt;=6.0.3 to &gt;=6.0.3,&lt;6.2.0 ([`7429d18`](https://github.com/HLasse/TextDescriptives/commit/7429d188d25ea2d6eb736c55e6386d638e5df9f3))

* Merge pull request #34 from HLasse/add-black-wf

add: black workflow and format everything ([`11c4edb`](https://github.com/HLasse/TextDescriptives/commit/11c4edbc35b5b27776356fe7996e9ad645b8a211))

* Merge pull request #40 from HLasse/workflow-patch

Fixed error causing workflows to pass ([`fe2f27a`](https://github.com/HLasse/TextDescriptives/commit/fe2f27aa0a7077e5d5ecef4d6ef0496cdcacd174))

* :arrow_up: Bump schneegans/dynamic-badges-action from 1.2.0 to 1.3.0

Bumps [schneegans/dynamic-badges-action](https://github.com/schneegans/dynamic-badges-action) from 1.2.0 to 1.3.0.
- [Release notes](https://github.com/schneegans/dynamic-badges-action/releases)
- [Changelog](https://github.com/Schneegans/dynamic-badges-action/blob/master/changelog.md)
- [Commits](https://github.com/schneegans/dynamic-badges-action/compare/v1.2.0...v1.3.0)

---
updated-dependencies:
- dependency-name: schneegans/dynamic-badges-action
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`6ca4618`](https://github.com/HLasse/TextDescriptives/commit/6ca4618d60423a952629f81e7f851edb2335ddf0))

* Update pytest-cov-comment.yml ([`4f0d7bc`](https://github.com/HLasse/TextDescriptives/commit/4f0d7bcd22d78594d929ad10e64b5525d5d1612d))

* Update pytest-cov-comment.yml ([`956e773`](https://github.com/HLasse/TextDescriptives/commit/956e773b979f702ac8591b565c62c48f9369448a))

* Fixed error causing workflows to pass

fixed error causing workflows to pass even though tests fail caused by the purest not raising an error due to the tee. ([`2fea750`](https://github.com/HLasse/TextDescriptives/commit/2fea7505b123f0afd890f393ac357d3279bdfcf8))

* :arrow_up: Bump actions/setup-python from 2 to 3

Bumps [actions/setup-python](https://github.com/actions/setup-python) from 2 to 3.
- [Release notes](https://github.com/actions/setup-python/releases)
- [Commits](https://github.com/actions/setup-python/compare/v2...v3)

---
updated-dependencies:
- dependency-name: actions/setup-python
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`87b692b`](https://github.com/HLasse/TextDescriptives/commit/87b692b4047e4ea1e7dd586773b7f5dc50018780))

* :arrow_up: Update ftfy requirement from &lt;6.1.0,&gt;=6.0.3 to &gt;=6.0.3,&lt;6.2.0

Updates the requirements on [ftfy]() to permit the latest version.

---
updated-dependencies:
- dependency-name: ftfy
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`6182cd0`](https://github.com/HLasse/TextDescriptives/commit/6182cd052be5b80e3e6256ed91c6fedf6e8738ae))

* Merge branch &#39;master&#39; into add-black-wf ([`5966854`](https://github.com/HLasse/TextDescriptives/commit/5966854a620151d606253fd9255336819cde2278))

* add: black workflow and format everything ([`451090e`](https://github.com/HLasse/TextDescriptives/commit/451090e34a781c715290cd5730b178b9dede0eb9))

* Merge pull request #25 from HLasse/Update_setup

Updated setup ([`9bf044a`](https://github.com/HLasse/TextDescriptives/commit/9bf044a4a1a7cf094d5a2331b37f4f01fd006f90))

* Update pytest-cov-comment.yml

update dependencies ([`e9979ab`](https://github.com/HLasse/TextDescriptives/commit/e9979ab1803db52527d7ceb8f5690a8067cf35bf))

* Merge branch &#39;master&#39; into Update_setup ([`3ad0267`](https://github.com/HLasse/TextDescriptives/commit/3ad0267f3a2fde9a89c8fdf9f29d6a303fe33d62))

* Merge pull request #26 from HLasse/Add-dependabot-workflow

Added dependabot workflow ([`de0ba76`](https://github.com/HLasse/TextDescriptives/commit/de0ba76b56a9cc5a756a2f5dad7f2f84e6f4dbca))

* Merge pull request #27 from HLasse/clean-ci

updated ci workflow ([`29d0041`](https://github.com/HLasse/TextDescriptives/commit/29d0041fef649a39edd448f9b3918cfb565b40fb))

* Update .github/workflows/pytest-cov-comment.yml ([`e8739a0`](https://github.com/HLasse/TextDescriptives/commit/e8739a066e783e0a2228c295fbdab07a13b5a702))

* Merge pull request #30 from HLasse/fix-tests

fixes failing tests ([`294b6dd`](https://github.com/HLasse/TextDescriptives/commit/294b6ddd2970b09cf1de4b7a2ff5124f2fc44dfe))

* update: more wiggle room for dep dist tests ([`0e95ec5`](https://github.com/HLasse/TextDescriptives/commit/0e95ec548de4397e2adf97def309d2c59c5e3b77))

* update: more wiggle room for pos tests ([`74650ba`](https://github.com/HLasse/TextDescriptives/commit/74650ba2d6c67f97ab5c27f3ccb9b5ac12489a8c))

* Update README.md ([`a597dbb`](https://github.com/HLasse/TextDescriptives/commit/a597dbbb67913d84ac688a3faa1edd24f25f8d2d))

* updated ci workflow ([`90f97b2`](https://github.com/HLasse/TextDescriptives/commit/90f97b2a152d15c20ca4bc2244495e779b15fb51))

* Added dependabot workflow ([`40810de`](https://github.com/HLasse/TextDescriptives/commit/40810defa8f3886901e3a364cb298e4e7b76352b))

* Updated setup ([`06fb4f7`](https://github.com/HLasse/TextDescriptives/commit/06fb4f74112fd3cf682b99dff93fce21ae716743))


## v1.0.6 (2021-10-28)

### Unknown

* updated version given recent bug fix ([`e0be97c`](https://github.com/HLasse/TextDescriptives/commit/e0be97cbabc163939666226ece9419bca77eb26c))

* Merge pull request #19 from frillecode/patch-1

Fixed to work with attribute ruler ([`bbfe011`](https://github.com/HLasse/TextDescriptives/commit/bbfe011034cce116d9d1c486b25a84e02818a0c6))

* Fixed to work with attribute ruler

The pipeline does not work for e.g. the Danish pipeline which use an attribute ruler (as opposed to a tagger) for assigning POS-tags. Maybe it is worth removing this restriction all together assuming other things could also set the POS tag. Instead check for whether the document is POS tagged using the `has_annotation`.

Frida and Kenneth ([`7862cbf`](https://github.com/HLasse/TextDescriptives/commit/7862cbf706c4f6585fe6f5dd179be4163f1f6764))

* minor fix ([`6606e90`](https://github.com/HLasse/TextDescriptives/commit/6606e90358d40bf5530ae5862d4a01f49a300c65))

* Merge pull request #18 from HLasse/missing_word

Added missing word ([`342c8be`](https://github.com/HLasse/TextDescriptives/commit/342c8be0f27c4aa15bb335dad4a0ed41eee4c901))

* Added type hint ([`89ced1b`](https://github.com/HLasse/TextDescriptives/commit/89ced1b9fa24f059fcf2db037ed8c6f710de7f57))

* Added missing word ([`6965875`](https://github.com/HLasse/TextDescriptives/commit/696587516365ae59173175cae7ce3ff633c24f7e))

* Update README.md ([`d4e359c`](https://github.com/HLasse/TextDescriptives/commit/d4e359cfe9cf3b7ed57ab617f56c8de2abae18d7))

* add news ([`dbf5975`](https://github.com/HLasse/TextDescriptives/commit/dbf597538e00bb38713c623a2ce1abff7726a981))

* change default behaviour of pos_stats ([`b1129d2`](https://github.com/HLasse/TextDescriptives/commit/b1129d2ad85224ba7dd6dcfa95a23d9c124c8d6e))

* Merge pull request #16 from HLasse/minor-patch-1

Added references and changed pos-stats to part-of-speech stats ([`57c7b68`](https://github.com/HLasse/TextDescriptives/commit/57c7b68b41235b4b47dda18eff5476503648405c))

* added code elements ([`eab14b4`](https://github.com/HLasse/TextDescriptives/commit/eab14b4781b3eb2efff956b7b918157b98d92b46))

* added references ([`e180f07`](https://github.com/HLasse/TextDescriptives/commit/e180f073834d733239691612b751a423ad069721))

* Update posstats.rst ([`c50e4b7`](https://github.com/HLasse/TextDescriptives/commit/c50e4b75106f22ab3ccd3f12ea07673999b7f1b0))

* Merge pull request #14 from martbern/master

Add Span support to pos_proportions ([`fdebbeb`](https://github.com/HLasse/TextDescriptives/commit/fdebbebc2453c333ea87290e8797870ac4a77f1e))

* Avoid redefining built-in &#34;input&#34; ([`068a3a7`](https://github.com/HLasse/TextDescriptives/commit/068a3a7e75b08526f941ae2bae6a6f9abc5c8e62))

* Update documentation ([`9515753`](https://github.com/HLasse/TextDescriptives/commit/9515753be6f4b6a428370c5691576422577e662a))

* Sync with main repo ([`c639bb1`](https://github.com/HLasse/TextDescriptives/commit/c639bb1e94a8faa5e4c7b129f56654e6bf670379))

* Add support for series ([`ea54a46`](https://github.com/HLasse/TextDescriptives/commit/ea54a462ada7b1e98d36702d7790da45a8639d54))

* Merge pull request #11 from HLasse/numpy_version

change numpy requirement ([`66d2360`](https://github.com/HLasse/TextDescriptives/commit/66d23601908e488652691b3a387989377e9ae65a))

* change numpy requirement ([`30a2f69`](https://github.com/HLasse/TextDescriptives/commit/30a2f69f748137aad9664e526040c14e2aefee8d))

* Merge pull request #9 from HLasse/posstatistics

Add documentation for pos_stats ([`adad7e0`](https://github.com/HLasse/TextDescriptives/commit/adad7e0f02f894f59abacee5b4235021b0a0ca00))

* raise error if no tagger with pos_stats, fix tests ([`554c539`](https://github.com/HLasse/TextDescriptives/commit/554c539dedcd8740e3a692495998c4f5b21bc77e))

* Merge pull request #8 from martbern/posstatistics

Add documentation for pos_stats ([`adecfc1`](https://github.com/HLasse/TextDescriptives/commit/adecfc1f2bef61204acae5c9d6b3d3672c9af88f))

* Update README.md ([`72cff9c`](https://github.com/HLasse/TextDescriptives/commit/72cff9c62af2cd253442d57eb35ce9f88050c5f9))

* Add documentation for pos_stats ([`578a7b3`](https://github.com/HLasse/TextDescriptives/commit/578a7b349fd0abd9cb9d71e28aa48ea6b748bb94))

* Delete test.py ([`2d2c8c8`](https://github.com/HLasse/TextDescriptives/commit/2d2c8c8c2c18a3e6e50f495e581ab3eed3a0aa84))

* Add documentation for pos_stats ([`7b1c8dc`](https://github.com/HLasse/TextDescriptives/commit/7b1c8dcf44861fa3b53dfa81fca784da3a346c45))

* bump version ([`8c27773`](https://github.com/HLasse/TextDescriptives/commit/8c277737de258544b3eba464068626bac4e47b20))

* Merge pull request #7 from HLasse/master

master to posstatistics ([`64f9f17`](https://github.com/HLasse/TextDescriptives/commit/64f9f17184047becd7fe95735054edbfc1a0de2e))

* suggested changes ([`555f091`](https://github.com/HLasse/TextDescriptives/commit/555f0915121ee63176f4423eda8819e048ffcf46))

* Move pos_proportions into new pos_stats component and add tests ([`b6f872d`](https://github.com/HLasse/TextDescriptives/commit/b6f872d234c38d567648a190cb076ceddc26fa26))

* Apply suggestions from code review

Make PR more pythonic

Co-authored-by: HLasse &lt;lasseh0310@gmail.com&gt; ([`efc7fbf`](https://github.com/HLasse/TextDescriptives/commit/efc7fbf3151fc447daa551590a148ee3b031e0c8))

* Add pos_proportions and attempt at test ([`6da3dd1`](https://github.com/HLasse/TextDescriptives/commit/6da3dd1d992db5f13a903fb569ee07bb7792e4b4))

* Add docstring to DescriptiveStatistics.counts ([`ab40f1c`](https://github.com/HLasse/TextDescriptives/commit/ab40f1c579267583ac8210e9250ba7146125c194))

* bump version to 1.0.3 

adds `extract_dict` ([`d4b818e`](https://github.com/HLasse/TextDescriptives/commit/d4b818eb175b484ed95c0965e33d658a7b8f2270))

* Merge pull request #5 from HLasse/dev

add extract_dict function ([`70f1494`](https://github.com/HLasse/TextDescriptives/commit/70f14943c7d077cf7f6fbd036c6e92ff261572c4))

* Merge branch &#39;dev&#39; of https://github.com/HLasse/TextDescriptives into dev ([`a72ab59`](https://github.com/HLasse/TextDescriptives/commit/a72ab59c63fe94fdcaaf4f69e17b559e4bcd7ed7))

* fix subsetter test ([`24afa64`](https://github.com/HLasse/TextDescriptives/commit/24afa64b1c27c53445a362cd029c1e0d04faf338))

* Apply suggestions from code review

Co-authored-by: Kenneth Enevoldsen &lt;kennethcenevoldsen@gmail.com&gt; ([`e8b2fe4`](https://github.com/HLasse/TextDescriptives/commit/e8b2fe4a630b7451c370eb32ee58bc6b2cf297d4))

* minor ([`7792895`](https://github.com/HLasse/TextDescriptives/commit/77928957986d2c0eb541d683f57fdf21292f6ab7))

* add extract_dict function ([`cb22a22`](https://github.com/HLasse/TextDescriptives/commit/cb22a22f84fcbe1ffbdc95a399217d54c154bb50))

* Update about.py ([`a7ad3d6`](https://github.com/HLasse/TextDescriptives/commit/a7ad3d65b96227831fd941a33713d756a88ad346))

* Update setup.py ([`70d6c26`](https://github.com/HLasse/TextDescriptives/commit/70d6c263d9f767692fa5f230e0660b452067e48b))

* Update README.md ([`50282be`](https://github.com/HLasse/TextDescriptives/commit/50282be837523de7bcb9ee24f3ca3639bb5339c4))

* minor ([`c77c98e`](https://github.com/HLasse/TextDescriptives/commit/c77c98ec7226e98150d809ca7b4db4ac88d2a558))

* minor formatting ([`89ce874`](https://github.com/HLasse/TextDescriptives/commit/89ce87476299e75491d2401521fc70eb1649c050))


## v1.0.1 (2021-08-09)

### Unknown

* add link to docs in readme ([`d9cdff7`](https://github.com/HLasse/TextDescriptives/commit/d9cdff71767cec2bf911cc631f92f4c04e88e524))

* bump to version 1.0.0 ([`d7be7c3`](https://github.com/HLasse/TextDescriptives/commit/d7be7c36f2e98af41d6ac7c18639ac6cdb737425))

* fix setup typo ([`0d5bd30`](https://github.com/HLasse/TextDescriptives/commit/0d5bd302cb12036311216a1a2eb535cf05780500))

* fix datahint and setup typo ([`ce36172`](https://github.com/HLasse/TextDescriptives/commit/ce3617283da9af5a9f3544e0737f549d13b3ae79))

* fix spacy model version ([`f0ed4d2`](https://github.com/HLasse/TextDescriptives/commit/f0ed4d2ffec77c86d74149c5ee452f7d541fa584))

* update tests to use en_core_web_sm v3.1.0 ([`ae291a3`](https://github.com/HLasse/TextDescriptives/commit/ae291a3287a34d017eba1d359fc94970ca2b668b))

* fix type hint and add spacy mode to req for tests ([`c235aa7`](https://github.com/HLasse/TextDescriptives/commit/c235aa78671bb566f234b383e44d8ed81bd5d350))

* fix workflow branch ([`7d23b3d`](https://github.com/HLasse/TextDescriptives/commit/7d23b3d7f8448eb3b42f3fb5bf2d123b6ef2ac3b))

* fix test ([`5ec7a84`](https://github.com/HLasse/TextDescriptives/commit/5ec7a8406ee3eb7e9793e9d772632efea37cebf0))

* Merge pull request #2 from HLasse/spacy_v

complete remake to use spaCy - stanza version deprecated (but saved as release and on stanza-version branch) ([`d62985c`](https://github.com/HLasse/TextDescriptives/commit/d62985c89688db928fe9c91832aba14666ec5020))

* Merge branch &#39;spacy_v&#39; of https://github.com/HLasse/TextDescriptives into spacy_v ([`758dc0f`](https://github.com/HLasse/TextDescriptives/commit/758dc0f749874f6781c776c89a510f34d1d81e63))

* minor changes and rename extractor ([`752fe30`](https://github.com/HLasse/TextDescriptives/commit/752fe30661d8671fdd9a1bdb2ad98406bd9f725b))

* Update docs/index.rst

Co-authored-by: Kenneth Enevoldsen &lt;kennethcenevoldsen@gmail.com&gt; ([`cd419e1`](https://github.com/HLasse/TextDescriptives/commit/cd419e134f7e48df60177340a7f48cd2836a3158))

* Update conf.py ([`d33d129`](https://github.com/HLasse/TextDescriptives/commit/d33d129854043d64289844388f717cc5a18dc1dc))

* Update pytest-cov-comment.yml ([`db59fb8`](https://github.com/HLasse/TextDescriptives/commit/db59fb8018bdce166be613e018a7586242f353e2))

* Update pytest-cov-comment.yml ([`401dbfc`](https://github.com/HLasse/TextDescriptives/commit/401dbfcc9c84142866613d6cf7f84f81c30d672f))

* Update docs/index.rst

Co-authored-by: Kenneth Enevoldsen &lt;kennethcenevoldsen@gmail.com&gt; ([`a5cb105`](https://github.com/HLasse/TextDescriptives/commit/a5cb105e2a7db533593e4d1264ecdd6f284921f7))

* Update README.md ([`c067bde`](https://github.com/HLasse/TextDescriptives/commit/c067bde3408cc0cadc5d1032bf38e2d3970b1a61))

* Update README.md ([`8cca8a3`](https://github.com/HLasse/TextDescriptives/commit/8cca8a3b8638ff9d658568bcf494b040d227a11e))

* update docs ([`98a8aa8`](https://github.com/HLasse/TextDescriptives/commit/98a8aa81ea1dd722df2a43866d3be6e06bea6673))

* Merge pull request #4 from HLasse/pypi_integration

add pypi integration to spacy version ([`de8a92f`](https://github.com/HLasse/TextDescriptives/commit/de8a92fb93e0f26e525d845cfe04cc213c375d30))

* Merge branch &#39;spacy_v&#39; into pypi_integration ([`6243a83`](https://github.com/HLasse/TextDescriptives/commit/6243a8364afad560bf0199a807330cfe1430b6bc))

* Update docs/installation.rst

Co-authored-by: HLasse &lt;lasseh0310@gmail.com&gt; ([`cf1278e`](https://github.com/HLasse/TextDescriptives/commit/cf1278e1f68c94e150d55f92729d588308f85e69))

* Update docs/installation.rst

Co-authored-by: HLasse &lt;lasseh0310@gmail.com&gt; ([`8726a4d`](https://github.com/HLasse/TextDescriptives/commit/8726a4d8a196c9a46f29a5f75c29f172c9cddcba))

* Update docs/conf.py

Co-authored-by: HLasse &lt;lasseh0310@gmail.com&gt; ([`e78d7b6`](https://github.com/HLasse/TextDescriptives/commit/e78d7b66dd89a850b57e6e828efa2718f823fe8f))

* Update docs/conf.py

Co-authored-by: HLasse &lt;lasseh0310@gmail.com&gt; ([`1af522f`](https://github.com/HLasse/TextDescriptives/commit/1af522f380ef287bf646ed14afd2f0b744f4b219))

* docs ([`b5ae477`](https://github.com/HLasse/TextDescriptives/commit/b5ae47748240167dd0067d903e53a5483e310a35))

* couple more extractor tests ([`5d72b99`](https://github.com/HLasse/TextDescriptives/commit/5d72b990a73df21927050ec35e75940b1174d933))

* Delete robustness.rst ([`2e12410`](https://github.com/HLasse/TextDescriptives/commit/2e12410a58ec9a193f8c3ebd7f9da2512080d15c))

* add tests, minor fixes ([`48e1b3c`](https://github.com/HLasse/TextDescriptives/commit/48e1b3c10888a85e8e5b1c22085167180da117d4))

* update readme and minor updates ([`483c86e`](https://github.com/HLasse/TextDescriptives/commit/483c86e14d4ac876ed8c7cd4be2ffe2f732d537f))

* update readme ([`100b7a8`](https://github.com/HLasse/TextDescriptives/commit/100b7a805d98625d93915da9d7e0a85ce3d24e53))

* minor setup changes ([`2e63cbd`](https://github.com/HLasse/TextDescriptives/commit/2e63cbddb2404b6d931adba1fdeb3a646a69635f))

* add pipe loader ([`43f3a5b`](https://github.com/HLasse/TextDescriptives/commit/43f3a5b17edd05ad314e855c6c0d6e43164bba5f))

* add span and token attributes ([`1cf1527`](https://github.com/HLasse/TextDescriptives/commit/1cf1527da169f32c58a7d868b0f66572d4e55ae0))

* Merge branch &#39;spacy_v&#39; of https://github.com/HLasse/TextDescriptives into spacy_v ([`88299f8`](https://github.com/HLasse/TextDescriptives/commit/88299f89aebd7714a589dab98e8272535a51633c))

* add token and span level dep distance, rm pandas ([`b1630ea`](https://github.com/HLasse/TextDescriptives/commit/b1630ea4099c3c3990c080d4aac00b87e0426528))

* Update textdescriptives/extractor.py

Co-authored-by: Kenneth Enevoldsen &lt;kennethcenevoldsen@gmail.com&gt; ([`ab70ee7`](https://github.com/HLasse/TextDescriptives/commit/ab70ee71747a5d394454343cd2314368cc37714d))

* Update textdescriptives/components/descriptive_stats.py

Co-authored-by: Kenneth Enevoldsen &lt;kennethcenevoldsen@gmail.com&gt; ([`4bc7c27`](https://github.com/HLasse/TextDescriptives/commit/4bc7c271a6b2ce15e82ff29416986382e1f81821))

* added CI for pytest and coverage ([`9baf1fc`](https://github.com/HLasse/TextDescriptives/commit/9baf1fc37eae961d57b9ee406fd484f02de0f72e))

* cleaned gitignore ([`499aad5`](https://github.com/HLasse/TextDescriptives/commit/499aad52920cabb5ab71c78b27879b9f276606dc))

* added documentation files ([`2ff1c5e`](https://github.com/HLasse/TextDescriptives/commit/2ff1c5e8c32260896122cceec04263f5e2d9d8b5))

* added custom issues ([`7d43105`](https://github.com/HLasse/TextDescriptives/commit/7d4310553adfff9c7b469182be3b1f83c648e694))

* added wf to publish to pypi ([`bea5b62`](https://github.com/HLasse/TextDescriptives/commit/bea5b6275ca90c3d4952b3d5f8e81849a131dfe9))

* update readme to spacy version ([`b11223b`](https://github.com/HLasse/TextDescriptives/commit/b11223ba8b0f6f3c99d5830916ccb012ab6924bc))

* remove old ([`92a7b93`](https://github.com/HLasse/TextDescriptives/commit/92a7b939d7669aacc968edb7a165156d2a50b3ee))

* Merge remote-tracking branch &#39;spacy-textdescriptives/main&#39; into spacy_v ([`fde613e`](https://github.com/HLasse/TextDescriptives/commit/fde613ea297d1d7fd9ea284ad30910497e7bbf95))

* clean up ([`c079c66`](https://github.com/HLasse/TextDescriptives/commit/c079c6617ef266b54f28c51e619d2429a5dafb83))

* add readability and extractor ([`5564280`](https://github.com/HLasse/TextDescriptives/commit/55642807e8961ef36d1f6ddbe10a7021413a10c3))

* add dependency distance ([`7ad95eb`](https://github.com/HLasse/TextDescriptives/commit/7ad95ebd47309318f6c89c6b223b5faf7af21d3f))

* add utils and desc stats ([`6fdcd3b`](https://github.com/HLasse/TextDescriptives/commit/6fdcd3b324ecf9d3908dc29376f636c440a60f17))

* Initial commit ([`4c25726`](https://github.com/HLasse/TextDescriptives/commit/4c257268dd5cc5c84bbb86c07f79a7ddef98d4c6))

* Update README.md ([`6494fe9`](https://github.com/HLasse/TextDescriptives/commit/6494fe94d952c545fffa5834a7294f57df170233))

* Update README.md ([`adddda8`](https://github.com/HLasse/TextDescriptives/commit/adddda8c08b2838917e96b00b5ef1d2ea7b643cb))

* Update README.md ([`8c3f5a1`](https://github.com/HLasse/TextDescriptives/commit/8c3f5a1a46f1f36b922d3ecd0bca358df3176565))

* Update README.md ([`f08a6f4`](https://github.com/HLasse/TextDescriptives/commit/f08a6f472d2aa511bc5a7ca1b1ee94983e6d580b))

* Update README.md ([`0579397`](https://github.com/HLasse/TextDescriptives/commit/05793972dfc15f8c1c7e0bc8c8c3fa0d3d1c39d3))

* Update README.md ([`8bdeba3`](https://github.com/HLasse/TextDescriptives/commit/8bdeba36766bc8c9b611d6dfa58a44e0eac52b65))

* update stanza model_dir ([`f75f7fc`](https://github.com/HLasse/TextDescriptives/commit/f75f7fcbb2d5dfd323e1f238967f2a535ac8f7d2))

* .. ([`ba5ed6e`](https://github.com/HLasse/TextDescriptives/commit/ba5ed6ec14ee6979343f842fe33d16abda6414a3))

* fix typo ([`7711d9e`](https://github.com/HLasse/TextDescriptives/commit/7711d9ec0c29d0c5c04c418cc770926a0f392315))

* Merge branch &#39;dev_ludvig&#39; ([`40b805d`](https://github.com/HLasse/TextDescriptives/commit/40b805d1098c72bdff0d8fb84ecf4522cf263b2b))

* Get processors from global s_nlp pipeline ([`8c5a048`](https://github.com/HLasse/TextDescriptives/commit/8c5a04818ea564e8fef116f4017067b7022423cf))

* Merge branch &#39;dev_ludvig&#39; ([`be6a6f2`](https://github.com/HLasse/TextDescriptives/commit/be6a6f28e7989cfd3a52d0a03d1c9d0027231180))

* Better loading of stanza pipeline

Only uses already loaded pipeline if settings match those we wish to use ([`c7f1064`](https://github.com/HLasse/TextDescriptives/commit/c7f10640da6bcac59fb82fb933a31b4a84d163a0))

* Merge branch &#39;master&#39; into dev_ludvig ([`b51f143`](https://github.com/HLasse/TextDescriptives/commit/b51f14318cdad2337b2eef8b764b7e2357af48ed))

* adds news section ([`7725eac`](https://github.com/HLasse/TextDescriptives/commit/7725eac59c3a9d2f7ba8c46aa6719aa8342d6e1e))

* author section ([`8c7b1dc`](https://github.com/HLasse/TextDescriptives/commit/8c7b1dc0f40aa05aedb7444209a8daaa5cf4784d))

* minor ([`6a09daa`](https://github.com/HLasse/TextDescriptives/commit/6a09daa54b7fc800d9d2e5896d7ca364b3f00b0d))

* Merge branch &#39;dev_ludvig&#39; ([`0d7ee70`](https://github.com/HLasse/TextDescriptives/commit/0d7ee70909e71ec5763ca415e762f79834e9e303))

* minor ([`9dbdc05`](https://github.com/HLasse/TextDescriptives/commit/9dbdc0510e86179d8e542e5068022ccd58b1d73d))

* Merge branch &#39;dev_ludvig&#39; ([`872ac88`](https://github.com/HLasse/TextDescriptives/commit/872ac88536594b907e132fa6b17a183f92073b27))

* minor ([`eb95c10`](https://github.com/HLasse/TextDescriptives/commit/eb95c10e7f6766a19ff64a34c409fcc931629f33))

* rename governor to head ([`9b6bdd1`](https://github.com/HLasse/TextDescriptives/commit/9b6bdd1403d4178f9c15d49d32fbe62b92709840))

* Now uses stanza instead of stanfordnlp ([`f097515`](https://github.com/HLasse/TextDescriptives/commit/f097515ed3f94ee98272757a9785578baba00b8d))

* stanza_resources ([`0775770`](https://github.com/HLasse/TextDescriptives/commit/0775770d58eb0572fafa9fc62cd423701596c248))

* Merge branch &#39;master&#39; into dev_ludvig ([`23c7393`](https://github.com/HLasse/TextDescriptives/commit/23c7393880b8db5c04ef6b713f604bfd32f56ca4))

* minor ([`cd1880d`](https://github.com/HLasse/TextDescriptives/commit/cd1880d9f3540c66c38247c0bd9b928d2dcd0dec))

* Merge branch &#39;dev_ludvig&#39; ([`0aca4b4`](https://github.com/HLasse/TextDescriptives/commit/0aca4b46daa4cdc5df31052c9b846ce20cc0ca42))

* readability uses Text class. Moves lix and rix. Renames calculator ([`f9293fd`](https://github.com/HLasse/TextDescriptives/commit/f9293fd55aafc824fedccfdd61c65375735ec92f))

* Merge branch &#39;master&#39; into dev_ludvig ([`951c5ce`](https://github.com/HLasse/TextDescriptives/commit/951c5ceee41691670f21f9353b07d0223a851887))

* Calculators uses Text class. Simplifies basics() method. ([`8d68d86`](https://github.com/HLasse/TextDescriptives/commit/8d68d86492b7b8950fa2ad624935d72df3793184))

* Adds Text class for storing different version of a text

Allows us not to repeat the tokenization w/m. ([`63cb161`](https://github.com/HLasse/TextDescriptives/commit/63cb1613b9d926b2d5ac27c01f954715f148a228))

* rename word_id to token_id ([`94ec805`](https://github.com/HLasse/TextDescriptives/commit/94ec80576bc15f7216e4148cc807407739769e7d))

* Merge branch &#39;dev_ludvig&#39; ([`a70de99`](https://github.com/HLasse/TextDescriptives/commit/a70de99d2024028a8817c4ba41b2c1c3c3336431))

* minor cleanup ([`0c62b18`](https://github.com/HLasse/TextDescriptives/commit/0c62b18cc89cba4fc7ee5d38e0042e9453130d7d))

* Add getter methods ([`0d5dc18`](https://github.com/HLasse/TextDescriptives/commit/0d5dc184ac0a7be2439570bca42c1619410685c7))

* minor ([`370769f`](https://github.com/HLasse/TextDescriptives/commit/370769f05d14825d71a11d86c609f10c0a4a4af8))

* Rewrite to use pandas ([`d62babe`](https://github.com/HLasse/TextDescriptives/commit/d62babe28d549c3c284e1b24ab9982453cb08a01))

* Update README.md ([`bb7fca4`](https://github.com/HLasse/TextDescriptives/commit/bb7fca44ebf5f00cc4e78f564643161b08d31ae1))

* Update README.md ([`02e1d6b`](https://github.com/HLasse/TextDescriptives/commit/02e1d6bcd0cd78a69f08ad07b1f067dda77e5fe3))

* Update README.md ([`426a28b`](https://github.com/HLasse/TextDescriptives/commit/426a28babbf36a4e727885cd9c8358d3ca538482))

* Update README.md ([`c75e9af`](https://github.com/HLasse/TextDescriptives/commit/c75e9af2a2ffb76d61d32e26e0b3e4753e18d7b6))

* Update README.md ([`8e874b6`](https://github.com/HLasse/TextDescriptives/commit/8e874b61f6251df1de17176a44424123a128e7ec))

* lix/rix to readability + option for mean only ([`39a6e00`](https://github.com/HLasse/TextDescriptives/commit/39a6e00ce63c5a195b791ef0aaadcc89c52fad3e))

* Merge branch &#39;master&#39; of https://github.com/HLasse/TextDescriptives ([`4ce1348`](https://github.com/HLasse/TextDescriptives/commit/4ce134831f70bfbde5104b7a211d17edfd70b77e))

* function based ([`53cfd54`](https://github.com/HLasse/TextDescriptives/commit/53cfd54d31c61b46c6e06defd74ba6aa3053dd76))

* Update README.md ([`57a2ce1`](https://github.com/HLasse/TextDescriptives/commit/57a2ce1c491e383c3987470ecfe60205db9d0ef4))

* Update README.md ([`5ac1d1e`](https://github.com/HLasse/TextDescriptives/commit/5ac1d1e5a4f65867c939a177ff4761b9651dfbbd))

* Update README.md ([`dd9f2a2`](https://github.com/HLasse/TextDescriptives/commit/dd9f2a21c9748793bbbcad0169851a0db6012d1a))

* Update README.md ([`83f436c`](https://github.com/HLasse/TextDescriptives/commit/83f436cfb83de66416dac5a7ee7420b1e362e445))

* Merge branch &#39;master&#39; of https://github.com/HLasse/TextDescriptives ([`a2c646d`](https://github.com/HLasse/TextDescriptives/commit/a2c646d1e05dbef6154ff4b71124ac88026383f9))

* fix pip install ([`76e696a`](https://github.com/HLasse/TextDescriptives/commit/76e696aae31840bc514e436ea799809db5d714b8))

* add manifest ([`25ffb1f`](https://github.com/HLasse/TextDescriptives/commit/25ffb1ff131818ddaf80d44c0455c9a0f1425422))

* Update README.md ([`158013e`](https://github.com/HLasse/TextDescriptives/commit/158013e749a67c31f22dd8c50ba647558cbd407f))

* Merge pull request #1 from HLasse/add-license-1

Create LICENSE ([`d24006d`](https://github.com/HLasse/TextDescriptives/commit/d24006d9ab5f8957b7d5d24c09f5bd96ea3a9e34))

* Create LICENSE ([`dfa1ac3`](https://github.com/HLasse/TextDescriptives/commit/dfa1ac377e209ea6da482eead6816255e5a262b0))

* Update README.md ([`0172be0`](https://github.com/HLasse/TextDescriptives/commit/0172be0b1426c763b3fc56a6d0e85d89e1747720))

* Update README.md ([`a02156e`](https://github.com/HLasse/TextDescriptives/commit/a02156e203c155d089a10db93c181397ccfb7d26))

* Merge branch &#39;master&#39; of https://github.com/HLasse/TextDescriptives ([`58738bf`](https://github.com/HLasse/TextDescriptives/commit/58738bf9fa824796fefeff7cbd973ae689fa6e6d))

* fix pip install ([`a133abf`](https://github.com/HLasse/TextDescriptives/commit/a133abfffbd4e665e1e92c55600c4b068d8eea56))

* Update README.md ([`8f2e4f2`](https://github.com/HLasse/TextDescriptives/commit/8f2e4f2822b0fbaf636cab82b6b11a577a927a8d))

* Update README.md ([`6b107f2`](https://github.com/HLasse/TextDescriptives/commit/6b107f264b5829de9c60f0351a3320bd8665d007))

* Update README.md ([`5e734fc`](https://github.com/HLasse/TextDescriptives/commit/5e734fca67690b7e34dfc17eddb9631cf9481a53))

* Update README.md ([`299bf00`](https://github.com/HLasse/TextDescriptives/commit/299bf00f211d74b9919d68258d671e793e2e8be0))

* Update README.md ([`af6c584`](https://github.com/HLasse/TextDescriptives/commit/af6c584e99e43da7ac442d1a90346a4e38844e3a))

* Delete __init__.cpython-37.pyc ([`78dbc6b`](https://github.com/HLasse/TextDescriptives/commit/78dbc6b35f1d5c38ed432414dd03ed5c4e09ea72))

* Delete settings.json ([`acbe80d`](https://github.com/HLasse/TextDescriptives/commit/acbe80d1eec7f68574e98e28f2e136bad3c4f347))

* can be pip installed ([`40c1909`](https://github.com/HLasse/TextDescriptives/commit/40c19097aba72642c30ac9b0848995cb340bae50))

* move stuff around ([`69226a9`](https://github.com/HLasse/TextDescriptives/commit/69226a9226f475ace4ffd6461d8e6dd95515b1cc))

* add dependency distance ([`77f61e8`](https://github.com/HLasse/TextDescriptives/commit/77f61e81458cb3b963ad44148fad21906bd3bafb))

* Add etymology ([`bdc9f3d`](https://github.com/HLasse/TextDescriptives/commit/bdc9f3daa47136fee55fcc0ca5293fd60b722b99))

* Initial commit ([`5f6b3f6`](https://github.com/HLasse/TextDescriptives/commit/5f6b3f6d3acb117cd3ec0ab9873157d3c1860b14))

* Initial commit ([`9f0c245`](https://github.com/HLasse/TextDescriptives/commit/9f0c2457d65a9acc8389fac44f865ca3118eb4b2))
