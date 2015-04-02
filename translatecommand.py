import sublime, sublime_plugin
import re
import urllib
import json


class TranslateCommand(sublime_plugin.TextCommand):

    def run(self, edit, key):
        self.key = key

        '''
        mom_is_wash_the_rama
        МамаМылаРаму
        MamaMilaRamu
        фывыфв
        '''

        sel = self.view.sel()[0]

        phrase = self.view.substr(sel)
        if '' == phrase.strip():
            phrase = self.view.substr(self.view.line(sel)).strip()
            if '' == phrase:
                return

        if re.search('[a-z]', phrase, re.I) is not None:
            direction = 'en-ru'
        else:
            direction = 'ru-en'

        phrase = re.sub('[_\-]', ' ', phrase)
        phrase = re.sub('([A-ZА-Я])', r' \1', phrase)

        def translate():
            self.request_translation(phrase, direction)

        sublime.set_timeout_async(translate, 0)


    def request_translation(self, phrase, direction):
        link = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key=%s' % self.key

        query = urllib.parse.urlencode(dict(text = phrase, lang = direction))
        link = link + '&' + query

        url = urllib.request.urlopen(link)
        answer = url.read()
        answer = answer.decode('utf-8')

        answer = json.loads(answer)
        self.view.show_popup_menu(["Яндекс.Перевод: " + answer['text'][0]], None)
