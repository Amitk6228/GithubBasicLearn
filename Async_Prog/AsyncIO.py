#Latest Python Feature for Asynchronus Programming
import asyncio
import time

async def waiter(n):
    await asyncio.sleep(n)
    print(f"Waited for {n} seconds")

async def main():
    #  print("HEllo")
    #  await asyncio.sleep(1)
    #  print("world")
    task1 = asyncio.create_task(waiter(2))
    task2 = asyncio.create_task(waiter(3))
    print(time.strftime('%X'))
    await task1
    await task2
    print(time.strftime('%X'))


if __name__ == '__main__':
    asyncio.run(main())
    print("Program ended")
