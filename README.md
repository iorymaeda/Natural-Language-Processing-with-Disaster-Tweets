# [Natural Language Processing with Disaster Tweets](https://www.kaggle.com/competitions/nlp-getting-started/overview)

There i'm trying to solve kaggle NLP task in a few ways:

- [X] Classify on BERT embeddings
  - AUC: 0.8397
- [X] Tune BERT
  - AUC: 0.8831
- [X] Classify on tuned BERT embeddings
  - AUC: 0.8849
- [X] Tune BERT with preproccesing
  - AUC: 0.8695   O.o
- [ ] Classify on tuned BERT with preproccesing
- [ ] Try BERT large instead BERT base (300m vs 100m parameters)
- [ ] Train transformer from scratch

## Results

1. Gradient Accumulated + Gradient Checkpoint increase batch_size from ~16 to ~512
2. BERT tuning better than classify on BERT's embeddings

## References

Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. [arxiv abs](https://arxiv.org/abs/1810.04805), 2019.
