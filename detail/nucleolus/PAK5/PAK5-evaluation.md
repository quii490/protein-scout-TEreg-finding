---
type: protein-evaluation
gene: "PAK5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PAK5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAK5 / PAK5 |
| 蛋白名称 | Serine/threonine-protein kinase PAK 6 |
| 蛋白大小 | 681 aa / 74.9 kDa |
| UniProt ID | Q9NQU5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear membrane, Mitochondria, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 681 aa / 74.9 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=73 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.0; PDB: 2C30, 2ODB, 4KS7, 4KS8, 6QDR, 6QDS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000095, IPR036936, IPR011009, IPR051931, IPR033 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear membrane, Mitochondria, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell junction (GO:0030054)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- fibrillar center (GO:0001650)
- nucleoplasm (GO:0005654)
- postsynaptic density (GO:0014069)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 73 |
| PubMed broad count | 133 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PAK5 |

**关键文献**:
1. PAK5 promotes the trastuzumab resistance by increasing HER2 nuclear accumulation in HER2-positive breast cancer.. *Cell death & disease*. PMID: 40258843
2. Differential roles and regulation of the protein kinases PAK4, PAK5 and PAK6 in melanoma cells.. *The Biochemical journal*. PMID: 35969127
3. PAK5-mediated PKM2 phosphorylation is critical for anaerobic glycolysis in endometriosis.. *Frontiers of medicine*. PMID: 39331255
4. Targeted disruption of the gene for the PAK5 kinase in mice.. *Molecular and cellular biology*. PMID: 14517284
5. PAK5 is a potential target in myelodysplastic syndrome through interacting with LMO2 and GATA1.. *Cellular and molecular biology (Noisy-le-Grand, France)*. PMID: 36905268

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.0 |
| 高置信度残基 (pLDDT>90) 占比 | 38.8% |
| 置信残基 (pLDDT 70-90) 占比 | 8.2% |
| 中等置信 (pLDDT 50-70) 占比 | 8.7% |
| 低置信 (pLDDT<50) 占比 | 44.3% |
| 有序区域 (pLDDT>70) 占比 | 47.0% |
| 可用 PDB 条目 | 2C30, 2ODB, 4KS7, 4KS8, 6QDR, 6QDS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.0），有序残基占 47.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000095, IPR036936, IPR011009, IPR051931, IPR033923; Pfam: PF00786, PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC42 | 0.996 | 0.763 | — |
| NCK1 | 0.946 | 0.171 | — |
| RAC2 | 0.940 | 0.303 | — |
| ARHGEF7 | 0.939 | 0.113 | — |
| ARHGEF6 | 0.934 | 0.113 | — |
| RAC3 | 0.934 | 0.303 | — |
| ROBO2 | 0.929 | 0.071 | — |
| ROBO1 | 0.922 | 0.071 | — |
| LIMK1 | 0.919 | 0.076 | — |
| NCK2 | 0.918 | 0.171 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| eef1a1o.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| hdlbp.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| LZTS2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TUBGCP4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PDLIM7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCDC59 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| S100A9 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| S100A7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HIGD1A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.0 + PDB: 2C30, 2ODB, 4KS7, 4KS8, 6QDR,  | pLDDT=66.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Nuclear membrane, Mitochondria, C | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PAK5 — Serine/threonine-protein kinase PAK 6，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小681 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 73 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=66.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQU5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101349-PAK5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAK5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQU5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000101349-PAK5/subcellular

![](https://images.proteinatlas.org/20444/2122_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/20444/2122_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/20444/284_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/20444/284_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/20444/286_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/20444/286_A3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NQU5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
