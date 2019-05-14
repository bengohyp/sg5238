.PHONY: help
help: Makefile
	@echo "possible make targets: ";
	@ sed -n 's/^##//p' $<

## make run - runs the emotion-detection program
.PHONY: run
run:
	@echo "\nmaking run";
	python3 emotion-detection.py;
## make test-run - runs the emotion-detection program without an ncs stick
.PHONY: test-run
test-run:
	@echo "\nmaking run with no ncs";
	python3 emotion-detection.py -t True;
## make test-ncs - runs the test program to check for presence of ncs stick
.PHONY: test-ncs
test-ncs:
	@echo "\nmaking test";
	python3 test.py;