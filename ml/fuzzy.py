import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the input (antecedent) fuzzy variables
quality = ctrl.Antecedent(np.arange(0, 11, 1), "quality")  # Food quality (0 to 10)
service = ctrl.Antecedent(np.arange(0, 11, 1), "service")  # Service quality (0 to 10)

# Define the output (consequent) fuzzy variable
tip = ctrl.Consequent(np.arange(0, 26, 1), "tip")  # Tip percentage (0% to 25%)

# Automatically create fuzzy membership functions for service and quality
quality.automf(3)  # Poor, Average, Good
service.automf(3)  # Poor, Average, Good

# Define custom membership functions for the tip
tip["low"] = fuzz.trimf(tip.universe, [0, 0, 13])       # Low tip range
tip["medium"] = fuzz.trimf(tip.universe, [0, 13, 25])   # Medium tip range
tip["high"] = fuzz.trimf(tip.universe, [13, 25, 25])    # High tip range

# Visualize membership functions
quality["average"].view()
service.view()
tip.view()

# Define fuzzy rules for the tipping system
rule1 = ctrl.Rule(quality["poor"] | service["poor"], tip["low"])      # If food or service is poor, tip is low
rule2 = ctrl.Rule(service["average"], tip["medium"])                  # If service is average, tip is medium
rule3 = ctrl.Rule(service["good"] | quality["good"], tip["high"])     # If food or service is good, tip is high

# Create a control system from the defined rules
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# Create a simulation of the control system
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# Set input values for quality and service
tipping.input["quality"] = 6.5  # Quality rating out of 10
tipping.input["service"] = 9.8  # Service rating out of 10

# Compute the output tip based on the inputs
tipping.compute()

# Output the result and visualize the tip
print(f"Suggested tip: {tipping.output["tip"]:.2f}%")  # Display the computed tip
tip.view(sim=tipping)  # Visualize the output membership function with the computed result
