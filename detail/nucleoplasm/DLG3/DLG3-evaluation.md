---
type: protein-evaluation
gene: "DLG3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DLG3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DLG3 / KIAA1232 |
| 蛋白名称 | Disks large homolog 3 |
| 蛋白大小 | 817 aa / 90.3 kDa |
| UniProt ID | Q92796 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 817 aa / 90.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=72 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=73.8; PDB: 1UM7, 2FE5, 2I1N |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019583, IPR016313, IPR019590, IPR035763, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **97.0/180** | |
| **归一化总分** | | | **53.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- AMPA glutamate receptor complex (GO:0032281)
- basolateral plasma membrane (GO:0016323)
- bicellular tight junction (GO:0005923)
- cytosol (GO:0005829)
- extracellular space (GO:0005615)
- glutamatergic synapse (GO:0098978)
- neuromuscular junction (GO:0031594)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 72 |
| PubMed broad count | 163 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1232 |

**关键文献**:
1. Further phenotypical delineation of DLG3-related neurodevelopmental disorders.. *European journal of human genetics : EJHG*. PMID: 40983642
2. COP1 facilitates the proliferation, invasion, and migration of glioma cells by ubiquitination of DLG3 protein.. *Neurological research*. PMID: 37356109
3. DLG3 variants caused X-linked epilepsy with/without neurodevelopmental disorders and the genotype-phenotype correlation.. *Frontiers in molecular neuroscience*. PMID: 38249294
4. Multifaceted roles of DLG3/SAP102 in neurophysiology, neurological disorders and tumorigenesis.. *Neuroscience*. PMID: 39638232
5. Dlg3 trafficking and apical tight junction formation is regulated by nedd4 and nedd4-2 e3 ubiquitin ligases.. *Developmental cell*. PMID: 21920314

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.8 |
| 高置信度残基 (pLDDT>90) 占比 | 47.5% |
| 置信残基 (pLDDT 70-90) 占比 | 20.4% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 28.8% |
| 有序区域 (pLDDT>70) 占比 | 67.9% |
| 可用 PDB 条目 | 1UM7, 2FE5, 2I1N |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1UM7, 2FE5, 2I1N）+ AlphaFold高质量预测（pLDDT=73.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019583, IPR016313, IPR019590, IPR035763, IPR008145; Pfam: PF00625, PF00595, PF10600 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GRIN2B | 0.998 | 0.739 | — |
| GRIN2A | 0.998 | 0.506 | — |
| DLG4 | 0.997 | 0.547 | — |
| DLG2 | 0.984 | 0.217 | — |
| DLG1 | 0.974 | 0.606 | — |
| NBEA | 0.963 | 0.169 | — |
| SYNGAP1 | 0.946 | 0.379 | — |
| NEDD4 | 0.946 | 0.095 | — |
| LRFN2 | 0.944 | 0.143 | — |
| LLGL1 | 0.939 | 0.050 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Kcnj12 | psi-mi:"MI:0096"(pull down) | pubmed:15024025 |
| Dlgap1 | psi-mi:"MI:0018"(two hybrid) | pubmed:9115257 |
| Dlgap2 | psi-mi:"MI:0018"(two hybrid) | pubmed:9115257 |
| Dlgap3 | psi-mi:"MI:0018"(two hybrid) | pubmed:9115257 |
| Dlgap4 | psi-mi:"MI:0018"(two hybrid) | pubmed:9115257 |
| Dynll1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14760703 |
| MPP3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NOA1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ABCA1 | psi-mi:"MI:0081"(peptide array) | pubmed:16192269|imex:IM-20073 |
| ATP2B4 | psi-mi:"MI:0096"(pull down) | pubmed:11274188|imex:IM-19015| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.8 + PDB: 1UM7, 2FE5, 2I1N | pLDDT=73.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DLG3 — Disks large homolog 3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小817 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 72 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92796
- Protein Atlas: https://www.proteinatlas.org/ENSG00000082458-DLG3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DLG3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92796
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000082458-DLG3/subcellular

![](https://images.proteinatlas.org/78130/1704_B8_27_cr57d8446cdb816_red_green.jpg)
![](https://images.proteinatlas.org/78130/1704_B8_7_cr57d8445d770d4_red_green.jpg)
![](https://images.proteinatlas.org/78130/1747_H3_18_cr58063a49a69b3_red_green.jpg)
![](https://images.proteinatlas.org/78130/1747_H3_6_cr58063a4019af8_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92796-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
