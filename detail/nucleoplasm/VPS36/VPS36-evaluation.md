---
type: protein-evaluation
gene: "VPS36"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VPS36 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VPS36 / C13orf9, EAP45 |
| 蛋白名称 | Vacuolar protein-sorting-associated protein 36 |
| 蛋白大小 | 386 aa / 43.8 kDa |
| UniProt ID | Q86VN1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles, Lysosomes; 额外: Plasma membrane, Cell Junctions; UniProt: Cytoplasm; Endosome; Late endosome; Membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 386 aa / 43.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=50 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=82.8; PDB: 2HTH, 2ZME, 3CUQ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR021648, IPR011993, IPR040608, IPR037855, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Lysosomes; 额外: Plasma membrane, Cell Junctions | Supported |
| UniProt | Cytoplasm; Endosome; Late endosome; Membrane; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endosome (GO:0005768)
- ESCRT II complex (GO:0000814)
- extracellular exosome (GO:0070062)
- late endosome membrane (GO:0031902)
- lysosome (GO:0005764)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 50 |
| PubMed broad count | 67 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C13orf9, EAP45 |

**关键文献**:
1. Structurally divergent and recurrently mutated regions of primate genomes.. *Cell*. PMID: 38428424
2. VPS36-Dependent Multivesicular Bodies Are Critical for Plasmamembrane Protein Turnover and Vacuolar Biogenesis.. *Plant physiology*. PMID: 27879389
3. PI(3,4)P2-mediated cytokinetic abscission prevents early senescence and cataract formation.. *Science (New York, N.Y.)*. PMID: 34882480
4. Endosomal Arl4A attenuates EGFR degradation by binding to the ESCRT-II component VPS36.. *Nature communications*. PMID: 38030597
5. VPS36-Mediated plasma membrane protein turnover is critical for Arabidopsis root gravitropism.. *Plant signaling & behavior*. PMID: 28340324

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.8 |
| 高置信度残基 (pLDDT>90) 占比 | 52.1% |
| 置信残基 (pLDDT 70-90) 占比 | 29.3% |
| 中等置信 (pLDDT 50-70) 占比 | 10.4% |
| 低置信 (pLDDT<50) 占比 | 8.3% |
| 有序区域 (pLDDT>70) 占比 | 81.4% |
| 可用 PDB 条目 | 2HTH, 2ZME, 3CUQ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2HTH, 2ZME, 3CUQ）+ AlphaFold高质量预测（pLDDT=82.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR021648, IPR011993, IPR040608, IPR037855, IPR036388; Pfam: PF04157, PF11605 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VPS25 | 0.999 | 0.999 | — |
| CHMP6 | 0.999 | 0.873 | — |
| SNF8 | 0.999 | 0.999 | — |
| VPS28 | 0.999 | 0.975 | — |
| TSG101 | 0.997 | 0.751 | — |
| CHMP3 | 0.990 | 0.000 | — |
| CHMP2A | 0.990 | 0.312 | — |
| HGS | 0.987 | 0.094 | — |
| RPS27A | 0.982 | 0.958 | — |
| UBC | 0.982 | 0.962 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP82 | psi-mi:"MI:0397"(two hybrid array) | pubmed:15766533 |
| Hey | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG11275 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| eIF3j | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Vps25 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Rbbp5 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| lush | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| SNF8 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15329733 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| VPS20.2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.8 + PDB: 2HTH, 2ZME, 3CUQ | pLDDT=82.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Endosome; Late endosome; Membrane; Nucl / Vesicles, Lysosomes; 额外: Plasma membrane, Cell Jun | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. VPS36 — Vacuolar protein-sorting-associated protein 36，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小386 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 50 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86VN1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136100-VPS36/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VPS36
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86VN1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (supported)。来源: https://www.proteinatlas.org/ENSG00000136100-VPS36/subcellular

![](https://images.proteinatlas.org/39734/451_B10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39734/451_B10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39734/454_B10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39734/454_B10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39734/456_B10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39734/456_B10_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86VN1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
