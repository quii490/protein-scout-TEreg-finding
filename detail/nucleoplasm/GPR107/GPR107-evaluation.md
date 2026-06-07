---
type: protein-evaluation
gene: "GPR107"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPR107 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR107 / KIAA1624, LUSTR1 |
| 蛋白名称 | Protein GPR107 |
| 蛋白大小 | 600 aa / 67.0 kDa |
| UniProt ID | Q5VW38 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Cell membrane; Golgi apparatus, trans-Golgi network membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 600 aa / 67.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR053937, IPR009637; Pfam: PF06814 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Approved |
| UniProt | Cell membrane; Golgi apparatus, trans-Golgi network membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- clathrin-coated vesicle (GO:0030136)
- early endosome (GO:0005769)
- Golgi apparatus (GO:0005794)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.5 |
| 高置信度残基 (pLDDT>90) 占比 | 16.7% |
| 置信残基 (pLDDT 70-90) 占比 | 45.3% |
| 中等置信 (pLDDT 50-70) 占比 | 14.0% |
| 低置信 (pLDDT<50) 占比 | 24.0% |
| 有序区域 (pLDDT>70) 占比 | 62.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.5，有序区 62.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR053937, IPR009637; Pfam: PF06814 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LMX1B | 0.726 | 0.000 | — |
| GPR146 | 0.665 | 0.000 | — |
| TM9SF4 | 0.646 | 0.000 | — |
| FAM168B | 0.631 | 0.000 | — |
| LRIT3 | 0.591 | 0.591 | — |
| AMY2A | 0.547 | 0.000 | — |
| RGP1 | 0.538 | 0.000 | — |
| TPRA1 | 0.536 | 0.000 | — |
| ZDHHC5 | 0.526 | 0.000 | — |
| GPR137B | 0.523 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BIRC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NEK7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NDUFA12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LNPEP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| REEP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMEM17 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| TMEM216 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| SGCA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BTNL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.5 + PDB: 无 | pLDDT=70.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Golgi apparatus, trans-Golgi networ / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GPR107 — Protein GPR107，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小600 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VW38
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148358-GPR107/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR107
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VW38
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000148358-GPR107/subcellular

![](https://images.proteinatlas.org/31704/371_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/31704/371_B11_4_red_green.jpg)
![](https://images.proteinatlas.org/31704/372_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/31704/372_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/31704/374_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/31704/374_B11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5VW38-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5VW38 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR053937;IPR009637; |
| Pfam | PF06814; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000148358-GPR107/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARFRP1 | Opencell | false |
| HTN1 | Opencell | false |
| JTB | Opencell | false |
| KRAS | Biogrid | false |
| SCFD1 | Opencell | false |
| SYAP1 | Opencell | false |
| TMEM165 | Opencell | false |
| TMEM230 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
