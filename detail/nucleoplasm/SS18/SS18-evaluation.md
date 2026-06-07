---
type: protein-evaluation
gene: "SS18"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SS18 — REJECTED (研究热度过高 (PubMed strict=312，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SS18 / SSXT, SYT |
| 蛋白名称 | Protein SSXT |
| 蛋白大小 | 418 aa / 45.9 kDa |
| UniProt ID | Q15532 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 418 aa / 45.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=312 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.7; PDB: 7VRB |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007726; Pfam: PF05030 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- GBAF complex (GO:0140288)
- microtubule cytoskeleton (GO:0015630)
- npBAF complex (GO:0071564)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- SWI/SNF complex (GO:0016514)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 312 |
| PubMed broad count | 554 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SSXT, SYT |

**关键文献**:
1. Genomic analyses identify recurrent MEF2D fusions in acute lymphoblastic leukaemia.. *Nature communications*. PMID: 27824051
2. Molecular Profiling Defines Three Subtypes of Synovial Sarcoma.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39257029
3. Advances of SS18-SSX fusion gene in synovial sarcoma: Emerging novel functions and therapeutic potentials.. *Biochimica et biophysica acta. Reviews on cancer*. PMID: 39528099
4. Synovial sarcoma: the misdiagnosed sarcoma.. *EFORT open reviews*. PMID: 38457918
5. DNA demethylating agents suppress preclinical models of synovial sarcoma.. *The Journal of clinical investigation*. PMID: 40299558

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.7 |
| 高置信度残基 (pLDDT>90) 占比 | 10.8% |
| 置信残基 (pLDDT 70-90) 占比 | 2.4% |
| 中等置信 (pLDDT 50-70) 占比 | 31.3% |
| 低置信 (pLDDT<50) 占比 | 55.5% |
| 有序区域 (pLDDT>70) 占比 | 13.2% |
| 可用 PDB 条目 | 7VRB |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.7），有序残基占 13.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007726; Pfam: PF05030 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMARCE1 | 0.999 | 0.994 | — |
| BCL7C | 0.999 | 0.994 | — |
| SMARCA4 | 0.996 | 0.914 | — |
| SMARCA2 | 0.996 | 0.896 | — |
| SMARCB1 | 0.995 | 0.921 | — |
| ARID1A | 0.993 | 0.922 | — |
| SMARCD2 | 0.991 | 0.894 | — |
| SMARCC1 | 0.991 | 0.874 | — |
| SMARCD1 | 0.991 | 0.891 | — |
| ACTL6A | 0.991 | 0.792 | — |

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
| 三维结构 | AlphaFold pLDDT=53.7 + PDB: 7VRB | pLDDT=53.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SS18 — Protein SSXT，研究基础较多，新颖性有限。
2. 蛋白大小418 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 312 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=53.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 312 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15532
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141380-SS18/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SS18
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15532
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000141380-SS18/subcellular

![](https://images.proteinatlas.org/59539/1164_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/59539/1164_D6_3_red_green.jpg)
![](https://images.proteinatlas.org/59539/1174_D6_3_red_green.jpg)
![](https://images.proteinatlas.org/59539/1174_D6_4_red_green.jpg)
![](https://images.proteinatlas.org/59539/1368_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/59539/1368_F1_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15532-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q15532 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR007726; |
| Pfam | PF05030; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000141380-SS18/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARID1A | Biogrid, Opencell | true |
| ATF2 | Intact, Biogrid | true |
| SMARCA4 | Intact, Biogrid, Opencell | true |
| SMARCD1 | Biogrid, Opencell | true |
| SMARCD2 | Biogrid, Opencell | true |
| SMARCE1 | Biogrid, Opencell | true |
| ACTG1 | Opencell | false |
| ACTL6A | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
