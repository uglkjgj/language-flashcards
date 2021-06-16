import pandas
import json

class Translate:

    def __init__(self, lang, skill):
        self.lang = lang
        self.skill = skill
        self.file = f"words/{lang} words/{skill}/{lang.capitalize()} {skill.capitalize()}.xlsx"

    def get_info(self):
        with open(f"words/{self.lang} words/{self.skill}/{self.lang.capitalize()} {self.skill.capitalize()}.json", 'r') as f:
            self.data = json.load(f)

        return self.data

    def reset_data(self, new_data=None):
        if new_data is None:
            info = pandas.read_excel(self.file)
            info = info.to_dict()
            if self.lang == 'mandarin':
                items = ['Character ', 'Pinyin', 'English']
            elif self.lang == 'french':
                items = ['English', 'French']
            self.info = {k: info[k] for k in items if k in info}

            with open(f'words/{self.lang} words/{self.skill}/{self.lang.capitalize()} {self.skill.capitalize()}.json',
                      'w') as f:
                json.dump(self.info, f, indent=4)
        else:
            with open(f'words/{self.lang} words/{self.skill}/{self.lang.capitalize()} {self.skill.capitalize()}.json',
                      'w') as f:
                json.dump(new_data, f, indent=4)
