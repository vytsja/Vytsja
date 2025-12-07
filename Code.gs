/**
 * Створює 1 лист "Бюджет" з 4 секціями, іменованими діапазонами, формулами,
 * валідаціями, фільтром, форматами та умовним форматуванням.
 * Локаль формул — коми. Валюта — CZK без копійок.
 */
function buildBudget() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  ss.setSpreadsheetLocale('en_US'); // коми в формулах
  ss.setSpreadsheetTimeZone('Europe/Prague');

  // Лист
  const name = 'Бюджет';
  const sheet = ss.getSheetByName(name) || ss.insertSheet(name);
  sheet.clear();

  // ---- РОЗМІТКА І ЗАГОЛОВКИ ----
  // Налаштування A1:F10
  sheet.getRange('A1').setValue('💰 БЮДЖЕТНИЙ КОНТРОЛЬ - [МІСЯЦЬ] [РІК]');
  sheet.getRange('A2').setValue('Період:');
  sheet.getRange('B2').setValue('');
  sheet.getRange('C2').setValue('до');
  sheet.getRange('D2').setValue('');
  sheet.getRange('A3').setValue('Валюта:');
  sheet.getRange('B3').setValue('CZK');
  sheet.getRange('A4').setValue('Резерв початковий:');
  sheet.getRange('B4').setValue('');
  sheet.getRange('A5').setValue('Ціль резерву:');
  sheet.getRange('B5').setValue('');
  // Авто-період поточного місяця
  const tz = ss.getSpreadsheetTimeZone();
  const today = new Date();
  const mStart = new Date(today.getFullYear(), today.getMonth(), 1);
  const mEnd = new Date(today.getFullYear(), today.getMonth()+1, 0);
  sheet.getRange('B2').setValue(Utilities.formatDate(mStart, tz, 'yyyy-MM-dd'));
  sheet.getRange('D2').setValue(Utilities.formatDate(mEnd, tz, 'yyyy-MM-dd'));

  // Доходи A12:F18
  sheet.getRange('A12').setValue('🟢 ДОХОДИ');
  sheet.getRange('A13:F13').setValues([[
    'Категорія','План','Факт','Відхилення','%','Статус'
  ]]);
  sheet.getRange('A14:A18').setValues([
    ['💵 Зарплата/Чайові'],
    ['🎁 Підробіток'],
    ['👨‍👩‍👧 Від сім\'ї'],
    ['🔄 Повернення боргів'],
    ['💼 Інші джерела']
  ]);

  // Витрати A20:F32
  sheet.getRange('A20').setValue('🔴 ВИТРАТИ');
  sheet.getRange('A21:F21').setValues([[
    'Категорія','План','Факт','Відхилення','%','Статус'
  ]]);
  sheet.getRange('A22:A32').setValues([
    ['🏠 Оренда'],
    ['💡 Комунальні + інтернет'],
    ['🍕 Їжа'],
    ['🚗 Транспорт'],
    ['👶 Дитина'],
    ['📱 Телефон/Зв\'язок'],
    ['🚬 Курілки'],
    ['👤 Особисті витрати'],
    ['💳 Борги/кредити'],
    ['⚠️ Непередбачені'],
    ['🛒 Інше']
  ]);

  // Транзакції A34:I200
  sheet.getRange('A34').setValue('📝 ЖУРНАЛ ТРАНЗАКЦІЙ');
  sheet.getRange('A35:I35').setValues([[
    'Дата','Тип','Автокатегорія','Сума','Опис','Оплата','Баланс','NET день','NET кумул.'
  ]]);

  // Стартові значення над журналом
  sheet.getRange('G35').setFormula('=$B$4');
  sheet.getRange('I35').setValue(0);

  // Підсумки A202:E210
  sheet.getRange('A202').setValue('📊 ПІДСУМКИ');
  sheet.getRange('A203').setValue('Загальний дохід:');
  sheet.getRange('A204').setValue('Загальні витрати:');
  sheet.getRange('A205').setValue('Чистий результат:');
  sheet.getRange('A206').setValue('Резерв поточний:');
  sheet.getRange('A207').setValue('До цілі резерву:');

  // ---- ІМЕНОВАНІ ДІАПАЗОНИ ----
  ss.setNamedRange('TR_DATE',   sheet.getRange('A36:A200'));
  ss.setNamedRange('TR_TYPE',   sheet.getRange('B36:B200'));
  ss.setNamedRange('TR_CAT',    sheet.getRange('C36:C200'));
  ss.setNamedRange('TR_AMOUNT', sheet.getRange('D36:D200'));
  ss.setNamedRange('TR_DESC',   sheet.getRange('E36:E200'));
  ss.setNamedRange('TR_PAY',    sheet.getRange('F36:F200'));
  ss.setNamedRange('TR_BAL',    sheet.getRange('G36:G200'));
  ss.setNamedRange('TR_NET_DAY',sheet.getRange('H36:H200'));
  ss.setNamedRange('TR_NET_CUM',sheet.getRange('I36:I200'));

  // ---- ФОРМУЛИ ----
  // Доходи C/D/E/F 14..18
  for (let r = 14; r <= 18; r++) {
    sheet.getRange(r, 3).setFormula(`=SUMIFS(TR_AMOUNT,TR_TYPE,"Дохід",TR_CAT,$A${r})`); // C
    sheet.getRange(r, 4).setFormula(`=C${r}-B${r}`); // D
    sheet.getRange(r, 5).setFormula(`=IF(B${r}>0,C${r}/B${r},0)`); // E
    sheet.getRange(r, 6).setFormula(`=IF(E${r}>=0.9,"✅","⚠️")`); // F
  }

  // Витрати C/D/E/F 22..32
  for (let r = 22; r <= 32; r++) {
    sheet.getRange(r, 3).setFormula(`=SUMIFS(TR_AMOUNT,TR_TYPE,"Витрата",TR_CAT,$A${r})`); // C
    sheet.getRange(r, 4).setFormula(`=C${r}-B${r}`); // D
    sheet.getRange(r, 5).setFormula(`=IF(B${r}>0,C${r}/B${r},0)`); // E
    sheet.getRange(r, 6).setFormula(`=IF(E${r}<=1,"✅","⚠️")`); // F
  }

  // Транзакції C/G/H/I 36..200
  sheet.getRange('C36').setFormula('=CATEGORYZE(E36,D36)');
  sheet.getRange('C36').copyTo(sheet.getRange('C36:C200'));
  sheet.getRange('G36').setFormula('=IF($B36="Дохід",G35+$D36,G35-$D36)');
  sheet.getRange('H36').setFormula('=SUMIFS(TR_AMOUNT,TR_DATE,$A36,TR_TYPE,"Дохід")-SUMIFS(TR_AMOUNT,TR_DATE,$A36,TR_TYPE,"Витрата")');
  sheet.getRange('I36').setFormula('=I35+H36');
  sheet.getRange('G36:I36').copyTo(sheet.getRange('G36:I200'));

  // Підсумки формули
  sheet.getRange('B203').setFormula('=SUMIF(B36:B200,"Дохід",D36:D200)');
  sheet.getRange('B204').setFormula('=SUMIF(B36:B200,"Витрата",D36:D200)');
  sheet.getRange('B205').setFormula('=B203-B204');
  sheet.getRange('B206').setFormula('=$B$4+B205');
  sheet.getRange('B207').setFormula('=$B$5-B206');

  // ---- ДАНІ ТА ВАЛІДАЦІЯ ----
  // Тип
  let dvType = SpreadsheetApp.newDataValidation()
    .requireValueInList(['Дохід','Витрата'], true)
    .setAllowInvalid(false)
    .build();
  sheet.getRange('B36:B200').setDataValidation(dvType);
  // Оплата
  let dvPay = SpreadsheetApp.newDataValidation()
    .requireValueInList(['Готівка','Картка','Змішано'], true)
    .setAllowInvalid(false)
    .build();
  sheet.getRange('F36:F200').setDataValidation(dvPay);
  // Дата
  sheet.getRange('A36:A200').setNumberFormat('yyyy-mm-dd');
  // Сума: >0
  let dvAmt = SpreadsheetApp.newDataValidation()
    .requireNumberGreaterThan(0)
    .setAllowInvalid(false)
    .build();
  sheet.getRange('D36:D200').setDataValidation(dvAmt);

  // ---- УМОВНЕ ФОРМАТУВАННЯ ----
  const rules = sheet.getConditionalFormatRules();
  // Доходи E14:E18 >= 0.9 → зелений текст
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenNumberGreaterThanOrEqualTo(0.9)
    .setFontColor('#0B8043')
    .setRanges([sheet.getRange('E14:E18')])
    .build());
  // Витрати E22:E32 > 1.2 → червона заливка
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenNumberGreaterThan(1.2)
    .setBackground('#F4C7C3')
    .setRanges([sheet.getRange('E22:E32')])
    .build());
  // Транзакції D36:D200 > 10000 → жовта заливка
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenNumberGreaterThan(10000)
    .setBackground('#FFF2CC')
    .setRanges([sheet.getRange('D36:D200')])
    .build());
  sheet.setConditionalFormatRules(rules);

  // ---- ФОРМАТИ, МЕЖІ, ІНТЕРФЕЙС ----
  // Валюта CZK без копійок для D,G,H,I і B203:B207
  sheet.getRangeList(['D14:D32','D36:D200','G36:G200','H36:H200','I36:I200','B203:B207'])
       .setNumberFormat('[$CZK] #,##0');

  // Заголовки по центру, жирні, світла заливка
  sheet.getRangeList(['A13:F13','A21:F21','A35:I35']).setHorizontalAlignment('center');
  sheet.getRangeList(['A13:F13','A21:F21','A35:I35']).setFontWeight('bold');
  sheet.getRangeList(['A13:F13','A21:F21','A35:I35']).setBackground('#F5F5F5');

  // Налаштування — м'яка сіра заливка
  sheet.getRange('A1:F10').setBackground('#F2F2F2');

  // Секційні заголовки більший кегль
  sheet.getRangeList(['A12','A20','A34','A202']).setFontSize(14).setFontWeight('bold');

  // Межі тонкі
  const borderColor = '#E0E0E0';
  ['A1:F10','A12:F18','A20:F32','A34:I200','A202:E210'].forEach(r => {
    sheet.getRange(r).setBorder(true,true,true,true,true,true,borderColor,SpreadsheetApp.BorderStyle.SOLID);
  });

  // Фільтр і фіксація
  // Видалити попередній фільтр якщо є
  const existingFilter = sheet.getFilter();
  if (existingFilter) existingFilter.remove();
  sheet.getRange('A35:I200').createFilter();
  sheet.setFrozenRows(35);

  // Автовирівнювання ширини для читабельності
  sheet.autoResizeColumns(1, 9);
}

/**
 * Користувацька функція авто-категоризації
 * =CATEGORYZE(desc, amount)
 */
function CATEGORYZE(desc, amount) {
  const t = (desc || '').toString().toLowerCase();
  const a = Number(amount) || 0;
  if ((/оренда|rent/).test(t) && a > 15000) return '🏠 Оренда';
  if ((/tesco|albert|billa|lidl|penny/).test(t)) return '🍕 Їжа';
  if ((a >= 200 && a <= 800) && (/зв.?яз|телефон|phone|youtube|net|internet|o2|vodafone|t-?mobile/).test(t)) return '📱 Телефон/Зв\'язок';
  if ((/садок|školka|kindergarten|аліска/).test(t)) return '👶 Дитина';
  return '🛒 Інше';
}
