all: test

deps: should-dsl specloud

should-dsl:
	@python -c 'import should_dsl' 2>/dev/null || pip install http://github.com/hugobr/should-dsl/tarball/master

specloud:
	@python -c 'import specloud' 2>/dev/null || pip install specloud --no-deps -r http://github.com/hugobr/specloud/raw/master/requirements.txt

test: deps
	@echo ==============================================
	@echo ============ Running unit specs ==============
	@specloud calve_machine/spec
	@echo

