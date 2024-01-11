.PHONY: update-protocol

update-protocol:
	@if [ -d "../agent-protocol/sdk/python/agent_protocol" ]; then \
		cp -r ../agent-protocol/sdk/python/agent_protocol startgpt; \
		rm -Rf startgpt/agent_protocol/utils; \
		rm -Rf startgpt/agent_protocol/cli.py; \
		echo "Protocol updated successfully!"; \
	else \
		echo "Error: Source directory ../agent-protocol/sdk/python/agent_protocol does not exist."; \
		exit 1; \
	fi

change-protocol:
	@if [ -d "startgpt/agent_protocol" ]; then \
		cp -r startgpt/agent_protocol ../agent-protocol/sdk/python; \
		rm ../agent-protocol/sdk/python/agent_protocol/README.md; \
		echo "Protocol reversed successfully!"; \
	else \
		echo "Error: Target directory startgpt/agent_protocol does not exist."; \
		exit 1; \
	fi
