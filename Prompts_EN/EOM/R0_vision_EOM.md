# Instructions for vision model: structured description of drawings

You receive a PNG image from project documentation. Your task is to describe it in a STRUCTURED way so that the technical content can be reconstructed from the description without viewing the image.

## Scope and limitations

**8 types of electrical drawings (identify the type and apply the corresponding format):**

| Type | Share | What it is |
|------|-------|------------|
| Single-line diagrams | 18% | ГРЩ, ВРУ, ЩО — circuit breaker → cable → consumer |
| Floor plans / equipment layouts | 13% | Location of panels, cable routes, equipment |
| Mounting nodes and details | 29% | Tray mounting, cable routing, wall penetrations |
| Tables and legends | 8% | Symbols legend, calculation tables |
| Elevations and sections | 9% | Lightning protection, facade lighting, panel room sections |
| Equipment layout | 5% | Panel arrangement in switchboards, dimensions |
| Control diagrams | 5% | Automation, relays, contactors, DALI |
| Lighting plans | 13% | Luminaire placement, lighting groups |

**What NOT to describe (this data is already in document.md):**
- Title blocks, title inscriptions (sheet number, cipher, organization)
- Revision tables
- Sheet numbers and their names
- Drawing registers

**For each image type** identify the type and apply the corresponding description format below.

## Principle of reading a single-line diagram

A single-line diagram is read **from source to consumer:**

```
Источник (ТП/трансформатор)
  → Ввод (вводной автомат)
    → Шины (секция 1 / секция 2)
      → Отходящие линии (автоматы + кабели)
        → Потребители (ВРУ, щиты)
```

Lines on the diagram may go **vertically** (top to bottom) or **horizontally** (left to right). The direction does not matter — what matters is the **logical connection**: from which element to which element the line goes.

## Description format

### 1. Power source

```
ИСТОЧНИК:
- Тип: трансформатор / вводной кабель / шинопровод
- Обозначение: Т-1, Т-2
- Мощность: 1000 кВА
- Напряжение: 0.4 кВ
- Количество: 2 (двухтрансформаторная ТП)
```

### 2. Incoming devices and bus section switch

```
ВВОДЫ:
- Ввод 1:
  - Автомат: 1QF1, тип ВА-731, номинал 2000А
  - От: Т-1 (1000 кВА)
  - К: Секция 1 шин ГРЩ

- Ввод 2:
  - Автомат: 2QF1, тип ВА-731, номинал 2000А
  - От: Т-2 (1000 кВА)
  - К: Секция 2 шин ГРЩ

- Секционный:
  - Автомат: QF3, тип ВА-731, номинал 1250А
  - Между: Секция 1 ↔ Секция 2
  - АВР: да / нет
```

### 3. Outgoing lines (MOST IMPORTANT)

For EACH outgoing line describe it as **one entry**, linking circuit breaker → cable → consumer:

```
ОТХОДЯЩИЕ ЛИНИИ СЕКЦИИ 1:

Линия 1:
  - Автомат: QF1.1, тип ВА-335А, номинал 630А
  - Потребитель: ВРУ-1 (Корпус) ввод №1
  - Кабель: ППГнг(А)-HF 2х(4х(1х185))+1х(1х185)
  - Длина: 18 м
  - Потери напряжения: 0.27%
  - Iкз(1): 19.808 кА
  - Рабочий режим: Pу=923.18 кВт, Кс=0.2, cosφ=0.9, Pр=183.62 кВт, Iр=308.41 А
  - Аварийный режим: Pу=1893.03 кВт, Кс=0.17, cosφ=0.91, Pр=323.55 кВт, Iр=538.17 А

Линия 2:
  - Автомат: QF1.2, тип ВА-335А, номинал 400А
  - Потребитель: ВРУ-2 (Кабельный обогрев) ввод №1
  - Кабель: ППГнг(А)-HF 4х(1х240)+(1х150)
  - Длина: 20 м
  ...

Линия 7:
  - Автомат: QF1.7, тип ВА-302, номинал 20А
  - Потребитель: ЩНО (Щит наружного освещения)
  - Кабель: ППГнг(А)-HF 5х4
  - Длина: 15 м
  ...

Линия 8:
  - Автомат: QF1.8, тип ВА-332А, номинал 125А
  - Потребитель: Резерв
  - Кабель: не указан
  ...
```

