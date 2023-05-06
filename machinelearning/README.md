## approach

1- train autoencoder on the data, use the encoder part as feature extractor <br />
2- use swin transformer feature extractor <br />
3- concatenate the two feature extractors <br />
4- train a classifier on the concatenated features <br />