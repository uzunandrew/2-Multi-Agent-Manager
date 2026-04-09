# Codex Runtime

Изолированный контур для запуска аудита на `codex exec` без записи в основной проект.

Важно: сам `Codex/` внутри репозитория теперь играет роль шаблона. Реальный model-runtime по умолчанию поднимается во внешней ASCII-папке `D:\MAM_CODEX_RUNTIME`, чтобы обойти проблему `codex exec` с кириллическим путем git-репозитория.

## Что здесь лежит

- `Audits/` — локальные копии Python-этапов пайплайна.
- `Prompts_EN/` — снапшот рабочих prompt-файлов для Codex.
- `norms/` — локальная копия текущей JSON-базы норм.
- `projects/` — локальные зеркала исходных проектов внутри шаблона.
- `orchestrator.py` — запуск стадий Codex-пайплайна.

## Как это работает

1. Оркестратор синхронизирует шаблон `Codex/` во внешний runtime `D:\MAM_CODEX_RUNTIME` или в путь из `--runtime-root`.
2. Исходный проект из корневого `projects/...` копируется уже в `D:\MAM_CODEX_RUNTIME\projects\...`.
3. Если у проекта уже есть `_output/document_enriched.md`, он переиспользуется.
4. Если `document_enriched.md` нет, оркестратор собирает его из `md_file` / `md_files`.
5. Срезы, prompt-wrapper файлы и все `_output` создаются только во внешнем runtime.
6. `codex exec` запускается с ASCII-корнем workspace, поэтому не упирается в UTF-8 проблему кириллического git-пути.

## Текущий профиль

Сейчас поднят рабочий профиль для `EOM` в объеме, который уже стабилен в текущем проекте:

- `consistency`
- `tables`
- `cables`
- `fire_safety`
- `cable_routes`
- `metering`
- `power_equipment`
- `norms`

## Команды

Полный core-run по зеркалу проекта:

```powershell
& "C:\Users\uzun.a.i\AppData\Local\Programs\Python\Python313\python.exe" ".\Codex\orchestrator.py" run --project "projects/EOM/133_23-ГК-ГРЩ" --model gpt-5.4-mini
```

Только подготовка и сборка critic payload:

```powershell
& "C:\Users\uzun.a.i\AppData\Local\Programs\Python\Python313\python.exe" ".\Codex\orchestrator.py" run --project "projects/EOM/133_23-ГК-ГРЩ" --from-group prepare --to-group critic_payload
```

Только оптимизация поверх уже готовых findings:

```powershell
& "C:\Users\uzun.a.i\AppData\Local\Programs\Python\Python313\python.exe" ".\Codex\orchestrator.py" run --project "projects/EOM/133_23-ГК-ГРЩ" --from-group optimization --to-group optimization_review --model gpt-5.4-mini
```

Явно указать другой ASCII-runtime:

```powershell
& "C:\Users\uzun.a.i\AppData\Local\Programs\Python\Python313\python.exe" ".\Codex\orchestrator.py" run --runtime-root "D:\MAM_CODEX_RUNTIME_ALT" --project "projects/EOM/133_23-ГК-ГРЩ"
```

## Важно

- Все новые результаты model-runtime пишутся во внешний `D:\MAM_CODEX_RUNTIME\projects/.../_output`.
- Снапшот prompt-файлов и Python-скриптов в `Codex/` автономный; дальнейшие изменения можно вносить только в `Codex/`, не трогая основной пайплайн.
- Позже сюда можно будет подключить новую нормативную базу из MD/vault, не ломая основной проект.
