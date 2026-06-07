---
type: protein-evaluation
gene: "ALKBH5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ALKBH5 — REJECTED (研究热度过高 (PubMed strict=689，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ALKBH5 / ABH5, OFOXD1 |
| 蛋白名称 | RNA demethylase ALKBH5 |
| 蛋白大小 | 394 aa / 44.3 kDa |
| UniProt ID | Q6P6C2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Golgi apparatus; UniProt: Nucleus speckle; Nucleus, nucleoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 394 aa / 44.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=689 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=72.2; PDB: 4NJ4, 4NRM, 4NRO, 4NRP, 4NRQ, 4O61, 4O7X |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027450, IPR037151, IPR032860; Pfam: PF13532 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Golgi apparatus | Approved |
| UniProt | Nucleus speckle; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- paraspeckles (GO:0042382)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 689 |
| PubMed broad count | 1154 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ABH5, OFOXD1 |

**关键文献**:
1. Liver ALKBH5 regulates glucose and lipid homeostasis independently through GCGR and mTORC1 signaling.. *Science (New York, N.Y.)*. PMID: 40014709
2. ALKBH5-mediated m6A modification of IL-11 drives macrophage-to-myofibroblast transition and pathological cardiac fibrosis in mice.. *Nature communications*. PMID: 38443404
3. Lactylation of HDAC1 Confers Resistance to Ferroptosis in Colorectal Cancer.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39888307
4. RNA demethylase ALKBH5 in cancer: from mechanisms to therapeutic potential.. *Journal of hematology & oncology*. PMID: 35063010
5. eIF3d controls the persistent integrated stress response.. *Molecular cell*. PMID: 37683648

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.2 |
| 高置信度残基 (pLDDT>90) 占比 | 46.4% |
| 置信残基 (pLDDT 70-90) 占比 | 7.4% |
| 中等置信 (pLDDT 50-70) 占比 | 14.2% |
| 低置信 (pLDDT<50) 占比 | 32.0% |
| 有序区域 (pLDDT>70) 占比 | 53.8% |
| 可用 PDB 条目 | 4NJ4, 4NRM, 4NRO, 4NRP, 4NRQ, 4O61, 4O7X, 4OCT, 7V4G, 7WKV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4NJ4, 4NRM, 4NRO, 4NRP, 4NRQ, 4O61, 4O7X, 4OCT, 7V4G, 7WKV）+ AlphaFold极高置信度预测（pLDDT=72.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027450, IPR037151, IPR032860; Pfam: PF13532 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FTO | 0.990 | 0.000 | — |
| DDX46 | 0.981 | 0.000 | — |
| ALKBH1 | 0.980 | 0.000 | — |
| YTHDF1 | 0.957 | 0.000 | — |
| METTL14 | 0.956 | 0.000 | — |
| WTAP | 0.939 | 0.000 | — |
| METTL3 | 0.922 | 0.000 | — |
| YTHDC2 | 0.921 | 0.000 | — |
| YTHDC1 | 0.920 | 0.000 | — |
| YTHDF2 | 0.905 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=72.2 + PDB: 4NJ4, 4NRM, 4NRO, 4NRP, 4NRQ,  | pLDDT=72.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus speckle; Nucleus, nucleoplasm / Nucleoplasm, Cytosol; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ALKBH5 — RNA demethylase ALKBH5，研究基础较多，新颖性有限。
2. 蛋白大小394 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 689 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 689 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P6C2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000091542-ALKBH5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ALKBH5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P6C2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000091542-ALKBH5/subcellular

![](https://images.proteinatlas.org/7196/71_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/7196/71_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/7196/72_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/7196/72_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/7196/73_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/7196/73_B12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P6C2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6P6C2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027450;IPR037151;IPR032860; |
| Pfam | PF13532; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000091542-ALKBH5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| KPNA1 | Biogrid, Opencell | true |
| DDX39B | Opencell | false |
| KPNA6 | Opencell | false |
| LMNA | Biogrid | false |
| MINK1 | Opencell | false |
| PRPF4B | Opencell | false |
| RBM8A | Opencell | false |
| USP36 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
