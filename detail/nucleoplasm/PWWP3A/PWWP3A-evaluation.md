---
type: protein-evaluation
gene: "PWWP3A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PWWP3A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PWWP3A / EXPAND1, MUM1 |
| 蛋白名称 | PWWP domain-containing DNA repair factor 3A |
| 蛋白大小 | 710 aa / 78.6 kDa |
| UniProt ID | Q2TAK8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 710 aa / 78.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.1; PDB: 3PMI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035504, IPR040263, IPR048795, IPR048765; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EXPAND1, MUM1 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.1 |
| 高置信度残基 (pLDDT>90) 占比 | 22.0% |
| 置信残基 (pLDDT 70-90) 占比 | 24.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.7% |
| 低置信 (pLDDT<50) 占比 | 46.1% |
| 有序区域 (pLDDT>70) 占比 | 46.2% |
| 可用 PDB 条目 | 3PMI |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.1），有序残基占 46.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035504, IPR040263, IPR048795, IPR048765; Pfam: PF20884, PF20886, PF20887 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NDUFS8 | 0.975 | 0.742 | — |
| MT-ND3 | 0.975 | 0.747 | — |
| MT-ND4 | 0.975 | 0.747 | — |
| NDUFV1 | 0.975 | 0.745 | — |
| MT-ND1 | 0.975 | 0.747 | — |
| NDUFV2 | 0.975 | 0.746 | — |
| NDUFS1 | 0.975 | 0.743 | — |
| NDUFS2 | 0.974 | 0.742 | — |
| NDUFS3 | 0.974 | 0.742 | — |
| CYC1 | 0.945 | 0.616 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BAIAP2L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP1R15A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CEP55 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| GOPC | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| KLK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FEM1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SMPD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MKI67 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26949251|imex:IM-26415 |
| PTGES3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.1 + PDB: 3PMI | pLDDT=63.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PWWP3A — PWWP domain-containing DNA repair factor 3A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小710 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2TAK8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160953-PWWP3A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PWWP3A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2TAK8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000160953-PWWP3A/subcellular

![](https://images.proteinatlas.org/48063/1423_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/48063/1423_D9_3_red_green.jpg)
![](https://images.proteinatlas.org/48063/835_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/48063/835_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/48063/844_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/48063/844_D9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q2TAK8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q2TAK8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 411..472; /note="PWWP" |
| InterPro | IPR035504;IPR040263;IPR048795;IPR048765; |
| Pfam | PF20884;PF20886;PF20887; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000160953-PWWP3A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SMC6 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
