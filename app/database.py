MALWARE_DATABASE = {
    "silverfox-v1": {
        "id": "silverfox-v1",
        "name": "SilverFox v1",
        "type": "Rootkit",
        "danger_level": "Critical",
        "description": (
            "Использует kernel-драйвер для подавления запросов на сброс антивируса, "
            "обхода AV/EDR решений и жесткого закрепления в операционной системе."
        ),
        "mechanisms": [
            "Загрузка подписанного kernel-драйвера для перехвата системных вызовов",
            "Подавление запросов на сброс и отключение антивирусного ПО",
            "Обход сигнатурного и поведенческого анализа EDR-агентов",
            "Закрепление через автозагрузку и модификацию системных служб",
            "Скрытие процессов и файлов от пользовательского пространства",
        ],
        "indicators_of_compromise": {
            "hashes": [
                "a3f8c2d91e4b7a6053c8d9f12e4a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3",
                "7b2e9f4a1c8d3e6f5a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8",
            ],
            "files": [
                "C:\\Windows\\System32\\drivers\\sfdrv.sys",
                "C:\\ProgramData\\SilverFox\\svchost.exe",
                "C:\\Windows\\Temp\\sf_install.log",
            ],
            "registry": [
                "HKLM\\SYSTEM\\CurrentControlSet\\Services\\SilverFoxDrv",
                "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\\SFService",
            ],
        },
    },
    "silverfox-v2": {
        "id": "silverfox-v2",
        "name": "SilverFox v2",
        "type": "Trojan / Stealer",
        "danger_level": "Critical",
        "description": (
            "Модифицированная версия. Обладает продвинутыми механизмами Anti-VM "
            "(определение виртуального окружения) и Anti-Analysis (детект запущенных "
            "утилит типа ProcMon, x64dbg). Повышает привилегии в системе через обрубание "
            "Windows Defender и атаку DLL Hijacking в легитивных процессах Google Chrome. "
            "Является стилером паролей, сессий и персональных данных."
        ),
        "mechanisms": [
            "Детектирование виртуальных машин по артефактам гипервизора и MAC-адресам",
            "Обнаружение инструментов анализа: ProcMon, x64dbg, Wireshark, IDA",
            "Отключение Windows Defender через модификацию политик и реестра",
            "DLL Hijacking в процессах Google Chrome для повышения привилегий",
            "Эксфильтрация паролей, cookie-сессий и персональных данных",
            "Шифрование канала связи с C2-сервером",
        ],
        "indicators_of_compromise": {
            "hashes": [
                "f1e2d3c4b5a69788796a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3",
                "2c4e6a8b0d2f4a6c8e0b2d4f6a8c0e2b4d6f8a0c2e4b6d8f0a2c4e6b8d0f2a4",
            ],
            "files": [
                "C:\\Users\\Public\\chrome_elf.dll",
                "C:\\ProgramData\\SF2\\loader.exe",
                "C:\\Users\\%USERNAME%\\AppData\\Local\\Temp\\sf2_cache.dat",
            ],
            "registry": [
                "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\DisableAntiSpyware",
                "HKCU\\Software\\SF2\\Config",
            ],
        },
    },
    "kitty": {
        "id": "kitty",
        "name": "Kitty",
        "type": "Trojan",
        "danger_level": "High",
        "description": (
            "Распространялся под видом кастомного серверного ПО для Minecraft. "
            "После запуска маскируется и скрыто работает в фоновом режиме. "
            "Извлекает и крадет сохраненные пароли браузеров, активные игровые "
            "сессии и токены авторизации пользователя."
        ),
        "mechanisms": [
            "Маскировка под легитимный Minecraft Server JAR/EXE",
            "Фоновое выполнение без видимого окна интерфейса",
            "Извлечение сохраненных паролей из Chrome, Firefox, Edge",
            "Кража игровых сессий и токенов авторизации Minecraft",
            "Периодическая отправка данных на удаленный сервер",
        ],
        "indicators_of_compromise": {
            "hashes": [
                "9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8",
                "4a6c8e0b2d4f6a8c0e2b4d6f8a0c2e4b6d8f0a2c4e6b8d0f2a4c6e8b0d2f4",
            ],
            "files": [
                "C:\\Users\\%USERNAME%\\AppData\\Roaming\\.minecraft\\kitty.jar",
                "C:\\Users\\%USERNAME%\\AppData\\Local\\Kitty\\svchost.exe",
                "C:\\ProgramData\\MinecraftServer\\server.properties.bak",
            ],
            "registry": [
                "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\MinecraftServer",
                "HKCU\\Software\\Kitty\\LastSync",
            ],
        },
    },
    "sorry": {
        "id": "sorry",
        "name": "Sorry",
        "type": "Ransomware",
        "danger_level": "High",
        "description": (
            "Шифровальщик, ориентированный на Linux-системы. Перед началом деструктивной "
            "деятельности массово генерирует и оставляет файлы типа WriteUp (требования выкупа), "
            "после чего шифрует все доступные файлы пользователя с изменением расширения на .sorry."
        ),
        "mechanisms": [
            "Массовое создание файлов WriteUp с требованиями выкупа",
            "Рекурсивное шифрование файлов пользователя (AES-256)",
            "Переименование зашифрованных файлов с расширением .sorry",
            "Удаление теневых копий и снимков файловой системы",
            "Самоудаление исполняемого файла после завершения шифрования",
        ],
        "indicators_of_compromise": {
            "hashes": [
                "b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5",
                "e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0",
            ],
            "files": [
                "/home/*/.sorry",
                "/home/*/WriteUp.txt",
                "/tmp/sorry_encrypt.log",
                "/var/log/sorry_ransom.log",
            ],
            "registry": [],
        },
    },
    "dscourier": {
        "id": "dscourier",
        "name": "DSCourier",
        "type": "Exploitation Tool",
        "danger_level": "Critical",
        "description": (
            "Хакерский инструментарий, предназначенный для обхода подсистем безопасности Windows. "
            "Реализует специфичные механизмы bypass для выполнения произвольного неподписанного "
            "кода в обход встроенных защитных механизмов ОС."
        ),
        "mechanisms": [
            "Обход Driver Signature Enforcement (DSE) через уязвимые подписанные драйверы",
            "Эксплуатация уязвимостей в подсистеме CI (Code Integrity)",
            "Загрузка неподписанного кода в ядро через BYOVD-технику",
            "Отключение PatchGuard и SMEP/SMAP на уровне ядра",
            "Интеграция с фреймворками постэксплуатации",
        ],
        "indicators_of_compromise": {
            "hashes": [
                "c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8",
                "1a3b5c7d9e1f3a5c7d9e1f3a5c7d9e1f3a5c7d9e1f3a5c7d9e1f3a5c7d9e1f3",
            ],
            "files": [
                "C:\\Tools\\DSCourier\\dscourier.exe",
                "C:\\Windows\\System32\\drivers\\vuln_drv.sys",
                "C:\\Temp\\dsc_payload.bin",
            ],
            "registry": [
                "HKLM\\SYSTEM\\CurrentControlSet\\Services\\VulnDriver",
                "HKLM\\SOFTWARE\\DSCourier\\Config",
            ],
        },
    },
}
