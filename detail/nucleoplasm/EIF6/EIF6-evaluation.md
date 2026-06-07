---
type: protein-evaluation
gene: "EIF6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF6 — REJECTED (研究热度过高 (PubMed strict=172，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF6 / EIF3A, ITGB4BP |
| 蛋白名称 | Eukaryotic translation initiation factor 6 |
| 蛋白大小 | 245 aa / 26.6 kDa |
| UniProt ID | P56537 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 245 aa / 26.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=172 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=91.0; PDB: 6LQM, 6LSR, 6LSS, 6LU8, 7OW7, 8A3D, 8FKP |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002769; Pfam: PF01912 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- lamin filament (GO:0005638)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- synapse (GO:0045202)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 172 |
| PubMed broad count | 234 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EIF3A, ITGB4BP |

**关键文献**:
1. Network Pharmacology and Bioinformatics Study of Six Medicinal Food Homologous Plants Against Colorectal Cancer.. *International journal of molecular sciences*. PMID: 39940699
2. Ribosome ADP-ribosylation inhibits translation and maintains proteostasis in cancers.. *Cell*. PMID: 34314702
3. HectD1 controls hematopoietic stem cell regeneration by coordinating ribosome assembly and protein synthesis.. *Cell stem cell*. PMID: 33711283
4. Convergent somatic evolution commences in utero in a germline ribosomopathy.. *Nature communications*. PMID: 37608017
5. Reduced EIF6 dosage attenuates TP53 activation in models of Shwachman-Diamond syndrome.. *The Journal of clinical investigation*. PMID: 39964763

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.0 |
| 高置信度残基 (pLDDT>90) 占比 | 84.1% |
| 置信残基 (pLDDT 70-90) 占比 | 8.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.1% |
| 低置信 (pLDDT<50) 占比 | 1.6% |
| 有序区域 (pLDDT>70) 占比 | 92.3% |
| 可用 PDB 条目 | 6LQM, 6LSR, 6LSS, 6LU8, 7OW7, 8A3D, 8FKP, 8FKQ, 8FKR, 8FKS |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6LQM, 6LSR, 6LSS, 6LU8, 7OW7, 8A3D, 8FKP, 8FKQ, 8FKR, 8FKS）+ AlphaFold极高置信度预测（pLDDT=91.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002769; Pfam: PF01912 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RPL31 | 0.999 | 0.993 | — |
| RPL18A | 0.999 | 0.992 | — |
| RPL30 | 0.998 | 0.991 | — |
| GTPBP4 | 0.998 | 0.995 | — |
| RPL4 | 0.997 | 0.993 | — |
| RPL23 | 0.997 | 0.992 | — |
| RPL5 | 0.997 | 0.991 | — |
| RPL34 | 0.997 | 0.990 | — |
| NMD3 | 0.997 | 0.992 | — |
| RPL6 | 0.996 | 0.992 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| XRN2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| 728833 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ENSP00000502429.1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ARF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| BCCIP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RUVBL1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYDGF | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF1AX | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| FSCN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.0 + PDB: 6LQM, 6LSR, 6LSS, 6LU8, 7OW7,  | pLDDT=91.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleolus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EIF6 — Eukaryotic translation initiation factor 6，研究基础较多，新颖性有限。
2. 蛋白大小245 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 172 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 172 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P56537
- Protein Atlas: https://www.proteinatlas.org/ENSG00000242372-EIF6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P56537
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P56537-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P56537 |
| SMART | SM00654; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002769; |
| Pfam | PF01912; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000242372-EIF6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BCCIP | Intact, Biogrid | true |
| DHX58 | Intact, Biogrid | true |
| EIF2AK2 | Intact, Biogrid | true |
| OAS3 | Intact, Biogrid | true |
| RPL4 | Biogrid, Opencell | true |
| ANLN | Biogrid | false |
| CCNF | Biogrid | false |
| CHMP4B | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
