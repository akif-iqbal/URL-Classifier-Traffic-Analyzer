import pickle
import os

class MNB:
    def testing(self, url):
        filename = 'mnb_2.pkl'
        mnbModel = pickle.load(open('datasets/'+filename, 'rb'))
        #_ = os.system('cls')
        return mnbModel.predict(url)
        
    def testRun(self):
        filename = 'mnb_2.pkl'
        loaded_model = pickle.load(open('datasets/'+filename, 'rb'))
        #_ = os.system('cls')
        print('business today: ', loaded_model.predict(['http://www.businesstoday.net/']))
        print('miniclip: ', loaded_model.predict(['http://www.miniclip.com/']))
        print('friv: ', loaded_model.predict(['http://www.friv.com/']))
        print('pesuacademy: ', loaded_model.predict(['http://www.pesuacademy.com/']))
        print('bbc: ', loaded_model.predict(['http://www.bbc.com/']))
        print('jbl: ', loaded_model.predict(['http://www.jbl.com/']))
        print('croma: ', loaded_model.predict(['http://www.croma.com/']))
        print('google: ', loaded_model.predict(['http://www.google.com/']))
        print('microsoft: ', loaded_model.predict(['http://www.microsoft.com/']))
        print('wikipedia: ', loaded_model.predict(['http://www.wikipedia.org/']))
        print('playdoh: ', loaded_model.predict(['http://www.playdoh.com/']))
        print('lego: ', loaded_model.predict(['http://www.lego.com/']))
        print('manipal: ', loaded_model.predict(['http://www.manipalhospitals.com/']))
        print('hamleys: ', loaded_model.predict(['http://www.hamleys.in/']))
        print('firstcry: ', loaded_model.predict(['http://www.firstcry.com/']))
        print('medium: ', loaded_model.predict(['http://www.medium.com/']))
        print('weareteachers: ', loaded_model.predict(['http://www.weareteachers.com/']))
        print('indianexpress: ', loaded_model.predict(['http://www.indianexpress.com/']))
        print('timesofindia: ', loaded_model.predict(['http://www.timesofindia.com/']))
        print('99acres: ', loaded_model.predict(['http://www.99acres.com/']))
        print('magicbricks: ', loaded_model.predict(['http://www.magicbricks.com/']))
        print('nobroker: ', loaded_model.predict(['http://www.nobroker.in/']))

# obj = MNB()
# print("Naive Bayes result: ", obj.testing(['http://www.nobroker.in/']))