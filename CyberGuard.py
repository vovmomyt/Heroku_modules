#meta developer: @krevetkoff and @pakk_user
#changelog: init dev
__version__ = (0, 0, 1)
from .. import loader, utils
from telethon import events
from telethon.tl.types import MessageEntityMention, MessageEntityMentionName
from datetime import datetime

@loader.tds
class CyberGuardMod(loader.Module):
    """CyberGuard — Get all your mentions in one place!"""
    
    # Default strings (English)
    strings = {
        "name": "CyberGuard",
        "enabled": "<b>✅ CyberGuard enabled (reacts to mentions and replies)</b>",
        "disabled": "<b>⏹️ CyberGuard disabled</b>",
        "status_info": (
            "<b>CyberGuard Status:</b>\n\n"
            "Enabled: <b>{}</b>\n"
            "Log Chat: <b><code>{}</code></b>\n\n"
            "Commands: <code>{prefix}setlog @chat</code>, <code>{prefix}guard_on</code>, <code>{prefix}guard_off</code>, <code>{prefix}guard_status</code>"
        ),
        "log_chat_unset": "not set",
        "setlog_usage": "❌ Specify @username or ID (example: <code>{prefix}setlog @mylog</code> or <code>{prefix}setlog -1001234567890</code>)",
        "setlog_success": "✅ Log chat set successfully: <b>{}</b>",
        "setlog_error": "❌ Failed to set chat: {}",
        "reason_mention_id": "mention (by id)",
        "reason_mention_username": "mention (by @username)",
        "reason_reply": "reply to your message",
        "chat_default": "Chat",
        "log_header": (
            "🚨 <b>CyberGuard</b>\n\n"
            "📍 <b>Chat:</b> <code>{}</code>\n"
            "👤 <b>From:</b> {} (ID: {})\n"
            "🕒 <b>Detection Time:</b> {}\n"
            "⚠️ <b>Reason:</b> {}\n\n"
        ),
        "log_footer": "\n🔗 <b>Link:</b> {}",
        "media_placeholder": "(media/sticker/other)",
        "log_error_send": "[CyberGuard] Log sending error: {}",
        "log_error_message": "Error sending to log chat: {}\nOriginal: {}",
        "_cfg_read_mentions": "Mark a mention as read"
    }

    # Russian strings
    strings_ru = {
        "enabled": "<b>✅ CyberGuard включён (реагирует на упоминания и ответы)</b>",
        "disabled": "<b>⏹️ CyberGuard выключен</b>",
        "status_info": (
            "<b>CyberGuard:</b>\n\n"
            "Включён: <b>{}</b>\n"
            "Чат для логов: <b><code>{}</code></b>\n\n"
            "Команды: <code>{prefix}setlog @chat</code>, <code>{prefix}guard_on</code>, <code>{prefix}guard_off</code>, <code>{prefix}guard_status</code>"
        ),
        "log_chat_unset": "не задан",
        "setlog_usage": "❌ Укажи @username чата или ID (пример: <code>{prefix}setlog @mylog</code> или <code>{prefix}setlog -1001234567890</code>)",
        "setlog_success": "✅ Чат для логов установлен: <b>{}</b>",
        "setlog_error": "❌ Не удалось установить чат: {}",
        "reason_mention_id": "упоминание (по id)",
        "reason_mention_username": "упоминание (по @username)",
        "reason_reply": "ответ на твоё сообщение",
        "chat_default": "Чат",
        "log_header": (
            "🚨 <b>CyberGuard</b>\n\n"
            "📍 <b>Чат:</b> <code>{}</code>\n"
            "👤 <b>От:</b> {} (ID: {})\n"
            "🕒 <b>Время обнаружения:</b> {}\n"
            "⚠️ <b>Причина:</b> {}\n\n"
        ),
        "log_footer": "\n🔗 <b>Ссылка:</b> {}",
        "media_placeholder": "(медиа/стикер/другое)",
        "log_error_send": "[CyberGuard] Ошибка отправки логов: {}",
        "log_error_message": "Ошибка отправки в лог-чат: {}\nОригинал: {}",
        "_cfg_read_mentions": "Отметить упоминание как прочитанное"
    }
    
    # Ukrainian strings
    strings_ua = {
        "enabled": "<b>✅ CyberGuard увімкнено (реагує на згадки та відповіді)</b>",
        "disabled": "<b>⏹️ CyberGuard вимкнено</b>",
        "status_info": (
            "<b>CyberGuard:</b>\n\n"
            "Увімкнено: <b>{}</b>\n"
            "Чат для логів: <b><code>{}</code></b>\n\n"
            "Команди: <code>{prefix}setlog @chat</code>, <code>{prefix}guard_on</code>, <code>{prefix}guard_off</code>, <code>{prefix}guard_status</code>"
        ),
        "log_chat_unset": "не задано",
        "setlog_usage": "❌ Вкажи @username чату або ID (приклад: <code>{prefix}setlog @mylog</code> або <code>{prefix}setlog -1001234567890</code>)",
        "setlog_success": "✅ Чат для логів встановлено: <b>{}</b>",
        "setlog_error": "❌ Не вдалося встановити чат: {}",
        "reason_mention_id": "згадка (за id)",
        "reason_mention_username": "згадка (за @username)",
        "reason_reply": "відповідь на твоє повідомлення",
        "chat_default": "Чат",
        "log_header": (
            "🚨 <b>CyberGuard</b>\n\n"
            "📍 <b>Чат:</b> <code>{}</code>\n"
            "👤 <b>Від:</b> {} (ID: {})\n"
            "🕒 <b>Час виявлення:</b> {}\n"
            "⚠️ <b>Причина:</b> {}\n\n"
        ),
        "log_footer": "\n🔗 <b>Посилання:</b> {}",
        "media_placeholder": "(медіа/стікер/інше)",
        "log_error_send": "[CyberGuard] Помилка надсилання логів: {}",
        "log_error_message": "Помилка надсилання в лог-чат: {}\nОригінал: {}",
        "_cfg_read_mentions": "Позначити згадку як прочитану"
    }

    # German strings
    strings_de = {
        "enabled": "<b>✅ CyberGuard aktiviert (reagiert auf Erwähnungen und Antworten)</b>",
        "disabled": "<b>⏹️ CyberGuard deaktiviert</b>",
        "status_info": (
            "<b>CyberGuard-Status:</b>\n\n"
            "Aktiviert: <b>{}</b>\n"
            "Log-Chat: <b><code>{}</code></b>\n\n"
            "Befehle: <code>{prefix}setlog @chat</code>, <code>{prefix}guard_on</code>, <code>{prefix}guard_off</code>, <code>{prefix}guard_status</code>"
        ),
        "log_chat_unset": "nicht festgelegt",
        "setlog_usage": "❌ Gib den @username oder die ID des Chats an (Beispiel: <code>{prefix}setlog @mylog</code> или <code>{prefix}setlog -1001234567890</code>)",
        "setlog_success": "✅ Log-Chat erfolgreich festgelegt: <b>{}</b>",
        "setlog_error": "❌ Festlegen des Chats fehlgeschlagen: {}",
        "reason_mention_id": "Erwähnung (nach ID)",
        "reason_mention_username": "Erwähnung (nach @username)",
        "reason_reply": "Antwort auf deine Nachricht",
        "chat_default": "Chat",
        "log_header": (
            "🚨 <b>CyberGuard</b>\n\n"
            "📍 <b>Chat:</b> <code>{}</code>\n"
            "👤 <b>Von:</b> {} (ID: {})\n"
            "🕒 <b>Erkennungszeit:</b> {}\n"
            "⚠️ <b>Grund:</b> {}\n\n"
        ),
        "log_footer": "\n🔗 <b>Link:</b> {}",
        "media_placeholder": "(Medien/Sticker/Sonstiges)",
        "log_error_send": "[CyberGuard] Fehler beim Senden von Logs: {}",
        "log_error_message": "Fehler beim Senden an den Log-Chat: {}\nOriginal: {}",
        "_cfg_read_mentions": "Eine Erwähnung als gelesen markieren"
    }
    
    # --- Module Implementation ---
    
    def __init__(self):
        self.log_chat = None
        self.enabled = True
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "read_mentions",
                False,
                lambda: self.strings("_cfg_read_mentions"),
                validator=loader.validators.Boolean()
            )
        )

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.me = await client.get_me()
        self.my_id = self.me.id
        self.c, _ = await utils.asset_channel(
            self._client,
            "CyberGuard",
            "🔇 Chat for CyberGuard messages",
            silent=True,
            invite_bot=True,
        )
        self.enabled = db.get("CyberGuard", "enabled", False)
        self.log_chat = db.get("CyberGuard", "log_chat", None)
        if self.log_chat == None:
            self.log_chat = f"-100{self.c.id}"
            db.set("CyberGuard","log_chat", f"-100{self.c.id}")
        client.add_event_handler(self.on_message, events.NewMessage(incoming=True))

    # --- Commands ---
    
    async def guard_oncmd(self, message):
        """Включить оповещения """
        self.enabled = True
        self.db.set("CyberGuard", "enabled", True)
        await message.edit(self.strings("enabled"))

    async def guard_offcmd(self, message):
        """Выключить оповещения (.guard_off)"""
        self.enabled = False
        self.db.set("CyberGuard", "enabled", False)
        await message.edit(self.strings("disabled"))

    async def guard_statuscmd(self, message):
        """Статус CyberGuard (.guard_status)"""
        unset_text = self.strings("log_chat_unset")
        status_info_template = self.strings("status_info")

        chat_info = unset_text if not self.log_chat else str(self.log_chat)
        status_text = status_info_template.format(
            self.enabled,
            chat_info,
            prefix=self.get_prefix()
        )
        await message.edit(status_text)


    async def setlogcmd(self, message):
        """Задать чат для логов (.setlog @chat или .setlog chat_id)"""
        args = utils.get_args_raw(message)
        if not args:
            return await message.edit(self.strings("setlog_usage").format(prefix=self.get_prefix()))
        try:
            entity = await self.client.get_entity(args)
            self.log_chat = entity.id
            self.db.set("CyberGuard", "log_chat", self.log_chat)
            chat_name = getattr(entity, 'title', getattr(entity, 'username', str(self.log_chat)))
            await message.edit(self.strings("setlog_success").format(chat_name))
        except Exception as e:
            await message.edit(self.strings("setlog_error").format(e))

    # --- Utility ---
    
    def _make_msg_link(self, chat, event):
        try:
            if getattr(chat, "username", None):
                return f"https://t.me/{chat.username}/{event.id}"
            cid = int(chat.id)
            if cid != 0:
                cid_str = str(cid)
                if cid_str.startswith("-100"):
                    short = cid_str[4:]
                else:
                    short = cid_str.lstrip("-")
                return f"https://t.me/c/{short}/{event.id}"
        except:
            pass
        return "n/a"

    # --- Main Logic ---
    
    async def on_message(self, event):
        if not self.enabled:
            return
        if event.is_private:
            return
        if event.sender_id == self.my_id:
            return

        reason = None
        entities = getattr(event.message, "entities", []) or []
        text_raw = event.raw_text or ""

        my_username = self.me.username.lower() if self.me.username else None
        
        for ent in entities:
            if isinstance(ent, MessageEntityMentionName):
                try:
                    if getattr(ent, "user_id", None) == self.my_id:
                        reason = self.strings("reason_mention_id")
                        break
                except:
                    pass
            
            if isinstance(ent, MessageEntityMention) and my_username:
                start = ent.offset
                end = ent.offset + ent.length
                mentioned_text = text_raw[start:end].lower()
                
                if mentioned_text == f"@{my_username}":
                    reason = self.strings("reason_mention_username")
                    break
        if not reason and event.is_reply:
            try:
                reply = await event.get_reply_message()
                if reply and reply.sender_id == self.my_id:
                    reason = self.strings("reason_reply")
            except:
                pass

        if not reason:
            return

        try:
            sender = await event.get_sender()
        except:
            sender = None
        try:
            chat = await event.get_chat()
        except:
            chat = None

        time_str = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        sender_name = (sender.username and f"@{sender.username}") or (sender.first_name or f"id{getattr(sender,'id','?')}")
        chat_title = getattr(chat, "title", getattr(chat, "username", self.strings("chat_default")))

        header = self.strings("log_header").format(
            chat_title,
            sender_name,
            getattr(sender, 'id', 'n/a'),
            time_str,
            reason
        )

        link = self._make_msg_link(chat, event)
        footer = self.strings("log_footer").format(link)

        target = self.log_chat or "me"
        if self.config["read_mentions"]:
            await self._client.send_read_acknowledge(
            chat.id,
            clear_mentions=True,
        )

        try:
            if event.message.media:
                await event.message.forward_to(target)
                media_text = self.strings("media_placeholder")
                await self.inline.bot.send_message(target, header + media_text + footer, parse_mode='html')
            else:
                preview = event.raw_text or ""
                if len(preview) > 800:
                    preview = preview[:800] + "…"

                await self.inline.bot.send_message(target, header + f"💬 <i>{preview}</i>" + footer, parse_mode='html')
        except Exception as e:
            print(self.strings("log_error_send").format(e))
            try:
                error_msg = self.strings("log_error_message").format(
                    e,
                    event.raw_text or self.strings("media_placeholder")
                )
                await self.client.send_message("me", header + error_msg, parse_mode='html')
            except:
                pass