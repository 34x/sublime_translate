Sublime Text 3 translate plugin (for Yandex.Translate)
======================================================


### Installation

1. Download plugin to your plugin folder (**Preferences -> Browse Packages**)

2. Request Yandex.Translate api key: https://translate.yandex.ru/developers

3. Add to you user key bindings (**Preferences -> Key Bindings - User**) shortcut for translate:

        {
            "keys": ["command+'"],
            "command": "translate",
            "args" : {"key" : "yandex_translate_api_key"}
        }

    Where **yandex_translate_api_key** key that you get by step 2

4. Set cursor on line to translate full line or select word and press chosen key bindings