# [Natural Language Processing with Disaster Tweets](https://www.kaggle.com/competitions/nlp-getting-started/overview)

There i'm trying to solve kaggle NLP task in a few ways:

1. Classify on BERT embeddings
2. Tune BERT
3. Train transformer from scratch

## Todo

- [X] Classify on BERT embeddings
- [X] Tune BERT
- [X] Classify on tuned BERT embeddings
- [X] Tune BERT with preproccesing
- [X] Try BERT large instead BERT base (300m vs 100m parameters)
- [ ] Train transformer from scratch

## Results

| model name                         | AUC              |
| ---------------------------------- | ---------------- |
| Classify on BERT embeddings        | 0.8397           |
| Tune BERT 100m. WD == 0.           | 0.8825           |
| Tune BERT 100m. WD == 0.01         | 0.8831           |
| Tune BERT 100m. WD == 0.05         | 0.8843           |
| Tune BERT 100m. WD == 0.10         | 0.8781           |
| Tune BERT 100m. with preproccesing | 0.8695           |
| Classify on tuned BERT embeddings  | 0.8849           |
| Tune BERT 300m. WD == 0.           | 0.8871           |
| Tune BERT 300m. WD == 0.01         | **0.8893**       |

<sub>pre-trained BERT from huggingface</sup>
<br>
<sub>WD is Weight decay</sup>

## Conclusions

1. Gradient Accumulated + Gradient Checkpoint increase batch_size from ~16 to ~512 (acum_iter (4) *batch_size (128)) on base BERT 100m parameters
2. BERT tuning better than classify on BERT's embeddings

## References

BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. [arxiv abs](https://arxiv.org/abs/1810.04805), 2019.

Decoupled Weight Decay Regularization. Ilya Loshchilov, Frank Hutter. [arxiv abs](https://arxiv.org/abs/1711.05101), 2017.
