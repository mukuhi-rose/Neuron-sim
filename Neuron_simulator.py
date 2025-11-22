lcharge = 0
threshold = 5# neuron fires when charge reaches this
time_step = 1
print("Neuron simulator starting...")

while charge < threshold:
    print("Current charge:", charge)
    charge += time_step   #charge in the neuron increases
    input("Press Enter to continue to next step...")
print("Neuron fired! ")
