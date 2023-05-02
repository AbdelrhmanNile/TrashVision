## approach

1- train autoencoder on the data, use the encoder part as feature extractor
2- use swin transformer feature extractor
3- concatenate the two feature extractors
4- train a classifier on the concatenated features