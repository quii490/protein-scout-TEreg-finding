---
type: protein-evaluation
gene: "HDC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HDC — REJECTED (研究热度过高 (PubMed strict=579，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HDC |
| 蛋白名称 | Histidine decarboxylase |
| 蛋白大小 | 662 aa / 74.1 kDa |
| UniProt ID | P19113 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 662 aa / 74.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=579 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=80.4; PDB: 4E1O, 7EIW, 7EIX, 7EIY |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR010977, IPR002129, IPR015424, IPR015421, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.0/180** | |
| **归一化总分** | | | **45.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 579 |
| PubMed broad count | 2895 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Histamine pharmacogenomics.. *Pharmacogenomics*. PMID: 19450133
2. Contribution of cuproptosis and immune-related genes to idiopathic pulmonary fibrosis disease.. *Frontiers in immunology*. PMID: 39991151
3. Histidine decarboxylase inhibition attenuates cancer-associated muscle wasting.. *The Journal of experimental medicine*. PMID: 40600951
4. The Hdc GC box is critical for Hdc gene transcription and histamine-mediated anaphylaxis.. *The Journal of allergy and clinical immunology*. PMID: 36804390
5. Glucocorticoids, genes and brain function.. *Progress in neuro-psychopharmacology & biological psychiatry*. PMID: 29180230

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.4 |
| 高置信度残基 (pLDDT>90) 占比 | 71.9% |
| 置信残基 (pLDDT 70-90) 占比 | 0.6% |
| 中等置信 (pLDDT 50-70) 占比 | 0.3% |
| 低置信 (pLDDT<50) 占比 | 27.2% |
| 有序区域 (pLDDT>70) 占比 | 72.5% |
| 可用 PDB 条目 | 4E1O, 7EIW, 7EIX, 7EIY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4E1O, 7EIW, 7EIX, 7EIY）+ AlphaFold高质量预测（pLDDT=80.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010977, IPR002129, IPR015424, IPR015421, IPR015422; Pfam: PF00282 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HNMT | 0.966 | 0.000 | — |
| AOC1 | 0.963 | 0.000 | — |
| CNDP2 | 0.952 | 0.000 | — |
| HAL | 0.944 | 0.000 | — |
| CNDP1 | 0.929 | 0.000 | — |
| CARNS1 | 0.921 | 0.000 | — |
| CPA3 | 0.883 | 0.000 | — |
| MS4A2 | 0.819 | 0.000 | — |
| HRH2 | 0.799 | 0.000 | — |
| HRH1 | 0.798 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CycK | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| IKBKG | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| heca | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| EndoA | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Bub1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG14113 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| unk | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15821|pubmed:22068330 |
| CFTR | psi-mi:"MI:0096"(pull down) | pubmed:29924966|imex:IM-27204 |
| ALDH3A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ALDH2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.4 + PDB: 4E1O, 7EIW, 7EIX, 7EIY | pLDDT=80.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HDC — Histidine decarboxylase，研究基础较多，新颖性有限。
2. 蛋白大小662 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 579 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 579 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P19113
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140287-HDC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HDC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P19113
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000140287-HDC/subcellular

![](https://images.proteinatlas.org/38891/1847_G7_61_blue_red_green.jpg)
![](https://images.proteinatlas.org/38891/1847_G7_62_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P19113-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
