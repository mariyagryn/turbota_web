from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
import os

# Імпортуємо необхідні модулі для роботи зі шрифтами
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# --- Шляхи до шрифтів ---
# Переконайтеся, що ці шляхи коректні для вашої системи та розташування шрифтів.
# Якщо OpenSans-Regular.ttf знаходиться в папці 'fonts' поруч зі скриптом:
FONT_DIR = "fonts"
REGULAR_FONT_PATH = os.path.join(FONT_DIR, "OpenSans-Regular.ttf")
BOLD_FONT_PATH = os.path.join(FONT_DIR, "OpenSans-Bold.ttf")

# --- Реєстрація шрифтів ---
# Це потрібно зробити один раз на початку скрипту
try:
    pdfmetrics.registerFont(TTFont('OpenSans', REGULAR_FONT_PATH))
    pdfmetrics.registerFont(TTFont('OpenSans-Bold', BOLD_FONT_PATH))
    print("Шрифти OpenSans успішно зареєстровані.")
except Exception as e:
    print(f"Помилка при реєстрації шрифтів: {e}")
    print("Переконайтеся, що файли шрифтів (.ttf) знаходяться за вказаними шляхами.")
    # Ви можете вийти з програми або продовжити з базовими шрифтами (будуть квадрати)
    exit()  # або pass

