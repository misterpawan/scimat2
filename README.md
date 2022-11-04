# SCIMAT: Science and Mathematics Dataset

## Authors: Snehith, Neeraj, and Pawan, IIIT, Hyderabad, copyright 2021

Paper: SCIMAT: Dataset of Problems in Science and Mathematics, arXiv: 2109.15005, 2021, [Paper](https://arxiv.org/abs/2109.15005)

## Remark on using the dataset

-You may use this dataset with Char2Char or Word2Word encoding in Transformer or in LSTM as shown in the paper above.

-You may also generate different variations of the questions using the generator files.

# Information: 
- This is an open source project, so feeel free to help us grow this dataset!
- For any dataset, the generator files can be used to generate the required number of samples.
- Some existing range of values for quantities in generator file may not make sense, feel free to adapt those.
- some part of Mathematics dataset is adapted from deepmind dataset, for more Mathematics data see: https://github.com/deepmind/mathematics_dataset
- Some part of the codes for mathematics datasets were written by Pratik Mandlecha (Microsoft, Hyderabad)

## If you find this useful, then please do cite our work as follows:

Neeraj Kollepara, Snehith Kumar Chatakonda and Pawan Kumar, SCIMAT: Science and Mathematics Dataset, arXiv: 2109.15005, 2021.

## If you prefer Bibtex, then cite the following publications:

@inbook{doi:10.1137/1.9781611977172.33,
author = {Pratik Mandlecha and Snehith Kumar Chatakonda and Neeraj Kollepara and Pawan Kumar},
title = {Hybrid Tokenization and Datasets for Solving Mathematics and Science Problems Using Transformers},
booktitle = {Proceedings of the 2022 SIAM International Conference on Data Mining (SDM)},
chapter = {},
pages = {289-297},
doi = {10.1137/1.9781611977172.33},
URL = {https://epubs.siam.org/doi/abs/10.1137/1.9781611977172.33},
eprint = {https://epubs.siam.org/doi/pdf/10.1137/1.9781611977172.33},
abstract = { Abstract Transformers, which were introduced for solving the task of machine translation, have expanded their utility in multiple domains. A recent application of transformers is in solving elementary mathematics problems. In this paper, we use a hybrid tokenization technique for encoding the mathematics and science problems and answers, which is used to train the transformer. We compare the performance of our tokenization with that of the char-to-char tokenzation in solving various types of mathematics and science problems. We discuss the accuracy, memory usage, and time to train the model with proposed tokenization. The proposed tokenization shows higher accuracy for some problems, and requires lesser memory compared to char-to-char tokenization. We propose an extended dataset of science and mathematics problems that consists of billions of samples in question-answer format in raw text. Code and Dataset: https://github.com/misterpawan/scimat2. }
}

@misc{scimat,      
title={SCIMAT: Science and Mathematics Dataset},     
author={Neeraj Kollepara and Snehith Kumar Chatakonda and Pawan Kumar},      
year={2021},      
eprint={2109.15005},      
archivePrefix={arXiv},      
primaryClass={math.NA}      
}

@inproceedings{10.1007/978-3-030-93620-4_16,
author = {Chatakonda, Snehith Kumar and Kollepara, Neeraj and Kumar, Pawan},
title = {SCIMAT: Dataset of Problems in Science and Mathematics},
year = {2021},
isbn = {978-3-030-93619-8},
publisher = {Springer-Verlag},
address = {Berlin, Heidelberg},
url = {https://doi.org/10.1007/978-3-030-93620-4_16},
doi = {10.1007/978-3-030-93620-4_16},
abstract = {Datasets play an important role in driving innovation in algorithms and architectures for supervised deep learning tasks. Numerous datasets exist for images, language translation, etc. One of the interesting challenge problems for deep learning is to solve high school problems in mathematics and sciences. To this end, a comprehensive set of dataset containing hundreds of millions of samples, and the generation modules is required that can propel research for these problems. In this paper, a large set of datasets covering mathematics and science problems is proposed, and the dataset generation codes are proposed. Test results on the proposed datasets for character-to-character transformer architecture show promising results with test accuracy above 95%, however, for some datasets it shows test accuracy of below 30%. Dataset will be available at: .},
booktitle = {Big Data Analytics: 9th International Conference, BDA 2021, Virtual Event, December 15-18, 2021, Proceedings},
pages = {211–226},
numpages = {16},
keywords = {Mathematics, Transformer, Question-Answering, Science}
}

Our NeurIPS-W paper is here:

https://datacentricai.org/neurips21/papers/45_CameraReady_paper_45_update.pdf
