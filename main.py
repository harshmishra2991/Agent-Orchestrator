from agents.parser import parser
from agents.validator import validator
from orchestrator.orchestrator import Orchestrator
context = {"user_input" : "book me a flight to paris on friday"}

steps = [parser, validator]
orch = Orchestrator(steps)

print(orch.run(context))