# Дані для PDF-файлів (теми, назви файлів та тексти) - Ваш існуючий словник
materials_data = {
    "Етика та етикет": [
        {"file": "Ввічливість у спілкуванні – Іваненко 2023.pdf",
         "text": "Ввічливість є фундаментом приємного та ефективного спілкування, адже вона відображає нашу повагу до співрозмовника. Вміння використовувати \"чарівні слова\" – такі як \"будь ласка\", \"дякую\", \"вибачте\" – та звертатися до людей з належною повагою, допомагає створити позитивну атмосферу, уникнути непорозумінь і побудувати міцні, довірливі стосунки як у повсякденному житті, так і в будь-якому колективі."},
        {"file": "Рольові ігри етикету – Петренко 2022.pdf",
         "text": "Рольові ігри є чудовим інструментом для вивчення та закріплення правил етикету в ігровій формі, дозволяючи дітям та підліткам безпечно практикувати різні ситуації, такі як знайомство, поведінка на святі чи розмова по телефону. Завдяки таким іграм учасники можуть відчути себе в різних ролях, зрозуміти значення кожного ввічливого жесту чи фрази та навчитися адаптувати свою поведінку до різних соціальних контекстів, що є важливим для їхньої інтеграції в суспільство."},
        {"file": "Поведінка за столом – Коваленко 2024.pdf",
         "text": "Правильна поведінка за столом є невід'ємною частиною загального етикету, що свідчить про вихованість та повагу до тих, хто сидить поруч. Знання основних правил – як правильно тримати столові прилади, коли починати їсти, як поводитися під час розмови за обідом чи вечерею – допомагає почуватися впевнено в будь-якій компанії, чи то сімейне свято, чи офіційний прийом, і сприяє приємній атмосфері під час спільної трапези."},
        {"file": "Друзі та шана – Назарчук 2021.pdf",
         "text": "Справжня дружба ґрунтується на взаємній повазі та вмінні цінувати один одного, що є запорукою міцних і тривалих стосунків. Шана до друзів проявляється у здатності слухати, розуміти, підтримувати у важкі мовили та радіти успіхам, а також у вмінні вибачатися за свої помилки та прощати, що зміцнює довіру та робить дружбу по-справжньому цінною."},
        {"file": "Ввічливі фрази – Олійник 2023.pdf",
         "text": "Ввічливі фрази є невеликим, але дуже потужним інструментом у спілкуванні, що відкриває двері до взаєморозуміння та гарних стосунків. Прості слова, такі як \"доброго ранку\", \"дякую за допомогу\", \"чи не могли б ви\", \"будьте здорові\" чи \"приємного дня\", не тільки роблять розмову більш приємною, а й демонструють нашу вихованість та турботу про почуття інших, що надзвичайно важливо для створення позитивної атмосфери."},
        {"file": "Етикет у школі – Шевчук 2022.pdf",
         "text": "Етикет у школі – це набір правил поведінки, що допомагають створити поважне та продуктивне середовище для навчання та взаємодії між учнями, вчителями та персоналом. Від того, як учні вітаються з дорослими, поводяться на уроках, під час перерв та у шкільній їдальні, залежить атмосфера всього навчального закладу, сприяючи взаємоповазі, дисципліні та успішному засвоєнню знань."},
        {"file": "Листи подяки – Зозуля 2023.pdf",
         "text": "Написання листів подяки – це важлива навичка, що дозволяє висловити щиру вдячність та визнання за отриману допомогу, подарунок або підтримку. Такий лист є не лише проявом ввічливості, а й способом зміцнити стосунки з людьми, демонструючи їм, що їхні зусилля були помічені та оцінені, що робить його цінним інструментом у будь-якій сфері життя."},
        {"file": "Вміння слухати – Ткаченко 2024.pdf",
         "text": "Вміння слухати – це не просто здатність чути слова, а справжнє мистецтво розуміння та емпатії, що є основою будь-якої ефективної комунікації. Коли ми уважно слухаємо співрозмовника, ми даємо йому відчути свою цінність, що допомагає розкритися та висловити свої думки та почуття, будуючи довірливі та глибокі стосунки як у особистому, так і в професійному житті."}
    ],
    "Математичні вправи": [
        {"file": "Додавання і віднімання – Петренко 2023.pdf",
         "text": "Додавання і віднімання є двома основними арифметичними діями, що становлять фундамент для вивчення всієї подальшої математики. Ці операції допомагають нам розуміти, як змінюється кількість об'єктів при їхньому об'єднанні або вилученні, і є невід'ємною частиною повсякденного життя, від підрахунку іграшок до управління особистими фінансами."},
        {"file": "Логічні ряди – Іванова 2022.pdf",
         "text": "Логічні ряди – це послідовності чисел, символів або зображень, які побудовані за певним правилом, і завдання полягає у визначенні цього правила та продовженні ряду. Такі вправи чудово розвивають логічне мислення, вміння аналізувати, знаходити закономірності та передбачати, що є важливими навичками не лише в математиці, а й у вирішенні життєвих завдань."},
        {"file": "Прості рівняння – Кравченко 2024.pdf",
         "text": "Прості рівняння – це математичні вирази, що містять невідому величину, яку потрібно знайти, використовуючи арифметичні дії. Розв'язування таких рівнянь вчить дітей працювати з невідомими величинами, використовувати логіку та обернені операції для пошуку рішення, закладаючи основи для більш складних математичних завдань у майбутньому."},
        {"file": "Геометричні фігури – Бондарчук 2021.pdf",
         "text": "Вивчення геометричних фігур – це захоплива подорож у світ форм, ліній та простору, що оточує нас щодня. Від простих трикутників і квадратів до об'ємних кубів та пірамід, розуміння їхніх властивостей допомагає дітям розвивати просторове мислення, логіку та вміння спостерігати світ, а також є важливим для подальшого вивчення математики та інженерії."},
        {"file": "Таблиця множення – Савченко 2023.pdf",
         "text": "Таблиця множення – це фундаментальний інструмент в математиці, який дозволяє швидко виконувати операції множення та є основою для багатьох інших математичних понять, таких як ділення, дроби та алгебра. Її міцне запам'ятовування значно прискорює обчислення та розвиває числову грамотність, що є незамінним у навчанні та повсякденному житті."},
        {"file": "Математичні кросворди – Гнатюк 2022.pdf",
         "text": "Математичні кросворди – це цікавий та інтерактивний спосіб закріпити математичні знання, перетворюючи розв'язування прикладів на захопливу гру. Такі завдання не лише допомагають відпрацювати додавання, віднімання, множення та ділення, а й розвивають логічне мислення, уважність та вміння концентруватися, роблячи процес навчання математики більш цікавим та ефективним."},
        {"file": "Завдання на порівняння – Романенко 2023.pdf",
         "text": "Завдання на порівняння в математиці вчать дітей аналізувати величини, числа або групи об'єктів та визначати їхні співвідношення – чи є одне більше, менше чи дорівнює іншому. Ці вправи розвивають критичне мислення, спостережливість та вміння застосовувати математичні знаки порівняння (>, <, =) у різних контекстах, що є важливим для розуміння числових понять."},
        {"file": "Числові головоломки – Литвин 2024.pdf",
         "text": "Числові головоломки – це веселі та складні завдання, які вимагають від учасників логічного мислення та креативного підходу до використання чисел та математичних операцій для досягнення певного результату. Вони чудово тренують розум, розвивають нестандартне мислення, вміння шукати різні шляхи розв'язання проблем та покращують навички швидких обчислень."}
    ],
    "Пізнавальні теми": [
        {"file": "Світ тварин – Коваль 2022.pdf",
         "text": "Світ тварин є безмежним і захопливим, пропонуючи нескінченні можливості для вивчення різноманіття живих істот, їхніх звичок, середовищ існування та ролі в екосистемі. Від найменших комах до величних китів, кожна тварина має свої унікальні особливості, а знайомство з ними розвиває допитливість, повагу до природи та розуміння важливості збереження біорізноманіття."},
        {"file": "Рослини України – Бойко 2023.pdf",
         "text": "Рослини України – це невід'ємна частина нашої природи, що вражає своїм розмаїттям та красою, від могутніх дубів і струнких беріз до ніжних весняних квітів і корисних трав. Вивчення місцевої флори допомагає дітям дізнатися про значення рослин для екосистеми, їхню роль у житті людини, а також вчить берегти природу та розпізнавати види, що ростуть навколо нас."},
        {"file": "Космос і планети – Максименко 2021.pdf",
         "text": "Таємниці космосу і загадки планет завжди захоплювали людство, відкриваючи безмежні простори для уяви та наукових відкриттів. Вивчення Сонячної системи, далеких зірок та галактик допомагає дітям зрозуміти місце Землі у Всесвіті, розвиває астрономічні знання та спонукає до роздумів про нескінченність простору та часу."},
        {"file": "Пори року – Степанова 2024.pdf",
         "text": "Пори року – це природний цикл, що демонструє постійні зміни в природі, кожна з яких приносить свої унікальні особливості, кольори та явища. Від весняного пробудження та літнього тепла до осіннього врожаю та зимових снігів, вивчення пір року допомагає дітям зрозуміти природні процеси, їхній вплив на життя рослин, тварин та людини, а також вчить спостерігати за навколишнім світом."},
        {"file": "Професії – Клименко 2022.pdf",
         "text": "Світ професій є надзвичайно різноманітним, пропонуючи безліч можливостей для реалізації талантів та здібностей кожної людини. Знайомство з різними професіями – від лікаря та вчителя до інженера та художника – допомагає дітям зрозуміти важливість праці, її роль у суспільстві, а також спонукає до мрій та планування свого майбутнього."},
        {"file": "Винаходи людства – Гончар 2023.pdf",
         "text": "Винаходи людства – це свідчення геніальності та творчого потенціалу людини, що кардинально змінили світ і продовжують формувати наше майбутнє. Від колеса до інтернету, кожен винахід є результатом допитливості, наполегливості та прагнення вирішувати проблеми, надихаючи наступні покоління на нові відкриття та інновації."},
        {"file": "Географічні загадки – Яценко 2021.pdf",
         "text": "Географічні загадки запрошують у захопливу подорож світом, відкриваючи невідомі куточки, дивовижні ландшафти та унікальні культури різних народів. Розгадування цих загадок розвиває знання про материки, країни, міста, річки та гори, а також розширює кругозір, спонукаючи до вивчення географії та пізнання планети."},
        {"file": "Пізнай світ – Левченко 2024.pdf",
         "text": "Пізнай світ – це заклик до нескінченної подорожі відкриттів, що включає в себе вивчення природи, історії, культури, науки та технологій. Це всеосяжна тема, яка заохочує допитливість, розвиває критичне мислення та допомагає зрозуміти складність і взаємозв'язок усіх явищ у нашому Всесвіті, формуючи цілісне світобачення."}
    ],
    "Соціальні навички": [
        {"file": "Емпатія у дії – Сидоренко 2023.pdf",
         "text": "Емпатія у дії – це здатність не лише розуміти почуття інших, а й проявляти це розуміння через свої вчинки, допомагаючи та підтримуючи тих, хто цього потребує. Це ключова соціальна навичка, що дозволяє будувати глибокі та довірливі стосунки, ефективно вирішувати конфлікти та створювати атмосферу взаємоповаги та співчуття в будь-якому колективі."},
        {"file": "Робота в команді – Павленко 2022.pdf",
         "text": "Ефективна робота в команді є запорукою успіху багатьох проєктів і завдань, оскільки вона дозволяє об'єднати різні таланти, знання та навички для досягнення спільної мети. Вміння слухати, ділитися ідеями, розподіляти обов'язки, підтримувати один одного та знаходити компроміси – це ті якості, що допомагають команді працювати злагоджено та досягати видатних результатів."},
        {"file": "Вирішення конфліктів – Шаповал 2024.pdf",
         "text": "Вирішення конфліктів – це важлива життєва навичка, що дозволяє знайти конструктивні шляхи подолання розбіжностей та непорозумінь без шкоди для стосунків. Навчання мирним методам вирішення проблем, таким як активне слухання, висловлення своїх почуттів без агресії, пошук спільних рішень та компромісів, допомагає перетворювати конфліктні ситуації на можливості для росту та взаєморозуміння."},
        {"file": "Співпраця та дружба – Бабенко 2021.pdf",
         "text": "Співпраця та дружба тісно пов'язані, адже справжні друзі вміють ефективно співпрацювати, підтримуючи один одного у спільних справах та починаннях. Навчання працювати разом, ділитися відповідальністю, допомагати товаришам і радіти їхнім успіхам не тільки зміцнює дружні зв'язки, а й розвиває важливі соціальні навички, необхідні для успіху в будь-якій сфері життя."},
        {"file": "Прощення та розуміння – Кравець 2023.pdf",
         "text": "Прощення та розуміння – це важливі аспекти емоційного благополуччя та гармонійних стосунків, що дозволяють звільнитися від образ і рухатися далі. Вміння пробачати не означає забути про подію, а радше звільнити себе від негативних емоцій, а розуміння мотивів інших допомагає бачити ситуацію ширше та будувати більш здорові та міцні зв'язки."},
        {"file": "Повага до відмінностей – Демченко 2022.pdf",
         "text": "Повага до відмінностей – це фундаментальний принцип толерантності та інклюзивності, що навчає нас цінувати унікальність кожної людини, її культури, поглядів та здібностей. Розвиток цієї навички допомагає створити відкрите та доброзичливе середовище, де кожен відчуває себе прийнятим і цінним, сприяючи взаєморозумінню та гармонійному співіснуванню в різноманітному суспільстві."},
        {"file": "Уміння домовлятися – Олексієнко 2024.pdf",
         "text": "Уміння домовлятися – це ключова навичка для досягнення взаємовигідних рішень у будь-якій ситуації, від повсякденних питань до складних переговорів. Воно включає в себе здатність чітко висловлювати свої потреби, активно слухати іншу сторону, знаходити спільні інтереси та бути гнучким, що дозволяє знаходити компроміси та будувати міцні, конструктивні стосунки."},
        {"file": "Емоційний інтелект – Цимбал 2023.pdf",
         "text": "Емоційний інтелект – це здатність розуміти та керувати власними емоціями, а також розпізнавати та впливати на емоції інших, що є вирішальним для успіху у всіх сферах життя. Розвиток цієї навички допомагає краще справлятися зі стресом, будувати міцніші стосунки, ефективно спілкуватися та приймати обґрунтовані рішення, роблячи людину більш адаптивною та впевненою у собі."}
    ],
    "Художня творчість": [
        {"file": "Малюнки природи – Бондаренко 2024.pdf",
         "text": "Малюнки природи – це прекрасний спосіб висловити своє захоплення красою навколишнього світу, від величних гір і безкраїх лісів до ніжних квітів і грайливих тварин. Ця тема дозволяє розвивати спостережливість, передавати настрій через кольори та форми, а також сприяє єднанню з природою, розслабленню та розвитку художнього смаку."},
        {"file": "Основи кольорознавства – Соколова 2022.pdf",
         "text": "Основи кольорознавства – це вивчення взаємодії кольорів, їхніх властивостей, гармонійних поєднань та психологічного впливу, що є фундаментальним для будь-якої художньої творчості. Розуміння холодних і теплих відтінків, контрастів та відтінків допомагає митцям створювати виразніші роботи, передавати емоції та створювати потрібну атмосферу в своїх творіннях."},
        {"file": "Аплікації з паперу – Рибак 2023.pdf",
         "text": "Аплікації з паперу – це захопливий вид творчості, що дозволяє створювати яскраві та об'ємні композиції шляхом вирізання та наклеювання елементів на основу. Ця техніка розвиває дрібну моторику, посидючість, уяву та відчуття композиції, даючи дітям можливість перетворювати прості аркуші паперу на унікальні витвори мистецтва."},
        {"file": "Техніки розфарбовок – Федорчук 2021.pdf",
         "text": "Техніки розфарбовок – це більше, ніж просто заповнення контурів кольором; це мистецтво використання різних матеріалів (олівців, фломастерів, фарб) та методів (штрихування, градієнти, накладання шарів) для створення об'єму, тіні та світла. Опанування цих технік розвиває акуратність, почуття кольору та уважність до деталей, дозволяючи перетворити прості розмальовки на справжні художні роботи."},
        {"file": "Створення скетчів – Віняр 2023.pdf",
         "text": "Створення скетчів – це швидкі начерки та замальовки, що дозволяють миттєво фіксувати ідеї, спостереження та враження, розвиваючи око та руку художника. Ця техніка допомагає покращити навички композиції, пропорцій, ліній та форм, а також сприяє креативному мисленню та вмінню бачити красу у повсякденних речах."},
        {"file": "Ліпка з пластиліну – Гуменна 2022.pdf",
         "text": "Ліпка з пластиліну – це чудовий вид творчості, що дозволяє створювати об'ємні фігури та композиції, розвиваючи дрібну моторику, просторове мислення, уяву та відчуття форми. Робота з м'яким та податливим матеріалом сприяє розвитку тактильних відчуттів, заспокоює та дає можливість дітям виражати свої ідеї у тривимірному форматі."},
        {"file": "Рисунок олівцем – Тарасенко 2024.pdf",
         "text": "Рисунок олівцем є основою багатьох художніх технік, дозволяючи створювати як деталізовані зображення, так і легкі начерки, вивчаючи основи світлотіні, перспективи та текстури. Ця техніка розвиває окомір, точність рухів, вміння передавати об'єм та форму, а також є чудовим способом для самовираження та розвитку художнього бачення."},
        {"file": "Моделювання листівок – Козак 2023.pdf",
         "text": "Моделювання листівок – це творчий процес створення унікальних вітальних карток, що поєднує в собі елементи дизайну, аплікації, малювання та декорування. Ця діяльність розвиває креативність, дрібну моторику, вміння працювати з різними матеріалами та почуття композиції, дозволяючи дітям висловлювати свої почуття та побажання близьким людям через рукотворні шедеври."}
    ]
}


