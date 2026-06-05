---
type: protein-evaluation
gene: "CA13"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CA13 — REJECTED (研究热度过高 (PubMed strict=136，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CA13 |
| 蛋白名称 | Carbonic anhydrase 13 |
| 蛋白大小 | 262 aa / 29.4 kDa |
| UniProt ID | Q8N1Q1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; 额外: Nucleoplasm, Vesicles; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 262 aa / 29.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=136 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=96.8; PDB: 3CZV, 3D0N, 3DA2, 4HU1, 4KNM, 4KNN, 4QIZ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001148, IPR036398, IPR023561, IPR018338; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm, Vesicles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- myelin sheath (GO:0043209)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 136 |
| PubMed broad count | 371 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic architectures of the human hippocampus and those involved in neuropsychiatric traits.. *BMC medicine*. PMID: 39394562
2. Causal Relationships Between Epilepsy, Anti-Epileptic Drugs, and Serum Vitamin D and Vitamin D Binding Protein: A Bidirectional and Drug Target Mendelian Randomization Study.. *CNS neuroscience & therapeutics*. PMID: 39703113
3. Prognostic implications of metabolism-related genes in acute myeloid leukemia.. *Frontiers in genetics*. PMID: 39421301
4. The cell-type-specific genetic architecture of chronic pain in brain and dorsal root ganglia.. *The Journal of clinical investigation*. PMID: 41055971
5. Mesalazine and thymoquinone attenuate intestinal tumour development in Msh2(loxP/loxP) Villin-Cre mice.. *Gut*. PMID: 25429050

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.8 |
| 高置信度残基 (pLDDT>90) 占比 | 97.3% |
| 置信残基 (pLDDT 70-90) 占比 | 1.5% |
| 中等置信 (pLDDT 50-70) 占比 | 0.4% |
| 低置信 (pLDDT<50) 占比 | 0.8% |
| 有序区域 (pLDDT>70) 占比 | 98.8% |
| 可用 PDB 条目 | 3CZV, 3D0N, 3DA2, 4HU1, 4KNM, 4KNN, 4QIZ, 4QJP, 4QJX, 4QSJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3CZV, 3D0N, 3DA2, 4HU1, 4KNM, 4KNN, 4QIZ, 4QJP, 4QJX, 4QSJ）+ AlphaFold极高置信度预测（pLDDT=96.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001148, IPR036398, IPR023561, IPR018338; Pfam: PF00194 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYP24A1 | 0.854 | 0.000 | — |
| CA1 | 0.651 | 0.000 | — |
| CA2 | 0.642 | 0.000 | — |
| ALB | 0.576 | 0.000 | — |
| RPF2 | 0.561 | 0.268 | — |
| TG | 0.535 | 0.000 | — |
| RNASE1 | 0.531 | 0.000 | — |
| CA7 | 0.530 | 0.000 | — |
| CA3 | 0.530 | 0.000 | — |
| FTH1 | 0.507 | 0.053 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CRACR2B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CRTC3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.8 + PDB: 3CZV, 3D0N, 3DA2, 4HU1, 4KNM,  | pLDDT=96.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; 额外: Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

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
1. CA13 — Carbonic anhydrase 13，研究基础较多，新颖性有限。
2. 蛋白大小262 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 136 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 136 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N1Q1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185015-CA13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CA13
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N1Q1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000185015-CA13/subcellular

![](https://images.proteinatlas.org/24689/239_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/24689/239_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/24689/240_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/24689/240_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/24689/241_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/24689/241_C9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N1Q1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
