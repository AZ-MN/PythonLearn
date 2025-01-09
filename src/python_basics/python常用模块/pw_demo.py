import asyncio
from playwright.async_api import async_playwright


async def manual_record():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # 注释掉错误的调用
        # await page.start_recording(path='manual_recorded_script.js', format='javascript')

        print('请在打开的浏览器窗口中进行操作，操作完成后在控制台输入"stop"并回车。')
        while True:
            user_input = input()
            if user_input.lower() =='stop':
                break

        # 注释掉错误的调用
        # await page.stop_recording()
        await browser.close()


if __name__ == '__main__':
    asyncio.run(manual_record())