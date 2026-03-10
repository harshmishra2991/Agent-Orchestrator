from agents.parser import parser
from agents.validator import validator
from agents.providers import provider_a, provider_b, provider_c
from agents.aggregator import aggregator
from agents.formatter import formatter
from orchestrator.orchestrator import Orchestrator

context = {"user_input": "book me a flight to paris on friday"}

steps = [
    parser,
    validator,
    [provider_a, provider_b, provider_c],  # parallel stage
    aggregator,
    formatter
]

orch = Orchestrator(steps)

result = orch.run(context)

print(result["message"])
print(result["trace"])