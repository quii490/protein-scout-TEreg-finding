---
type: protein-evaluation
gene: "PDC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PDC — REJECTED (研究热度过高 (PubMed strict=1786，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PDC |
| 蛋白名称 | Phosducin |
| 蛋白大小 | 246 aa / 28.2 kDa |
| UniProt ID | P20941 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytosol; Nucleus; Cell projection, cilium, photor |
| 蛋白大小 | 10/10 | ×1 | 10 | 246 aa / 28.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1786 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001200, IPR051499, IPR023196, IPR024253, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **85.5/180** | |
| **归一化总分** | | | **47.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytosol; Nucleus; Cell projection, cilium, photoreceptor outer segment; Photoreceptor inn... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- photoreceptor inner segment (GO:0001917)
- photoreceptor outer segment (GO:0001750)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1786 |
| PubMed broad count | 10017 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A decrease in Flavonifractor plautii and its product, phytosphingosine, predisposes individuals with phlegm-dampness constitution to metabolic disorders.. *Cell discovery*. PMID: 40097405
2. PDHX acetylation facilitates tumor progression by disrupting PDC assembly and activating lactylation-mediated gene expression.. *Protein & cell*. PMID: 39311688
3. Aberrant CHCHD2-associated mitochondriopathy in Kii ALS/PDC astrocytes.. *Acta neuropathologica*. PMID: 38750212
4. Novel mouse models based on intersectional genetics to identify and characterize plasmacytoid dendritic cells.. *Nature immunology*. PMID: 36928414
5. Chronic activation of pDCs in autoimmunity is linked to dysregulated ER stress and metabolic responses.. *The Journal of experimental medicine*. PMID: 36053251

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.9 |
| 高置信度残基 (pLDDT>90) 占比 | 54.9% |
| 置信残基 (pLDDT 70-90) 占比 | 22.8% |
| 中等置信 (pLDDT 50-70) 占比 | 12.2% |
| 低置信 (pLDDT<50) 占比 | 10.2% |
| 有序区域 (pLDDT>70) 占比 | 77.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=82.9，有序区 77.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001200, IPR051499, IPR023196, IPR024253, IPR036249; Pfam: PF02114 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNGT1 | 0.975 | 0.900 | — |
| GNB1 | 0.965 | 0.914 | — |
| SUCLG2 | 0.933 | 0.000 | — |
| RHO | 0.828 | 0.000 | — |
| SAG | 0.772 | 0.000 | — |
| PLIN2 | 0.766 | 0.000 | — |
| RCVRN | 0.664 | 0.000 | — |
| RPE65 | 0.662 | 0.000 | — |
| GRK2 | 0.647 | 0.300 | — |
| F13B | 0.623 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TSPY2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PLXNC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DCC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CYRIB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ITM2B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-29868|pubmed:34446781 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.9 + PDB: 无 | pLDDT=82.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus; Cell projection, cili / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PDC — Phosducin，研究基础较多，新颖性有限。
2. 蛋白大小246 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1786 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1786 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P20941
- Protein Atlas: https://www.proteinatlas.org/search/PDC
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PDC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P20941
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