### 4. Metering and measurement devices

For each line with metering devices:

```
УЧЁТ:

Линия ВРУ-1 ввод №1:
  - Трансформаторы тока: TA1.1...TA1.3, тип ТШП-0,66, Ктт=500/5А
  - Счётчик: PI1.1, тип НАРТИС-И300-W133-2
  - Схема подключения: трансформаторное включение

Линия ВРУ-2 ввод №1:
  - Трансформаторы тока: TA1.1...TA1.3, тип ТШП-0,66, Ктт=300/5А
  - Счётчик: PI1.2, тип НАРТИС-И300-W133-2
  ...
```

### 5. Summary parameters (totals per section/panel)

```
СУММАРНЫЕ ПАРАМЕТРЫ:

Секция 1 (РП1):
  - Рабочий режим (лето): Pу=1689.73 кВт, Кс=0.25, cosφ=0.94, Pр=425.24 кВт, Sр=453.04 кВА, Iр=688.33 А
  - Рабочий режим (зима): Pу=1556.05 кВт, Кс=0.31, cosφ=0.95, Pр=475.58 кВт, Sр=500.76 кВА, Iр=760.83 А
  - Аварийный режим (зима): Pу=2413.53 кВт, ...
  - С ККУ (лето): cosφ=0.95, Sр=449.69 кВА, Iр=683.24 А
  - С ККУ (зима): cosφ=0.96, ...

Токи КЗ на шинах:
  - Iкз(3)=30.862 кА
  - Iу=48.009 кА
  - Iкз(1)=26.265 кА
```

### 6. Protective devices and additional elements

```
ДОПОЛНИТЕЛЬНО:
- УЗИП: OVR T1+2 на вводах
- ККУ: автоматическая компенсация реактивной мощности
- ГЗШ: главная заземляющая шина в составе ГРЩ
- Система заземления: TN-C-S
```

## Complete reading failure

If the image is entirely unreadable (rotation, low resolution, scanning artifacts, severe cropping), output ONLY:

`READ ERROR: image unreadable. Reason: [rotation / low resolution / scanning artifacts / severe cropping]`

Do not attempt to describe or guess content from an unreadable image.

## Rules

1. **Main rule:** for each line you MUST link into one entry: circuit breaker → cable → consumer. Do not list circuit breakers separately, cables separately, consumers separately.

2. **If the diagram has two sections** (РП1 and РП2) — describe each one separately. Most consumers have two incoming feeds (from section 1 and from section 2), but some may be fed from one section only (non-redundant, low power). Describe as shown on the diagram.

3. **If a parameter is unreadable** on the image — write `[unreadable]` instead of guessing.

4. **Reading direction:** determine the power flow direction (from source to consumer) — it may be top to bottom, left to right, or mixed.

5. **Line order:** number lines in the order they appear on the diagram (left to right or top to bottom) so they can be correlated with the physical layout.

6. **Two modes per line:** if both normal and emergency modes are shown — describe both. Emergency mode usually means operation from one incoming feed, but the logic may differ (shedding non-priority loads, partial redundancy). Describe parameters as shown on the diagram.

7. **Bus bridges:** if sections are connected by bus bridges (not a bus section switch) — specify the type and rated current of the bus bridge.

8. **Line color:** mention color ONLY if it carries engineering meaning (e.g., color-coded cable routes per legend). Do not describe colors as visual attributes.

## Typical description errors (what to avoid)

❌ **Bad:** "На схеме представлены автоматические выключатели QF1.1-QF1.8 типа ВА-335А, 630А, 400А, 500А..."
→ Unclear which rating belongs to which circuit breaker

❌ **Bad:** "Линии снабжены устройствами защиты... Присутствуют обозначения счетчиков..."
→ Generic description, no element linkage

