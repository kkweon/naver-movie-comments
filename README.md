# Naver Movie Rating and Sentiment Predict 
Built a sentiment predictor model based on movie comments.

## Included Files
- tensorflow_train.ipynb
    - train the model using tensorflow and save a checkpoint
- sklearn_bagging_test.ipynb
    - build a second model by using sklearn bagging classifier
    - test the model against user inputs

## Datasets
Comments collected from [Naver Movie](http://movie.naver.com) by [Stompesi](https://github.com/stompesi)
- Training Set  : 5,224,838 comments
- Validation Set: 1,741,613 comments
- Test Set      : 1,741,613 comments

However, the whole dataset is not included in this repo due to the large file size.
Sample of the datasets looks like below:

|Rating|Comments                                                                                                                 |ID      | 
|:------:|-------------------------------------------------------------------------------------------------------------------------|--------| 
|8       |모두 다 피해자 ㅜㅜㅜ 그래도 니카타를 사랑하는 두 남자 주인공 둘다 멋있어..                                              |11594313|
|4       |이런 영화가 다 있다길래 챙겨봤는데, 실망이 가득하네.. 그 당시에는 획기적인 영화였나?..                                   |11519625|
|8       |레옹의 모티브가 된 장 르노의 연기,배드 보이스의 악역의 모티브가 된 체키 카요,할리우드와 다른 액션장르 연출의 대가 뤽 베송|11494458|
|...     |... |...|


## Highlights
```
Input : 병신 실망 매우 실망 ㅜㅜ 쓰레기
Result: 부정(negative)

Input : 개굳 개쩐다
Result: 긍정(positive)

Input : 아오 1점도 주기아깝다 알바를 위한 알바에 의한 알바의 영화네  진심재미없네에휴
Result: 부정(negative)
```
