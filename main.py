import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from app.config.settings import settings
from app.bot.middlewares.auth import AuthMiddleware
from app.bot.middlewares.rate_limit import RateLimitMiddleware
from app.bot.handlers import general, email, template, unban
from app.database.models import init_db

logging.basicConfig(level=logging.INFO)

async def main():
    await init_db()
    
    bot = Bot(token=settings.bot_token, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())
    
    dp.message.middleware(AuthMiddleware())
    dp.callback_query.middleware(AuthMiddleware())
    
    # Rate limit middleware specifically for commands
    dp.message.middleware(RateLimitMiddleware())
    
    dp.include_routers(general.router, template.router, email.router, unban.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
