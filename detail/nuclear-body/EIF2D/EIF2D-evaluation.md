---
type: protein-evaluation
gene: "EIF2D"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EIF2D 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF2D |
| 蛋白名称 | Eukaryotic translation initiation factor 2D |
| 蛋白大小 | 584 aa / 64.7 kDa |
| UniProt ID | P41214 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nuclear bodies; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 584 aa / 64.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.1; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 25 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.5/180** | |
| **归一化总分** | | | **55.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nuclear bodies | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 48 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Study on the molecular mechanism of dietary FCE supplementation in regulating chicken meat quality.. *Gene*. PMID: 41173221
2. RNA m(5)C Modifications in the Development and Prognosis of Muscle-Invasive Bladder Cancer.. *Mol Carcinog*. PMID: 40994220
3. eIF2D promotes 40S ribosomal subunit recycling during intrinsic ribosome destabilization.. *Nucleic Acids Res*. PMID: 41335470
4. In Search of Novel Diagnostic Biomarkers for Psychoneurological and Neurodegenerative Diseases: Translation Factors DENR and eIF2D.. *Biochemistry (Mosc)*. PMID: 41354083
5. Loss of non-canonical translation initiation factors impairs perinatal cardiac function in mice.. *Exp Anim*. PMID: 40350286

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.1 |
| 高置信度残基 (pLDDT>90) 占比 | 30.0% |
| 置信残基 (pLDDT 70-90) 占比 | 44.2% |
| 中等置信 (pLDDT 50-70) 占比 | 10.6% |
| 低置信 (pLDDT<50) 占比 | 15.2% |
| 有序区域 (pLDDT>70) 占比 | 74.2% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=76.1，有序区 74.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF1 | 0.000 | 0.000 | — |
| DENR | 0.000 | 0.000 | — |
| RPS25 | 0.000 | 0.000 | — |
| RACK1 | 0.000 | 0.000 | — |
| RPS16 | 0.000 | 0.000 | — |
| RPS3 | 0.000 | 0.000 | — |
| RPS13 | 0.000 | 0.000 | — |
| RPS4X | 0.000 | 0.000 | — |
| RPS6 | 0.000 | 0.000 | — |
| RPS7 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q06609 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:P41214 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P11142 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:A1L106 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9VPM1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| intact:EBI-25426411 | psi-mi:"MI:2195"(clash) | pubmed:- |
| intact:EBI-20560157 | psi-mi:"MI:2195"(clash) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 25
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 25 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.1 + PDB: 无 | pLDDT=76.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 25 + 25 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EIF2D — Eukaryotic translation initiation factor 2D，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小584 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P41214
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143486-EIF2D/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF2D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P41214
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P41214 |
| SMART | SM00359; |
| UniProt Domain [FT] | DOMAIN 93..173; /note="PUA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00161"; DOMAIN 383..467; /note="SWIB/MDM2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01273"; DOMAIN 491..564; /note="SUI1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00200" |
| InterPro | IPR039757;IPR048247;IPR039759;IPR041366;IPR002478;IPR015947;IPR048248;IPR001950;IPR036877;IPR058886;IPR036885;IPR003121;IPR057429; |
| Pfam | PF17832;PF26292;PF01253;PF26291;PF25304; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000143486-EIF2D/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EIF1 | Biogrid | false |
| EIF1B | Biogrid | false |
| HARS1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
