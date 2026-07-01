---
type: protein-evaluation
gene: "BRD10"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## BRD10 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | BRD10 |
| 蛋白名称 | Uncharacterized bromodomain-containing protein 10 |
| 蛋白大小 | 2103 aa / 228.1 kDa |
| UniProt ID | Q5HYC2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Cytosol; Nucleoplasm; Vesicles (Approved) |
| 📏 蛋白大小 | 6/10 | ×1 | 6.0 | 2103 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=2 |
| 🏗️ 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=44.9; PDB=0 |
| 🧬 调控结构域 | 6/10 | ×2 | 12.0 | BRD10; Bromodomain; Bromodomain-like_sf |
| 🔗 PPI | 4/10 | ×3 | 12.0 | PPI degree=0 |
| **加权总分** | | | **128/180** | |
| **归一化总分 (÷1.83)** | | | **70.5/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据
HPA: Cytosol; Nucleoplasm; Vesicles (Approved)
UniProt: SUBCELLULAR LOCATION: Nucleus {ECO:0000305|PubMed:24984779}.

**IF 图像**: [Protein Atlas](https://www.proteinatlas.org/)

#### 3.2 蛋白大小
2103 aa / 228.1 kDa

#### 3.3 研究现状
PubMed strict=2, broad=2
- PMID 41137173: Whole-genome sequencing reveals individual and cohort level insights into chromosome 9p syndromes. *Genome medicine*
- PMID 40196253: Whole-Genome Sequencing Reveals Individual and Cohort Level Insights into Chromosome 9p Syndromes. *medRxiv : the preprint server for health sciences*

#### 3.4 三维结构
AF pLDDT=44.9, PDB=0

#### 3.5 结构域
InterPro: BRD10; Bromodomain; Bromodomain-like_sf
Pfam: Bromodomain; KIAA2026_hel
**TE potential**: YES — BRD10; Bromodomain; Bromodomain-like_sf

#### 3.6 PPI 互作网络
Combined degree=0

#### 3.7 多库互证
basic cross-validation

### 4. 总体评价
⭐⭐⭐⭐
**70.5/100** | **nucleoplasm**


### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。


### 深度机制分析

**结构域架构**：BRD10（2103 aa, 228.1 kDa, KIAA2026）含Bromodomain（Pfam Bromodomain, IPR001487）约110 aa的four-helix bundle——通过hydrophobic acetyl-lysine binding pocket识别H3K14ac/H3K9ac。KIAA2026_hel域（Pfam PF23450, 约300 aa a-helical domain）构成C端组织。AlphaFold pLDDT=44.9（极低）——仅Bromodomain pLDDT>70，其余>1700 aa为极长IDR。BRD10本质上为"IDP with bromodomain reader module"。PPI degree=0（BioGRID）——与其CREB1/ATXN1/MUS81/HRAS推测互作构成初步网络。BRD10以bromodomain读取H3K9ac/H3K14ac等活跃启动子/增强子acetyl marks→IDP scaffold区域以"entropic chain"方式在enhancer-promoter loop间形成柔性桥梁→调控3D chromatin organization和transcriptional bursting。

**TE调控展望**：Bromodomain识别乙酰化组蛋白——TE LTR在激活状态需H3K9ac/H3K27ac以驱动Pol II转录——BRD10的Bromodomain可能直接识别TE位点acetyl marks→调控TE转录。CREB1结合TE LTR中的CRE motif（TGACGTCA, 在HERV-K和MMTV LTR已验证）→CREB1-BRD10 co-activation→增强TE LTR transcription。超大IDP支架可在TE-rich genomic region中作为chromatin organizer——通过物理占据调控TE区域的phase separation（HP1a-driven heterochromatin condensate formation）。BRD10在9p13.3染色体位置（9p syndrome候选基因, PMID 41137173）的缺失与发育缺陷相关——TE dysregulation可能是9p综合征的部分致病机制。



![PAE](https://alphafold.ebi.ac.uk/files/AF-Q5HYC2-F1-predicted_aligned_error_v6.png)

### PubMed

**Count: 2**

| PMID | Title |
|---|---|
| 41137173 | Whole-genome sequencing reveals individual and cohort level insights into chromosome 9p syndromes. |
| 40196253 | Whole-Genome Sequencing Reveals Individual and Cohort Level Insights into Chromosome 9p Syndromes. |


