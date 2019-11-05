The code in this repository uses the SKlearn library to classify images from the [German Traffic Sign Research Benchmark](http://benchmark.ini.rub.de/?section=gtsrb&subsection=news). The images from the train set are standardized to 40 pixels high x 40 pixels wide, and are then fed into various classifiers to train the models. After this, the classifiers are tested with images from the test dataset (also standardized to the same size) to see which classifier is most accurate on the traffic sign data.
The accuaracies for each classifer are provided below:

| Classifier        | Accuracy           | Note  |
|-------------|-------------|-----|
| LinearSVC      | 74.4% | Long training time, extremely quick predictions |
| PassiveAggressiveClassifier      | 69.8%      |    |
| RidgeClassifier | 73.8%      |     |
| SGDClassifier | 69.4%      |     |
| KNeighborsClassifier | 51%      | Very inefficient    |