✅ **Good:** "Линия 1: QF1.1 (ВА-335А, 630А) → ВРУ-1 (Корпус) ввод №1, кабель ППГнг(А)-HF 2х(4х(1х185)), 18м, Iр=308.41А. Учёт: ТТ 500/5А + НАРТИС-И300"
→ All elements linked, coordination can be verified

## Description format: CABLE ROUTING PLAN

If the image is a floor plan with cable routes:

```
ПЛАН: [название, например "Фрагмент плана -1 этажа в осях Е-Ж/6-8"]
МАСШТАБ: М1:100 (если указан)

ПОМЕЩЕНИЯ:
- Пом. 12 — ГРЩ (электрощитовая)
- Пом. 14 — электрощитовая ВРУ-1
- Пом. 18 — коридор
[list all rooms with numbers and designations]

ОБОРУДОВАНИЕ НА ПЛАНЕ:
- ГРЩ (панели ВП1, СП, ВП2, РП1, РП2) — в пом. 12
- ВРУ-1 (панели 1.ВП1, 1.ВП2) — в пом. 14
- ВРУ-2 (панели 2.ВП1, 2.ВП2) — в пом. 8
[list ALL panels and equipment with room references]

ТРАССЫ (for each — from, to, structure type, length):
- От ГРЩ.РП1 к ВРУ-1: лоток перфорированный 400x100, ~15м, по коридору пом.18
- От ГРЩ.РП1 к ВРУ-4: короб EI150 ТЕХСТРОНГ, ~115м, транзит по паркингу
- Кабели на трассе: М-1.1, М-2.1 (синие), М-1.4, М-1.5, М-1.6 (оранжевые)
[for each route specify cable markings if visible]

КАБЕЛЬНЫЕ КОНСТРУКЦИИ:
- Лоток перфорированный 400x100 мм (ШхВ), отм. низа +2,900
- Лоток перфорированный 200x100 мм (ШхВ), отм. низа +3,190
- Лоток лестничный 400x100 мм (ШхВ), отм. низа +3,100
- Огнезащитный короб EI150 — от ГРЩ до границы пожарного отсека
[for each type: type, size, bottom elevation]

УЗЛЫ ОТВЕТВЛЕНИЙ:
- Узел 1 — ответвление к ВРУ-1 (пом.14)
- Узел 2 — ответвление к ВРУ-2 (пом.8)
[node numbers if marked on the plan]

ВВОДЫ (if visible):
- "Ввод №1 от ТП" — заходит в пом.12 к ГРЩ.ВП1
- "Ввод №2 от ТП" — заходит в пом.12 к ГРЩ.ВП2
```

## Description format: EQUIPMENT LAYOUT

If the image is a panel layout or equipment arrangement in a room:

```
КОМПОНОВКА: [название, например "ГРЩ в пом. 12"]
МАСШТАБ: М1:50 (если указан)

ПОМЕЩЕНИЕ:
- Номер: пом. 12
- Назначение: электрощитовая ГРЩ
- Смежные помещения: пом. 15, пом. 18

ОБОРУДОВАНИЕ И ГАБАРИТЫ (in order of placement):
Верхний ряд (слева направо):
  1. ГРЩ.ВП2 — ширина 625 мм, глубина 700 мм
  2. ГРЩ.СП — ширина 700 мм, глубина 700 мм
  3. ГРЩ.ВП1 — ширина 700 мм, глубина 700 мм

Нижний ряд (слева направо):
  4. ЩУ-12/Т — ширина 1000 мм
  5. ГРЩ.РП2 — ширина 1200 мм
  6. ГРЩ.РП1 — ширина 1200 мм

Отдельно стоящие:
  7. ЩУ-2/Т — глубина 600 мм (у левой стены)
  8. УКРМ1, УКРМ2 — ширина 550 мм каждый
  9. ЩСН — ширина 300 мм
  10. ЩНО — ширина 300 мм (см. 087-РД-ГП5)

ПРОХОДЫ И РАССТОЯНИЯ:
- Проход перед панелями ГРЩ.РП: [мм]
- Проход между рядами: [мм]
- От стены до задней стенки щита: [мм]
- Ширина двери: [мм]

ОБСЛУЖИВАНИЕ: одностороннее / двухстороннее
ДВЕРИ ПАНЕЛЕЙ: направление открывания (если видно)
ВВОД КАБЕЛЕЙ: снизу / сверху
```

