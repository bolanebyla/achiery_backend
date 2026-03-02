# Сущности

## Цель (Objective)

- Цель: ачивка (прокачка навыка), квест (разовые задачи), вызов (периодическая задача/привычка)
- Таблица: `objectives`
- Поля:
    - id
    - title
    - description
    - created_at
    - user_id (fk `users.id`)
    - archived_at
    - kind (`ACHIEVEMENT`, `QUEST`, `CHALLENGE`)
    - current_value
    - target_value
    - completed_at
    - difficulty (`1`, `2`, `3`, `4`)
    - parent_id (fk `objectives.id`)
    - frequency (`WEEKLY`, `DAILY`, `MONTHLY`)

## Прогресс периодических целей (ObjectivePeriodProgress)

- Отслеживание выполнения челенджей за периоды
- Таблица: `objective_period_progress`
- Поля:
    - id
    - objective_id (fk `objectives.id`)
    - created_at
    - period_start
    - period_end
    - current_value

## Событие прогресса (ProgressEvent)

- Лог выполнения целей, начисления экспы и перехода на уровни
- Таблица: `progress_events`
- Поля:
    - id
    - user_id (fk `users.id`)
    - created_at
    - event_type (`OBJECTIVE_PROGRESS`, `LVL_UP`)
    - objective_id (fk `objectives.id`)
    - delta_value
    - delta_exp
    - level_id (fk `levels.id`)

## Уровень (Level)

- Соответствие уровня и необходимой экспы для перехода
- Таблица: `levels`
- Поля:
    - id
    - lvl
    - target_exp

## Прогресс пользователя (UserProgress)

- Уровень и экспа пользователя
- Таблица: `user_progress`
- Поля:
    - id
    - user_id (unic fk `users.id`)
    - level_id (fk `levels.id`)
    - total_exp