---
type: protein-evaluation
gene: "SS18L1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SS18L1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SS18L1 / CREST, KIAA0693 |
| 蛋白名称 | Calcium-responsive transactivator |
| 蛋白大小 | 396 aa / 43.0 kDa |
| UniProt ID | O75177 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus; Chromosome, centromere, kinetochore |
| 蛋白大小 | 10/10 | ×1 | 10 | 396 aa / 43.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007726; Pfam: PF05030 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Nucleus; Chromosome, centromere, kinetochore | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- kinetochore (GO:0000776)
- nBAF complex (GO:0071565)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CREST, KIAA0693 |

**关键文献**:
1. Identification of novel SSX1 fusions in synovial sarcoma.. *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc*. PMID: 34504309
2. Common origin of the human synovial sarcoma associated SS18 and SS18L1 gene loci.. *Cytogenetic and genome research*. PMID: 16484776
3. Transcription factor SS18L1 regulates the proliferation, migration and differentiation of Schwann cells in peripheral nerve injury.. *Frontiers in veterinary science*. PMID: 36046506
4. Longitudinal genetic studies of cognitive characteristics.. *Vavilovskii zhurnal genetiki i selektsii*. PMID: 33659785
5. Identification of a novel MEF2C::SS18L1 fusion in childhood acute B-lymphoblastic leukemia.. *Journal of cancer research and clinical oncology*. PMID: 38907739

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.0 |
| 高置信度残基 (pLDDT>90) 占比 | 11.4% |
| 置信残基 (pLDDT 70-90) 占比 | 1.8% |
| 中等置信 (pLDDT 50-70) 占比 | 14.9% |
| 低置信 (pLDDT<50) 占比 | 72.0% |
| 有序区域 (pLDDT>70) 占比 | 13.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=51.0），有序残基占 13.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007726; Pfam: PF05030 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DPF3 | 0.973 | 0.836 | — |
| DPF2 | 0.972 | 0.840 | — |
| DPF1 | 0.970 | 0.694 | — |
| SMARCD1 | 0.964 | 0.837 | — |
| SMARCE1 | 0.946 | 0.847 | — |
| SMARCC2 | 0.934 | 0.817 | — |
| ACTL6B | 0.928 | 0.076 | — |
| ARID1A | 0.887 | 0.624 | — |
| BCL7C | 0.884 | 0.737 | — |
| SSX1 | 0.878 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000333012.3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| RFX6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SF3B4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| USP30 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| SMARCB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31759698|imex:IM-27540 |
| TNK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| C1orf94 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MAPK1IP1L | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| USP54 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.0 + PDB: 无 | pLDDT=51.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere, kinetochore / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SS18L1 — Calcium-responsive transactivator，非常新颖，仅有少数基础研究。
2. 蛋白大小396 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=51.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75177
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184402-SS18L1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SS18L1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75177
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000184402-SS18L1/subcellular

![](https://images.proteinatlas.org/11827/613_A8_2_red_green.jpg)
![](https://images.proteinatlas.org/11827/613_A8_3_red_green.jpg)
![](https://images.proteinatlas.org/11827/617_A8_4_red_green.jpg)
![](https://images.proteinatlas.org/11827/617_A8_5_red_green.jpg)
![](https://images.proteinatlas.org/59046/1060_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/59046/1060_D9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75177-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