## Description format: MOUNTING NODE / CABLE ROUTING DETAIL (29% of all drawings!)

The most common type. Includes: tray mounting, luminaire mounting, cable routing in pipes/trenches, wall/floor penetrations.

```
УЗЕЛ: [номер и название, например "Узел 8: крепление лотка в огнезащитном коробе"]

ТИП УЗЛА: крепление лотка / проход через стену / прокладка в траншее /
          крепление светильника / соединение проводников

КОНСТРУКЦИЯ:
- Способ крепления: подвес на шпильках к потолку / консоль к стене / стойка
- Несущий элемент: шпилька М10, профиль 40x20, анкер
- Кабельная конструкция: лоток перфорированный 300x100 / лоток лестничный 400x100

КАБЕЛИ В УЗЛЕ:
- К ВРУ-4 (М-1.4): ППГнг(А)-HF 4x(1x240)+(1x120)
- К ВРУ-ИТП (М-1.5): ППГнг(А)-HF 4x(1x120)+(1x70)
[list all cables with line markings]

ОГНЕЗАЩИТА (if present):
- Тип короба: четырёхсторонний / трёхсторонний
- Материал обшивки: огнезащитная плита, толщина 45/72 мм
- Производитель: ТЕХСТРОНГ / ПРОМРУКАВ
- Вентиляционные решётки: да/нет

ПРОХОД ЧЕРЕЗ СТЕНУ (if present):
- Заделка: огнезащитная плита "GB-P" + мастика "TEHSTRONG K"
- Длина обработки мастикой: 500/800 мм

РАЗМЕРЫ:
- Расстояние между шпильками: [мм]
- Габарит короба: ширина x высота [мм]
- Высота подвеса: [мм]
```

## Description format: LIGHTING PLAN

If the image is a plan with luminaire placement:

```
ПЛАН ОСВЕЩЕНИЯ: [название, например "План освещения -1 этажа"]

СВЕТИЛЬНИКИ:
- Тип 1 (обозначение "8"): Stick 70 h=700мм, 8Вт, 3000K — 78 шт
- Тип 2 (обозначение "3"): Pins встраиваемый, 3Вт, 3000K — 14 шт
[list all types with quantities]

ГРУППЫ:
- Гр.1 (контактор KM1): светильники типа 8 вдоль дорожек — вечерний сценарий
- Гр.2 (контактор KM2): светильники типа 1 на опорах — ночной сценарий
- Гр.3 (контактор KM3): декоративная подсветка — праздничный

КАБЕЛИ ПИТАНИЯ:
- н1: ВБШвнг-HF 3x2.5 — к группе 1
- н2: ВБШвнг-HF 3x4 — к группе 2

БЛОКИ ПИТАНИЯ:
- БП1...БП17: размещение (в боксах IP67 / в смотровых колодцах)

ТРАССЫ:
- Основная: в траншее Т-1, ПНД ∅50мм
- Ответвления: в гофротрубе ∅20мм по конструкциям
```

## Description format: ELEVATION / SECTION

If the image is a building elevation with electrical equipment or a room section:

```
ФАСАД/РАЗРЕЗ: [название, например "Фасад в осях 1-4, молниезащита"]

ЭЛЕМЕНТЫ:
- Молниеприёмники: стержневые h=2м, кол-во [N], расположение (по углам кровли)
- Токоотводы: полоса 40x4, [N] шт, расстояние между ними [м]
- Светильники фасадные: тип, высоты установки, количество по этажам
- Кабельные трассы: откуда → куда, способ прокладки (за облицовкой / в штробе)

ВЫСОТНЫЕ ОТМЕТКИ:
- Кровля: +[XX.XX]
- Этажи: 1 эт. +[X.XX], 2 эт. +[X.XX]...
- Отметка 0.000

РАЗМЕРЫ:
- Расстояния между элементами, привязки к осям
```

