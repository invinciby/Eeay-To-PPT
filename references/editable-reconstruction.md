# Editable Reconstruction

Use this reference only after all slide images are approved and the user requests editable PPTX.

## Scope

Convert approved full-slide images into a more editable PPTX. Treat this as a reconstruction step, not as a guarantee of full-native PowerPoint recovery.

Expected outcome:

- readable text becomes editable where OCR is reliable;
- simple cards, lines, tables, and shapes become native objects where practical;
- complex illustrations, generated diagrams, photos, and strict figures remain as tight image crops;
- limitations are recorded in an editability report.

## Mode Selection

Choose per slide:

1. **Reconstruction**
   - Use for structured academic/business slides with simple geometry, tables, modules, arrows, cards, and labels.
   - Rebuild simple geometry natively.
   - Keep complex visuals as crops.

2. **Clean background + editable text**
   - Use when the slide is visually complex but text editability matters.
   - Remove source text from background before placing editable text.
   - Do not leave duplicate source text under editable text.

3. **Image-only fallback**
   - Use only when the user accepts limited editability or OCR/reconstruction is not reliable.
   - Label the output clearly as limited editability.

## Required Artifacts

For each reconstructed slide, create or maintain:

- original approved slide image;
- `ocr_results.json`;
- OCR review or correction manifest;
- reconstruction plan or text layout manifest;
- rendered preview if possible;
- `editability_report.json`.

For multi-slide decks, aggregate per-slide reports into a deck-level editability summary.

## OCR Rules

- Run OCR before creating editable text.
- Review OCR before inserting text into PPTX.
- Correct obvious OCR errors using the approved content spec, not imagination.
- Default to line-level trace for Chinese text fidelity.
- Avoid PowerPoint auto-wrap when it causes one-character Chinese wraps.
- Omit low-confidence decorative glyphs, icons, and accidental text unless meaningful.

## Native Reconstruction Rules

Rebuild as native PPT objects when practical:

- title and body text;
- simple rectangles, cards, panels, badges, dividers;
- circles and markers;
- straight arrows and simple connectors;
- real row/column tables;
- simple chart scaffolds only when data is available.

Keep as tight crops:

- generated SCI-style illustrations;
- complex diagrams whose geometry would drift;
- real experiment/data figures;
- screenshots;
- photos;
- dense charts without source data;
- gradients, shadows, or complex visual fields.

Do not approximate-redraw real experiment/data figures.

## Anti-Duplicate Text Rule

Never ship a slide where the original text-bearing full-slide image remains underneath editable text. That creates duplicate text, not useful editability.

Acceptable approaches:

- textless background + editable text;
- native reconstruction + tight crops;
- image-only fallback explicitly labeled.

## Editability Report

Include:

- slide count;
- editable text body count;
- OCR accepted/corrected/omitted counts;
- native shape count;
- native table count;
- picture/crop count;
- strict figures preserved as crops;
- known visual drift;
- slides with limited editability;
- whether duplicate text was avoided.

## User-Facing Limitation Text

Use this phrasing when needed:

```text
可编辑版会尽量把文字、简单卡片、线条和表格重建为 PPT 原生对象；复杂插图、真实实验图和无法可靠重建的视觉区域会作为裁剪图片保留。这样可以保护真实结果图不被重画，同时提供主要文本和简单结构的可编辑性。
```
