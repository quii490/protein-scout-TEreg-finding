---
type: protein-evaluation
gene: "C8orf76"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C8orf76 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C8orf76 / C8orf76 |
| 蛋白名称 | Zinc fingers and homeoboxes protein 1, isoform 2 |
| 蛋白大小 | 292 aa / 33.3 kDa |
| UniProt ID | Q96EF9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 292 aa / 33.3 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.7; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR041404, IPR011990; Pfam: PF17826 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C8orf76 |

**关键文献**:
1. Development of a breast cancer invasion score to predict tumor aggressiveness and prognosis via PI3K/AKT/mTOR pathway analysis.. *Cell death discovery*. PMID: 40204712
2. C8orf76 Modulates Ferroptosis in Liver Cancer via Transcriptionally Up-Regulating SLC7A11.. *Cancers*. PMID: 35884471
3. High Expression of C8orf76 Is an Independent Predictive Factor of Poor Prognosis in Patients with Breast Cancer.. *Advances in therapy*. PMID: 35482249
4. Chromosome 8 Open Reading Frame 76 (C8orf76) Co-Expressed with Cyclin-Dependent Kinase 4 (CDK4) as a Prognostic Indicator of Colorectal Cancer.. *Biomedical and environmental sciences : BES*. PMID: 40928275
5. Multi-omics pan-cancer analysis reveals the diagnostic and prognostic value of C8orf76, with experimental validation of its impact on lung adenocarcinoma cell proliferation.. *Frontiers in genetics*. PMID: 40206508

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.7 |
| 高置信度残基 (pLDDT>90) 占比 | 52.4% |
| 置信残基 (pLDDT 70-90) 占比 | 18.2% |
| 中等置信 (pLDDT 50-70) 占比 | 13.0% |
| 低置信 (pLDDT<50) 占比 | 16.4% |
| 有序区域 (pLDDT>70) 占比 | 70.6% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.7，有序区 70.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041404, IPR011990; Pfam: PF17826 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NSMCE2 | 0.498 | 0.000 | — |
| ZNF623 | 0.497 | 0.000 | — |
| COMMD5 | 0.497 | 0.000 | — |
| TIGD5 | 0.477 | 0.000 | — |
| POP1 | 0.473 | 0.000 | — |
| NUDCD1 | 0.466 | 0.000 | — |
| C8orf33 | 0.465 | 0.000 | — |
| FAM83H | 0.462 | 0.000 | — |
| MTERF3 | 0.437 | 0.000 | — |
| UBR5 | 0.437 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZHX1-C8orf76 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HTT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ZDHHC17 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ANXA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| PAK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| CRYAA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| DLST | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| CALR | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| DYNC1H1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| FECH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 1 / 13 = 8%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 8%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.7 + PDB: 无 | pLDDT=78.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. C8orf76 — Zinc fingers and homeoboxes protein 1, isoform 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小292 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96EF9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000189376-C8orf76/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C8orf76
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96EF9
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:28:11

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000189376-C8orf76/subcellular

![](https://images.proteinatlas.org/23708/236_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/23708/236_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/23708/237_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/23708/237_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/23708/268_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/23708/268_D12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96EF9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
