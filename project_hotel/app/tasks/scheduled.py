from app.tasks.celery import celery
import asyncio


async def get_data():
    await asyncio.sleep(5)

@celery.task(name="periodic_task")
def periodic_task():
    """Пример запуска асинхронной функции внутри celery таски"""
    print(12345)
    asyncio.run(get_data())