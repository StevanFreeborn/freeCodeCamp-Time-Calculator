# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

print(add_time("2:59 AM", "24:00"))
print(add_time("11:59 AM", "24:05"))

# Run unit tests automatically
main(module='test_module', exit=False)