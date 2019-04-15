


.PHONY: run
run:
	@echo "\nmaking run";
	python3 emotion-detection.py;

.PHONY: test-run
test-run:
	@echo "\nmaking run with no ncs";
	python3 emotion-detection.py -t True;

.PHONY: test-ncs
test-ncs:
	@echo "\nmaking test";
	python3 test.py;

.PHONY: help
help:
	@echo "possible make targets: ";
	@echo "  make help - shows this message";
	@echo "  make run - runs the emotion-detection program";
	@echo "  make test-run - runs the emotion-detection program without an ncs stick";
	@echo "  make test-ncs - runs the test program to check for presence of ncs stick";
