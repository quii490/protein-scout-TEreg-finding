---
type: protein-evaluation
gene: "ERBB2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ERBB2 — REJECTED (研究热度过高 (PubMed strict=6115，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERBB2 / HER2, MLN19, NEU, NGL |
| 蛋白名称 | Receptor tyrosine-protein kinase erbB-2 |
| 蛋白大小 | 1255 aa / 137.9 kDa |
| UniProt ID | P04626 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm, Cytosol; UniProt: Cell membrane; Cell projection, ruffle membrane; Cell membra |
| 蛋白大小 | 5/10 | ×1 | 5 | 1255 aa / 137.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=6115 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=74.0; PDB: 1MFG, 1MFL, 1MW4, 1N8Z, 1QR1, 1S78, 2A91 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006211, IPR006212, IPR032778, IPR009030, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm, Cytosol | Enhanced |
| UniProt | Cell membrane; Cell projection, ruffle membrane; Cell membrane; Early endosome; Cytoplasm, perinucle... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- apical plasma membrane (GO:0016324)
- basal plasma membrane (GO:0009925)
- basolateral plasma membrane (GO:0016323)
- cytosol (GO:0005829)
- early endosome (GO:0005769)
- endosome membrane (GO:0010008)
- ERBB3:ERBB2 complex (GO:0038143)
- membrane (GO:0016020)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6115 |
| PubMed broad count | 25886 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HER2, MLN19, NEU, NGL |

**关键文献**:
1. High-Throughput Functional Evaluation of Variants of Unknown Significance in ERBB2.. *Clinical cancer research : an official journal of the American Association for Cancer Research*. PMID: 29967253
2. Determinants of sensitivity to HER2-targeted antibody drug conjugates in urothelial cancer.. *Nature communications*. PMID: 41422272
3. Full-length transcriptome atlas of gallbladder cancer reveals trastuzumab resistance conferred by ERBB2 alternative splicing.. *Signal transduction and targeted therapy*. PMID: 39948369
4. Clinicopathological value of ErbB2 gene and protein expression in osteochondroma.. *Acta orthopaedica et traumatologica turcica*. PMID: 32175895
5. Correlation of ErbB2 gene status, mRNA and protein expression.. *Onkologie*. PMID: 16770085

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.0 |
| 高置信度残基 (pLDDT>90) 占比 | 42.0% |
| 置信残基 (pLDDT 70-90) 占比 | 24.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.6% |
| 低置信 (pLDDT<50) 占比 | 24.5% |
| 有序区域 (pLDDT>70) 占比 | 66.9% |
| 可用 PDB 条目 | 1MFG, 1MFL, 1MW4, 1N8Z, 1QR1, 1S78, 2A91, 2JWA, 2KS1, 2L4K |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1MFG, 1MFL, 1MW4, 1N8Z, 1QR1, 1S78, 2A91, 2JWA, 2KS1, 2L4K）+ AlphaFold极高置信度预测（pLDDT=74.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006211, IPR006212, IPR032778, IPR009030, IPR011009; Pfam: PF00757, PF14843, PF07714 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ERBB4 | 0.999 | 0.850 | — |
| GRB7 | 0.999 | 0.840 | — |
| NRG1 | 0.999 | 0.898 | — |
| EGFR | 0.999 | 0.998 | — |
| ERBIN | 0.999 | 0.842 | — |
| GRB2 | 0.999 | 0.934 | — |
| SHC1 | 0.999 | 0.921 | — |
| ERBB3 | 0.999 | 0.997 | — |
| CD44 | 0.999 | 0.695 | — |
| SRC | 0.999 | 0.850 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.0 + PDB: 1MFG, 1MFL, 1MW4, 1N8Z, 1QR1,  | pLDDT=74.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell projection, ruffle membrane; C / Plasma membrane; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ERBB2 — Receptor tyrosine-protein kinase erbB-2，研究基础较多，新颖性有限。
2. 蛋白大小1255 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 6115 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 6115 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P04626
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141736-ERBB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERBB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P04626
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
