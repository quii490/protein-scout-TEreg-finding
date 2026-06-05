---
type: protein-evaluation
gene: "HES4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HES4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HES4 / BHLHB42 |
| 蛋白名称 | Transcription factor HES-4 |
| 蛋白大小 | 221 aa / 23.5 kDa |
| UniProt ID | Q9HCC6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 221 aa / 23.5 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=53 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050370, IPR036638, IPR003650; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 53 |
| PubMed broad count | 96 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHB42 |

**关键文献**:
1. Inferring and perturbing cell fate regulomes in human brain organoids.. *Nature*. PMID: 36198796
2. RNAi screens identify HES4 as a regulator of redox balance supporting pyrimidine synthesis and tumor growth.. *Nature structural & molecular biology*. PMID: 38769389
3. Glycosyltransferase B4GALNT1 promotes immunosuppression in hepatocellular carcinoma via the HES4-SPP1-TAM/Th2 axis.. *Molecular biomedicine*. PMID: 39616302
4. HES1 and HES4 have non-redundant roles downstream of Notch during early human T-cell development.. *Haematologica*. PMID: 31919081
5. NOTCH1 dimeric signaling is essential for T-cell leukemogenesis and leukemia maintenance.. *Blood*. PMID: 40009499

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.0 |
| 高置信度残基 (pLDDT>90) 占比 | 31.2% |
| 置信残基 (pLDDT 70-90) 占比 | 20.8% |
| 中等置信 (pLDDT 50-70) 占比 | 33.5% |
| 低置信 (pLDDT<50) 占比 | 14.5% |
| 有序区域 (pLDDT>70) 占比 | 52.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.0，有序区 52.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050370, IPR036638, IPR003650; Pfam: PF07527, PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NRARP | 0.632 | 0.071 | — |
| JAG2 | 0.586 | 0.072 | — |
| NOTCH3 | 0.576 | 0.072 | — |
| NOTCH1 | 0.570 | 0.071 | — |
| DLL1 | 0.564 | 0.072 | — |
| JAG1 | 0.526 | 0.072 | — |
| DTX1 | 0.515 | 0.071 | — |
| MAML1 | 0.513 | 0.000 | — |
| NOTCH2 | 0.499 | 0.072 | — |
| DLL4 | 0.492 | 0.072 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LTN1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| ZC3H13 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| HSP90AB1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| RGS3 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| CMSS1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| KIF5C | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| LRRIQ1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| COPG2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| EEF1B2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| ATP13A4 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.0 + PDB: 无 | pLDDT=72.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. HES4 — Transcription factor HES-4，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小221 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 53 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HCC6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188290-HES4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HES4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HCC6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000188290-HES4/subcellular

![](https://images.proteinatlas.org/62465/1191_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/62465/1191_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/62465/1194_F7_3_red_green.jpg)
![](https://images.proteinatlas.org/62465/1194_F7_5_red_green.jpg)
![](https://images.proteinatlas.org/62465/1273_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/62465/1273_H2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HCC6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
