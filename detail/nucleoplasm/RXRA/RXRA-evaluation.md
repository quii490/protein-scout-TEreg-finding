---
type: protein-evaluation
gene: "RXRA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RXRA — REJECTED (研究热度过高 (PubMed strict=345，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RXRA / NR2B1 |
| 蛋白名称 | Retinoic acid receptor RXR-alpha |
| 蛋白大小 | 462 aa / 50.8 kDa |
| UniProt ID | P19793 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus; UniProt: Nucleus; Cytoplasm; Mitochondrion |
| 蛋白大小 | 10/10 | ×1 | 10 | 462 aa / 50.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=345 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=75.4; PDB: 1BY4, 1DSZ, 1FBY, 1FM6, 1FM9, 1G1U, 1G5Y |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035500, IPR021780, IPR000536, IPR050274, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus | Supported |
| UniProt | Nucleus; Cytoplasm; Mitochondrion | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- receptor complex (GO:0043235)
- RNA polymerase II transcription regulator complex (GO:0090575)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 345 |
| PubMed broad count | 545 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NR2B1 |

**关键文献**:
1. Evolutionary history of sickle-cell mutation: implications for global genetic medicine.. *Human molecular genetics*. PMID: 33461216
2. UBR5 forms ligand-dependent complexes on chromatin to regulate nuclear hormone receptor stability.. *Molecular cell*. PMID: 37478846
3. Pericytes recruited by CCL28 promote vascular normalization after anti-angiogenesis therapy through RA/RXRA/ANGPT1 pathway in lung adenocarcinoma.. *Journal of experimental & clinical cancer research : CR*. PMID: 39075504
4. The Duck RXRA Gene Promotes Adipogenesis and Correlates with Feed Efficiency.. *Animals : an open access journal from MDPI*. PMID: 36830469
5. TERC Stimulates Fatty Acid Metabolism to Promote Bladder Cancer Progression.. *Cancer research*. PMID: 40759031

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.4 |
| 高置信度残基 (pLDDT>90) 占比 | 54.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.1% |
| 低置信 (pLDDT<50) 占比 | 29.7% |
| 有序区域 (pLDDT>70) 占比 | 63.2% |
| 可用 PDB 条目 | 1BY4, 1DSZ, 1FBY, 1FM6, 1FM9, 1G1U, 1G5Y, 1K74, 1MV9, 1MVC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1BY4, 1DSZ, 1FBY, 1FM6, 1FM9, 1G1U, 1G5Y, 1K74, 1MV9, 1MVC）+ AlphaFold极高置信度预测（pLDDT=75.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035500, IPR021780, IPR000536, IPR050274, IPR001723; Pfam: PF00104, PF11825, PF00105 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NR1H4 | 0.999 | 0.973 | — |
| NCOA1 | 0.999 | 0.995 | — |
| PPARA | 0.999 | 0.840 | — |
| NR1I2 | 0.999 | 0.970 | — |
| RARA | 0.999 | 0.991 | — |
| NCOA2 | 0.999 | 0.991 | — |
| NR1H3 | 0.999 | 0.986 | — |
| PPARG | 0.999 | 0.999 | — |
| NR1H2 | 0.998 | 0.909 | — |
| NCOR2 | 0.996 | 0.982 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.4 + PDB: 1BY4, 1DSZ, 1FBY, 1FM6, 1FM9,  | pLDDT=75.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Mitochondrion / Nucleoplasm; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. RXRA — Retinoic acid receptor RXR-alpha，研究基础较多，新颖性有限。
2. 蛋白大小462 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 345 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 345 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P19793
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186350-RXRA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RXRA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P19793
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000186350-RXRA/subcellular

![](https://images.proteinatlas.org/5352/635_G3_1_red_green.jpg)
![](https://images.proteinatlas.org/5352/635_G3_2_red_green.jpg)
![](https://images.proteinatlas.org/5352/639_G3_1_red_green.jpg)
![](https://images.proteinatlas.org/5352/639_G3_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P19793-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P19793 |
| SMART | SM00430;SM00399; |
| UniProt Domain [FT] | DOMAIN 227..458; /note="NR LBD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01189" |
| InterPro | IPR035500;IPR021780;IPR000536;IPR050274;IPR001723;IPR000003;IPR001628;IPR013088; |
| Pfam | PF00104;PF11825;PF00105; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000186350-RXRA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MED1 | Intact, Biogrid | true |
| MED25 | Intact, Biogrid | true |
| NCOA1 | Intact, Biogrid | true |
| NCOA2 | Intact, Biogrid | true |
| NR1H2 | Intact, Biogrid | true |
| NR1H3 | Intact, Biogrid | true |
| PPARG | Intact, Biogrid | true |
| RARA | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
