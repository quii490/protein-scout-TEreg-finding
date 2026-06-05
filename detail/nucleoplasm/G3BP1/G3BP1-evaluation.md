---
type: protein-evaluation
gene: "G3BP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## G3BP1 — REJECTED (研究热度过高 (PubMed strict=561，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | G3BP1 / G3BP |
| 蛋白名称 | Ras GTPase-activating protein-binding protein 1 |
| 蛋白大小 | 466 aa / 52.2 kDa |
| UniProt ID | Q13283 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm, cytosol; Perikaryon; Cytoplasm, Stress granule; N |
| 蛋白大小 | 10/10 | ×1 | 10 | 466 aa / 52.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=561 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.8; PDB: 3Q90, 4FCJ, 4FCM, 4IIA, 5FW5, 6TA7, 7S17 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR034374, IPR032710, IPR002075, IPR018222, IPR012 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Enhanced |
| UniProt | Cytoplasm, cytosol; Perikaryon; Cytoplasm, Stress granule; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic stress granule (GO:0010494)
- cytosol (GO:0005829)
- focal adhesion (GO:0005925)
- nucleus (GO:0005634)
- perikaryon (GO:0043204)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 561 |
| PubMed broad count | 788 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: G3BP |

**关键文献**:
1. G3BP1 Is a Tunable Switch that Triggers Phase Separation to Assemble Stress Granules.. *Cell*. PMID: 32302571
2. Ubiquitination of G3BP1 mediates stress granule disassembly in a context-specific manner.. *Science (New York, N.Y.)*. PMID: 34739333
3. Stress granule homeostasis is modulated by TRIM21-mediated ubiquitination of G3BP1 and autophagy-dependent elimination of stress granules.. *Autophagy*. PMID: 36692217
4. QKI shuttles internal m(7)G-modified transcripts into stress granules and modulates mRNA metabolism.. *Cell*. PMID: 37379838
5. G3BP1 promotes DNA binding and activation of cGAS.. *Nature immunology*. PMID: 30510222

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.8 |
| 高置信度残基 (pLDDT>90) 占比 | 27.5% |
| 置信残基 (pLDDT 70-90) 占比 | 17.4% |
| 中等置信 (pLDDT 50-70) 占比 | 12.4% |
| 低置信 (pLDDT<50) 占比 | 42.7% |
| 有序区域 (pLDDT>70) 占比 | 44.9% |
| 可用 PDB 条目 | 3Q90, 4FCJ, 4FCM, 4IIA, 5FW5, 6TA7, 7S17, 7SUO, 7XHF, 7XHG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.8），有序残基占 44.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034374, IPR032710, IPR002075, IPR018222, IPR012677; Pfam: PF02136, PF00076 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CAPRIN1 | 0.999 | 0.987 | — |
| USP10 | 0.999 | 0.987 | — |
| TIA1 | 0.998 | 0.292 | — |
| TIAL1 | 0.996 | 0.292 | — |
| PABPC1 | 0.995 | 0.784 | — |
| RASA1 | 0.994 | 0.292 | — |
| EIF4G1 | 0.991 | 0.621 | — |
| G3BP2 | 0.987 | 0.872 | — |
| EIF3B | 0.983 | 0.432 | — |
| TARDBP | 0.983 | 0.629 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000504627.1 | psi-mi:"MI:0966"(ultraviolet-visible spectroscopy) | imex:IM-28817|pubmed:33495715 |
| PUF60 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NME2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1257125 | psi-mi:"MI:0096"(pull down) | pubmed:19463016|imex:IM-17246 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| EPHA8 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| DTX1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.8 + PDB: 3Q90, 4FCJ, 4FCM, 4IIA, 5FW5,  | pLDDT=66.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Perikaryon; Cytoplasm, Stress  / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. G3BP1 — Ras GTPase-activating protein-binding protein 1，研究基础较多，新颖性有限。
2. 蛋白大小466 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 561 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 561 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13283
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145907-G3BP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=G3BP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13283
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (enhanced)。来源: https://www.proteinatlas.org/ENSG00000145907-G3BP1/subcellular

![](https://images.proteinatlas.org/4052/26_D12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/4052/26_D12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/4052/27_D12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/4052/27_D12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/4052/28_D12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/4052/28_D12_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13283-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
