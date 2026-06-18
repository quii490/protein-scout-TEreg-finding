# PPT Slide Image Generation Prompts (16:9, White Background, High-Res)

> **使用方式**: 将以下 prompt 发送给 GPT-4o（支持图像生成的版本），每次一个。
> **注意**: 含数据的图表（Slide 3/6/7/8/9）建议直接用现有的 SVG/PNG 插入 PPT，GPT 无法生成准确的科学图表。仅 Slide 1/2/4/5/10 适合用 AI 生成配图。

---

## Slide 1 — 封面

```
A minimalist scientific presentation cover slide, 16:9 aspect ratio, white background.

Top half (60% of space): a clean abstract graphic of a cell nucleus with chromatin fibers inside, rendered as a scientific illustration in navy blue (#1E3A5F) and steel blue (#4682B4) tones. The nucleus has a subtle glow effect. Floating around the nucleus are small gold dots representing candidate proteins being selected.

Bottom text centered:
Title in large bold Helvetica: "TE Regulation Nuclear Protein Screening"
Subtitle in smaller grey Helvetica: "A Systematic Multi-Dimensional Pipeline from 4,756 Genes to Manually Curated Candidates"
Bottom-most line in small grey: "Machicheng  |  Group Meeting  |  June 2026"

No AI-artifacts. Clean, professional, suitable for an academic presentation. Do not include any text that looks garbled or nonsensical. White background, high resolution, suitable for printing.
```

---

## Slide 2 — 问题背景（概念图）

```
A clean scientific diagram illustration, 16:9 aspect ratio, white background.

The illustration should depict the concept of "screening nuclear proteins from a massive pool."

Left side: A large funnel or sieve shape with many small grey dots entering from the top, representing ~5,000 genes. The funnel narrows down.

Right side: A stylized cell nucleus (navy blue outline, semi-transparent fill) with a few gold-highlighted dots inside and around it, representing the selected candidate proteins.

Below the illustration, simple iconic labels:
- Left: "4,756 genes" with a database icon
- Middle: "Systematic evaluation" with a checklist/magnifying glass icon
- Right: "~25 candidates" with a target/bullseye icon

Style: Flat vector illustration, scientific journal cover quality. Colors: navy (#1E3A5F), gold (#B8860B), grey (#6B7280). No text in the illustration itself (labels can be added in PPT). White background.
```

---

## Slide 4 — 评分体系示意

```
A clean scientific diagram, 16:9 aspect ratio, white background, showing a multi-dimensional protein scoring system.

Central element: A hexagonal radar/spider chart with 6 axes labeled with small icons:
1. Nucleus icon (for Nuclear Localization, ×4 weight)
2. Ruler icon (for Protein Size, ×1 weight)
3. Lightbulb icon (for Research Novelty, ×5 weight)
4. 3D cube icon (for 3D Structure, ×3 weight)
5. DNA helix icon (for Regulatory Domains, ×2 weight)
6. Network nodes icon (for PPI Network, ×3 weight)

Each axis has a weight multiplier displayed next to the icon. The radar has a partial fill in blue showing a sample protein profile.

Below the radar, a simple formula display in a rounded box:
"Normalized Score = (Nuc×4 + Size×1 + Novelty×5 + Structure×3 + Domains×2 + PPI×3 + Cross-Validation) / 1.83"

Style: Clean flat vector, scientific textbook quality. Colors: navy blue, steel blue, gold accents. All text should be legible Helvetica/Arial. White background. No AI garbled text.
```

---

## Slide 5 — 筛选流程示意图（抽象版）

```
A clean process flow diagram illustration, 16:9 aspect ratio, white background.

Horizontal flow from left to right:

[Step 1: Database icon + "4,756"] → [Step 2: Document icon + "5,647 reports"] → [Branch: two parallel gates]

Top gate: Red box "Nuclear ≤ 3" with a crossed-out mitochondria icon → "760 eliminated"
Bottom gate: Orange box "PubMed > 100" with a crossed-out book icon → "710 eliminated"

After the gates, they merge back into:
[Step 3: Checkmark icon + "4,128 scored"] → [7 colored category tags: Chromatin(red), Nucleoplasm(orange), Nucleolus(blue), Nuclear Speckle(green), etc.]

Style: Clean flat process diagram, no AI artifacts. Arrow connectors between steps. White background. All icons are simple line icons. Colors are muted and professional.
```

