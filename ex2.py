import asyncio
import time

print("!")
async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"

print("!!")
async def main():
    task1 = fetch_data(1)  # Could be awaited directly. task1 is a coroutine
    task2 = fetch_data(2)  # Could be awaited directly
    result1 = await task1
    print("Task 1 fully completed")
    result2 = await task2
    print("Task 2 fully completed")
    return [result1, result2]

print("!!!")
t1 = time.perf_counter()

results = asyncio.run(main())
print("results")
print(results)
print("!!!!")
t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")