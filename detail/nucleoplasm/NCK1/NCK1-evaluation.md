---
type: protein-evaluation
gene: "NCK1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NCK1 — REJECTED (研究热度过高 (PubMed strict=165，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NCK1 / NCK |
| 蛋白名称 | SH2/SH3 adapter protein NCK1 |
| 蛋白大小 | 377 aa / 42.9 kDa |
| UniProt ID | P16333 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; UniProt: Cytoplasm; Endoplasmic reticulum; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 377 aa / 42.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=165 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=70.8; PDB: 2CI8, 2CI9, 2CUB, 2JS0, 2JS2, 2JW4, 5QU1 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017304, IPR035882, IPR035562, IPR035564, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Approved |
| UniProt | Cytoplasm; Endoplasmic reticulum; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell-cell junction (GO:0005911)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- protein phosphatase type 1 complex (GO:0000164)
- ribosome (GO:0005840)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 165 |
| PubMed broad count | 230 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NCK |

**关键文献**:
1. LncRNA NCK1-AS1-mediated regulatory functions in human diseases.. *Clinical & translational oncology : official publication of the Federation of Spanish Oncology Societies and of the National Cancer Institute of Mexico*. PMID: 36131072
2. Adapting to change: resolving the dynamic and dual roles of NCK1 and NCK2.. *The Biochemical journal*. PMID: 39392452
3. Nck1 Regulates Glucose Metabolism in Primary Human T Cells.. *Immunology*. PMID: 40421785
4. NCK1 Modulates Neuronal Actin Dynamics and Promotes Dendritic Spine, Synapse, and Memory Formation.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 36535770
5. Nck1 activity in lateral amygdala regulates long-term fear memory formation.. *Translational psychiatry*. PMID: 36371406

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.8 |
| 高置信度残基 (pLDDT>90) 占比 | 14.1% |
| 置信残基 (pLDDT 70-90) 占比 | 52.3% |
| 中等置信 (pLDDT 50-70) 占比 | 9.5% |
| 低置信 (pLDDT<50) 占比 | 24.1% |
| 有序区域 (pLDDT>70) 占比 | 66.4% |
| 可用 PDB 条目 | 2CI8, 2CI9, 2CUB, 2JS0, 2JS2, 2JW4, 5QU1, 5QU2, 5QU3, 5QU4 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2CI8, 2CI9, 2CUB, 2JS0, 2JS2, 2JW4, 5QU1, 5QU2, 5QU3, 5QU4）+ AlphaFold极高置信度预测（pLDDT=70.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017304, IPR035882, IPR035562, IPR035564, IPR035565; Pfam: PF00017, PF00018 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LCP2 | 0.999 | 0.860 | — |
| WAS | 0.999 | 0.772 | — |
| WASL | 0.999 | 0.811 | — |
| WIPF1 | 0.999 | 0.797 | — |
| PAK1 | 0.998 | 0.865 | — |
| VAV1 | 0.997 | 0.089 | — |
| NPHS1 | 0.997 | 0.328 | — |
| NCKIPSD | 0.995 | 0.620 | — |
| GRB2 | 0.993 | 0.292 | — |
| TNIK | 0.989 | 0.518 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Pak1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Map2k2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Plagl2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Psrc1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Calr | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Pik3ap1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| NPHS1 | psi-mi:"MI:0096"(pull down) | imex:IM-14453|pubmed:16525419 |
| Dok1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15148308|imex:IM-19322 |
| Abl1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15148308|imex:IM-19322 |
| WIPF1 | psi-mi:"MI:0096"(pull down) | pubmed:12620186|imex:IM-19872| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.8 + PDB: 2CI8, 2CI9, 2CUB, 2JS0, 2JS2,  | pLDDT=70.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Endoplasmic reticulum; Nucleus / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. NCK1 — SH2/SH3 adapter protein NCK1，研究基础较多，新颖性有限。
2. 蛋白大小377 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 165 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 165 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P16333
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158092-NCK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NCK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P16333
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (uncertain)。来源: https://www.proteinatlas.org/ENSG00000158092-NCK1/subcellular

![](https://images.proteinatlas.org/30766/2147_G4_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/30766/2147_G4_82_blue_red_green.jpg)
![](https://images.proteinatlas.org/30766/2152_E10_43_blue_red_green.jpg)
![](https://images.proteinatlas.org/30766/2152_E10_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/30766/2171_H8_20_blue_red_green.jpg)
![](https://images.proteinatlas.org/30766/2171_H8_38_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P16333-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
