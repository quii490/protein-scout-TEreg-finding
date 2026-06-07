---
type: protein-evaluation
gene: "MEOX2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MEOX2 — REJECTED (研究热度过高 (PubMed strict=120，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MEOX2 / GAX, MOX2 |
| 蛋白名称 | Homeobox protein MOX-2 |
| 蛋白大小 | 304 aa / 33.6 kDa |
| UniProt ID | P50222 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Nucleus speckle |
| 蛋白大小 | 10/10 | ×1 | 10 | 304 aa / 33.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=120 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR020479, IPR017970, IPR009057, IPR042 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Nucleus speckle | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 120 |
| PubMed broad count | 217 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GAX, MOX2 |

**关键文献**:
1. Interneuron-specific dual-AAV SCN1A gene replacement corrects epileptic phenotypes in mouse models of Dravet syndrome.. *Science translational medicine*. PMID: 40106582
2. MEOX2 homeobox gene promotes growth of malignant gliomas.. *Neuro-oncology*. PMID: 35468210
3. Transcription factor mesenchyme homeobox protein 2 (MEOX2) modulates nociceptor function.. *The FEBS journal*. PMID: 35029322
4. MEOX2-mediated regulation of Cathepsin S promotes cell proliferation and motility in glioma.. *Cell death & disease*. PMID: 35436995
5. KMV-mediated cardiomyocyte-to-endothelial cell signaling drives capillary rarefaction to promote heart failure following pressure overload.. *Theranostics*. PMID: 40303341

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.5 |
| 高置信度残基 (pLDDT>90) 占比 | 17.1% |
| 置信残基 (pLDDT 70-90) 占比 | 3.3% |
| 中等置信 (pLDDT 50-70) 占比 | 47.7% |
| 低置信 (pLDDT<50) 占比 | 31.9% |
| 有序区域 (pLDDT>70) 占比 | 20.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.5），有序残基占 20.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR020479, IPR017970, IPR009057, IPR042634; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TCF15 | 0.837 | 0.053 | — |
| MEOX1 | 0.830 | 0.768 | — |
| ZEB2 | 0.697 | 0.328 | — |
| MYF5 | 0.673 | 0.088 | — |
| AGMO | 0.670 | 0.000 | — |
| PAX1 | 0.648 | 0.328 | — |
| MYOD1 | 0.631 | 0.088 | — |
| SIX1 | 0.602 | 0.047 | — |
| MAFB | 0.580 | 0.052 | — |
| PAX9 | 0.566 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VIP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KRTAP4-12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TULP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HSPA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| SAMM50 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PB1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| PA | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| M | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| NA | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| PB2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.5 + PDB: 无 | pLDDT=60.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MEOX2 — Homeobox protein MOX-2，研究基础较多，新颖性有限。
2. 蛋白大小304 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 120 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 120 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P50222
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106511-MEOX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEOX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P50222
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03





<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P50222-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P50222 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001356;IPR020479;IPR017970;IPR009057;IPR042634; |
| Pfam | PF00046; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106511-MEOX2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CNTNAP2 | Intact, Biogrid | true |
| EFEMP1 | Intact, Biogrid | true |
| PAX3 | Intact, Biogrid | true |
| PRKAB2 | Intact, Biogrid | true |
| ACTN4 | Intact | false |
| ADAMTS12 | Intact | false |
| AGPAT1 | Intact | false |
| AHCYL1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
