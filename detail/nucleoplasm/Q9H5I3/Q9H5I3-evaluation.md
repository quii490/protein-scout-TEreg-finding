---
type: protein-evaluation
gene: "Q9H5I3"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## Q9H5I3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | Q9H5I3 |
| 蛋白名称 | cDNA: FLJ23407 fis, clone HEP19601 |
| 蛋白大小 | 209 aa / 24.2 kDa |
| UniProt ID | Q9H5I3 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 209 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=82.6; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | Znf_C2H2_sf; Znf_C2H2_type |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **122/180** | |
| **归一化总分** | | | **67.2/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=82.6 PDB=0
- InterPro: Znf_C2H2_sf; Znf_C2H2_type
- Pfam: zf-C2H2
- PPI degree=0 ChIP: None


### 4. 总体评价
**67.2/100** | **nucleoplasm**
TE candidate: Znf_C2H2_sf; Znf_C2H2_type


### 补充分析 (UniProt API)

**蛋白全称**: cDNA: FLJ23407 fis, clone HEP19601

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: cDNA: FLJ23407 fis, clone HEP19601

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H5I3-F1-predicted_aligned_error_v6.png)

### 深度机制分析

**结构域架构**：Q9H5I3（cDNA: FLJ23407, 209 aa / 24.2 kDa）的主要结构域注释为IPR036236（Zinc finger, C2H2-type superfamily）和IPR013087（Zinc finger C2H2-type）。Pfam识别到PF00096（zf-C2H2, classical C2H2 zinc finger domain）。该蛋白的pLDDT=82.6（高置信度），结构预测显示compact C2H2 fold——全蛋白可能由2-3个tandem C2H2 fingers组成。无实验PDB结构。PubMed=0，为完全uncharacterized的TrEMBL entry。虽被评为TE candidate（拥有Znf_C2H2_sf; Znf_C2H2_type domain），但HPA nuclear annotation为nan，核定位证据缺失是其最大缺陷。

**PPI互作网络解读**：PPI degree=0——当前无任何公共PPI数据库记录的互作伙伴。该蛋白完全uncharacterized, 无法基于PPI network进行function inference。

**结构解读**：C2H2 zinc finger (PF00096) 是eukaryotic transcription factor中最为普遍的DNA-binding domain——每个finger unit (~30 aa) 包含两个cysteine和两个histidine residues chelating一个Zn2+ ion, 形成ββα fold that inserts α-helix into DNA major groove for sequence-specific recognition。C2H2-ZF protein中finger的数量和排列determine其DNA sequence specificity。Q9H5I3的209 aa长度可容纳~2-3 typical C2H2 fingers—sufficient for recognizing a 6-9 bp DNA motif。

**机制模型**：基于C2H2-ZF domain的classical function，Q9H5I3极可能作为sequence-specific DNA-binding transcription factor。Standard mechanism：(1) C2H2 fingers recognize and bind specific DNA motif in gene promoters/enhancers；(2) Protein recruits transcriptional co-activators or co-repressors through additional PPI surfaces——但这些surfaces在Q9H5I3中尚未被annotated；(3) Transcriptional output determined by the cofactor repertoire。在TE调控context中，C2H2-ZF蛋白是transposable element silencing的最核心effector——KRAB-ZFP/KAP1 pathway代表the most extensively characterized C2H2-mediated TE silencing mechanism。但Q9H5I3 lacks a KRAB domain，因此其确切功能类别（activator/repressor）未知。

**TE调控展望**：Q9H5I3的TE regulation潜力基于其C2H2-ZF domain。TE调控关联性取决于：(1) Q9H5I3的C2H2 fingers能否直接识别TE-derived sequences——人类基因组中有~700+ C2H2-ZF genes, 其中大量evolutionarily dedicated to TE silencing；(2) 缺乏KRAB domain暗示Q9H5I3 either (a) uses alternative repression mechanism, (b) functions as transcriptional activator of TE-embedded genic promoters, or (c) mediates TE recognition through recruitment of other silencing factors；(3) The complete absence of any functional data (PubMed=0, PPI=0) makes TE regulation inference entirely domain-based speculation。建议优先级较低，应首先通过protein expression (WB), subcellular localization (IF) 和transcriptional activity (luciferase reporter fused to Gal4-DBD) 建立该蛋白的基本functional characterization before any TE-specific investigation。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/Q9H5I3
