# Qianfan-VL: Domain-Enhanced Vision-Language Models
**Source**: https://github.com/baidubce/Qianfan-VL
**Date**: 2026-03-18
**Author**: Baidu Cloud (baidubce)
**Keywords**: Qianfan-VL, Baidu, vision-language model, OCR, document understanding, enterprise AI, multilingual, layout-as-thought

## Elevator pitch
Qianfan-VL is Baidu's enterprise-focused vision-language model family (3B-70B) with specialized OCR and document understanding capabilities, scoring 880 on OCRBench and 93.12% on OmniDocBench with multilingual support across 192 languages.

## Takeaways
- Model range: 3B, 8B, and 70B parameter variants for different compute budgets and task requirements.
- Specialized OCR and document understanding, not general vision—enterprise document parsing is the primary target.
- OCRBench score of 880; OmniDocBench 93.12%—strong performance on document-specific benchmarks.
- Chain-of-Thought reasoning support for 8B and 70B models enables complex document analysis tasks.
- Layout-as-Thought innovation for document analysis—structural understanding of document layout rather than just text extraction.
- Multilingual support across 192 languages including multiple scripts.
- Available on HuggingFace and ModelScope; deployment via HuggingFace transformers and vLLM.

## Synthesis
Document understanding is one of the highest-value enterprise AI applications, and it's an area where general-purpose vision models often underperform domain-specialized ones. Most LLM benchmarks test visual question answering on natural images; document parsing requires different capabilities—understanding table structures, form layouts, multi-column text, mixed image/text documents, and dense text with specific formatting conventions.

The Layout-as-Thought innovation is the technically interesting contribution. Most OCR-enhanced models extract text from images but don't explicitly model document structure. Layout-as-Thought appears to treat document layout as a reasoning intermediate, allowing the model to understand how spatial relationships in a document (this text is a table header, this block is a footer, these columns belong together) inform interpretation. This structural reasoning capability is what differentiates document AI from general vision AI.

192-language multilingual support at this performance level is significant for enterprise deployment. Enterprise documents are multilingual in global organizations; document AI that degrades substantially for non-English content is limited to English-centric organizations. Broad script support (presumably including Chinese, Arabic, Devanagari, etc.) expands the addressable market substantially.

Baidu's enterprise AI positioning through Qianfan-VL reflects a broader pattern in Chinese AI development: building specialized, high-performance models for specific enterprise domains rather than competing head-to-head with general-purpose frontier models. This strategy produces models that compete effectively in their target domains while avoiding direct commodity pricing pressure from open models in general capabilities.
