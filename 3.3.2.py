#Это задание я не особо понял, если придумаете что-то лучше пишите
from sklearn.feature_extraction import DictVectorizer
data_dict = [{'Зелёный': 23, 'Карий': 21, 'Голубой': 36, 'Фиолетовый': 3}]
dictvectorizer = DictVectorizer(sparse = False)
features = dictvectorizer.fit_transform(data_dict)
print(features)
