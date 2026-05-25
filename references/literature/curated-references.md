# Curated Literature References

This folder stores citation metadata, source links, and design notes. It intentionally does not vendor copyrighted PDFs or journal cover images.

## Core Technical Papers

| Theme | Citation | Source | Visual / Method Notes |
|---|---|---|---|
| LLM-assisted P300 spelling | Hong J, Wang W, Najafizadeh L. ChatBCI, a P300 speller BCI with context-driven word prediction leveraging large language models, from concept to evaluation. Scientific Reports. 2026. | DOI: https://doi.org/10.1038/s41598-025-25660-7; PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12909297/ | P300 matrix, LLM suggestions, keystroke/time savings, phrase-level completion. |
| Local LLM + adaptive stopping | Hong J, Rao P, Wang W, et al. ChatBCI-Assist: An intent-based P300 speller with a locally deployed LLM and adaptive stopping strategy. IEEE Transactions on Biomedical Engineering. 2026. | DOI: https://doi.org/10.1109/TBME.2026.3693965; PubMed: https://pubmed.ncbi.nlm.nih.gov/42139128/ | Closed-loop intent selection, local model node, adaptive confidence ring. |
| Foundational P300 BCI spelling | Farwell LA, Donchin E. Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials. Electroencephalography and Clinical Neurophysiology. 1988. | DOI: https://doi.org/10.1016/0013-4694(88)90149-6 | Classic P300 speller origin: stimulus grid, event-related response, communication prosthesis. |
| BCI speller design review | Rezeika A, Benda M, Stawicki P, Gembler F, Saboor A, Volosyak I. Brain-computer interface spellers: a review. Brain Sciences. 2018. | DOI: https://doi.org/10.3390/brainsci8040057 | Survey of speller layouts, control signals, and UI tradeoffs. |
| Language-model assisted BCI typing | Speier W, Arnold C, Lu J, Deshpande A, Pouratian N. Natural language processing with dynamic classification improves P300 speller performance. Journal of Neural Engineering. 2014. | DOI: https://doi.org/10.1088/1741-2560/11/4/046004 | Language model as probability field rather than chatbot UI. |

## Figure Design Implications

| Layer | What To Show | What To Avoid |
|---|---|---|
| Human signal | EEG cap nodes, P300 impulse, neural trajectory | Generic robot head or cartoon brain |
| Selector | Sparse grid / target flashes / confidence ring | Dense dashboard UI |
| Language model | Semantic manifold, token constellation, local model core | Chat bubble as the main concept |
| Output | One completed phrase, visually downstream from intent | Claims of clinical readiness |
