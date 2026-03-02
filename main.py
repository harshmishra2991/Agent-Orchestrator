from agents.parser import parser
from agents.validator import validator
from orchestrator.orchestrator import Orchestrator
from agents.providers import provider_a, provider_b, provider_c
from agents.aggregator import aggregator
# context = {"user_input" : "book me a flight to paris on friday"}

# providers = [provider_a, provider_b, provider_c]


# steps = [parser, validator]


# orch = Orchestrator(steps)

# parallel_results = orch.run_parallel(providers, context, timeout= 3)
# print("final results:")
# print(parallel_results)


mock_context = {
    "provider_results": [
        {"status": "success", "provider": "provider_a", "price": 450, "reason": None},
        {"status": "success", "provider": "provider_b", "price": 400, "reason": None},
        {"status": "failure", "provider": "provider_c", "price": None, "reason": "timeout"}
    ]
}

result = aggregator(mock_context)
print(result)




