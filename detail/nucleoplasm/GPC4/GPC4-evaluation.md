---
type: protein-evaluation
gene: "GPC4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPC4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPC4 |
| 蛋白名称 | Glypican-4 |
| 蛋白大小 | 556 aa / 62.4 kDa |
| UniProt ID | O75487 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm; UniProt: Cell membrane; Secreted, extracellular space |
| 蛋白大小 | 10/10 | ×1 | 10 | 556 aa / 62.4 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=86 篇 (≤100→2) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001863, IPR019803; Pfam: PF01153 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.5/180** | |
| **归一化总分** | | | **53.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm | Approved |
| UniProt | Cell membrane; Secreted, extracellular space | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell surface (GO:0009986)
- external side of plasma membrane (GO:0009897)
- extracellular exosome (GO:0070062)
- glutamatergic synapse (GO:0098978)
- Golgi lumen (GO:0005796)
- lysosomal lumen (GO:0043202)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 86 |
| PubMed broad count | 187 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Neutrophil Elastase Targets Select Proteins on Human Blood-Monocyte-Derived Macrophage Cell Surfaces.. *International journal of molecular sciences*. PMID: 39684750
2. Pathogenic Variants in GPC4 Cause Keipert Syndrome.. *American journal of human genetics*. PMID: 30982611
3. Serum glypican-4 is associated with the 10-year clinical outcome of patients with peripheral artery disease.. *International journal of cardiology*. PMID: 35944770
4. Large-scale plasma proteomics uncovers preclinical molecular signatures of Parkinson's disease and overlap with other neurodegenerative disorders.. *medRxiv : the preprint server for health sciences*. PMID: 40766128
5. Xq26 duplications lead to undergrowth or overgrowth via competing pathways including GPC3/GPC4.. *Annals of human genetics*. PMID: 31583675

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.2 |
| 高置信度残基 (pLDDT>90) 占比 | 69.2% |
| 置信残基 (pLDDT 70-90) 占比 | 9.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 15.1% |
| 有序区域 (pLDDT>70) 占比 | 78.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.2，有序区 78.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001863, IPR019803; Pfam: PF01153 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LRRTM4 | 0.955 | 0.197 | — |
| FZD7 | 0.930 | 0.052 | — |
| FZD2 | 0.929 | 0.052 | — |
| FZD3 | 0.919 | 0.052 | — |
| FZD8 | 0.917 | 0.052 | — |
| FZD5 | 0.915 | 0.052 | — |
| FZD9 | 0.914 | 0.052 | — |
| FZD1 | 0.911 | 0.052 | — |
| FZD6 | 0.910 | 0.052 | — |
| FZD4 | 0.908 | 0.052 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IQCB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| SQSTM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| CSNK2A2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| SPCS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GPC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PDPK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| KSR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27086506|imex:IM-25748 |
| SCGB2A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GPR183 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.2 + PDB: 无 | pLDDT=83.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Secreted, extracellular space / Plasma membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GPC4 — Glypican-4，研究基础较多，新颖性有限。
2. 蛋白大小556 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 86 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75487
- Protein Atlas: https://www.proteinatlas.org/ENSG00000076716-GPC4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75487
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000076716-GPC4/subcellular

![](https://images.proteinatlas.org/30834/1789_A11_1_cr5961fc340c048_blue_red_green.jpg)
![](https://images.proteinatlas.org/30834/1789_A11_25_cr5961fc340cad8_blue_red_green.jpg)
![](https://images.proteinatlas.org/30834/1870_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30834/1870_E6_7_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75487-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75487 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001863;IPR019803; |
| Pfam | PF01153; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000076716-GPC4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CAMKV | Biogrid, Bioplex | true |
| SRP14 | Biogrid, Opencell, Bioplex | true |
| CANX | Opencell | false |
| CD36 | Biogrid | false |
| FGF1 | Bioplex | false |
| FGF4 | Bioplex | false |
| GPC6 | Intact, Biogrid | false |
| HADHA | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
