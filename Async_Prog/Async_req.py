import asyncio
import aiohttp
import time

async def fetchFromGoogle():
    url='https://www.google.com'
    session=aiohttp.ClientSession()
    resp=await session.get(url)
    await resp.content.read()
    async with open("file.text",'w') as file:
        await resp.content.read(256)
    await session.close()

async def main():
    print(time.strftime('%X'))
    #most fastest time in asynchronus manner----
    await asyncio.gather(
        *[
            fetchFromGoogle() for _ in range(20) 
        ]
    )
 #-----------------
    #if we try in synchronus manner 
    # for _ in range(20):
    #     await fetchFromGoogle()
    print(time.strftime('%X'))

if __name__ == "__main__":
    asyncio.run(main())