def create_pdf(filepath, title, content):
    """Створює PDF-файл за вказаним шляхом з заголовком та текстом."""
    doc = SimpleDocTemplate(filepath, pagesize=A4,
                            rightMargin=2.5 * cm, leftMargin=2.5 * cm,
                            topMargin=2.5 * cm, bottomMargin=2.5 * cm)

    styles = getSampleStyleSheet()

    # Використовуємо зареєстрований шрифт 'OpenSans'
    styles.add(ParagraphStyle(name='TitleStyle',
                              fontName='OpenSans-Bold',  # Використовуємо жирний варіант для заголовка
                              fontSize=18,
                              leading=22,
                              alignment=TA_JUSTIFY,
                              spaceAfter=14))

    styles.add(ParagraphStyle(name='BodyTextJustified',
                              fontName='OpenSans',  # Використовуємо звичайний варіант для тексту
                              fontSize=12,
                              leading=14,
                              alignment=TA_JUSTIFY,
                              spaceAfter=6))

    story = []

    story.append(Paragraph(title, styles['TitleStyle']))
    story.append(Spacer(1, 0.5 * cm))

    story.append(Paragraph(content, styles['BodyTextJustified']))
    story.append(Spacer(1, 1 * cm))

    try:
        doc.build(story)
        print(f"Створено файл: {filepath}")
    except Exception as e:
        print(f"Помилка при створенні {filepath}: {e}")


def main():
    """Головна функція для створення всіх PDF-файлів."""
    print("Починаю генерацію PDF-матеріалів...")

    for category_name, category_files in materials_data.items():
        if not os.path.exists(category_name):
            os.makedirs(category_name)
            print(f"Створено папку: {category_name}")

        for item in category_files:
            file_name = item["file"]
            text_content = item["text"]

            title = file_name.replace('.pdf', '')

            filepath = os.path.join(category_name, file_name)

            create_pdf(filepath, title, text_content)

    print("\nГенерація PDF-матеріалів завершена.")


if __name__ == "__main__":
    main()