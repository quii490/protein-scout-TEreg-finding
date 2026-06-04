---
type: protein-evaluation
gene: "ELL3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ELL3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ELL3 |
| 蛋白名称 | RNA polymerase II elongation factor ELL3 |
| 蛋白大小 | 397 aa / 45.4 kDa |
| UniProt ID | Q9HB65 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/ELL3/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/ELL3/IF_images/HEK293_1.jpg|HEK293]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; 额外: Mitotic chromosome; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 397 aa / 45.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031176, IPR019464, IPR010844; Pfam: PF10390, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Mitotic chromosome | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cell junction (GO:0030054)
- chromosome (GO:0005694)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription elongation factor complex (GO:0008023)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Maternal ELL3 loss-of-function leads to oocyte aneuploidy and early miscarriage.. *Nature structural & molecular biology*. PMID: 39820605
2. Young LINE-1 transposon 5' UTRs marked by elongation factor ELL3 function as enhancers to regulate naïve pluripotency in embryonic stem cells.. *Nature cell biology*. PMID: 37591949
3. The RNA Pol II elongation factor Ell3 marks enhancers in ES cells and primes future gene activation.. *Cell*. PMID: 23273992
4. Ell3 enhances differentiation of mouse embryonic stem cells by regulating epithelial-mesenchymal transition and apoptosis.. *PloS one*. PMID: 22768269
5. Ell3 stabilizes p53 following CDDP treatment via its effects on ubiquitin-dependent and -independent proteasomal degradation pathways in breast cancer cells.. *Oncotarget*. PMID: 26540344

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.8 |
| 高置信度残基 (pLDDT>90) 占比 | 20.2% |
| 置信残基 (pLDDT 70-90) 占比 | 29.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 42.1% |
| 有序区域 (pLDDT>70) 占比 | 49.7% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/ELL3/ELL3-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=61.8），有序残基占 49.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031176, IPR019464, IPR010844; Pfam: PF10390, PF07303 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AFF4 | 0.998 | 0.838 | — |
| AFF1 | 0.998 | 0.842 | — |
| MLLT1 | 0.997 | 0.819 | — |
| MLLT3 | 0.997 | 0.836 | — |
| CCNT1 | 0.992 | 0.788 | — |
| ELL | 0.992 | 0.833 | — |
| EAF1 | 0.992 | 0.848 | — |
| CCNT2 | 0.991 | 0.792 | — |
| EAF2 | 0.989 | 0.846 | — |
| ICE1 | 0.986 | 0.829 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FTH1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SIRT1 | psi-mi:"MI:0096"(pull down) | imex:IM-12078|pubmed:19343720 |
| MLLT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21729782|imex:IM-16559 |
| CDK9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21729782|imex:IM-16559 |
| MED26 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21729782|imex:IM-16559 |
| EAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21729782|imex:IM-16559 |
| AFF4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PIP4K2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AFF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCNT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.8 + PDB: 无 | pLDDT=61.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli; 额外: Mitotic chromosome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ELL3 — RNA polymerase II elongation factor ELL3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小397 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HB65
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128886-ELL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ELL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HB65
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-body/ELL3/ELL3-PAE.png]]




