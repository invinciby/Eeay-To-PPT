---
name: easy-to-ppt-image-editable
description: This skill should be used when the user asks to create a Chinese academic or report PPT from documents, papers, code, experiment notes, Markdown, source images, reference PPT screenshots, color/style preferences, or bilingual preferences; when the workflow requires outline approval, per-slide content approval, Image2/Nano2 full-slide image generation, strict preservation of real experiment/data figures, image-only PPTX packaging, or optional image-to-editable PPTX reconstruction.
---

# Easy To PPT Image Editable

Build Chinese academic/report slide decks from source material through a staged, approval-gated workflow. Treat the deck as a faithful reporting artifact first, a visual design artifact second, and a PPTX artifact last. Never invent data, results, citations, experiments, or conclusions not grounded in the user-provided source material.

This skill combines three patterns:

- Use `codex-ppt`-style orchestration for outline gates, per-slide jobs, Image2 full-slide generation, provenance, and packaging.
- Use `rw-consulting-ppt`-style visual governance for sample approval, deck-system consistency, proof-object clarity, and rejection of weak generated slides.
- Use `ppt-to-editable`-style reconstruction only when the user requests editable PPTX from approved slide images.

## Operating Contract

Produce a deck through explicit gates. Do not skip a gate unless the user explicitly says to skip it.

Default output is approved full-slide PNGs and, when requested, an image-only PPTX. If the user requests editable PPTX, run the editable reconstruction phase after all slide images are approved. Do not promise full-native editability; preserve text and simple geometry as editable where practical, and keep complex visuals as tight source crops.

Use Image2/Nano2-style native full-slide image generation for slide images. Do not render final slide images with HTML, CSS, SVG, canvas, screenshots, Python/Pillow, PptxGenJS, or local drawing. Code may be used only for manifests, validation, packaging, OCR/reconstruction, contact sheets, and deterministic file operations.

## Required Workflow

1. **Intake and alignment**
   - Collect source material, required images, reference PPT screenshots, color/style preferences, language preference, target page count, audience/use case, and output format.
   - If important preferences are missing, ask concise alignment questions before generating artifacts.
   - Read `references/intake-and-gates.md` for the full checklist.

2. **Source analysis and outline agent**
   - Analyze only the supplied source material.
   - Draft the deck title, target page count, reporting logic, and slide-by-slide outline.
   - Show the outline in chat and wait for approval.
   - Do not create final slide briefs, image prompts, generated images, PPTX plans, or editable reconstruction plans before outline approval.

3. **Per-slide content agent**
   - After outline approval, write per-slide content specs with page claim, key points, source basis, suggested visual/proof object, required image mapping, and open uncertainties.
   - Ensure every slide serves its approved title.
   - Keep content slide-ready; avoid paper-like paragraphs.
   - Read `references/slide-content-spec.md`.

4. **Markdown production pack**
   - Consolidate approved outline and per-slide content into a Markdown production file.
   - Use the schema in `examples/production-pack.example.md` as the preferred shape.
   - Treat the Markdown pack as the canonical content contract for image prompts.

5. **Style and sample gate**
   - Derive the visual direction from user-provided reference PPT screenshots or selected style templates.
   - If a reference image is provided, treat it as a style reference, not a layout to copy mechanically.
   - Generate 1-2 representative sample pages only after content and style are confirmed.
   - Do not batch-generate the whole deck before sample approval.
   - Read `references/style-and-image-generation.md`.

6. **Image2/Nano2 slide generation**
   - Create one prompt job per slide using the approved production pack and deck style contract.
   - Use the same selected image backend for all slides.
   - Use the Chinese prompt templates in `references/expected-prompt-templates.md` as the default wording pattern for outline, per-slide content, first slide image, subsequent slide image, and strict experiment figure preservation.
   - Include approved sample images as style references where the backend supports image context.
   - For each slide, generate one complete 16:9 full-slide PNG.
   - Record generation backend, prompt path, source image inputs, and QA result.

7. **Per-slide QA and revision**
   - Inspect every generated slide for Chinese text accuracy, title fidelity, source faithfulness, image inclusion, experiment-figure preservation, layout, aspect ratio, and style consistency.
   - Regenerate any failed slide with a revised prompt before continuing.
   - Read `references/qa-and-real-figure-policy.md`.

8. **Real experiment/data figure protection**
   - Treat real experiment figures, plots, screenshots, tables, and data charts as strict input assets.
   - Insert them only by proportional scaling/cropping rules. Do not redraw, restyle, translate, relabel, smooth, replot, distort, or let the image model alter their internal pixels.
   - If the selected image backend cannot preserve a strict figure safely, stop and ask whether to switch to a layout/reconstruction route that places the figure mechanically.

9. **PPTX output**
   - If the user wants image-only PPTX, package approved slide PNGs with one full-slide image per slide.
   - If the user wants editable PPTX, run editable reconstruction per slide after image approval. Use OCR, line-level text review, native simple shapes, native tables where reliable, and tight source crops for complex visuals.
   - Read `references/editable-reconstruction.md`.

10. **Final report**
   - Report output paths, slide count, image backend, whether image-only or editable mode was used, strict figures preserved, and known limitations.

## Image Backend Policy

Prefer the runtime's built-in image generation tool when available. If no built-in Image2/Nano2-style backend is available, use an explicitly configured API/CLI fallback. Configure external API keys only for fallback mode or when the user explicitly asks for external API usage.

Record the selected backend before generating the first sample. Keep the backend fixed after sample approval unless the user approves a change.

## Failure Conditions

Stop or revise when any of these occur:

- Source claim invented or unsupported.
- Approved title changed without user approval.
- Chinese text garbled, misspelled, warped, or unreadable.
- Real experiment/data figure modified internally.
- Slide generated by local code rendering instead of image backend.
- Full deck generated before outline and sample approval.
- Style drifts after sample approval.
- Editable PPTX delivered as a full-slide image with text overlay and duplicate source text.

## Resources

- `references/intake-and-gates.md` - Alignment questions and approval gates.
- `references/slide-content-spec.md` - Per-slide content schema and source-faithfulness rules.
- `references/style-and-image-generation.md` - Style extraction, Image2 prompt shape, sample and deck contract.
- `references/expected-prompt-templates.md` - Chinese prompt templates adapted from the expected workflow.
- `references/qa-and-real-figure-policy.md` - QA checklist and strict figure preservation policy.
- `references/editable-reconstruction.md` - Optional image-to-editable PPTX workflow.
- `examples/production-pack.example.md` - Canonical Markdown production pack example.
- `examples/slide-job.example.json` - Per-slide image job example.
- `scripts/validate_production_pack.py` - Lightweight production pack validator.
