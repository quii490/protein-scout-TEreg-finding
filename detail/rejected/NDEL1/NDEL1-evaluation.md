---
type: protein-evaluation
gene: "NDEL1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NDEL1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=127，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NDEL1 / EOPA, MITAP1, NUDEL |
| 蛋白名称 | Nuclear distribution protein nudE-like 1 |
| 蛋白大小 | 345 aa / 38.4 kDa |
| UniProt ID | Q9GZM8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, microtubul |
| 蛋白大小 | 10/10 | ×1 | 10 | 345 aa / 38.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=127 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=77.4; PDB: 2V66 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033494, IPR006964; Pfam: PF04880 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **67.0/180** | |
| **归一化总分** | | | **37.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Chromos... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon cytoplasm (GO:1904115)
- axon hillock (GO:0043203)
- cell leading edge (GO:0031252)
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- kinesin complex (GO:0005871)
- kinetochore (GO:0000776)
- microtubule (GO:0005874)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 127 |
| PubMed broad count | 234 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EOPA, MITAP1, NUDEL |

**关键文献**:
1. Novel lissencephaly-associated NDEL1 variant reveals distinct roles of NDE1 and NDEL1 in nucleokinesis and human cortical malformations.. *Acta neuropathologica*. PMID: 38194050
2. Protein-Protein and Peptide-Protein Interactions of NudE-Like 1 (Ndel1): A Protein Involved in Schizophrenia.. *Current protein & peptide science*. PMID: 25961396
3. Dynein at the kinetochore.. *Journal of cell science*. PMID: 36861883
4. Nde1 and Ndel1: Outstanding Mysteries in Dynein-Mediated Transport.. *Frontiers in cell and developmental biology*. PMID: 35493069
5. Ndel1 disfavors dynein-dynactin-adaptor complex formation in two distinct ways.. *The Journal of biological chemistry*. PMID: 37086789

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.4 |
| 高置信度残基 (pLDDT>90) 占比 | 53.0% |
| 置信残基 (pLDDT 70-90) 占比 | 10.7% |
| 中等置信 (pLDDT 50-70) 占比 | 11.9% |
| 低置信 (pLDDT<50) 占比 | 24.3% |
| 有序区域 (pLDDT>70) 占比 | 63.7% |
| 可用 PDB 条目 | 2V66 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=77.4，有序区 63.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033494, IPR006964; Pfam: PF04880 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAFAH1B1 | 0.999 | 0.914 | — |
| DISC1 | 0.999 | 0.834 | — |
| NDE1 | 0.982 | 0.782 | — |
| YWHAE | 0.965 | 0.474 | — |
| NUDC | 0.940 | 0.000 | — |
| ANK2 | 0.930 | 0.920 | — |
| ARHGAP1 | 0.868 | 0.095 | — |
| PLK1 | 0.854 | 0.000 | — |
| DIXDC1 | 0.841 | 0.600 | — |
| CDK5 | 0.835 | 0.295 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000333982.7 | psi-mi:"MI:0071"(molecular sieving) | imex:IM-18003|pubmed:22843697 |
| MAGEA11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MBIP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DISC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:12812986|imex:IM-19614 |
| ZNF365 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14941|pubmed:16682949 |
| CDK1 | psi-mi:"MI:0423"(in-gel kinase assay) | imex:IM-14941|pubmed:16682949 |
| MIS18A | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| CENPF | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| DIXDC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| KALRN | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.4 + PDB: 2V66 | pLDDT=77.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton,  / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NDEL1 — Nuclear distribution protein nudE-like 1，研究基础较多，新颖性有限。
2. 蛋白大小345 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 127 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9GZM8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166579-NDEL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NDEL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9GZM8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9GZM8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
