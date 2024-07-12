import time
import A
import B
import C
import D

def measure_time(module, func_name, runs=100):
    total_time = 0
    func = getattr(module, func_name)
    for _ in range(runs):
        start_time = time.time()
        func()
        end_time = time.time()
        total_time += end_time - start_time
    return total_time

# Assuming both snippet_A and snippet_B have a main function called `main` that runs the respective code.
time_A = measure_time(A, 'main', 100)
time_B = measure_time(B, 'main', 100)
time_C = measure_time(C, 'main', 100)
time_D = measure_time(D, 'main', 100)

print(f"Snippet A total time for 100 runs: {time_A} seconds")
print(f"Snippet B total time for 100 runs: {time_B} seconds")
print(f"Snippet C total time for 100 runs: {time_C} seconds")
print(f"Snippet D total time for 100 runs: {time_D} seconds")
