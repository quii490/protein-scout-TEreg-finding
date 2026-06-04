---
type: protein-evaluation
gene: "BRDT"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BRDT — REJECTED (研究热度过高 (PubMed strict=131，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRDT |
| 蛋白名称 | Bromodomain testis-specific protein |
| 蛋白大小 | 947 aa / 108.0 kDa |
| UniProt ID | Q58F21 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 947 aa / 108.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=131 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.4; PDB: 2RFJ, 4FLP, 4KCX, 5VBQ, 5VBR, 7BJY, 7L73 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031354, IPR043508, IPR043509, IPR050935, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 131 |
| PubMed broad count | 215 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic etiological spectrum of sperm morphological abnormalities.. *Journal of assisted reproduction and genetics*. PMID: 39417902
2. Ectopic expression of testis-specific transcription elongation factor in driving cancer.. *Science advances*. PMID: 40085698
3. BET Epigenetic Reader Proteins in Cardiovascular Transcriptional Programs.. *Circulation research*. PMID: 32324495
4. Dihydropyridine Lactam Analogs Targeting BET Bromodomains.. *ChemMedChem*. PMID: 34932262
5. In vivo versus in silico assessment of potentially pathogenic missense variants in human reproductive genes.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37459509

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.4 |
| 高置信度残基 (pLDDT>90) 占比 | 26.0% |
| 置信残基 (pLDDT 70-90) 占比 | 16.4% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 48.6% |
| 有序区域 (pLDDT>70) 占比 | 42.4% |
| 可用 PDB 条目 | 2RFJ, 4FLP, 4KCX, 5VBQ, 5VBR, 7BJY, 7L73, 7L99, 7L9A, 7LEJ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.4），有序残基占 42.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031354, IPR043508, IPR043509, IPR050935, IPR001487; Pfam: PF17035, PF17105, PF00439 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| H4C7 | 0.989 | 0.222 | — |
| H4C6 | 0.988 | 0.222 | — |
| BRD2 | 0.946 | 0.424 | — |
| DEFB1 | 0.930 | 0.000 | — |
| BRD4 | 0.926 | 0.421 | — |
| BRD3 | 0.915 | 0.000 | — |
| CDK9 | 0.913 | 0.528 | — |
| CCNT1 | 0.909 | 0.516 | — |
| H3-5 | 0.708 | 0.178 | — |
| H3C12 | 0.708 | 0.178 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VAV2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13772|pubmed:18654987 |
| Cdk9 | psi-mi:"MI:0096"(pull down) | pubmed:20593818|imex:IM-17619 |
| PB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28611246|imex:IM-25425 |
| Rab17 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26885862|imex:IM-24977 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.4 + PDB: 2RFJ, 4FLP, 4KCX, 5VBQ, 5VBR,  | pLDDT=62.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BRDT — Bromodomain testis-specific protein，研究基础较多，新颖性有限。
2. 蛋白大小947 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 131 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 131 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q58F21
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137948-BRDT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRDT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q58F21
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
