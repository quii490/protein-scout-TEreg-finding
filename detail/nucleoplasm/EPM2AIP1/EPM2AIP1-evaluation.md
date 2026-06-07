---
type: protein-evaluation
gene: "EPM2AIP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EPM2AIP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EPM2AIP1 / KIAA0766 |
| 蛋白名称 | EPM2A-interacting protein 1 |
| 蛋白大小 | 607 aa / 70.4 kDa |
| UniProt ID | Q7L775 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum |
| 蛋白大小 | 10/10 | ×1 | 10 | 607 aa / 70.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR040647; Pfam: PF18658 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasmic side of endoplasmic reticulum membrane (GO:0098554)
- nucleus (GO:0005634)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0766 |

**关键文献**:
1. EPM2AIP1 immunohistochemistry is inadequate as a surrogate marker for MLH1 promoter hypermethylation testing in colorectal cancer.. *Human pathology*. PMID: 38945374
2. EPM2AIP1 Immunohistochemistry Can Be Used as Surrogate Testing for MLH1 Promoter Methylation in Endometrial Cancer.. *The American journal of surgical pathology*. PMID: 34772843
3. MSI-XGNN: an explainable GNN computational framework integrating transcription- and methylation-level biomarkers for microsatellite instability detection.. *Briefings in bioinformatics*. PMID: 37833839
4. Identification of a novel protein interacting with laforin, the EPM2a progressive myoclonus epilepsy gene product.. *Genomics*. PMID: 12782127
5. Deficiency of a glycogen synthase-associated protein, Epm2aip1, causes decreased glycogen synthesis and hepatic insulin resistance.. *The Journal of biological chemistry*. PMID: 24142699

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.3 |
| 高置信度残基 (pLDDT>90) 占比 | 46.3% |
| 置信残基 (pLDDT 70-90) 占比 | 43.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.8% |
| 低置信 (pLDDT<50) 占比 | 3.5% |
| 有序区域 (pLDDT>70) 占比 | 89.8% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EPM2AIP1/EPM2AIP1-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=85.3，有序区 89.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040647; Pfam: PF18658 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EPM2A | 0.932 | 0.067 | — |
| CCNB1IP1 | 0.710 | 0.710 | — |
| NHLRC1 | 0.700 | 0.065 | — |
| NFU1 | 0.699 | 0.000 | — |
| PPP1R3C | 0.664 | 0.000 | — |
| SERPINF1 | 0.651 | 0.651 | — |
| LYG1 | 0.572 | 0.000 | — |
| TXNL1 | 0.564 | 0.045 | — |
| AMY1B | 0.548 | 0.000 | — |
| MLH1 | 0.535 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000406027.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CSNK1A1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| DHX40 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZSCAN18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Mycbp2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| CCNB1IP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| HSF2BP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRT75 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZBTB14 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KCTD9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.3 + PDB: 无 | pLDDT=85.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. EPM2AIP1 — EPM2A-interacting protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小607 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L775
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178567-EPM2AIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EPM2AIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L775
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EPM2AIP1/EPM2AIP1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7L775 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR040647; |
| Pfam | PF18658; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000178567-EPM2AIP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MAD2L1 | Intact, Biogrid, Bioplex | true |
| ZSCAN18 | Intact, Biogrid | true |
| ACTN1 | Intact | false |
| APPL2 | Intact | false |
| ARHGEF5 | Intact | false |
| C1orf50 | Intact | false |
| CCNB1IP1 | Intact | false |
| CNTROB | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