---

## Slide 10 — 总结页

```
A clean summary slide background, 16:9 aspect ratio, white background.

Layout: Two-column design with subtle dividing line.

Left column header: "Completed" (with a green checkmark icon)
Below, 5 items with simple line icons:
1. Database icon: "4,756 genes → 5,647 reports → 4,128 scored + 1,470 eliminated"
2. Scale icon: "7-dimension weighted scoring → 0-100 normalized"
3. Grid icon: "7 subcellular categories + Centrosome module"
4. Globe icon: "Interactive static website + visualization suite"
5. Target icon: "27 manually curated candidates"

Right column header: "Next Steps" (with an arrow icon)
Below, 3 items:
1. Magnifying glass: "Deep literature mining for candidates"
2. Flask/beaker: "Experimental validation prioritization"
3. Expand icon: "Centrosome module scale-up (Pilot 10 validated)"

Style: Clean, minimalist, academic presentation. Navy blue headers, grey body text. Simple line icons. White background. High resolution. No garbled text.
```

---

## 图标/元素独立生成（白底，用于 PPT 拼装）

### Icon Set A — 核蛋白筛选概念图标

```
A set of 6 simple flat vector icons on a pure white background, arranged in a 2x3 grid. Each icon should be about 200x200px, navy blue (#1E3A5F) with gold (#B8860B) accents. The icons should represent:
1. Cell nucleus with chromatin
2. DNA / transposable element
3. Protein molecule
4. Magnifying glass over a gene list
5. Funnel/filter
6. Target/bullseye

Style: Clean line icons, 2px stroke, rounded caps. White background. Suitable for use in an academic PowerPoint presentation. High resolution (at least 1024x1024 total).
```

### Icon Set B — 评分维度图标

```
A horizontal row of 7 simple flat vector icons on a pure white background. Each icon approximately 150x150px, in navy blue (#1E3A5F). The icons represent:
1. Nuclear localization - a circle (nucleus) inside a larger circle (cell)
2. Protein size - a ruler/scale
3. Research novelty - a lightbulb with spark
4. 3D structure - a 3D cube or protein ribbon
5. Regulatory domains - a DNA helix segment
6. PPI network - connected nodes/network graph
7. Cross-validation - two overlapping checkmarks

Style: Clean line icons, 2px stroke, rounded caps and joints. White background. Academic but modern. High resolution (at least 2048px wide).
```

### Process Arrow Element

```
A clean horizontal process arrow/flow element on a white background. 16:9 aspect ratio.

Four connected boxes in a row, connected by rightward arrows:
Box 1 (navy blue): "Input" with small "4,756" below
→ Box 2 (steel blue): "Evaluate" with small "5,647" below
→ Box 3 (teal): "Filter" with small "Two gates" below
→ Box 4 (green): "Select" with small "4,128" below

Clean flat design. No gradients. White text on colored boxes. Rounded corners (8px radius). Total height about 200px in the center of the canvas. Rest is white space. Perfect for PPT insertion.
```

---

## 使用建议

| Slide | 内容 | 配图策略 |
|-------|------|----------|
| 1 | 封面 | 用 Slide 1 prompt 生成背景图，PPT 里叠加文字 |
| 2 | 问题背景 | 用 Slide 2 prompt 生成概念图 |
| 3 | 筛选流水线 | **直接用 `fig1_screening_flow.svg`**（GPT 画不准漏斗） |
| 4 | 评分体系 | 用 Slide 4 prompt 生成示意图，或直接用 `fig2_scoring_system.svg` |
| 5 | 维度定义 | **直接用 `fig5_scoring_table.svg`**（纯表格） |
| 6 | 分数分布 | **直接用 `fig3_distribution.svg`**（含真实数据） |
| 7 | 分类对比 | **直接用 `fig4_category_panels.svg`**（含雷达图） |
| 8 | 筛选全景 | **直接用 `screening_atlas_candidates.png`**（4K 高分辨率） |
| 9 | 候选分析 | **直接用 `figB` + `figC` 拼在一起** |
| 10 | 总结 | 用 Slide 10 prompt 生成总结页背景 |
| 图标 | 任意页 | 用 Icon Set prompts 生成后按需插入 |

> **核心原则**: 含真实数据的图表用 SVG 直接插入 PPT（可无限放大不模糊，Illustrator 可编辑）；纯概念性、装饰性的示意图用 GPT 生成。
