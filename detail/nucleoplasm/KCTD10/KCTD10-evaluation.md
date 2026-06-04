---
type: protein-evaluation
gene: "KCTD10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KCTD10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KCTD10 / ULR061 |
| 蛋白名称 | BTB/POZ domain-containing adapter for CUL3-mediated RhoA degradation protein 3 |
| 蛋白大小 | 313 aa / 35.4 kDa |
| UniProt ID | Q9H3F6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 313 aa / 35.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=82.2; PDB: 5FTA |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045068, IPR000210, IPR011333, IPR003131; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.0/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 54 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ULR061 |

**关键文献**:
1. The CRL3(KCTD10) ubiquitin ligase-USP18 axis coordinately regulates cystine uptake and ferroptosis by modulating SLC7A11.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38959043
2. KCTD10 regulates brain development by destabilizing brain disorder-associated protein KCTD13.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38489388
3. KCTD10 inhibits lung cancer metastasis and angiogenesis via ubiquitin-mediated β-catenin degradation.. *Frontiers in immunology*. PMID: 40873559
4. Vascular smooth muscle cell-derived KIF13B inhibits proinflammatory responses to protect against atherosclerosis.. *The Journal of clinical investigation*. PMID: 41609725
5. KCTD10 regulates brown adipose tissue thermogenesis and metabolic function via Notch signaling.. *The Journal of endocrinology*. PMID: 34854382

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.2 |
| 高置信度残基 (pLDDT>90) 占比 | 60.7% |
| 置信残基 (pLDDT 70-90) 占比 | 15.0% |
| 中等置信 (pLDDT 50-70) 占比 | 11.5% |
| 低置信 (pLDDT<50) 占比 | 12.8% |
| 有序区域 (pLDDT>70) 占比 | 75.7% |
| 可用 PDB 条目 | 5FTA |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=82.2，有序区 75.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045068, IPR000210, IPR011333, IPR003131; Pfam: PF02214 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.996 | 0.839 | — |
| UBXN1 | 0.995 | 0.994 | — |
| UBXN7 | 0.995 | 0.994 | — |
| FAF1 | 0.994 | 0.994 | — |
| KCTD13 | 0.979 | 0.873 | — |
| TNFAIP1 | 0.975 | 0.873 | — |
| RBX1 | 0.958 | 0.421 | — |
| POLD2 | 0.798 | 0.095 | — |
| KCTD17 | 0.792 | 0.000 | — |
| USP25 | 0.782 | 0.775 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000228495.6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| cpfC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ATXN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| USP13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| KCTD13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| RHOB | psi-mi:"MI:0018"(two hybrid) | pubmed:19637314|imex:IM-20406 |
| Cd2ap | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| DCUN1D1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.2 + PDB: 5FTA | pLDDT=82.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KCTD10 — BTB/POZ domain-containing adapter for CUL3-mediated RhoA degradation protein 3，非常新颖，仅有少数基础研究。
2. 蛋白大小313 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H3F6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110906-KCTD10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KCTD10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H3F6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