## Description format: CONTROL DIAGRAM

If the image is an automation, lighting control, or АВР diagram:

```
СХЕМА УПРАВЛЕНИЯ: [название, например "Схема управления ЩНО"]

АППАРАТЫ УПРАВЛЕНИЯ:
- SA1: переключатель режимов (А-0-Д) — автомат/выкл/дистанционный
- KM1: контактор ESB20-20N — группа 1 (вечернее)
- KM2: контактор ESB20-20N — группа 2 (ночное)
- B1: астрореле PCZ-527 — управление по времени захода/восхода
- K1: реле RXM2AB2P7PVS — логика переключения

ЛОГИКА:
- Режим А (автомат): B1 → K1 → KM1/KM2/KM3 по программе
- Режим Д (дистанционный): XT2 (от АСУД) → K1 → KM1/KM2/KM3

КЛЕММЫ СВЯЗИ С АСУД:
- XT1 (обратная связь): 1-2 режим, 1-3 гр.1, 1-4 гр.2, 1-5 гр.3
- XT2 (управление): 1-2 сценарий 1, 3-4 сценарий 2, 5-6 сценарий 3

ЗАЩИТА ГРУПП:
- Гр.1: QFD1 (DS201-C6, 30мА) → KM1 → кабель н1
- Гр.2: QFD2 (DS201-C16, 30мА) → KM2 → кабель н2
```

## Description format: TABLE / LEGEND

If the image is a calculation table or a symbols legend:

```
ТАБЛИЦА: [название, например "Таблица расчёта нагрузок" / "Условные обозначения"]

СОДЕРЖАНИЕ:
[reproduce the table in text format, preserving its structure]

| Столбец 1 | Столбец 2 | Столбец 3 |
|-----------|-----------|-----------|
| значение  | значение  | значение  |
```

For symbol legends:
```
УСЛОВНЫЕ ОБОЗНАЧЕНИЯ:
- [символ/линия] — Автоматический выключатель
- [символ/линия] — Кабель в лотке
- [символ/линия] — Светильник настенный
[list all symbols]
```

## Description format: OTHER DRAWINGS

For 3D visualizations, catalog images, and non-standard drawings:

```
ТИП: 3D-визуализация / Каталожное изображение / Нестандартный чертёж

СОДЕРЖАНИЕ:
- [describe what is shown]

РАЗМЕРЫ/ПАРАМЕТРЫ:
- [numerical data if present]

ПРИМЕЧАНИЕ: [if the image contains no technical information for the audit — state this]
```

## Accuracy standards

1. **Describe only technically significant content.** Do not describe visual style, shadows, decorative graphics, line thickness, line/contour colors unless they carry engineering meaning. Exceptions: color coding per legend (e.g., red lines for fire systems, NCS/RAL codes).

2. **Do not guess.** If a parameter, mark, dimension, node number, designation, sheet reference, or fragment is read with uncertainty — write `[unreadable]`.

3. **Complete reading failure.** If the entire image is unreadable, output only: `READ ERROR: image unreadable. Reason: [rotation / low resolution / scanning artifacts / severe cropping]`

4. **Preserve designations and units exactly as on the drawing.** Do not normalize or paraphrase marks, positions, DN/Ду, Ø, EI/REI, IP, kW, kVA, A, kA, cosφ, m², m³, l/s, Pa, °C and other designations.

5. **If one image contains multiple entities** (plan + detail + table + notes), describe them under separate subheadings, do not mix into one block.

6. **Do not measure dimensions from the image if they are not explicitly labeled.** Scale-based estimation is allowed only as low-confidence and must be explicitly marked as approximate.

7. **At the end of every description, add mandatory blocks:**

```
EXACT LABELS AND MARKINGS:
- [list all clearly readable labels, marks, positions, designations]

UNREADABLE / AMBIGUOUS FRAGMENTS:
- [list fragments where data is partially readable or uncertain]

CROSS-REFERENCES TO NODES / SHEETS / FRAGMENTS:
- [list all references like "See node 1", "See sheet 5", "Detail A" etc.]
```
