# Curated Literature References

This folder stores citation metadata, source links, and design notes. It intentionally does not vendor copyrighted PDFs or journal cover images.

## Core Technical Papers

| Theme | Citation | Source | Visual / Method Notes |
|---|---|---|---|
| LLM-assisted P300 spelling | Hong J, Wang W, Najafizadeh L. ChatBCI, a P300 speller BCI with context-driven word prediction leveraging large language models, from concept to evaluation. Scientific Reports. 2026. | DOI: https://doi.org/10.1038/s41598-025-25660-7; PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12909297/ | P300 matrix, LLM suggestions, keystroke/time savings, phrase-level completion. |
| Local LLM + adaptive stopping | Hong J, Rao P, Wang W, et al. ChatBCI-Assist: An intent-based P300 speller with a locally deployed LLM and adaptive stopping strategy. IEEE Transactions on Biomedical Engineering. 2026. | DOI: https://doi.org/10.1109/TBME.2026.3693965; PubMed: https://pubmed.ncbi.nlm.nih.gov/42139128/ | Closed-loop intent selection, local model node, adaptive confidence ring. |
| Foundational P300 BCI spelling | Farwell LA, Donchin E. Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials. Electroencephalography and Clinical Neurophysiology. 1988. | DOI: https://doi.org/10.1016/0013-4694(88)90149-6 | Classic P300 speller origin: stimulus grid, event-related response, communication prosthesis. |
| BCI speller design review | Rezeika A, Benda M, Stawicki P, Gembler F, Saboor A, Volosyak I. Brain-computer interface spellers: a review. Brain Sciences. 2018. | DOI: https://doi.org/10.3390/brainsci8040057 | Survey of speller layouts, control signals, and UI tradeoffs. |
| P300 speller advances | Pan J, Chen X, Ban N, et al. Advances in P300 brain-computer interface spellers: toward paradigm design and performance evaluation. Frontiers in Human Neuroscience. 2022. | DOI: https://doi.org/10.3389/fnhum.2022.1077717; PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9810759/ | P300 paradigm design, performance evaluation, calibration, and selection strategy. |
| SSVEP speller review | Li M, He D, Li C, et al. Brain-computer interface speller based on steady-state visual evoked potential: a review focusing on the stimulus paradigm and performance. Brain Sciences. 2021. | DOI: https://doi.org/10.3390/brainsci11040450; PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8065759/ | Alternative high-throughput speller route; useful extension target for decoder interface. |
| Language-model assisted BCI typing | Speier W, Arnold C, Lu J, Deshpande A, Pouratian N. Natural language processing with dynamic classification improves P300 speller performance. Journal of Neural Engineering. 2014. | DOI: https://doi.org/10.1088/1741-2560/11/4/046004 | Language model as probability field rather than chatbot UI. |
| Predictive spelling rate | Speier W, Arnold C, Chandravadia N, et al. Improving P300 spelling rate using language models and predictive spelling. Brain-Computer Interfaces. 2018. | DOI: https://doi.org/10.1080/2326263X.2017.1410418; PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6294452/ | Joint spelling-rate improvement by candidate priors and predictive completions. |
| Predictive communication review | Caria A. Towards predictive communication: the fusion of large language models and brain-computer interface. Sensors. 2025. | DOI: https://doi.org/10.3390/s25133987; PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12252171/ | Motivates LLM-assisted BCI as a low-bandwidth communication amplifier. |

## Algorithmic Motifs To Carry Into The Project

| Literature Motif | Algorithm / Framework | Repository Mapping |
|---|---|---|
| ERP evidence accumulation | P300 posterior over candidate symbols or intents | `BCIDecoder.predict()` returns ranked `DecodedCandidate` objects. |
| Adaptive stopping | Stop when confidence and margin are sufficient, otherwise collect more evidence | `AdaptiveStoppingPolicy` checks posterior threshold and top-2 margin. |
| Predictive spelling | Language-model or phrase-prior re-ranking over partial text | `LanguagePredictor` protocol and `PhraseBankPredictor`. |
| Phrase-level output | Select a short intent and expand into a communicative phrase | `CommunicationPipeline.run(partial, context, top_k)`. |
| Input-efficiency analysis | Characters selected vs. characters communicated; keystroke saving | `compute_efficiency()` and CLI demo output. |
| Safety boundary | Assistive prototype without clinical/emergency guarantee | README, setup docs, figure annotations, and pipeline terminology. |

## Research Importance

Non-invasive BCI communication is bandwidth limited: every selection is slow, noisy, and cognitively costly. Language prediction changes the problem from typing every character to selecting sparse intent evidence that can be expanded into useful phrases. The open-source value of this project is to make that interaction loop reproducible: decoder output, stopping logic, phrase ranking, and input-efficiency metrics are explicit modules rather than hidden UI behavior.

## Figure Design Implications

| Layer | What To Show | What To Avoid |
|---|---|---|
| Human signal | EEG cap nodes, P300 impulse, neural trajectory | Generic robot head or cartoon brain |
| Selector | Sparse grid / target flashes / confidence ring | Dense dashboard UI |
| Language model | Semantic manifold, token constellation, local model core | Chat bubble as the main concept |
| Output | One completed phrase, visually downstream from intent | Claims of clinical readiness |
