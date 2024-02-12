import re

from src.Constants import Constants


class FormMapper:

    @staticmethod
    def convert(chars):
        res = {'word': chars[2]}
        for characteristic in chars:
            if characteristic in Constants.part_of_speech_map:
                res['part_of_speech'] = Constants.part_of_speech_map[characteristic]
            if characteristic in Constants.number:
                res['number'] = Constants.number[characteristic]
            if characteristic in Constants.case:
                res['case'] = Constants.case[characteristic]
            if characteristic in Constants.gender:
                res['gender'] = Constants.gender[characteristic]
            if characteristic in Constants.animation:
                res['animation'] = Constants.animation[characteristic]
            if characteristic in Constants.degree:
                res['degree'] = Constants.degree[characteristic]
            if characteristic in Constants.time:
                res['time'] = Constants.time[characteristic]
            if characteristic in Constants.type:
                res['type'] = Constants.type[characteristic]
            if characteristic in Constants.inclination:
                res['inclination'] = Constants.inclination[characteristic]
        print(res)
        return res
