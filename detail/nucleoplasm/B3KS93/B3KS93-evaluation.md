---
type: protein-evaluation
gene: "B3KS93"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, rebuilt]
status: shortlisted
---

## B3KS93 (cDNA FLJ35789 fis, clone TESTI2005703, highly similar to Suppressor of hairy wing homolog 1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | B3KS93 |
| 蛋白名称 | cDNA FLJ35789 fis, clone TESTI2005703, highly similar to Suppressor of hairy wing homolog 1 |
| UniProt ID | B3KS93 |
| 蛋白大小 | 542 aa |
| 评估日期 | 2026-06-29 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | UniProt GO-CC data pending |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 542 aa |
| 研究新颖性 | 5/10 | ×5 | 25.0 | Data pending |
| 三维结构 | 5/10 | ×3 | 15.0 | AlphaFold predicted |
| 调控结构域 | 4/10 | ×2 | 8.0 | Data pending |
| PPI | 5/10 | ×3 | 15.0 | Data pending |
| **加权总分** | | | **90/180** | |
| **归一化总分 (/1.83)** | | | **49.2/100** | 互证: +0 |

### 3. 分析

This report was automatically rebuilt after file corruption. Full manual evaluation pending.

### 4. 总体评价

**Data pending** — requires full evaluation.

### 补充分析 (UniProt API)

**蛋白全称**: cDNA FLJ35789 fis, clone TESTI2005703, highly similar to Suppressor of hairy wing homolog 1

**功能**: May function as a transcription factor

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR025243 |
| InterPro | IPR050527 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF13836 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

### 深度机制分析

**结构域架构**：B3KS93（542 aa, cDNA FLJ35789 fis, highly similar to Suppressor of hairy wing homolog 1）的功能注释为"May function as a transcription factor"。结构域注释涵盖C2H2型锌指fold IPR036236（Zinc finger, beta-beta-alpha motif）和IPR013087（Zinc finger C2H2-type）——C2H2锌指是经典DNA结合模块（每个finger约23-26 aa, CX2-4CX3FX5LX2HX3-5H canonical pattern）——通过α-helix插入DNA major groove识别特定碱基序列（3-4 bp per finger）——多个tandem C2H2 fingers串联可识别长DNA motif（12-18 bp）。IPR050527（SUHW-like domain）注释为Suppressor of hairy wing homolog特征域——SUHW/DREF/NURF家族蛋白在Drosophila中作为gypsy insulator蛋白——通过结合gypsy retrotransposon su(Hw)-binding site（12次重复的insulator core sequence）招募CP190和Mod(mdg4)形成chromatin loop boundary。Pfam PF13836为DUF（功能未知域）——可能在此背景中作为protein-protein interaction interface。该报告为文件损坏后自动重建（rebuilt after file corruption）——AlphaFold pLDDT、PDB结构、STRING/IntAct PPI和PubMed文献数均未填充——无法进行完整的结构-功能推理。TE调控展望：SUHW ortholog可能保留结合retrotransposon insulator sequence的ancestral function——C2H2锌指或许能识别人内源性逆转录病毒（HERV）LTR中的GYPSY-like motif——将enhancer-blocking insulator activity与TE silencing耦合。但目前无任何实验证据，需等待完整六维评估（pLDDT+PPI+PubMed）后进行验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B3KS93

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/B3KS93
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B3KS93
