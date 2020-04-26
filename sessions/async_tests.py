import asyncio

async def slow_function(name, time):
    print(f"Sleeping {time} from {name}")
    await asyncio.sleep(time)
    print(f"Finished {name}")

loop = asyncio.get_event_loop()

for name in "ABC":
    loop.create_task(slow_function(name, 3))

loop.run_forever()
