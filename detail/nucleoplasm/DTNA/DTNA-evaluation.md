---
type: protein-evaluation
gene: "DTNA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DTNA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DTNA / DRP3 |
| 蛋白名称 | Dystrobrevin alpha |
| 蛋白大小 | 743 aa / 83.9 kDa |
| UniProt ID | Q9Y4J8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cell Junctions, Intermediate filaments; 额外: Nucleoplasm; UniProt: Cytoplasm; Synapse; Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 743 aa / 83.9 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.0; PDB: 2E5R |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017432, IPR011992, IPR015153, IPR015154, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cell Junctions, Intermediate filaments; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm; Synapse; Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axon (GO:0030424)
- cell junction (GO:0030054)
- cytoplasm (GO:0005737)
- extrinsic component of cytoplasmic side of plasma membrane (GO:0031234)
- intermediate filament cytoskeleton (GO:0045111)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 62 |
| PubMed broad count | 121 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DRP3 |

**关键文献**:
1. Epidemiology and genetics of Meniere's disease.. *Current opinion in neurology*. PMID: 37865853
2. Melatonin alleviates depression-like behaviors and cognitive dysfunction in mice by regulating the circadian rhythm of AQP4 polarization.. *Translational psychiatry*. PMID: 37802998
3. Whole genome sequencing delineates regulatory, copy number, and cryptic splice variants in early onset cardiomyopathy.. *NPJ genomic medicine*. PMID: 35288587
4. Genetic architecture of Meniere's disease.. *Hearing research*. PMID: 31874721
5. Melatonin Mitigates Sleep Restriction-Induced Cognitive and Glymphatic Dysfunction Via Aquaporin-4 Polarization.. *Molecular neurobiology*. PMID: 40293704

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.0 |
| 高置信度残基 (pLDDT>90) 占比 | 33.8% |
| 置信残基 (pLDDT 70-90) 占比 | 23.3% |
| 中等置信 (pLDDT 50-70) 占比 | 11.8% |
| 低置信 (pLDDT<50) 占比 | 31.1% |
| 有序区域 (pLDDT>70) 占比 | 57.1% |
| 可用 PDB 条目 | 2E5R |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.0），有序残基占 57.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017432, IPR011992, IPR015153, IPR015154, IPR050774; Pfam: PF09068, PF09069, PF00569 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SSPN | 0.990 | 0.000 | — |
| DMD | 0.988 | 0.827 | — |
| SYNC | 0.987 | 0.000 | — |
| SNTA1 | 0.984 | 0.716 | — |
| SNTB2 | 0.974 | 0.749 | — |
| DAG1 | 0.974 | 0.000 | — |
| SNTB1 | 0.946 | 0.664 | — |
| SNTG2 | 0.945 | 0.744 | — |
| UTRN | 0.926 | 0.785 | — |
| SGCA | 0.901 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=69.0 + PDB: 2E5R | pLDDT=69.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Synapse; Cell membrane / Cell Junctions, Intermediate filaments; 额外: Nucleo | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DTNA — Dystrobrevin alpha，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小743 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y4J8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134769-DTNA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DTNA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y4J8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cell Junctions (supported)。来源: https://www.proteinatlas.org/ENSG00000134769-DTNA/subcellular

![](https://images.proteinatlas.org/71177/1357_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/71177/1357_D2_3_red_green.jpg)
![](https://images.proteinatlas.org/71177/1359_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/71177/1359_D2_3_red_green.jpg)
![](https://images.proteinatlas.org/71177/1564_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/71177/1564_D3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y4J8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
