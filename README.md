# AiReporter

# Data
動画からテキストを抽出  
AiReporter/blob/master/SpeechToText/stt.ipynb  
固有表現の抽出方法  
AiReporter/blob/master/data/create_train_data.ipynb  

# Training
SpeechToTextで生成した文書を校正したデータで学習（実際に動画生成に使用した文を生成しているモデル）  
AiReporter/blob/master/train/GPT2_train.ipynb  
校正できていないデータも含めSpeechToTextで生成した文書データで学習  
AiReporter/blob/master/train/GPT2_train\all.ipynb  

# Model
りんな社の Japanese GPT-2 model (medium-sized) を使用してファインチューニングを行っている。  
[rinnakk/japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) by [rinna Co., Ltd.](https://corp.rinna.co.jp/)  

# Licenese
[The MIT license](https://opensource.org/licenses/MIT)
